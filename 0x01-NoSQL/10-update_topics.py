#!/usr/bin/env python3
"""
Change school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    Function that changes all topics of a school document based on the name
    Args:
        mongo_collection: collection of documents
        name: school name to update
        topics: list of topics in a school
    """
    return mongo_collection.update_many({"name": name},
            {"$set": {"topics": topics}})
