#!/usr/bin/env python3

""" 4-mru_caching """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class """

    def __init__(self):
        """ Initialize MRUCache instance with parent init """
        super().__init__()

    def put(self, key, item):
        """ Adds an item to the console """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Move the most recently used key to the end (MRU algorithm)
        del self.cache_data[key]
        self.cache_data[key] = self.cache_data[key]

        return self.cache_data[key]
