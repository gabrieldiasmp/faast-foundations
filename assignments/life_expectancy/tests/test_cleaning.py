"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.cleaning import clean_data
from . import OUTPUT_DIR

def test_clean_data(
        raw_data: pd.DataFrame,
        life_expectancy_expected: pd.DataFrame):
    """It tests the clean function"""

    df_clean = clean_data(
        life_expectancy_data=raw_data,
        region="AT")

    pd.testing.assert_frame_equal(
        df_clean, life_expectancy_expected
    )
