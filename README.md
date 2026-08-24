# Loden

A warm theme family inspired by the olive-green dial, brushed steel, and cream markings of a Formex Reef watch. Loden is designed for sustained software-engineering work, with particular attention to readable syntax and high-information diffs in Neovim, Ghostty, Codex, and Claude Code.

Loden includes equal Day and Night variants. Both are authored from one canonical palette and share the ochre interaction color `#B17232` with black selected text.

| Variant | Background | Foreground | Intended use |
| --- | --- | --- | --- |
| Loden Night | `#171812` | `#C9BA99` | Low-light and evening work |
| Loden Day | `#EAE4D5` | `#34362C` | Bright offices and daytime work |

## Supported applications

- Ghostty
- Neovim and LazyVim, using Kanso as the integration base
- Codex CLI
- Claude Code
- Firefox
- Zsh ZLE visual mode
- macOS system selection and dynamic wallpaper assets
- Slack and Linear within their supported custom-theme surfaces

## Quick start

Install Python 3.12+ and [uv](https://docs.astral.sh/uv/), then generate and audit every artifact:

```sh
uv sync
uv run python scripts/build.py
```

The build fails if required contrast or perceptual-separation checks fail.

## Palette lab

Open `palette-preview.html` in a color-managed browser. Universal interaction tokens live in `palette/loden-shared.json`; polarity-specific tokens live in `palette/loden-night.json` and `palette/loden-day.json`.

The preview includes:

- foundation and accent swatches;
- representative syntax highlighting;
- line and inline diff treatments;
- terminal output for Git and AI coding tools;
- calculated WCAG contrast against the primary background.

The palette is authored in sRGB. The primary background is `#171812`.

## Palette and validation

The audit writes [the Night report](reports/loden-night-audit.md), [the Day report](reports/loden-day-audit.md), and machine-readable JSON covering WCAG, APCA, OKLCH, ΔEOK, and Machado color-vision simulations. Generation updates every integration from the same canonical JSON.

Generated artifacts:

- `ghostty/themes/loden-night`
- `ghostty/themes/loden-day`
- `colors/loden.lua`, `colors/loden-night.lua`, and `colors/loden-day.lua`
- `lua/loden/`
- `lua/lualine/themes/`
- `nvim/lazyvim-plugin.lua`
- `shell/loden.zsh`
- `macos/apply-highlight.sh`
- `wallpapers/loden.heic`
- `firefox/manifest.json`
- `codex/themes/loden-night.tmTheme` and `codex/themes/loden-day.tmTheme`
- `claude-code/themes/loden-night.json` and `claude-code/themes/loden-day.json`
- `slack/loden-night.txt` and `slack/loden-day.txt`
- `linear/loden-night.txt` and `linear/loden-day.txt`

The shared interaction pair is ochre `#B17232` with pure black text `#000000`. It drives Neovim Visual mode, Ghostty selections and cursor, Zsh selections, the macOS system highlight, and Firefox URL-bar selection.

## Installation

### Ghostty

Copy `ghostty/themes/loden-night` and `ghostty/themes/loden-day` into `~/.config/ghostty/themes/`. To follow macOS appearance automatically:

```ini
theme = light:loden-day,dark:loden-night
```

The generated dark theme uses Berkeley Mono Retina without font thickening. The light theme uses Berkeley Mono with `font-thicken = true`.

### Neovim and LazyVim

Copy `nvim/lazyvim-plugin.lua` into your LazyVim plugin specifications, then run `:Lazy sync`. The spec installs `achandran/loden` and its Kanso dependency directly from GitHub. Select `loden`, `loden-day`, or `loden-night` with `:colorscheme`; `loden` defaults to Loden Day.

On macOS, the included LazyVim spec also follows system appearance changes in running Neovim sessions. Install its native watcher first:

```sh
brew install cormacrelf/tap/dark-notify
```

Loden Day is selected in Light appearance and Loden Night in Dark appearance. Remove the `cormacrelf/dark-notify` entry from the spec if automatic switching is not wanted.

## AI coding tools

For Codex CLI, copy the generated `.tmTheme` files into `~/.codex/themes/`, then choose one with `/theme`. These themes explicitly define `markup.inserted` and `markup.deleted`, so Codex uses Loden's tuned diff backgrounds instead of its built-in mint and pink fallbacks.

For Claude Code 2.1.118 or newer, copy the generated JSON files into `~/.claude/themes/`, then choose one with `/theme`. The generated themes define full-line, dimmed-context, and word-level diff colors. Claude Code does not currently combine two custom files behind its `auto` selection, so select Loden Night or Loden Day when appearance changes.

## Slack and Linear

Slack exposes only a subset of its interface colors. In Preferences → Appearance → Custom theme, choose Import theme and paste the appropriate line from `slack/`. Keep window gradients off for the closest Loden result.

In Linear Preferences → Interface and theme, create a custom theme and paste the appropriate line from `linear/`. Linear derives its remaining surfaces from these seed colors, so minor generated shades are controlled by Linear rather than Loden.

## Repository layout

- `palette/`: canonical shared, dark, and light color definitions
- `colors/` and `lua/`: Neovim plugin runtime files
- `scripts/`: Python generation and automated palette audits
- `reports/`: generated human- and machine-readable audit results
- `palette-preview.html`: standalone visual palette and diff laboratory
- Application directories: generated integrations ready to install or import

Generated files should not be edited directly. Change the canonical palette or generator and rerun the build instead.

## Dynamic macOS wallpaper

`wallpapers/loden.heic` contains two 6016×3760 sRGB frames and Apple's appearance metadata. macOS displays the warm `#EAE4D5` Day frame in Light appearance and the olive-black `#171812` Night frame in Dark appearance.

To regenerate and inspect it on macOS:

```sh
swiftc -module-cache-path /private/tmp/loden-swift-cache scripts/generate_wallpaper.swift -o /private/tmp/generate-loden-wallpaper
/private/tmp/generate-loden-wallpaper generate wallpapers/loden.heic
/private/tmp/generate-loden-wallpaper inspect wallpapers/loden.heic
```
