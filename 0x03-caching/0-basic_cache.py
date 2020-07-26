#!/usr/bin/python3
""" This is an exercise in caching """


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("must implement put in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("must implement get in your cache class")


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
