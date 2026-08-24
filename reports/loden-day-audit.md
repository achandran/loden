# Loden Day palette audit

Overall: **PASS**

## Text contrast

| Role | WCAG | APCA Lc | Result |
|---|---:|---:|---|
| muted UI | 3.42:1 | 54.3 | PASS |
| comments | 4.82:1 | 64.8 | PASS |
| secondary text | 7.13:1 | 75.0 | PASS |
| normal text | 9.68:1 | 82.3 | PASS |
| bright text | 12.19:1 | 86.6 | PASS |
| highlighted text | 5.32:1 | 37.5 | PASS |
| highlight edge on Loden Day | 3.11:1 | 50.8 | PASS |
| highlight edge on white | 3.95:1 | 66.6 | PASS |
| syntax olive | 5.22:1 | 66.9 | PASS |
| syntax sage | 4.84:1 | 64.8 | PASS |
| syntax gold | 6.3:1 | 71.8 | PASS |
| syntax ochre | 4.99:1 | 65.5 | PASS |
| syntax clay | 5.11:1 | 66.0 | PASS |
| syntax coral | 5.03:1 | 65.3 | PASS |
| syntax aqua | 5.01:1 | 65.7 | PASS |
| syntax blue | 5.2:1 | 66.8 | PASS |
| syntax mauve | 5.16:1 | 66.6 | PASS |
| diff add | 7.63:1 | 65.8 | PASS |
| diff delete | 7.75:1 | 72.1 | PASS |
| diff change | 8.2:1 | 79.7 | PASS |
| diff hunk | 7.92:1 | 75.4 | PASS |
| inline add | 7.58:1 | -88.1 | PASS |
| inline delete | 7.86:1 | -88.6 | PASS |
| inline change | 7.98:1 | -89.2 | PASS |
| inline diff marker | 5.32:1 | 37.5 | PASS |
| conflict marker | 7.65:1 | 72.1 | PASS |
| ANSI red | 6.59:1 | 72.4 | PASS |
| ANSI green | 6.06:1 | 70.9 | PASS |
| ANSI yellow | 7.63:1 | 76.5 | PASS |
| ANSI blue | 6.23:1 | 71.6 | PASS |
| ANSI magenta | 6.29:1 | 71.8 | PASS |
| ANSI cyan | 5.88:1 | 70.0 | PASS |
| ANSI white | 7.13:1 | 75.0 | PASS |
| ANSI brightBlack | 3.42:1 | 54.3 | PASS |
| ANSI brightRed | 5.03:1 | 65.3 | PASS |
| ANSI brightGreen | 4.84:1 | 64.8 | PASS |
| ANSI brightYellow | 6.3:1 | 71.8 | PASS |
| ANSI brightBlue | 5.2:1 | 66.8 | PASS |
| ANSI brightMagenta | 5.16:1 | 66.6 | PASS |
| ANSI brightCyan | 5.01:1 | 65.7 | PASS |
| ANSI brightWhite | 9.68:1 | 82.3 | PASS |
| ANSI extendedOchre | 4.99:1 | 65.5 | PASS |
| ANSI extendedClay | 5.11:1 | 66.0 | PASS |

## Semantic separation under color-vision simulations

Values are ΔEOK distances. They are comparative signals, not universal accessibility thresholds.

| Pair | Normal | Protan | Deutan | Tritan | Gray | Result |
|---|---:|---:|---:|---:|---:|---|
| diff add/delete | 0.127 | 0.061 | 0.072 | 0.142 | 0.059 | PASS |
| diff add/change | 0.123 | 0.101 | 0.117 | 0.127 | 0.11 | PASS |
| diff delete/change | 0.074 | 0.061 | 0.056 | 0.059 | 0.051 | PASS |
| error/warning | 0.129 | 0.055 | 0.072 | 0.124 | 0.052 | PASS |
| ANSI blue/bright blue | 0.042 | 0.043 | 0.042 | 0.042 | 0.042 | PASS |
| ANSI cyan/bright cyan | 0.037 | 0.038 | 0.037 | 0.037 | 0.037 | PASS |

## Close accent pairs for visual review

- `olive/sage`: ΔEOK 0.026
- `ochre/clay`: ΔEOK 0.04
- `aqua/blue`: ΔEOK 0.04
- `clay/coral`: ΔEOK 0.042
