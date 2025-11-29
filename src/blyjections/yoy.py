import polars as pl


def get_consecutive_seasons(
    frame: pl.DataFrame, player_col: str = "player_id", season_col: str = "Season"
) -> pl.DataFrame:
    """Returns all consecutive player-seasons, includinding those with gaps between. Ex: 2021-2022, and 2024-2025

    Args:
        frame (pl.DataFrame): Any dataframe with season and player columns
        player_col (str, optional): Defaults to "player_id".
        season_col (str, optional): Defaults to "Season, the FanGraphs format"

    Returns:
        pl.DataFrame:
    """

    result = (
        frame.sort(player_col, season_col)
        .with_columns(
            (
                pl.col(season_col) - pl.col(season_col).rank("ordinal").over(player_col)
            ).alias("stretch_num")
        )
        .with_columns(
            pl.col("stretch_num").rank("dense").over(player_col).alias("stretch_id"),
            pl.len().over(player_col, "stretch_num").alias("stretch_len"),
        )
        .filter(pl.col("stretch_len") > 1)
        .drop("stretch_len", "stretch_num")
    )

    return result
