import os
import requests

from dotenv import load_dotenv

load_dotenv(verbose=True)
API_KEY = os.environ['API_KEY']
url = "https://eventregistry.org/api/v1/article/getArticles"
LIMIT = 1


def fetch_articles():
    page = 1
    for request_count in range(LIMIT):  # מגבלת בקשות
        body = {
            "action": "getArticles",
            "keyword": "terror attack",
            "ignoreSourceGroupUri": "paywall/paywalled_sources",
            "articlesPage": page,
            "articlesCount": 100,
            "articlesSortBy": "socialScore",
            "articlesSortByAsc": False,
            "dataType": ["news", "pr"],
            "forceMaxDataTimeWindow": 31,
            "resultType": "articles",
            "apiKey": API_KEY
        }
        try:
            response = requests.post(url, json=body)
            if response.status_code == 200:
                data = response.json()
                return data["articles"]['results']
        except(Exception, TypeError):
            return []


