#/!usr/bin/env python2.7
#-*- coding:utf-8 -*-

import logging
import collections

class LRUCache(object):
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.dict = collections.OrderedDict()

    # @return an integer
    def get(self, key):
        try:
            value = self.dict[key]
            del self.dict[key]
            self.dict[key] = value
            return value
        except:
            return None

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        try:
            del self.dict[key]
            self.dict[key] = value
        except:
            if self.length == self.capacity:
                self.dict.popitem(last = False)
                self.length -= 1
            self.dict[key] = value
            self.length +=1

CACHE = LRUCache(10000)

if __name__ == '__main__':
    CACHE.set("h", ('_mM3HcY7hbJ9SkYnngN', 'mytablex', '5fadca08-aec9-4e74-b74f-6196b82d5575'))
    CACHE.set("h", ('_mM3HcY7hbJ9SkYnngN', 'mytablex', '5fadca08-aec9-4e74-b74f-6196b82d5575'))
    CACHE.set("h", ('_mM3HcY7hbJ9SkYnngN', 'mytablex', '5fadca08-aec9-4e74-b74f-6196b82d5575'))
    CACHE.set("h", ('_mM3HcY7hbJ9SkYnngN', 'mytablex', '5fadca08-aec9-4e74-b74f-6196b82d5575'))
    CACHE.set("h", ('_mM3HcY7hbJ9SkYnngN', 'mytablex', '5fadca08-aec9-4e74-b74f-6196b82d5575'))
    CACHE.set("h", ('_mM3HcY7hbJ9SkYnngN', 'mytablex', '5fadca08-aec9-4e74-b74f-6196b82d5575'))
    CACHE.set("h", ('_mM3HcY7hbJ9SkYnngN', 'mytablex', '5fadca08-aec9-4e74-b74f-6196b82d5575'))

    print CACHE.get("h")
