import os
from pymongo import MongoClient
import pymongo


def getCollection(collection):
    my_client = MongoClient(os.environ["MONGO_URI"])
    db = my_client['bsergg']
    col = db[collection]
    return col
