#!/usr/bin/env python3
"""
List all documents in a collection
"""

import pymongo


def list_all(mongo_collection):
    """
    Function that lists all documents in a collection
    Args:
        mongo_collection: collection of documents
    Returns:
        an empty list if no documnets in collection
    """
    return mongo_collection.find()
