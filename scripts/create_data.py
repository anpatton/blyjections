import argparse
from blyjections.data import (
    pull_statcast_pitching,
    pull_fangraph_pitching,
    pull_fangraph_batting,
    pull_player_ids,
)
from blyjections.utils import read_yaml


config = read_yaml("config.yaml")
SEASON_MIN = config["min_season"]
SEASON_MAX = config["max_season"]
SEASONS = list(range(SEASON_MIN, SEASON_MAX + 1))

parser = argparse.ArgumentParser()
parser.add_argument('--no-statcast', dest='statcast', action='store_false')
parser.add_argument('--no-fangraphs', dest='fangraphs', action='store_false')
parser.add_argument('--no-chadwick', dest='chadwick', action='store_false')

args = parser.parse_args()

if args.statcast:
    pull_statcast_pitching(file_path="data/pitch_level_{}.parquet", seasons=SEASONS)
else:
    print("Skipping Statcast")

if args.fangraphs:
    pull_fangraph_batting(file_path="data/batting_seasons.parquet", seasons=SEASONS)
    pull_fangraph_pitching(file_path="data/pitching_seasons.parquet", seasons=SEASONS)
else:
    print("Skipping Fangraphs")

if args.chadwick:
    pull_player_ids(file_path="data/player_ids.parquet", min_year=SEASON_MIN)
else:
    print("Skipping Chadwick")
