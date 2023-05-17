"""Tests for the save data module"""
import pandas as pd
import unittest.mock as mock

from life_expectancy.cleaning import save_data
from . import FIXTURES_DIR, OUTPUT_DIR

def test_save_data(pt_life_expectancy_expected):
    """It tests the method that saves the cleaned data to the directory

    Args:
        pt_life_expectancy_expected (pd.DataFrame): It comes from a fixture
    """
    
    with mock.patch.object(pd.DataFrame, 'to_csv') as mock_to_csv:
        # call the function that writes to CSV
        save_data(
            life_expectancy=pt_life_expectancy_expected, 
            output_filename=OUTPUT_DIR / 'pt_life_expectancy.csv')

        # assert that the to_csv method was called with the correct arguments
        mock_to_csv.assert_called_once_with(OUTPUT_DIR / 'pt_life_expectancy.csv', index=False)