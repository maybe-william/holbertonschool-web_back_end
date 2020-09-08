#!/usr/bin/env python3
"""List all documents in a mongodb collection"""


def list_all(mongo_collection):
    """Return a list of all documents in a collection or an empty list"""
    return [x for x in mongo_collection.find()]
