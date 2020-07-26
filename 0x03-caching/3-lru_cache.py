#!/usr/bin/python3
""" This is an exercise in caching """


BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """ lru cache """

    def __init__(self):
        """ init """
        super().__init__()
        self.keys_in = []

    def put(self, key, item):
        """ put an item in """
        if item is None or key is None:
            return
        if len(self.keys_in) == BaseCaching.MAX_ITEMS:
            k = self.keys_in[0]
            print("DISCARD: " + str(k))
            del self.cache_data[k]
            self.keys_in = self.keys_in[1:]

        self.keys_in.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ get an item out """
        if key is None:
            return
        if key in self.keys_in:
            k = self.keys_in.remove(key)
            self.keys_in.append(k)
        return self.cache_data.get(key, None)
