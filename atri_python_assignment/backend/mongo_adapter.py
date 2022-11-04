from backend.types import UniqueViewsDocument
from typing import List
from backend.github_client import fetch_github_unique_views
import pymongo
from pymongo import MongoClient
client=0
class MongoDbAdapter():
    
    def get_client(self):
        # Add your code here to create a mongo db client
        # that can read and write data from github_stats collection
        client = MongoClient(self)

        # create new database and client collection
        pass

    def get_data() -> List[UniqueViewsDocument]:
        # Add your code here to read data from github_stats collection
        data = UniqueViewsDocument.find()
        for record in data:
            print(record)
        pass
    
    def store_data(data: List[UniqueViewsDocument]):
        # Add your code here to store data in github_stats collection
        # Save each entry in the data list as a mongodb document
        mydatabase = client[fetch_github_unique_views]
        git_stats = mydatabase["name","score"]
        List[UniqueViewsDocument]=git_stats
        pass