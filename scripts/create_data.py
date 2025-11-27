from blyjections.data import pull_statcast_pitching
from blyjections.utils import get_season_start_end, read_yaml

config = read_yaml("config.yaml")
SEASONS = config["seasons"]

# statcast
pull_statcast_pitching(file_path="data/pitch_level_{}.parquet", seasons=SEASONS)
