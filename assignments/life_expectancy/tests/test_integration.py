import pandas as pd
from life_expectancy.cleaning import main

from . import FIXTURES_DIR

def test_clean_data(life_expectancy_expected):
    """Run the `main` function and compare the output to the expected output"""
    cleaned_life_expectancy = main(
        input_filename=FIXTURES_DIR / "raw_data.tsv",
        region="AT")

    pd.testing.assert_frame_equal(
        cleaned_life_expectancy, life_expectancy_expected
    )
