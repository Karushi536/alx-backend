#!/usr/bin/env python3
"""
BasicCache module
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    BasicCache is a caching system with no limit.
    """

    def put(self, key, item):
        """
        Add an item to the cache.
        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key.
        If key is None or doesn't exist, return None.
        """
        return self.cache_data.get(key, None)
