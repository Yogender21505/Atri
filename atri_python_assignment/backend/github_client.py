from backend.types import UniqueViewsDocument
from typing import List
import requests


def fetch_github_unique_views() -> List[UniqueViewsDocument]:
    """
    Fetch GitHub data.
    """
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    response = requests.get(url)
    print("Status code: ", response.status_code)
    response_dict:response.json()
    # response_dict.keys()
    pass