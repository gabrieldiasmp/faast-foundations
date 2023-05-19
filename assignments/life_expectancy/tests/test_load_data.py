"""Tests for the load data module"""
import pandas as pd

from life_expectancy.load_data import LoadJSON, LoadTSV
from . import FIXTURES_DIR 

def test_load_data_tsv(raw_data):
    df_load = LoadTSV().load_file(path=FIXTURES_DIR / "raw_data.tsv")

    pd.testing.assert_frame_equal(
        df_load, raw_data
    )

def test_load_data_json(raw_json_data):
    load_json = pd.DataFrame(
        LoadJSON().load_file(path=FIXTURES_DIR / "sample_dict.json"))

    raw_json_converted_to_pd = pd.DataFrame(raw_json_data)
    
    pd.testing.assert_frame_equal(
        load_json, raw_json_converted_to_pd
    )
