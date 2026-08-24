"""Audit Loden's palette and write human- and machine-readable reports."""

from __future__ import annotations

import json
import sys
from itertools import combinations

from lodenlib import ROOT, apca, delta_e, load_palette, oklch, simulated_hex, wcag


SIMULATIONS = ("normal", "protan", "deutan", "tritan", "grayscale")


def main(variant: str = "loden-night") -> None:
    palette = load_palette(variant)
    backgrounds = palette["backgrounds"]
    foregrounds = palette["foregrounds"]
    accents = palette["accents"]
    ansi = palette["ansi"]
    diff = palette["diff"]
    highlight = palette["highlight"]

    contrast_specs = [
        ("muted UI", foregrounds["muted"], backgrounds["base"], 3.0, 25),
        ("comments", foregrounds["comment"], backgrounds["base"], 4.5, 45),
        ("secondary text", foregrounds["subtext"], backgrounds["base"], 7.0, 55),
        ("normal text", foregrounds["text"], backgrounds["base"], 7.0, 60),
        ("bright text", foregrounds["bright"], backgrounds["base"], 7.0, 75),
        ("highlighted text", highlight["foreground"], highlight["background"], 4.5, 35),
        # Selection/cursor boundaries are non-text UI components: WCAG 3:1
        # applies, while APCA is reported for reference but is not a gate.
        (f"highlight edge on {palette['name']}", highlight["background"], backgrounds["base"], 3.0, 0),
        ("highlight edge on white", highlight["background"], "#FFFFFF", 3.0, 0),
        *[(f"syntax {name}", color, backgrounds["base"], 4.5, 44) for name, color in accents.items()],
        ("diff add", diff["addForeground"], diff["addBackground"], 7.0, 60),
        ("diff delete", diff["deleteForeground"], diff["deleteBackground"], 7.0, 60),
        ("diff change", diff["changeForeground"], diff["changeBackground"], 7.0, 60),
        ("diff hunk", diff["hunkForeground"], diff["hunkBackground"], 7.0, 60),
        ("inline add", diff["inlineForeground"], diff["addEmphasis"], 7.0, 60),
        ("inline delete", diff["inlineForeground"], diff["deleteEmphasis"], 7.0, 60),
        ("inline change", diff["inlineForeground"], diff["changeEmphasis"], 7.0, 60),
        ("conflict marker", diff["conflictForeground"], diff["conflictBackground"], 7.0, 60),
        *[
            (f"ANSI {name}", color, backgrounds["base"], 3.0 if name == "brightBlack" else 4.5, 20 if name == "brightBlack" else 44)
            for name, color in ansi.items()
            if name != "black"
        ],
    ]

    contrasts = []
    failures = []
    for name, foreground, background, wcag_target, apca_target in contrast_specs:
        wcag_value = wcag(foreground, background)
        apca_value = apca(foreground, background)
        # Treat ratios within 0.005 of a two-decimal target as equal to the
        # displayed value. This avoids rejecting 2.999… when reported as 3.00.
        passed = wcag_value + 0.005 >= wcag_target and abs(apca_value) >= apca_target
        contrasts.append(
            {
                "name": name,
                "foreground": foreground,
                "background": background,
                "wcag": round(wcag_value, 2),
                "wcagTarget": wcag_target,
                "apcaLc": round(apca_value, 1),
                "apcaTarget": apca_target,
                "passed": passed,
            }
        )
        if not passed:
            failures.append(name)

    all_colors = {}
    for family in ("backgrounds", "highlight", "foregrounds", "accents", "ansi", "diff"):
        for name, value in palette[family].items():
            all_colors[f"{family}.{name}"] = value

    color_data = {}
    for name, value in all_colors.items():
        lightness, chroma, hue = oklch(value)
        color_data[name] = {
            "hex": value,
            "oklch": [round(lightness, 4), round(chroma, 4), round(hue, 1)],
            "inSrgb": True,
            "simulations": {mode: simulated_hex(value, mode) for mode in SIMULATIONS[1:]},
        }

    semantic_pairs = {
        # Diff state separation considers both foreground and line background.
        # Glyphs (+, -, ~) provide the final redundant, non-color cue.
        "diff add/delete": (
            diff["addForeground"], diff["deleteForeground"],
            diff["addBackground"], diff["deleteBackground"], 0.03,
        ),
        "diff add/change": (
            diff["addForeground"], diff["changeForeground"],
            diff["addBackground"], diff["changeBackground"], 0.03,
        ),
        "diff delete/change": (
            diff["deleteForeground"], diff["changeForeground"],
            diff["deleteBackground"], diff["changeBackground"], 0.03,
        ),
        "error/warning": (
            accents["coral"], accents["gold"],
            backgrounds["base"], backgrounds["base"], 0.05,
        ),
        "ANSI blue/bright blue": (
            ansi["blue"], ansi["brightBlue"], backgrounds["base"], backgrounds["base"], 0.03,
        ),
        "ANSI cyan/bright cyan": (
            ansi["cyan"], ansi["brightCyan"], backgrounds["base"], backgrounds["base"], 0.03,
        ),
    }
    separations = []
    for name, (first, second, first_bg, second_bg, floor) in semantic_pairs.items():
        values = {
            mode: round(max(delta_e(first, second, mode), delta_e(first_bg, second_bg, mode)), 3)
            for mode in SIMULATIONS
        }
        passed = min(values.values()) >= floor
        separations.append({"name": name, "deltaEOK": values, "floor": floor, "passed": passed})
        if not passed:
            failures.append(name)

    # Track all accent proximity for discovery without turning every close hue
    # into a failure; semantic intent determines whether proximity is harmful.
    proximity = []
    for (left_name, left), (right_name, right) in combinations(accents.items(), 2):
        value = delta_e(left, right)
        if value < 0.05:
            proximity.append({"pair": f"{left_name}/{right_name}", "deltaEOK": round(value, 3)})
    proximity.sort(key=lambda item: item["deltaEOK"])

    report = {
        "palette": palette["name"],
        "colorSpace": palette["colorSpace"],
        "passed": not failures,
        "failures": failures,
        "contrast": contrasts,
        "colors": color_data,
        "semanticSeparation": separations,
        "accentProximityReview": proximity,
    }

    reports = ROOT / "reports"
    reports.mkdir(exist_ok=True)
    report_stem = f"{variant}-audit"
    json_report = reports / f"{report_stem}.json"
    markdown_report = reports / f"{report_stem}.md"
    json_report.write_text(json.dumps(report, indent=2) + "\n")

    lines = [
        f"# {palette['name']} palette audit",
        "",
        f"Overall: **{'PASS' if report['passed'] else 'FAIL'}**",
        "",
        "## Text contrast",
        "",
        "| Role | WCAG | APCA Lc | Result |",
        "|---|---:|---:|---|",
    ]
    for check in contrasts:
        lines.append(
            f"| {check['name']} | {check['wcag']}:1 | {check['apcaLc']} | "
            f"{'PASS' if check['passed'] else 'FAIL'} |"
        )
    lines.extend(
        [
            "",
            "## Semantic separation under color-vision simulations",
            "",
            "Values are ΔEOK distances. They are comparative signals, not universal accessibility thresholds.",
            "",
            "| Pair | Normal | Protan | Deutan | Tritan | Gray | Result |",
            "|---|---:|---:|---:|---:|---:|---|",
        ]
    )
    for check in separations:
        values = check["deltaEOK"]
        lines.append(
            f"| {check['name']} | {values['normal']} | {values['protan']} | {values['deutan']} | "
            f"{values['tritan']} | {values['grayscale']} | {'PASS' if check['passed'] else 'FAIL'} |"
        )
    lines.extend(["", "## Close accent pairs for visual review", ""])
    lines.extend(f"- `{item['pair']}`: ΔEOK {item['deltaEOK']}" for item in proximity)
    markdown_report.write_text("\n".join(lines) + "\n")

    for check in contrasts:
        print(
            f"{'PASS' if check['passed'] else 'FAIL'}  WCAG {check['wcag']:>5}:1  "
            f"APCA {check['apcaLc']:>6}  {check['name']}"
        )
    for check in separations:
        minimum = min(check["deltaEOK"].values())
        print(f"{'PASS' if check['passed'] else 'FAIL'}  ΔEOK min {minimum:>5}  {check['name']}")
    print(f"\nWrote {markdown_report}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "loden-night")
