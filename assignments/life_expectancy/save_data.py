import pandas as pd

def save_data(
        life_expectancy: pd.DataFrame,
        output_filename: str):
    """It saves the data to the correct path

    Args:
        life_expectancy (pd.DataFrame): The cleaned DataFrame to be exported
        path_output (str): The path to export the data. 
                           Defaults to DATA_DIR / 'pt_life_expectancy.csv'
    """

    life_expectancy.to_csv(
        output_filename,
        index=False)
