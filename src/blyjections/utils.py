import yaml


def get_season_start_end(season: int = 2025, config_path: str = "config.yaml") -> list:
    """Returns a list of REG start and end dates via stored Sportsradar config file"""

    config = read_yaml(config_path)
    start = config["seasons"][season]["start_date"]
    end = config["seasons"][season]["end_date"]

    return [start, end]


def read_yaml(file_path: str = "config.yaml") -> dict:
    """Reads an arbirtary yaml and returns a dict"""

    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def write_yaml(data: dict, file_path: str = None) -> None:
    """Writes a dict to a yaml file"""
    
    with open(file_path, "w") as f:
        yaml.safe_dump(data, f, default_flow_style=False, sort_keys=False)
