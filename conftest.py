'''
Nora Luna
CS 202
Project 4-5
conftest.py

This file contains my fixtures for Grade, Assignment, Lab, Exam,
Node, LinkedList, and Student.
'''

import pytest
from Grade import Grade, Assignment, Lab, Exam
from LinkedList import Node, LinkedList
from Student import Student

@pytest.fixture
def Empty_Grade_setup():
    object = Grade()
    return object

@pytest.fixture
def Grade_setup():
    object = Grade()
    object._score = 98.0
    object._weight = 30.0
    object._letter = 'A'
    object._feedback = "great!"
    return object

@pytest.fixture
def Assignment_setup():
    object = Assignment()
    object._numSubmissions = 3
    object._submissions = [100,100,95]
    object._weights = [10,10,80]
    object.calculateScore()
    object._letter = 'A'
    object._weight = 20.0
    object._feedback = "nice!"
    return object

@pytest.fixture
def Lab_setup():
    object = Lab()
    object._complete = True
    object._score = 100.0
    object._weight = 10.0
    object._letter = 'A'
    object._feedback = "good job!"
    return object

@pytest.fixture
def Exam_setup():
    object = Exam()
    object._extraCredit = 3.0
    object._score = 85.0
    object._weight = 40.0
    object._letter = 'B'
    object._feedback = "study more?"
    object.totalScore()
    return object

@pytest.fixture
def Node_setup():
    object = Node(Grade_setup)
    return object

@pytest.fixture
def LinkedList_setup():
    object = LinkedList()
    object._head = Node_setup
    #object._head.setNext(Node_setup)
    #object._head.getNext().setNext(Node_setup)
    return object

@pytest.fixture
def position_setup():
    object = 3
    return object
    
@pytest.fixture
def Student_setup():
    object = Student()
    object._name = "Nora"
    object._classGrade = Grade_setup
    return object
    