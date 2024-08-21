#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that uses LIFO (Last-In-First-Out) algorithm.
    """

    def __init__(self):
        """
        Initialize the LIFOCache system.
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Add an item to the cache.
        If key or item is None, this method does nothing.
        If the cache exceeds the MAX_ITEMS limit,
        discard the last item added (LIFO).
        """
        if key is not None and item is not None:
            if len(
                    self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print(f"DISCARD: {self.last_key}")
                del self.cache_data[self.last_key]

            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """
        Get an item by key.
        If key is None or doesn't exist, return None.
        """
        return self.cache_data.get(key, None)
