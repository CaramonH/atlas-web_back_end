#!/usr/bin/env python3
"""Function that changes all topics"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on name"""
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})