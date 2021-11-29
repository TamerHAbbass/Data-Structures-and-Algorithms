"""
Queue

    A queue is an ordered collection of items where the addition of new items happens at one end, called the 
    “rear,” and the removal of existing items occurs at the other end, commonly called the “front.” As an 
    element enters the queue it starts at the rear and makes its way toward the front, waiting until that time 
    when it is the next element to be removed.
"""

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


"""
Python Queue module implementation.
"""
from queue import Queue

q = Queue(maxsize = 3)
 
# Add items to a queue
q.put('a')
 
# Remove items from queue
q.get()


"""
Deque implementation of a queue.
"""
from collections import deque

customers = deque()

# Add items to a queue
customers.append("Jane")

# Remove items from a queue
customers.popleft()


"""
Alternate Deque implementation.
"""
from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        try:
            return self._items.popleft()
        except IndexError:
            raise IndexError("dequeue from an empty queue") from None

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def __iter__(self):
        yield from self._items

    def __reversed__(self):
        yield from reversed(self._items)

    def __repr__(self):
        return f"Queue({list(self._items)})"