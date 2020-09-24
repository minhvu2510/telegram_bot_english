# code by vunm
from pymongo import MongoClient
# import sys
# sys.path.append('../')
from settings import *
print (MONGO_CLIENT)
client = MongoClient(MONGO_CLIENT)
# client_report = MongoClient(MONGO_REPORT)
db = client[MONGO_DATABASE]
from redis import Redis
r = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


def check_collection_exist(collection):

    if collection in db.list_collection_names():
        return True
    else:
        return False
def find_by_dict(collection, dictionary=None):

    if check_collection_exist(collection):
        col = db[collection]
        result = col.find(dictionary)
    else:
        result = None
    return result
def get_all_topics():
    return db.collection_names()
def get_total_record(collection):
    col = db[collection]
    return col.count();
    # return db.list_collection_names()
# -------------------redis-------------------
def get_all_keys_redis():
    return r.keys();
def get_number_record_redis():
    return r.dbsize()
def get_item_redis(key):
    return r.get(key)