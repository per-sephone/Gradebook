'''
Nora Luna
CS 202
Project 5
test_BST.py

This file contains the tests for the BST.py file. It contains test for
the TreeNode class and the BST class.
'''

from BST import TreeNode, BST
from Student import Student
from conftest import Student_setup
import pytest


#tests for TreeNode
student = Student()
node = TreeNode(student)
student2 = Student()
node2 = TreeNode(student2)
student3 = Student()
node3 = TreeNode(student3)

def test___init__(student):
    assert node._left == None
    assert node._right == None
    assert node._student == student
    
def test_setLeft():
    assert node._left == None
    node.setLeft(node2)
    assert node._left == node2
    
def test_setRight():
    assert node._right == None
    node.setRight(node2)
    assert node._right == node2
    
def test_setData():
    assert node._student == student
    
def test_getLeft():
    node.setLeft(node2)
    assert node.getLeft() == node2
    
def test_getRight():
    node.setRight(node2)
    assert node.getRight() == node2 

def test_getData():
    node.setData(student)
    assert node.getData() == student


#tests for BST

bst = BST()

def test___init__():
    bst._size == 0
    bst._root == None
    
def test_insert():
    bst.insert(student)
    assert bst._size == 1
    bst.insert(student2)
    assert bst._size == 2
    bst.insert(student3)
    assert bst._size == 3
    
def test_search():
    empty = "empty"
    bst.insert(student)
    bst.insert(student2)
    bst.insert(student3)
    assert bst.search(empty) == None
    
def test_remove():
    assert bst._size == 0
    bst.insert(student)
    bst.insert(student2)
    bst.insert(student3)
    assert bst._size == 3
    bst.remove(student2)
    assert bst._size == 2
    bst.remove(student3)
    assert bst._size ==1
    
def test_removeHelper():
    bst.insert(student)
    bst.insert(student2)
    bst.insert(student3)
    assert bst.removeHelper(node) == None
    
def test_findSuccessor():
    bst.insert(student)
    bst.insert(student2)
    bst.insert(student3)
    assert bst.findSuccessor(node) == node
    
def test_removeSuccessor():
    bst.insert(student)
    bst.insert(student2)
    bst.insert(student3)
    assert bst.removeSuccessor(bst._root, node3) == None
    
    