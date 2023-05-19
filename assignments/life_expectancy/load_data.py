from abc import ABC, abstractmethod
import pandas as pd
import json
from typing import List, Dict


class LoadData(ABC):
    """An interface to load data from different formats
    """

    @abstractmethod
    def load_file(self, path) -> pd.DataFrame:
        pass

class LoadTSV(LoadData):
    def load_file(self, path) -> pd.DataFrame:
        """It loads the .tsv that will be cleaned and exported

        Args:
            path (str): Path to the data to be imported.

        Returns:
            pd.DataFrame: Dataframe to be cleaned
        """

        print("========== Running TSV pipeline ==========")

        life_expectancy = pd.read_csv(
            path,
            sep='\t')

        return life_expectancy


class LoadJSON(LoadData):
    def load_file(self, path) -> List[Dict]:
        """It loads the .json that will be cleaned and exported

        Args:
            path (str): Path to the data to be imported.

        Returns:
            pd.DataFrame: Dataframe to be cleaned
        """

        print("========== Running JSON pipeline ==========")

        with open(path, 'r') as json_file:
            life_expectancy = json.load(json_file)

        return life_expectancy