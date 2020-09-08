#!/usr/bin/env python3
"""Update documents in a mongodb collection"""


def update_topics(mongo_collection, name, topics):
    """Update a school from name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
