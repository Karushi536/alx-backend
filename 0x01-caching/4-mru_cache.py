#!/usr/bin/env python3
"""
MRUCache module
"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that uses MRU (Most Recently Used) algorithm.
    """

    def __init__(self):
        """
        Initialize the MRUCache system.
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        Add an item to the cache.
        If key or item is None, this method does nothing.
        If the cache exceeds the MAX_ITEMS limit,
        discard the most recently used item.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.usage_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.usage_order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """
        Get an item by key.
        If key is None or doesn't exist, return None.
        Update the item's position in the usage order
        as it is now the most recently used.
        """
        if key in self.cache_data:
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data.get(key)
        return None
