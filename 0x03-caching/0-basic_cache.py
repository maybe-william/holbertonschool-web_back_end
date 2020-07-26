#!/usr/bin/python3
""" This is an exercise in caching """


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache extends BaseCaching:
    """ no limit cache """

    def put(self, key, item):
        """ put an item in """
        if item is None or key is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ get an item out """
        if key is None:
            return
        return self.cache_data.get(key, None)
