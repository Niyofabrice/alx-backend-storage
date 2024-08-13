#!/usr/bin/env python3
"""
Insert a document on python
"""


def insert_school(mongo_collection, **kwargs):
    """
    Function that inserts a new document in a collection base on kwargs
    Args:
        mongo_collection: collection of documents
        kwargs: attributes for the new document
    Returns:
        ID of the new document
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
