"""It cleans a dataset and exports it"""

import argparse
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"

def load_data(
        input_filename):
    """It loads the dataframe that will be cleaned and exported

    Args:
        path_input (str, optional): Path to the data to be imported. Defaults to DATA_DIR/'eu_life_expectancy_raw.tsv'.

    Returns:
        pd.DataFrame: Dataframe to be cleaned
    """

    life_expectancy = pd.read_csv(
        input_filename,
        sep='\t')

    return life_expectancy


def clean_data(
        life_expectancy: pd.DataFrame,
        region: str = "PT") -> pd.DataFrame:
    """It cleans the data

    Args:
        life_expectancy (pd.DataFrame): The df that will be cleaned by the function.
        region (str): Select the region to be selected from the dataframe. Defaults to "PT"

    Returns:
        pd.DataFrame: cleaned data
    """

    print(f"----------- selected region: {region} -----------")

    # Splitting a conjugated column in multiple column
    life_expectancy[['unit', 'sex', 'age', 'region']] = \
        life_expectancy['unit,sex,age,geo\\time'].str.split(',', expand=True)

    # Dropping the conjugated column
    life_expectancy.drop('unit,sex,age,geo\\time', axis=1, inplace=True)

    # From wide to long
    life_expectancy = pd.melt(
        life_expectancy,
        id_vars=['unit', 'sex', 'age', 'region'],
        var_name="year"
    )
    
    # Cleaning values that were supposed to be null and values with strings attached
    life_expectancy['value'].replace(': ', None, inplace=True)
    print(life_expectancy)
    life_expectancy['value'] = life_expectancy['value'].str.split(' ', expand=True)[0]

    # Changing column types
    life_expectancy['year'] = life_expectancy['year'].astype(int)
    life_expectancy['value'] = life_expectancy['value'].astype(float)

    # Dropping rows that contain null values
    life_expectancy = life_expectancy.dropna()

    # Filtering only observations about PT
    life_expectancy = life_expectancy[life_expectancy["region"] == region]

    return life_expectancy

def save_data(
        life_expectancy: pd.DataFrame,
        output_filename: str):
    """It saves the data to the correct path

    Args:
        life_expectancy (pd.DataFrame): The cleaned DataFrame to be exported
        path_output (str): The path to export the data. Defaults to DATA_DIR / 'pt_life_expectancy.csv'
    """

    life_expectancy.to_csv(
        path_output, 
        index=False)


def main(
        region: str,
        input_filename: str = DATA_DIR / 'eu_life_expectancy_raw.tsv',
        output_filename: str = DATA_DIR / 'pt_life_expectancy.csv'):
    """It runs the following steps:
        1) Load the data
        2) Clean the data
        3) Export the data
    """

    life_expectancy = load_data(input_filename)
    cleaned_life_expectancy = clean_data(life_expectancy, region)
    save_data(cleaned_life_expectancy, output_filename)


if __name__ == "__main__":  # pragma: no cover

    parser = argparse.ArgumentParser(description='Inputs for cleaning function')
    parser.add_argument('--region', default="PT", type=str, help='The region to be selected')

    args = parser.parse_args()

    main(
        region=args.region
    )
