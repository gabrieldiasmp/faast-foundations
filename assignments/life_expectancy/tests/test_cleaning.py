"""Tests for the cleaning module"""
import pandas as pd
from typing import List, Dict

from life_expectancy.clean_data import CleanJSON, CleanTSV
from life_expectancy.region import Region

def test_clean_data_tsv(
        raw_data: pd.DataFrame,
        life_expectancy_expected: pd.DataFrame):
    """It tests the clean function"""

    df_clean = CleanTSV().clean_data(
        life_expectancy_data=raw_data,
        region=Region("AT").value)

    pd.testing.assert_frame_equal(
        df_clean, life_expectancy_expected
    )

def test_clean_data_json(
        raw_json_data: List[Dict],
        expected_json_data: pd.DataFrame):
    """It tests the clean function"""

    raw_df = pd.DataFrame(raw_json_data)
    
    df_clean = CleanJSON().clean_data(
        life_expectancy_data=raw_df,
        region=Region("AT").value)

    pd.testing.assert_frame_equal(
        df_clean, expected_json_data
    )
