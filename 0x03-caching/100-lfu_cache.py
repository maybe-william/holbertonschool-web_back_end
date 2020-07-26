#!/usr/bin/python3
""" This is an exercise in caching """


from time import time
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """ lfu cache """

    def __init__(self):
        """ init """
        super().__init__()
        self.keys_in = {}
        self.keys_time = {}

    def put(self, key, item):
        """ put an item in """
        if item is None or key is None:
            return

        curr = key in self.cache_data.keys()
        if len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS and not curr:
            lowk = None
            lowv = None
            lowt = None
            for k, v in self.keys_in.items():
                if lowk is None:
                    lowk = k
                if lowv is None:
                    lowv = v
                if lowt is None:
                    lowt = self.keys_time.get(k, time())
                if v == lowv:
                    if self.keys_time.get(k, time()) < lowt:
                        lowk = k
                        lowv = v
                        lowt = self.keys_time.get(k, time())
                if v < lowv:
                    lowk = k
                    lowv = v
                    lowt = self.keys_time.get(k, time())

            print("DISCARD: " + str(lowk))
            del self.cache_data[lowk]
            del self.keys_in[lowk]
            del self.keys_time[lowk]

        self.keys_in[key] = self.keys_in.get(key, 0) + 1
        self.keys_time[key] = time()
        self.cache_data[key] = item

    def get(self, key):
        """ get an item out """
        if key is None:
            return
        if key in self.cache_data.keys():
            self.keys_in[key] = self.keys_in.get(key, 0) + 1
            self.keys_time[key] = time()
        return self.cache_data.get(key, None)
