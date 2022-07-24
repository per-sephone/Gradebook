'''
Nora Luna
CS 202
Project 4-5
LinkedList.py

This file contains my node implementation and my linked list implementation.
The Node contains functions to set and get the data in the node, as well
as the pointers. The linked list supports add, remove, and display. It can
also calculate all the grades in the list in order to get the class grade.
'''

from Grade import Grade, Lab, Assignment, Exam

#node implementation

class Node():

    #constructor with arg        
    def __init__(self, grade):
        self._data = grade
        self._next = None

    #set next pointer
    def setNext(self, newNext):
        self._next = newNext
     
    #get next pointer   
    def getNext(self):
        return self._next
    
    #set data
    def setData(self, grade):
        self._data = grade
    
    #get data    
    def getData(self):
        return self._data
    
    #display node
    def display(self):
        (self._data).display()
 
#linked list class definitons 
    
class LinkedList():
    #constructor
    def __init__(self):
        self._head = None
        self._size = 0
    
    #insert at head    
    def insert(self, newData):
        newNode = Node(newData)
        
        if(self._size == 0):
            self._head = newNode
        else:
            newNode.setNext(self._head)
            self._head = newNode
            
        self._size = self._size + 1
      
    #display list - wrapper function
    def display(self):
        if(self._size == 0):
            print("Grade list is empty.")
            return
        
        self._displayRecurse(self._head)
    
    #display list - recursive function    
    def _displayRecurse(self, head):
        #base case
        if(head == None):
            return
        
        (head.getData()).display()
        print()
        #print(head._data)
                
        self._displayRecurse(head.getNext())
    
    #remove item by position - wrapper function    
    def remove(self, position):
        count = 1
        
        if(self._size == 0):
            print("List is empty.")
            return
        
        if(position > self._size):
            print("Position not found.")
            #exception handling
        
        if(position == 1): #remove head
            temp = self._head
            self._head = self._head.getNext()
            del temp
            return
        
        return self._removeRecurse(self._head, self._head, position, count)       
    
    #remove item by position - recursive function    
    def _removeRecurse(self, head, prev, position, count):
        #base case
        if(head == None):
            #print("Position not found.")
            return
        
        if(count == position):
            prev.setNext(head.getNext())
            del head
            return
            

        self._removeRecurse(head.getNext(), head, position, count + 1)
        

         
    def calculateTotalGrade(self):
        total = 0.0
        weight = 0.0
        
        if(self._size == 0):
            return 0
        if(self._size == 1):
            return self._head.getData().getScore()
        
        return self._calculateTotalGradeRecurse(self._head, total, weight)

    def _calculateTotalGradeRecurse(self, head, total, weight):
        
        #base case
        if(head == None):
            while(weight == 0):
                print("Weight must be greather than zero.")
                temp = input("Enter weight: ")
                try:
                    weight = int(temp)
                except ValueError:
                    print("Enter a valid weight.")
                    head._data.setWeight()
                    
            totalGrade = total/weight
            return totalGrade    
        
        total = total + (head.getData()).calculateWeightedGrade()
        weight = weight + (head.getData()).getWeight()
        
        return self._calculateTotalGradeRecurse(head.getNext(), total, weight)
