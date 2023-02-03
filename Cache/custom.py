from collections import OrderedDict
from threading import Lock

class CustomCache(OrderedDict):

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
                pass
                # item will be popped based on the eviction policy

    def __contains__(self, key) -> bool:
        if(self.get(key) != None):
            return True
        else:
            return False

    def __delkey__(self, key):
        del self[key]

    def _len(self):
        with self.lock:
            return len(self)

    def _clear(self):
        """Clear all cache entries."""
        with self.lock:
            self.clear()