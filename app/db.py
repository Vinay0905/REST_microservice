from flask import current_app
from pymongo import MongoClient
from werkzeug.local import LocalProxy

class PyMongoWrapper:
    def __init__(self):
        self.client=None
    def init_app(self,app):
        uri = app.config.get("MONGODB_URI")
        if not uri:
            raise RuntimeError("MONGODB_URI not configured")
        self.client = MongoClient(uri,serverSelectionTimeoutMS=5000)
        app.mongo_client=self.client
        app.db=self.client[app.config.get("MONGODB_DB","ZEKA")]

    @property
    def db(self):
        return current_app.db

mongo = PyMongoWrapper()

def _get_db():
    return current_app.db

db = LocalProxy(_get_db)
