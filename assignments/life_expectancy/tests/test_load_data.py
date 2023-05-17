"""Tests for the load data module"""
import pandas as pd

from life_expectancy.cleaning import load_data
from . import FIXTURES_DIR

def test_load_data(raw_data):
    df_load = load_data(FIXTURES_DIR / "raw_data.tsv")

    pd.testing.assert_frame_equal(
        df_load, raw_data
    )
