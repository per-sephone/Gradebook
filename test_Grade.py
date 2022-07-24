'''
Nora Luna
CS 202
Project 4-5
test_Grade.py

This file contains my tests for my Grade file.
'''

import Grade
import pytest

#testing grade functions

object = Grade.Grade()

def test___init__():
    assert object._score == 0.0
    assert object._weight == 0.0
    assert object._letter == 'X'
    assert object._feedback == "none"
    
def test_getScore():
    assert object._score == 0.0

def test_getScore(Grade_setup):
    assert Grade_setup._score == 98.0
    
def test_getWeight():
    assert object._weight == 0.0
    
def test_getWeight(Grade_setup):
    assert Grade_setup.getWeight() == 30.0
    
def test___eq__(Grade_setup, Empty_Grade_setup):
    assert (Grade_setup == Empty_Grade_setup) == False
    
def test___ne__(Grade_setup, Empty_Grade_setup):
    assert(Grade_setup != Empty_Grade_setup) == True    

def test_inputScore(Grade_setup):
    assert Grade_setup._score != None
    
def test_setWeight():
    g = Grade.Grade()
    g.setWeight(40.0)
    assert g._weight == 40.0

def test_inputWeight():
    assert object._weight != 0.0
    
def test_getWeight():
    assert object.getWeight() == 0.0
    
def test_calculateLetter(Grade_setup):
    assert Grade_setup._letter == 'A'
    
def test_calculateWeightedGrade(Grade_setup):
    assert Grade_setup.calculateWeightedGrade() == 2940
    assert Grade_setup.calculateWeightedGrade() != 1
    

#testing assignment functions

assign = Grade.Assignment()

def test___init__():
    assert assign._numSubmissions == 3
    #assert assign._submissions == [0]
    #assert assign._weights == [0]
    
def test_changeNumSubmissions():
    assert assign._numSubmissions != 0
    assert assign._numSubmissions == 3

def test_inputSubmissions(Assignment_setup):
    assert Assignment_setup._submissions != None

def test_inputWeight(Assignment_setup):
    assert Assignment_setup._weights != None
    
def test_calculateScore(Assignment_setup):
    assert Assignment_setup._score == 96
    
def test_weightedGrade(Assignment_setup):
    assert (Assignment_setup._submissions[0] * Assignment_setup._weights[0]) == 1000
    assert (Assignment_setup._submissions[1] * Assignment_setup._weights[1]) == 1000
    assert (Assignment_setup._submissions[2] * Assignment_setup._weights[2]) == 7600
    
#testing Lab functions

lab = Grade.Lab()

def test___init__():
    assert lab._complete == False

def test_inputComplete(Lab_setup):
    assert Lab_setup._complete == True
    assert Lab_setup._score == 100

def test_newLab(Lab_setup):
    assert Lab_setup._score != 0
    assert Lab_setup._letter != 'X'
    
#testing Exam functions

exam = Grade.Exam()

def test___init__():
    assert exam._extraCredit == 0.0
    assert exam._totalScore == 0.0

def test_inputExtraCredit(Exam_setup):
    assert Exam_setup._extraCredit != 0
    
def test_totalScore(Exam_setup):
    assert Exam_setup._totalScore == 88.0
    assert Exam_setup._totalScore != 100.0
    

    
    


