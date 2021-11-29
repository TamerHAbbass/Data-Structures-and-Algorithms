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