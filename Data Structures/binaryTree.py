"""
BinaryTree

    A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree 
    can have only 2 children, we typically name them the left and right child.

    A Binary Tree node contains following parts.

    Data
    Pointer to left child
    Pointer to right child
"""

class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None


    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:

            # We insert a node and push the existing 
            # child down one level in the tree

            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t


    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:

            # We insert a node and push the existing 
            # child down one level in the tree

            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
