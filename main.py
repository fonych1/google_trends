import json

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from trends import SearchInterest


app = FastAPI()


@app.get('/search_interest/{keyword}')
def search_interest(keyword: str):
    se = SearchInterest()
    try:
        data = se.df_search_interest_over_time.get(['date', keyword]).set_index(keys='date')
        data = data.sort_values(by=keyword, ascending=False)
        return JSONResponse(json.loads(data.to_json()))
    except:
        return {}
