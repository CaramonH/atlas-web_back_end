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
                # Get the most recently used key and remove it from the cache
                discarded_key = max(self.cache_data, key=self.cache_data.get)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Move the most recently used key to the end
        value = self.cache_data.pop(key)
        self.cache_data[key] = value

        return value
