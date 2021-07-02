from pymongo import MongoClient

class conect:
    db = "" 
    def __init__(self,data) :
         client = MongoClient()
         db = client.db_wifu
         db.insert(data)
         
    
