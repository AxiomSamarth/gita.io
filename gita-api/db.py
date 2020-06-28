from pymongo import MongoClient

def get_client(host='localhost', port=27017):
    client = MongoClient(host, port)
    return client