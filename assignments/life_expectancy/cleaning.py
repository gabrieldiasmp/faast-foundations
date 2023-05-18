"""It cleans a dataset and exports it"""

import argparse
from pathlib import Path
import pandas as pd
from life_expectancy.load_data import LoadTSV, LoadJSON
from life_expectancy.clean_data import clean_data
from life_expectancy.save_data import save_data

DATA_DIR = Path(__file__).parent / "data"

class Pipeline:
    def __init__(
            self, 
            region: str, 
            load_type, 
            input_filename: str = DATA_DIR / 'eu_life_expectancy_raw.tsv', 
            output_filename: str = DATA_DIR / 'pt_life_expectancy.csv') -> None:

        self.region = region
        self.load_type = load_type
        self.input_filename = input_filename
        self.output_filename = output_filename
    
    def run(self):
        """It runs the following steps:
            1) Load the data
            2) Clean the data
            3) Export the data
        """

        life_expectancy = self.load_type.load_file(self.input_filename)
        cleaned_life_expectancy = clean_data(life_expectancy, self.region)
        print(cleaned_life_expectancy.head())
        save_data(cleaned_life_expectancy, self.output_filename)

        return cleaned_life_expectancy

if __name__ == "__main__":  # pragma: no cover

    parser = argparse.ArgumentParser(description='Inputs for cleaning function')
    parser.add_argument('--region', default="PT", type=str, help='The region to be selected')

    args = parser.parse_args()

    # Pipeline(
    #     region=args.region,
    #     load_type=LoadTSV()
    # ).run()

    print(DATA_DIR / 'eurostat_life_expect.json')
    # Pipeline(
    #     region=args.region,
    #     input_filename=DATA_DIR / 'eurostat_life_expect.json',
    #     load_type=LoadJSON()
    # ).run()

