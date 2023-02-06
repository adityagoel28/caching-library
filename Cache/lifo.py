from collections import OrderedDict
from threading import Lock

class LIFOCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.lock = Lock()

    def _get(self, key):
        with self.lock:
            if key not in self:
                return -1
            
            self.move_to_end(key)
            return self[key]

    def put(self, key, value):
        with self.lock:
            if key in self:
                self.move_to_end(key)
            self[key] = value
            if len(self) > self.capacity:
                self.popitem(last = True)
    
    def contains(self, key) -> bool:
        with self.lock: # thread safe
            if(self.get(key) != None):
                return True
            else:
                return False

    def delkey(self, key):
        with self.lock: # thread safe
            del self[key]

    def get_length(self):
        with self.lock:
            return len(self)

    def _clear(self): # using a different name than the built in clear() method
        """Clear all cache entries."""
        with self.lock:
            self.clear()