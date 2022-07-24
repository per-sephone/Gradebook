'''
Nora Luna
CS 202
Project 4-5
Student.py

This files contains the functions for the Student class, which contains
a class grade, a name, and a linkedlist of grades. There is functionality
for adding name, a new assignment, remove a grade from the linked list,
display all grades, calculate and display class grade, and display all.
'''
from operator import truediv
from Grade import Grade, Assignment, Lab, Exam
from LinkedList import Node, LinkedList

#student class definitions  
        
class Student:
    #constructor
    def __init__(self):
        self._name = "none"
        self._classGrade = Grade()
        self._Grades = LinkedList()
        
    #less than < overload
    def __lt__(self, other):
        if isinstance(other, Student):
            if(self._name < other._name):
                return True
            else:
                return False
        elif isinstance(other, str):
            if(self._name < other):
                return True
            else:
                return False
        else:
            raise TypeError
        
    #less than or equal to <= overload
    def __le__(self, other):
        if isinstance(other, Student):
            if(self._name <= other._name):
                return True
            else:
                return False
        elif isinstance(other, str):
            if(self._name <= other):
                return True
            else:
                return False
        else:
            raise TypeError       
            
        
    #greater than > overload
    def __gt__(self, other):
        if isinstance(other, Student):
            if(self._name > other._name):
                return True
            else:
                return False
        elif isinstance(other, str):
            if(self._name > other):
                return True
            else:
                return False         
        else:
            raise TypeError
        
    #greater than or equal to >= overload
    def __ge__(self, other):
        if isinstance(other, Student):
            if(self._name >= other._name):
                return True
            else:
                return False
        elif isinstance(other, str):      
            if(self._name >= other):
                    return True
            else:
                return False      
        else:
            raise TypeError
        
    #equal overload
    def __eq__(self, other):
        if isinstance(other, Student):
            if(self._name == other._name):
                return True
            else:
                return False
        elif isinstance(other, str): 
            if(self._name == other):
                return True
            else:
                return False 
        else:
            raise TypeError
               
    #not equal overload
    def __ne__(self, other):
        if isinstance(other, Student):
            if(self._name != other._name):
                return True
            else:
                return False
        elif isinstance(other, str):     
            if(self._name != other):
                    return True
            else:
                return False
        else:
            raise TypeError
        
    #input student's name
    def inputName(self):
        self._name = input("Enter student's full name: ")
     
    #adds a new assigment to the list   
    def addAssignment(self):
        print("a. Assignment")
        print("b. Lab")
        print("c. Exam")
        temp = input("Enter the assignment type: ")
        temp = temp.lower()

        if(temp == 'a'):
            newGrade = Assignment()
            newGrade.newAssignment()
        elif(temp == 'b'):
            newGrade = Lab()
            newGrade.newLab()
        elif(temp == 'c'):
            newGrade = Exam()
            newGrade.newExam()
        else:
            print("Error, invalid response.")
            self.addAssignment()        
        
        self._Grades.insert(newGrade)
    
    #remove grade from the list    
    def removeGrade(self):
        temp = input("Enter the position of the grade to remove: ")
        try:
            temp = int(temp)
        except ValueError:
            print("Enter a valid position.")
            self.removeGrade()
              
        self._Grades.remove(temp)
     
    #displays list of grades    
    def displayGrades(self):
        self._Grades.display()
    
    #displays class grade    
    def displayClassGrade(self):
        if(self._classGrade._score == 0):
            print("No grade.")
            return
        print("Class grade: ", self._classGrade._score, "% ", self._classGrade._letter)

        
    #calculates the class grade using the assignment, lab, and exam grades
    def calculateClassGrade(self):
        
        #turn into wrapper function??
        self._classGrade._score = self._Grades.calculateTotalGrade()
        self._classGrade.calculateLetter()
    
    #displays student, class grade, and coursework grades    
    def display(self):
        print("Student: ", self._name)
        print("Class Grade: ", self.displayClassGrade())
        print("Coursework grades: ", self._Grades.display())
        
    def displayName(self):
        print(self._name)
        
    #menu for student    
    def studentOptions(self):
        print("----------Student Menu---------")
        print("a. Add a new grade")
        print("b. Remove a grade by position in the student's grade list")
        print("c. Display all grades for the student")
        print("d. Display student's class grade")
        print("e. Exit Student Menu")
    
    #menu for student grades    
    def studentMenu(self):
    
        self.inputName()
        print()
        self.studentOptions()
        key = input("Select from above options: ")
        print()
        key = key.lower()
        while(key == 'a' or key == 'b' or key == 'c' or key == 'd'):
            print()
            if(key == 'a'):
                self.addAssignment()
            elif(key == 'b'):
                self.removeGrade()
            elif(key == 'c'):
                self.displayGrades()
            elif(key == 'd'):
                self.calculateClassGrade()
                self.displayClassGrade() 
            elif(key == 'e'):
                pass
            else:
                print("Please select a, b, c, d, or e")
        
            print()    
            self.studentOptions()
            key = input("Select from above options: ")
           