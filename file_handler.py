import os

import pandas as pd
from dotenv import load_dotenv

load_dotenv('.env')


class FileHandler:
    """Transform csv -> df"""

    @staticmethod
    def read_csv(file: str) -> pd.DataFrame:
        """Convert csv file into DataFrame

        :param file: path to file
        """
        try:
            return pd.read_csv(filepath_or_buffer=file)

        except FileNotFoundError as err:
            raise err

    @staticmethod
    def to_csv(df: pd.DataFrame, filepath: str = os.environ.get('DATABASE_CSV_FILE')) -> None:
        df.to_csv(path_or_buf=filepath)
