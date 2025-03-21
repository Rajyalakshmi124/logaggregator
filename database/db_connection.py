from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
def get_db():  
    db = client["logaggregator"]  
    return db
