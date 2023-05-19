"""It cleans a dataset and exports it"""

import argparse
from pathlib import Path
from life_expectancy.load_data import LoadTSV, LoadJSON
from life_expectancy.clean_data import CleanTSV, CleanJSON
from life_expectancy.save_data import save_data

DATA_DIR = Path(__file__).parent / "data"

class Pipeline: # pylint: disable=R0903
    """It implements the pipeline that delivers the expected data
    """
    def __init__( # pylint: disable=R0913
            self,
            region: str,
            load_type,
            clean_type,
            input_filename: str = DATA_DIR / 'eu_life_expectancy_raw.tsv',
            output_filename: str = DATA_DIR / 'pt_life_expectancy.csv') -> None:

        self.region = region
        self.load_type = load_type
        self.clean_type = clean_type
        self.input_filename = input_filename
        self.output_filename = output_filename

    def run(self):
        """It runs the following steps:
            1) Load the data
            2) Clean the data
            3) Export the data
        """

        life_expectancy = self.load_type.load_file(self.input_filename)

        cleaned_life_expectancy = self.clean_type.clean_data(
            region=self.region,
            life_expectancy_data=life_expectancy)

        print(cleaned_life_expectancy.head())
        save_data(cleaned_life_expectancy, self.output_filename)

        return cleaned_life_expectancy

if __name__ == "__main__":  # pragma: no cover

    parser = argparse.ArgumentParser(description='Inputs for cleaning function')
    parser.add_argument('--region', default="PT", type=str, help='The region to be selected')

    args = parser.parse_args()

    Pipeline(
        region=args.region,
        input_filename=DATA_DIR / 'eu_life_expectancy_raw.tsv',
        load_type=LoadTSV(),
        clean_type=CleanTSV()
    ).run()

    Pipeline(
        region=args.region,
        input_filename=DATA_DIR / 'eurostat_life_expect.json',
        load_type=LoadJSON(),
        clean_type=CleanJSON()
    ).run()
