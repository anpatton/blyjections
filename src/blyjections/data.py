import warnings  # to deal with pandas bullshit
import polars as pl
import pybaseball as pyb
from blyjections.utils import get_season_start_end


def pull_statcast_pitching(
    file_path: str = "data/sc_pitch_level_{}.parquet", 
    seasons: list = None
) -> None:
    """Pulls yearly pitch level data from Statcast using pybaseball

    Args:
        file_path (str): Local file path to save data. Defaults to None.
    """

    for season in seasons:
        dates = get_season_start_end(season=season)
        start = dates[0]
        end = dates[1]
        file_path_season = file_path.format(season)

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            pitches = pyb.statcast(start_dt=start, end_dt=end, verbose=False)
            pitches = pl.from_pandas(pitches)

        pitches.write_parquet(file_path_season)
        print(f"Statcast pitch level data for {season} saved -> {file_path_season}.")


def pull_fangraph_batting(
    file_path="data/fg_batting_seasons.parquet", seasons: list = None
) -> None:
    """_summary_

    Args:
        file_path (str, optional): _description_. Defaults to "data/fg_batting_seasons.parquet".
        seasons (list, optional): _description_. Defaults to None.
    """
    start = seasons[0]
    stop = seasons[-1]

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        res = pyb.batting_stats(start_season=start, end_season=stop)
        res = pl.from_pandas(res)

    res.write_parquet(file_path)
    print(f"FanGraphs season level batting data [{start}-{stop}] saved -> {file_path}.")


def pull_fangraph_pitching(
    file_path="data/fg_pitching_seasons.parquet", seasons: list = None
) -> None:
    """_summary_

    Args:
        file_path (str, optional): _description_. Defaults to "data/fg_pitching_seasons.parquet".
        seasons (list, optional): _description_. Defaults to None.
    """
    start = seasons[0]
    stop = seasons[-1]

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        res = pyb.pitching_stats(start_season=start, end_season=stop)
        res = pl.from_pandas(res)

    res.write_parquet(file_path)
    print(
        f"FanGraphs season level pitching data [{start}-{stop}] saved -> {file_path}."
    )


def pull_player_ids(
    file_path: str = "data/cw_player_ids.parquet", min_year: int = None
) -> None:
    """_summary_

    Args:
        file_path (str, optional): _description_. Defaults to "data/cw_player_ids.parquet".
        min_year (int, optional): _description_. Defaults to None.
    """
    players = pyb.chadwick_register()
    players = pl.from_pandas(players).filter(pl.col("mlb_played_last") >= min_year)
    players.write_parquet(file_path)
    print(f"Player IDs saved -> {file_path}.")
