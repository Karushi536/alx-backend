#!/usr/bin/env python3
"""
LFUCache module
"""

from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """
    LFUCache is a caching system that uses LFU
    (Least Frequently Used) algorithm.
    If multiple items have the same usage frequency,
    the LRU (Least Recently Used)
    algorithm is used to determine which item to discard.
    """

    def __init__(self):
        """
        Initialize the LFUCache system.
        """
        super().__init__()
        self.usage_count = {}  # Tracks the frequency of access for each key
        self.usage_order = {}  # Tracks the order of usage for tie-breaking

    def put(self, key, item):
        """
        Add an item to the cache.
        If key or item is None, this method does nothing.
        If the cache exceeds the MAX_ITEMS limit,
        discard the least frequently used item.
        If there is a tie, discard the least recently used item.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update existing key
                self.cache_data[key] = item
                self.usage_count[key] += 1
                self.usage_order[key] = len(self.usage_order)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Find the least frequently used item
                    min_freq = min(self.usage_count.values())
                    lfu_keys = [k for k, v in self.usage_count.items() if v == min_freq]
                    if len(lfu_keys) > 1:
                        # If there's a tie, use LRU to break the tie
                        lfu_key = min(lfu_keys, key=lambda k: self.usage_order[k])
                    else:
                        lfu_key = lfu_keys[0]

                    del self.cache_data[lfu_key]
                    del self.usage_count[lfu_key]
                    del self.usage_order[lfu_key]
                    print(f"DISCARD: {lfu_key}")

                # Add the new item
                self.cache_data[key] = item
                self.usage_count[key] = 1
                self.usage_order[key] = len(self.usage_order)

    def get(self, key):
        """
        Get an item by key.
        If key is None or doesn't exist, return None.
        Update the frequency and order of usage.
        """
        if key in self.cache_data:
            self.usage_count[key] += 1
            self.usage_order[key] = len(self.usage_order)
            return self.cache_data.get(key)
        return None
