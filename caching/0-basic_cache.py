#!/usr/bin/env python3

""" 0-basic_cache """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class """

    def put(self, key,item):
        """add an item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ retirieve an item from the cache """
        return self.cache_data.get(key, None)
