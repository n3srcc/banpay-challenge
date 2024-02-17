from pymongo import MongoClient
from config import Config

class Database:
    def __init__(self):
        self.client = MongoClient(Config.MONGODB_URI)
        self.db = self.client.get_default_database()

db = Database().db
    