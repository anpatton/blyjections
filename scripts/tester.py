import polars as pl

frame = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

frame.write_parquet("data/test.parquet")