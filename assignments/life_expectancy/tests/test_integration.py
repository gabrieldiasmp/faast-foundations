import pandas as pd
from life_expectancy.cleaning import main


def test_clean_data(pt_life_expectancy_expected):
    """Run the `main` function and compare the output to the expected output"""
    cleaned_life_expectancy = main(region="PT")

    pd.testing.assert_frame_equal(
        cleaned_life_expectancy, pt_life_expectancy_expected
    )
