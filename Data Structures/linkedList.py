"""
Linked List

    The structure of a list is a collection of items where each item holds a relative position with respect to
    the others. Some possible operations are given below.

    - Time and Space Complexity
        - Time
            Indexing - O(n),
            Insertion - O(1),
            Search - O(n).
            Deletion - O(1),
    
        - Space
            Space - O(n)
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


"""
    - Unordered List

        - List() creates a new list that is empty. It needs no parameters and returns an empty list.
        
        - add(item) adds a new item to the list. It needs the item and returns nothing. Assume the item is not 
          already in the list.
        
        - remove(item) removes the item from the list. It needs the item and modifies the list. Assume the item 
          is present in the list.
        
        - search(item) searches for the item in the list. It needs the item and returns a boolean value.
        
        - isEmpty() tests to see whether the list is empty. It needs no parameters and returns a boolean value.
        
        - size() returns the number of items in the list. It needs no parameters and returns an integer.
        
        - append(item) adds a new item to the end of the list making it the last item in the collection. It needs 
         the item and returns nothing. Assume the item is not already in the list.
        
        - index(item) returns the position of item in the list. It needs the item and returns the index. Assume 
          the item is in the list.
        
        - insert(pos,item) adds a new item to the list at position pos. It needs the item and returns nothing.
          Assume the item is not already in the list and there are enough existing items to have position pos.
        
        - pop() removes and returns the last item in the list. It needs nothing and returns an item. Assume the
          list has at least one item.
        
        - pop(pos) removes and returns the item at position pos. It needs the position and returns the item. 
          Assume the item is in the list.
"""

class LinkedList:
    
    def __init__(self, head=None):
        self.head = head
        self.tail = None
        self.size = 0


    def isEmpty(self):
        return self.head == None


    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.size += 1


    def size(self):
        # For linked lists without a size attribute
        curr = self.head
        count = 0
        while curr != None:
            curr.getNext()
            count += 1
        return count


    def search(self, item):
        curr = self.head
        while curr != None and curr.getData() != item:
            if curr.getData() == item:
                found = True
            else:
                curr = curr.getNext()
        return found

        
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


"""
    - Ordered List

        - OrderedList() creates a new ordered list that is empty. It needs no parameters and returns an empty list.

        - add(item) adds a new item to the list making sure that the order is preserved. It needs the item and
           returns nothing. Assume the item is not already in the list.

        - remove(item) removes the item from the list. It needs the item and modifies the list. Assume the item is
          present in the list.

        - search(item) searches for the item in the list. It needs the item and returns a boolean value.

        - isEmpty() tests to see whether the list is empty. It needs no parameters and returns a boolean value.

        - size() returns the number of items in the list. It needs no parameters and returns an integer.

        - index(item) returns the position of item in the list. It needs the item and returns the index. Assume the
          item is in the list.

        - pop() removes and returns the last item in the list. It needs nothing and returns an item. Assume the list
          has at least one item.

        - pop(pos) removes and returns the item at position pos. It needs the position and returns the item. Assume
          the item is in the list.
"""


class OrderedLinkedList:

    def __init__(self):
        self.head = None


    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found


    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)