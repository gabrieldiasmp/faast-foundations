from ast import Load
import pandas as pd
from life_expectancy.cleaning import Pipeline
from life_expectancy.load_data import LoadJSON, LoadTSV
from . import FIXTURES_DIR

def test_clean_data(life_expectancy_expected):
    """Run the `run` function and compare the output to the expected output"""

    cleaned_life_expectancy = Pipeline(
        input_filename=FIXTURES_DIR / "raw_data.tsv",
        load_type=LoadTSV(),
        region="AT"
    ).run()

    pd.testing.assert_frame_equal(
        cleaned_life_expectancy, life_expectancy_expected
    )
