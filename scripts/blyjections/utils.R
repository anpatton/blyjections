#library(shiny)
#library(bslib)
#library(DT)
#library(arrow)

#batting_seasons <- arrow::read_parquet("scripts/data/batting_seasons.parquet")

demo_basic_cols <- c("IDfg", "Season", "Team", "Name", "Age", "G")

batting_basic_cols <- c(
  "AB",
  "PA",
  "H",
  "1B",
  "2B",
  "3B",
  "HR",
  "R",
  "RBI",
  "BB",
  "IBB",
  "SO",
  "HBP",
  "SF",
  "SH",
  "GDP",
  "SB",
  "CS",
  "AVG",
  "GB",
  "FB",
  "LD",
  "IFFB",
  "Pitches",
  "Balls",
  "Strikes",
  "IFH",
  "BU",
  "BUH",
  "BB%",
  "K%",
  "BB/K",
  "OBP",
  "SLG",
  "OPS",
  "ISO",
  "BABIP",
  "GB/FB"
)

batting_adv_cols <- c(
  "wOBA",
  "wRAA",
  "wRC",
  "Bat",
  "Fld",
  "Rep",
  "Pos",
  "RAR",
  "WAR",
  "Dol",
  "Spd",
  "WPA",
  "RE24"
)

batting_xplus_cols <- c(
  "AVG+",
  "BB%+",
  "K%+",
  "OBP+",
  "SLG+",
  "ISO+",
  "BABIP+",
  "LD+%",
  "GB%+",
  "FB%+",
  "HR/FB%+",
  "Pull%+",
  "Cent%+",
  "Oppo%+",
  "Soft%+",
  "Med%+",
  "Hard%+",
  "xBA",
  "xSLG",
  "xwOBA"
)

batting_swing_cols <- c(
  "O-Swing%",
  "Z-Swing%",
  "Swing%",
  "O-Contact%",
  "Z-Contact%",
  "Contact%",
  "Zone%",
  "F-Strike%",
  "SwStr%",
  "Pull%",
  "Cent%",
  "Oppo%",
  "Soft%",
  "Med%",
  "Hard%"
)
