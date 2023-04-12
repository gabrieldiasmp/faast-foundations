"""Pytest configuration file"""
import pandas as pd
import pytest

from . import FIXTURES_DIR, OUTPUT_DIR

@pytest.fixture(scope="session")
def life_expectancy_sample() -> pd.DataFrame:
    """Fixture to create a sample of the data"""

    df_dict = {
        'unit,sex,age,geo\\time': {
            0: 'YR,F,Y1,AL',
            1: 'YR,F,Y1,AM',
            2: 'YR,F,Y1,AT',
            3: 'YR,F,Y1,AZ',
            4: 'YR,F,Y1,BE'},
        '2021 ': {0: ': ', 1: ': ', 2: ': ', 3: ': ', 4: ': '},
        '2020 ': {0: '79.4 ', 1: ': ', 2: '82.9 ', 3: ': ', 4: '82.3 '},
        '2019 ': {0: '80.4 ', 1: '79.1 ', 2: '83.5 ', 3: '78.6 ', 4: '83.6 '},
        '2018 ': {0: '80.2 ', 1: '79.2 ', 2: '83.3 ', 3: '78.1 ', 4: '83.2 '}}

    df_sample = pd.DataFrame.from_dict(data = df_dict)

    return df_sample

@pytest.fixture(scope="session")
def life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""

    df_dict = {
        'unit': {0: 'YR', 1: 'YR', 2: 'YR'},
        'sex': {0: 'F', 1: 'F', 2: 'F'},
        'age': {0: 'Y1', 1: 'Y1', 2: 'Y1'},
        'region': {0: 'AT', 1: 'AT', 2: 'AT'},
        'year': {0: 2020, 1: 2019, 2: 2018},
        'value': {0: 82.9, 1: 83.5, 2: 83.3}
    }

    df_expected = pd.DataFrame.from_dict(data = df_dict)

    return df_expected

@pytest.fixture(scope="session")
def raw_data() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""

    raw_data = pd.read_csv(
        FIXTURES_DIR / "raw_data.tsv",
        sep='\t'
    )

    return raw_data


@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""

    pt_life_expectancy_actual = pd.read_csv(
        FIXTURES_DIR / "pt_life_expectancy_expected.csv"
    )

    return pt_life_expectancy_actual


@pytest.fixture(autouse=True)
def run_before_and_after_tests() -> None:
    """Fixture to execute commands before and after a test is run"""
    # Setup: fill with any logic you want

    yield # this is where the testing happens

    # Teardown : fill with any logic you want
    file_path = OUTPUT_DIR / "pt_life_expectancy.csv"
    file_path.unlink(missing_ok=True)
