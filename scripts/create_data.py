from blyjections.data import pull_statcast_pitching, pull_fangraph_pitching, pull_fangraph_batting
from blyjections.utils import get_season_start_end, read_yaml

config = read_yaml("config.yaml")
SEASONS = config["seasons"]

# statcast
#pull_statcast_pitching(file_path="data/pitch_level_{}.parquet", seasons=SEASONS)

pull_fangraph_batting(file_path="data/batting_seasons.parquet", seasons=SEASONS)
pull_fangraph_pitching(file_path="data/pitching_seasons.parquet", seasons=SEASONS)