"""Tests for the load data module"""
import pandas as pd

from life_expectancy.load_data import LoadJSON, LoadTSV
from . import FIXTURES_DIR

def test_load_data_tsv(raw_data):
    df_load = LoadTSV().load_file(path=FIXTURES_DIR / "raw_data.tsv")

    pd.testing.assert_frame_equal(
        df_load, raw_data
    )
