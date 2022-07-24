'''
Nora Luna
CS 202
Project 4-5
test_Student.py

This file contains my tests for Student.py
'''

import Student
import pytest

#studnet testing file

student = Student.Student()

def test___init__(Student_setup):
    assert Student_setup._name == "Nora"
    
def test___lt__(Student_setup):
    string = "Bear"
    assert Student_setup.__lt__(string) == False
    assert Student_setup.__lt__("Hello") == False
    assert Student_setup.__lt__(Student_setup) == False
    
def test___le__(Student_setup):
    assert Student_setup.__le__("Bear") == False
    assert Student_setup.__le__("Nora") == True
    assert Student_setup.__le__("Zebra") == True
    assert Student_setup.__le__("0") == False
    
def test___gt__(Student_setup):
    assert Student_setup.__gt__("Apple") == True
    assert Student_setup.__gt__("Zebra") == False
    assert Student_setup.__gt__(Student_setup) == False
    assert Student_setup.__gt__("Nora") == False
    
def test___ge__(Student_setup):
    assert Student_setup.__ge__("Apple") == True
    assert Student_setup.__ge__("Porch") == False
    assert Student_setup.__ge__("Nora") == True
    assert Student_setup.__ge__("3") == True
    
def test___eq__(Student_setup):
    assert Student_setup.__eq__("Nora") == True
    assert Student_setup.__eq__("Emma") == False
    assert Student_setup.__eq__(Student_setup) == True
    
def test___ne___(Student_setup):
    assert Student_setup.__ne__("Nora") == False
    assert Student_setup.__ne__(Student_setup) == False
    assert Student_setup.__ne__("Bread") == True
     
def test_inputName(Student_setup):
    assert Student_setup._name != None
    
def test_addAssignment():
    assert student._Grades != 0
    
    
def test_removeGrade():
    student.temp = 'a'
    assert ValueError

def test_calculateClassGrade():
    assert student._classGrade._score == 0
    
