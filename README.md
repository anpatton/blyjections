# blyjections

Mediocre to poor fantasy baseball projections.

`pip install git+https://github.com/anpatton/blyjections`

## Targets

| Scoring Group | Scoring Category          | Weight |
|:--------------|:--------------------------|:-------|
| Hitting       | Stolen Bases - Net (SBN)  | 1      |
| Hitting       | RBI (RBI)                 | 1      |
| Hitting       | Runs Scored (R)           | 1      |
| Hitting       | On Base Percentage (OBP)  | 1      |
| Hitting       | Slugging Percentage (SLG) | 1      |
| Pitching      | Strikeouts Pitched (K)    | 1      |
| Pitching      | Wins (W)                  | 1      |
| Pitching      | Earned Run Average (ERA)  | 1      |
| Pitching      | Saves + Holds (SVH)       | 1      |
| Pitching      | WHIP Ratio (WHIP)         | 1      |

### Independent Hitting

$\large OBP = \frac{H + BB + HBP}{AB + BB + HBP + SF}$

$\large SLG = \frac{1B + (2 \times 2B) + (3 \times 3B) + (4 \times HR)}{AB}$

### Dependent Hitting

-   RBI

-   R

### Pitching

-   K

-   W

$\large ERA = \frac{ER \times 9}{IP}$

$\large SVH = SV + HLD$

$\large WHIP = \frac{BB + H}{IP}$

### Misc.

$\large SBN = SB - CS$