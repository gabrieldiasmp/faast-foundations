"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.cleaning import load_data, clean_data, save_data, main
from . import OUTPUT_DIR

def test_clean_data(
        life_expectancy_sample: pd.DataFrame, 
        life_expectancy_expected: pd.DataFrame):
    """It tests the clean function"""

    df_clean = clean_data(
        life_expectancy_data=life_expectancy_sample,
        region="AT")

    pd.testing.assert_frame_equal(
        df_clean, life_expectancy_expected
    )
