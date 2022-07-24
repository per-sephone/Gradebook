'''
Nora Luna
CS 202
Project 5
BST.py

This file contains the TreeNode class and the BST class. The TreeNode class contains
the functions for set/get left/right pointers, as well as set/get data. It also
allows for display name of student, and display name + grade info for a student.
The BST class has both wrapper and recursive functions for insert, remove, search, 
and display. There are additional functions to help with removal and to find
the successor of a given node.
'''

import re
from Student import Student

#Tree node functions

class TreeNode:
    #constructor with argument
    def __init__(self, student):
        self._student = student
        self._left = None
        self._right = None
    
    #set left pointer
    def setLeft(self, newLeft):
        self._left = newLeft
        
    #set right pointer
    def setRight(self, newRight):
        self._right = newRight
    
    #get left pointer    
    def getLeft(self):
        return self._left
    
    #get right pointer
    def getRight(self):
        return self._right
    
    #get node data 
    def getData(self):
        return self._student
    
    #set node data
    def setData(self, newStudent):
        self._student = newStudent
    
    #display name only
    def display(self):
        (self._student).displayName()
    
    #display all student info    
    def displayAll(self):
        self._student.display()

 
#BST functions
        
class BST:
    #constructor
    def __init__(self):
        self._root = TreeNode(None)
        self._size = 0
    
    #insert wrapper function    
    def insert(self, student):
        
        if(self._root == None or self._size == 0):
            self._root.setData(student)
            self._size = self._size + 1
            return       
        
        self._insert(self._root, student)
     
    #insert recursive function        
    def _insert(self, root, student):
        
        #base case- reached the end
        if(root == None):
            root = TreeNode(student)
            self._size = self._size + 1
            return root
        
        #root > student, traverse left
        try:
            if(root.getData() > student):
                root.setLeft(self._insert(root.getLeft(), student))
                
        except TypeError: #checks overloaded operator
            print("Only class or string is supported")
        
        #root <= student, traverse right
        try:
            if(root.getData() <= student):
                root.setRight(self._insert(root.getRight(), student))
                
        except TypeError: #checks overloaded operator
            print("Only class or string is supported")
            
        return root
            
    #search wrapper function
    def search(self, key):
        
        if(self._root == None or self._size == 0):
            print("Tree is empty.")
            return
        
        try:
            self._search(self._root, key)
            
        except LookupError: 
            print("Not found")
    
    #search recursive function        
    def _search(self, root, key):
        
        if(root == None):
            raise LookupError
        
        #if we found the data, print it out
        if(root.getData() == key):
            root.displayAll()
            return

        try:
            #root is > key -> traverse left
            if(root.getData() > key):
                self._search(root.getLeft(), key)
                
        except TypeError: #checks overloaded operator
            print("Only class or string is supported")
        
        #root <= student, traverse right
        try:
            if(root.getData() < key):
                self._search(root.getRight(), key)
                
        except TypeError: #checks overloaded operator
            print("Only class or string is supported")
            
    #remove by name wrapper function
    def remove(self, key):
        
        if(self._root == None or self._size == 0):
            print("Tree is empty")
            return            
        
        try:
            temp = self._remove(self._root, key)
            
        except LookupError:
            print("Not found")
            
        #if removing the real root, reset the root            
        if(self._root.getData() == key):
            self._root = temp
            
    #remove by name recursive function    
    def _remove(self, root, key):
        if(root == None):
            raise LookupError
        
        if(root.getData() == key):
            root = self.removeHelper(root)
            self._size = self._size - 1
            return root
        
        try:
            #root is > key -> traverse left    
            if(root.getData() > key):
                root.setLeft(self._remove(root.getLeft(), key))
                
        except TypeError: #checks overloaded operator
            print("Only class or string is supported")
        
        #root <= student, traverse right
        try:
            if(root.getData() < key):
                root.setRight(self._remove(root.getRight(), key))
                
        except TypeError: #checks overloaded operator
            print("Only class or string is supported")
            
        
        return root
            
        
    #remove helper function
    def removeHelper(self, target):

        #two children
        if(target.getLeft() == None and target.getRight() == None):      
            return None
        
        #right child only
        elif(target.getLeft() == None and target.getRight() != None):
            return target.getRight()
        
        #left child only
        elif(target.getRight() == None and target.getLeft() != None):
            return target.getLeft()
        
        #two children
        elif(target.getRight() != None and target.getLeft() != None):
            
            #if successor is actually just the right child
            if((target.getRight()).getLeft() == None):
                (target.getRight()).setLeft(target.getLeft()) 
                target = target.getRight()
            
            #if successor is down the left side of the right child
            else:
                successor = self.findSuccessor(target.getRight())
                target.setData(successor.getData())
                target.setRight(self.removeSuccessor(target.getRight(), successor))
                successor = None    
             
        return target
        
    #finds inorder successor    
    def findSuccessor(self, target):

        if(target.getLeft() == None):
            return target
        
        return self.findSuccessor(target.getLeft(), target)
        
    def removeSuccessor(self, root, successor):
 
        if(root == None):
            return root
        
        if(root.getData() == successor.getData()):
            return None
        
        try:
            if(root.getData() > successor.getData()):
                root.setLeft(self._remove(root.getLeft(), successor))
                
        except TypeError: #checks overloaded operator
            print("Only class or string is supported")
        
        try:
            if(root.getData() < successor.getData()):
                root.setRight(self._remove(root.getRight(), successor))
                
        except TypeError: #checks overloaded operator
            print("Only class or string is supported")
           
        
    #display wrapper function    
    def display(self):

        if(self._root == None or self._size == 0):
            print()
            print("Tree is empty.")
            print()
            return
        self._display(self._root)
    
    #display recursive function    
    def _display(self, root):
        #base case
        if(root == None):
            return
        self._display(root.getLeft())
        root.display()
        self._display(root.getRight())