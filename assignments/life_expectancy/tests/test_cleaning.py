"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.cleaning import load_data, clean_data, save_data, main
from . import OUTPUT_DIR

def test_load_data():
    assert "blabla" == "blabla"

def test_clean_data(
        life_expectancy_sample: pd.DataFrame, 
        life_expectancy_expected: pd.DataFrame):
    """Run the `main` function and compare the output to the expected output"""

    df_clean = clean_data(
        life_expectancy_data=life_expectancy_sample,
        region="AT")

    pd.testing.assert_frame_equal(
        df_clean, life_expectancy_expected
    )

def test_save_data():
    assert "blabla" == "blabla"


# def test_clean_data(pt_life_expectancy_expected):
#     """Run the `main` function and compare the output to the expected output"""
#     main(region="PT")
#     pt_life_expectancy_actual = pd.read_csv(
#         OUTPUT_DIR / "pt_life_expectancy.csv"
#     )
#     pd.testing.assert_frame_equal(
#         pt_life_expectancy_actual, pt_life_expectancy_expected
#     )
