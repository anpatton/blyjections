import polars as pl
from blyjections.utils import read_yaml


def clean_batting_basic(
    frame: pl.DataFrame, config_path: str = "config.yaml", add_ids: bool = True
) -> pl.DataFrame:
    """Takes full FG batting frame and returns basic batting stats"""

    simple_cols = read_yaml(config_path)["batting_basic"]
    frame = frame.select(simple_cols)

    if add_ids:
        frame = create_ids(frame, id_col="IDfg", name_col="Name", new_id_col="player_id")

    return frame


def create_ids(
    frame: pl.DataFrame,
    id_col: str = "IDfg",
    name_col: str = "Name",
    new_id_col: str = "player_id",
) -> pl.DataFrame:
    """Creates player_id from id-name, defaults to FG format"""

    frame = (
        frame.with_columns(
            pl.concat_str(
                [pl.col(id_col), pl.col(name_col).cast(pl.Utf8)], separator="-"
            ).alias("player_id")
        )
        .drop(id_col, name_col)
        .select([new_id_col, pl.all().exclude(new_id_col)])
    )
    return frame
