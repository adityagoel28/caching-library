import Cache.fifo as fifo
import Cache.lifo as lifo
import Cache.lru as lru


print('Implementation of FIFO Cache:')
c = fifo.FIFOCache(2) # creating a FIFOCache with capacity 2
print(c._get(1)) # should return -1 because the cache is empty
c.put(1, 100) # should insert (1, 100) into the cache
print(c._get(1)) # should return 100
print('Length of the cache: ', len(c))
print('Length of the cache using module function: ', c.get_length())
c.put(2, 200)
print('Cache before clearing: ', c)
c._clear()
c.put(3, 300) # should insert (3, 300) into the cache
print('Cache before clearing and inserting (3, 300): ', c)
print(c._get(1)) # should return -1
print(c._get(2)) # should return -1

print('\nImplementation of LRU Cache:')
c = lru.LRUCache(2)
print(c._get(1))
c.put(1, 100)
print(c._get(1))
c.put(2, 200)
print(c)
c.put(3, 300)
print(c)
print(c._get(1))
print(c._get(2))

print('\nImplementation of LIFO Cache:')
c = lifo.LIFOCache(2)
print(c._get(1))
c.put(1, 100)
print(c._get(1))
c.put(2, 200)
print(c)
c.put(3, 300)
print(c)
print(c._get(1))
print(c._get(2))
print('Is the 2 present in the cache: ', c.contains(2))
c.delkey(2)
print('Is the 2 present in the cache after deleting: ', c.contains(2))