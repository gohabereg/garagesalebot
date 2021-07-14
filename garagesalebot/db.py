from pymongo import MongoClient
from os import getenv

from pymongo.database import Database

class DB:
    def __init__(self):
        self.client: MongoClient = MongoClient(getenv('MONGO_CONNECTION_URL'))
        self.db: Database = self.client.garagesalebot
