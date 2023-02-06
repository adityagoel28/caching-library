# caching-library
Designing and Implementing an in-memory caching library for general use

## Must Have
- ✅ Support for multiple Standard Eviction Policies ( FIFO, LRU, LIFO )
- ✅ Support to add custom eviction policies
## Good To Have
- ✅ Thread saftey

## In-memory caching
In-memory caching is a technique for temporarily storing data in a high-speed memory, such as RAM, so that it can be quickly retrieved and used again without having to be recalculated or fetched from a slower storage system, such as a hard disk drive or network.

The main benefit of in-memory caching is improved performance. By keeping frequently used data in memory, applications can access it much faster, reducing the time it takes to retrieve the data and perform operations on it. This can significantly improve the responsiveness and performance of the application, especially in cases where the data is used frequently or in real-time applications.

In-memory caching is commonly used in a variety of applications, including databases, web applications, and caching proxies, to name a few. In these systems, the cache is managed in a way that balances the tradeoff between the size of the cache, the speed of access, and the cost of storing data in memory. The cache is designed to hold the most frequently used data and remove the least frequently used data as necessary to make room for new data.

There are several algorithms for managing in-memory caches, including First-In-First-Out (FIFO), Least Recently Used (LRU), and Most Recently Used (MRU), each with its own trade-offs and advantages, depending on the need.

## Standard eviction policies
Standard eviction policies refer to commonly used algorithms for removing items from a cache when it reaches its maximum size limit. The three most common standard eviction policies are:

- FIFO (First-In-First-Out) - In this policy, the oldest item (first item added) is removed when the cache reaches its maximum size limit.
- LRU (Least Recently Used) - In this policy, the item that was least recently used is removed when the cache reaches its maximum size limit.
- LIFO (Last-In-First-Out) - In this policy, the most recently added item is removed when the cache reaches its maximum size limit.

These standard eviction policies are widely used and well-known, and their behavior is well understood, making them easy to implement and use in a cache.

## Thread safety
Thread safety refers to the ability of a piece of code to handle multiple threads accessing it simultaneously without any adverse effects. In other words, it means that if multiple threads access the same code or data simultaneously, they will not interfere with each other and the results will still be correct.

In the context of caching, thread safety is important because we want to make sure that multiple threads can access the cache simultaneously without any data corruption or incorrect behavior. For example, if two threads try to insert an item into the cache at the same time, we want to make sure that only one of them succeeds and the other thread waits until the first one is finished.

To achieve thread safety in a cache, we can use synchronization mechanisms such as locks to ensure that only one thread can access the cache at a time. For example, in the cache implementation provided below, a threading.Lock is used to synchronize access to the cache.

## Methodology
An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted. The order the items are inserted is remembered by OrderedDict.

### Example with LRUCache
`OrderedDict` is used as the parent class for the LRUCache class. This means that the LRUCache class inherits all the attributes and methods of the OrderedDict class and can use them as its own. By using OrderedDict as the parent class, the LRUCache class can take advantage of the ordered dictionary data structure to implement an LRU cache.
<br><br>
The `threading` library in Python provides support for multithreaded programming. The `Lock` class in this library provides a simple way to synchronize access to a resource shared by multiple threads. A lock is an object that is used to enforce mutual exclusion, ensuring that only one thread at a time can access a shared resource. The acquire method of the lock can be used to request ownership of the lock, and the release method can be used to release the lock once the thread is finished using the shared resource. This allows multiple threads to work concurrently on the same resource, without interfering with each other.
<br>
In the implementation of the LRUCache class, the lock is released when the with statement block for the lock is exited. In other words, the lock is released when the indented code block following the with `self.lock:` statement is completed. This is done in all the methods, where the lock is used to synchronize access to the cache. By releasing the lock after the critical section of code is executed, other threads can acquire the lock and access the shared resource, ensuring that the cache remains available for use by multiple threads.
