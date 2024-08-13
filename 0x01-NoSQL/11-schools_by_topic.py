#!/usr/bin/env python3
"""
Where can i learn Python?
"""


def schools_by_topic(mongo_collection, topic):
    """
    Function that returns the list of school having a specific topic
    Args:
        mongo_collection: collection of documents
        topic: that topic to search for
    Returns:
        List of school with the topic
    """
    return mongo_collection.find({"topics": {"$in": [topic]}})
