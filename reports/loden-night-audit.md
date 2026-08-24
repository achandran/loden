# Loden Night palette audit

Overall: **PASS**

## Text contrast

| Role | WCAG | APCA Lc | Result |
|---|---:|---:|---|
| muted UI | 3.72:1 | -27.3 | PASS |
| comments | 6.21:1 | -45.7 | PASS |
| secondary text | 8.04:1 | -57.3 | PASS |
| normal text | 9.33:1 | -64.8 | PASS |
| bright text | 12.09:1 | -79.7 | PASS |
| highlighted text | 5.32:1 | 37.5 | PASS |
| highlight edge on Loden Night | 4.53:1 | -34.0 | PASS |
| highlight edge on white | 3.95:1 | 66.6 | PASS |
| syntax olive | 7.56:1 | -54.4 | PASS |
| syntax sage | 7.94:1 | -56.7 | PASS |
| syntax gold | 8.97:1 | -62.9 | PASS |
| syntax ochre | 7.1:1 | -51.6 | PASS |
| syntax clay | 6.1:1 | -45.2 | PASS |
| syntax coral | 6.23:1 | -46.2 | PASS |
| syntax aqua | 6.98:1 | -50.8 | PASS |
| syntax blue | 7.81:1 | -55.9 | PASS |
| syntax mauve | 6.9:1 | -50.2 | PASS |
| diff add | 9.94:1 | -77.0 | PASS |
| diff delete | 8.34:1 | -63.3 | PASS |
| diff change | 7.84:1 | -68.6 | PASS |
| diff hunk | 8.63:1 | -67.0 | PASS |
| inline add | 7.09:1 | -71.1 | PASS |
| inline delete | 7.83:1 | -73.0 | PASS |
| inline change | 7.34:1 | -71.8 | PASS |
| conflict marker | 7.79:1 | -63.5 | PASS |
| ANSI red | 6.23:1 | -46.2 | PASS |
| ANSI green | 7.94:1 | -56.7 | PASS |
| ANSI yellow | 8.97:1 | -62.9 | PASS |
| ANSI blue | 7.81:1 | -55.9 | PASS |
| ANSI magenta | 6.9:1 | -50.2 | PASS |
| ANSI cyan | 6.98:1 | -50.8 | PASS |
| ANSI white | 8.04:1 | -57.3 | PASS |
| ANSI brightBlack | 3.72:1 | -27.3 | PASS |
| ANSI brightRed | 9.27:1 | -64.6 | PASS |
| ANSI brightGreen | 12.04:1 | -79.4 | PASS |
| ANSI brightYellow | 10.8:1 | -73.0 | PASS |
| ANSI brightBlue | 10.04:1 | -68.8 | PASS |
| ANSI brightMagenta | 9.55:1 | -66.1 | PASS |
| ANSI brightCyan | 10.05:1 | -68.8 | PASS |
| ANSI brightWhite | 12.09:1 | -79.7 | PASS |
| ANSI extendedOchre | 7.1:1 | -51.6 | PASS |
| ANSI extendedClay | 6.1:1 | -45.2 | PASS |

## Semantic separation under color-vision simulations

Values are ΔEOK distances. They are comparative signals, not universal accessibility thresholds.

| Pair | Normal | Protan | Deutan | Tritan | Gray | Result |
|---|---:|---:|---:|---:|---:|---|
| diff add/delete | 0.135 | 0.112 | 0.061 | 0.141 | 0.079 | PASS |
| diff add/change | 0.066 | 0.062 | 0.049 | 0.082 | 0.037 | PASS |
| diff delete/change | 0.1 | 0.091 | 0.066 | 0.065 | 0.066 | PASS |
| error/warning | 0.138 | 0.135 | 0.093 | 0.123 | 0.1 | PASS |
| ANSI blue/bright blue | 0.074 | 0.069 | 0.074 | 0.075 | 0.072 | PASS |
| ANSI cyan/bright cyan | 0.105 | 0.101 | 0.104 | 0.105 | 0.103 | PASS |

## Close accent pairs for visual review

- `olive/sage`: ΔEOK 0.019
- `clay/coral`: ΔEOK 0.035
- `aqua/blue`: ΔEOK 0.046
