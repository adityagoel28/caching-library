from collections import OrderedDict
from threading import Lock

class FIFOCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity # max capacity of the cache
        self.lock = Lock() # lock for thread safety

    def _get(self, key):
        with self.lock: # thread safe
            if key not in self: # if key is not in the cache
                return -1
            
            self.move_to_end(key) # move the key to the end of the cache
            return self[key]

    def put(self, key, value):
        with self.lock:
            if key in self:
                self.move_to_end(key)
            self[key] = value
            if len(self) > self.capacity: # if the cache is full
                self.popitem(last = False) # remove the first item in the cache

    def contains(self, key) -> bool: # returns a boolean value
        with self.lock: # thread safe
            if(self.get(key) != None): # if the key is in the cache
                return True
            else:
                return False

    def delkey(self, key):
        with self.lock: # thread safe
            del self[key] # delete the key from the cache

    def get_length(self):
        with self.lock:
            return len(self)

    def _clear(self): # using a different name than the built in clear() method
        """Clear all cache entries."""
        with self.lock:
            self.clear() # clear the cache
    