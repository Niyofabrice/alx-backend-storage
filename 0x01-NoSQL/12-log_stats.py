#!/usr/bin/env python3
"""
Log stats
"""

from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
col = client.logs.nginx

number_of_documents = col.count_documents({})
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print(f"{number_of_documents} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {col.count_documents({'method':method})}")
print(f"{col.count_documents({'method':'GET','path':'/status'})} status check")
