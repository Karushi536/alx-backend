#!/usr/bin/env python3
"""
FIFOCache module
"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that
    uses FIFO (First-In-First-Out) algorithm.
    """

    def __init__(self):
        """
        Initialize the FIFOCache system.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache.
        If key or item is None, this method does nothing.
        If the cache exceeds the MAX_ITEMS limit,
        discard the first item added (FIFO).
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Get an item by key.
        If key is None or doesn't exist, return None.
        """
        return self.cache_data.get(key, None)
