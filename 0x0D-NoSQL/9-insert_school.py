#!/usr/bin/env python3
"""Insert a document in a mongodb collection"""


def insert_school(mongo_collection, **kwargs):
    """Insert a school from kwargs"""
    new_id = mongo_collection.insert_one(kwargs).inserted_id
    return new_id
