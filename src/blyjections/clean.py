import polars as pl
from blyjections.utils import read_yaml

def clean_batting_basic(frame: pl.Dataframe, config_path: str = "config.yaml") -> pl.DataFrame:
    """Takes full FG batting frame and returns basic batting stats"""

    simple_cols = read_yaml(config_path)["batting_basic"]
    frame = frame.select(simple_cols)

    return frame



    
