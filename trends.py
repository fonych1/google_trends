import os

import pandas as pd
from pytrends.request import TrendReq
from dotenv import load_dotenv

from file_handler import FileHandler

load_dotenv('.env')


class TrendAnalyzer:

    def __init__(self, filepath: str = os.environ.get('SEARCH_KEYWORDS_FILE')) -> None:
        self.trends = TrendReq()
        self.keywords = FileHandler.read_csv(file=filepath)
        self.dataframe = pd.DataFrame()

    def data(self):
        for kws in self._chunks(self.keywords['keyword'].to_list(), 5):
            self.trends.build_payload(kws)
            trends_over_time = self._get_trends_over_time()

            if not self.dataframe.empty:
                self.dataframe = pd.merge(self.dataframe, trends_over_time, on='date')

            else:
                self.dataframe = trends_over_time

    def _get_trends_over_time(self) -> pd.DataFrame:
        trends_over_time = self.trends.interest_over_time()
        trends_over_time = trends_over_time[trends_over_time.columns.drop('isPartial')]

        return trends_over_time

    def _chunks(self, lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]


class SearchInterest:

    def __init__(self):
        self.df_search_interest_over_time = self._get_data()

    def _get_data(self, filepath: str = os.environ.get('DATABASE_CSV_FILE')):
        return FileHandler.read_csv(filepath)
