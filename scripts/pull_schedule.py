import os
import requests
import yaml
import polars as pl
from dotenv import load_dotenv
from blyjections.utils import write_yaml, read_yaml

load_dotenv()

key = os.getenv("SR_KEY")

url = "https://api.sportradar.com/mlb/trial/v8/en/league/seasons.json"

headers = {
    "accept": "application/json",
    "x-api-key": key
}

response = requests.get(url, headers=headers)
data = response.json()

df = (
    pl.DataFrame(data["seasons"])
    .unnest("type")
    .rename({"code": "type_code", "name": "type_name"})
)

df = (df.with_columns(
    pl.lit(data["league"]["alias"]).alias("league_alias"),
    pl.lit(data["league"]["name"]).alias("league_name"),
    pl.lit(data["league"]["id"]).alias("league_id"))
    .filter(pl.col("type_code") == "REG")
    .filter(pl.col("league_alias") == "MLB")
    .rename({"year": "season"})
    .select(["season", "start_date", "end_date"])
    )

seasons_dict = {
    season["season"]: {"start_date": season["start_date"], "end_date": season["end_date"]}
    for season in df.to_dicts()
}

cur_config = read_yaml("config.yaml")

cur_config["seasons"] = seasons_dict

write_yaml(cur_config, "config.yaml")

