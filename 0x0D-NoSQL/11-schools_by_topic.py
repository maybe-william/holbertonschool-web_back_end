#!/usr/bin/env python3
"""Find documents in a mongodb collection"""


def schools_by_topic(mongo_collection, topic):
    """Find a school from topic"""
    return [x for x in mongo_collection.find({"topics": topic})]
