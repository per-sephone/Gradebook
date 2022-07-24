'''
Nora Luna
CS 202
Project 4-5
test_LinkedList.py

This file contains the tests for the LinkedList.py file. It contains test for
the Node class and the LinkedList class.
'''

from LinkedList import Node, LinkedList
import pytest

from conftest import Grade_setup

#testing Node functions

node = Node(Grade_setup)

def test___init__():
    assert node._next == None

def test_setNext(Node_setup):
    assert Node_setup._next == None
    
def test_getNext(Node_setup):
    assert Node_setup._next == None
    
def test_setData():
    node.setData(50)
    assert node._data == 50
    
def test_getData(Node_setup):
    assert Node_setup._data == Grade_setup
    
#tested LinkedList functions

LL = LinkedList()

def test___init__():
    assert LL._head == None
    assert LL._size == 0
    assert LL._size != 1

def test_insert(LinkedList_setup, Grade_setup):
    assert LinkedList_setup._size != None
    assert LinkedList_setup._head != None
    LinkedList_setup.insert(Grade_setup)
    assert LinkedList_setup._size == 1
    LinkedList_setup.insert(Grade_setup)
    assert LinkedList_setup._size == 2
    
def test_remove():
    LL.insert(Grade_setup)
    LL.insert(Grade_setup)
    LL.insert(Grade_setup)
    LL.remove(1)
    assert LL._size == 3
    
def test__calculateTotalGradeRecurse():
    assert LL._calculateTotalGradeRecurse(LL._head, 100, 50) == 2
    assert LL._calculateTotalGradeRecurse(LL._head, 80, 20) == 4
    
    
