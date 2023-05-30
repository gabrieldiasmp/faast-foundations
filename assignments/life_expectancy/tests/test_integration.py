import pandas as pd
from life_expectancy.cleaning import Pipeline
from life_expectancy.load_data import LoadJSON, LoadTSV
from life_expectancy.clean_data import CleanJSON, CleanTSV
from . import FIXTURES_DIR

def test_clean_data_tsv(life_expectancy_expected):
    """Run the `run` function and compare the output to the expected output"""

    cleaned_life_expectancy = Pipeline(
        input_filename=FIXTURES_DIR / "raw_data.tsv",
        load_type=LoadTSV(),
        clean_type=CleanTSV(),
        region="AT"
    ).run()

    pd.testing.assert_frame_equal(
        cleaned_life_expectancy, life_expectancy_expected
    )

def test_clean_data_json(expected_json_data):
    """Run the `run` function and compare the output to the expected output"""

    cleaned_life_expectancy = Pipeline(
        input_filename=FIXTURES_DIR / "sample_dict.json",
        load_type=LoadJSON(),
        clean_type=CleanJSON(),
        region="AT"
    ).run()

    pd.testing.assert_frame_equal(
        cleaned_life_expectancy, expected_json_data
    )
