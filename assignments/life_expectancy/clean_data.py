import pandas as pd
# from abc import ABC, abstractmethod

# class CleanData(ABC):
#     """An interface to load data from different formats
#     """
#     @abstractmethod
#     def clean_data(
#             self, 
#             life_expectancy_data: pd.DataFrame, 
#             region: str) -> pd.DataFrame:
#         pass

# class CleanTSV(CleanData):

def clean_data(
        life_expectancy_data: pd.DataFrame,
        region: str = "PT") -> pd.DataFrame:
    """It cleans the data

    Args:
        life_expectancy (pd.DataFrame): The df that will be cleaned by the function.
        region (str): Select the region to be selected from the dataframe. Defaults to "PT"

    Returns:
        pd.DataFrame: cleaned data
    """

    print(f"----------- selected region: {region} -----------")

    life_expectancy = life_expectancy_data.copy()

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
    life_expectancy['value'] = life_expectancy['value'].str.split(' ', expand=True)[0]

    # Changing column types
    life_expectancy['year'] = life_expectancy['year'].astype(int)
    life_expectancy['value'] = life_expectancy['value'].astype(float)

    # Filtering observations of a specific region
    life_expectancy = life_expectancy[life_expectancy["region"] == region]

    # Dropping rows that contain null values
    life_expectancy = life_expectancy.dropna()

    return life_expectancy.reset_index(drop=True)
