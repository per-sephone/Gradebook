'''
Nora Luna
CS 202
Project 4-5
Grade.py

This file contains the Grade base class and the 3 derived classes: Assignement,
Lab, and Exam. Grade contains a score(grade), weight, letter grade, and a space for
feedback. Assignment contains two numpy arrays that contains a list of
progress submissions and their cooresponding weights, as well as the number
of submissions in the list. Lab contains a boolean to check whether it was completed
or not. Exam has an extra credit option and a total score. Grade contains functions
to set the different variables. There is a function to calculate the letter grade
based on the number score. There are two overloaded operators as well. There is a 
function to calculate weighted grade. The Assignment functions allow the user to
change the number of submissions, enter the submission scores and weights, calculate
the total score based on the submissions, and calculates the weighted grade. The
lab class allows the score to auto calculate depending on whether the Lab
was completed or not. The Exam class allos the user to input extra credit and
calculate the total score. 
'''

import numpy as np

#Grade class definitions

class Grade:
    #constructor
    def __init__(self):
        self._score = 0.0
        self._weight = 0.0
        self._letter = 'X'
        self._feedback = "none"
        
    def getScore(self):
        return self._score
    
    def getWeight(self):
        return self._weight

    #operator overloading ==
    def __eq__(self, other):
        if(self._score == other._score and self._weight == other._weight and self._letter == other._letter and self._feedback == other._feedback):
            return True
        else:
            return False
        
    #operator overloading !=
    def __ne__(self, other):
        if(self._score != other._score or self._weight != other._weight or self._letter != other._letter or self._feedback != other._feedback):
            return True
        else:
            return False
    
    #user enters score
    def inputScore(self):
        temp = input("Enter score: ")
        try:
            self._score = float(temp)
        except ValueError:
            print("Enter a valid score.")
            self.inputScore()
    
    #set weight with an argument
    def setWeight(self, value):
        self._weight = value
            
    #user enters weight
    def inputWeight(self):
        temp = input("Enter weight: ")
        try:
            self._weight = float(temp)
        except ValueError:
            print("Enter a valid weight.")
            self.inputWeight()
    
    #returns weight
    def getWeight(self):
        return self._weight
        
    #calculates letter grade
    def calculateLetter(self):
        if (self._score >= 90.0):
            self._letter = 'A'
        elif (self._score >= 80.0):
            self._letter = 'B'
        elif (self._score >= 70.0):
            self._letter = 'C'
        elif (self._score >= 60.0):
            self._letter = 'D'
        else:
            self._letter = 'F'
  
    #user enters feedback for grade
    def inputFeedback(self): 
        self._feedback = input("Enter feedback: ")
    
    #returns a weighted grade
    def calculateWeightedGrade(self):
        return self._score * self._weight
    
    #add a new grade input
    def newGrade(self):
        self.inputScore()
        self.inputWeight()
        self.calculateLetter()
        self.inputFeedback()
        
    #prints grade
    def display(self):
        #self._score = "{:.2f}".format(self._score)
        print("Grade: ", self._score)
        print("Weight: ", self._weight, "%")
        print("Letter: ", self._letter)
        print("Feedback: ", self._feedback)
 
#Assignment class definitions        
        
class Assignment(Grade):
    #constructor
    def __init__(self):
        super().__init__()
        self._numSubmissions = 3
        self._submissions = np.empty(0)
        self._weights = np.empty(0)

    #adds progress submissions & weights to two arrays
    def inputProgSubmissions(self):
        for i in range(self._numSubmissions):
            self.inputSubmissions()
            self.inputWeight()
        
    #input progress submission grade
    def inputSubmissions(self):
        temp = input("Enter progress submission score: ")
        try:
            temp = int(temp)
        except ValueError:
            print("Enter a valid score.")
            self.inputSubmissions()
            
        self._submissions = np.append(self._submissions, temp)
       
    #input progress submission weight 
    def inputWeight(self):
        temp = input("Enter weight of progress submission: ")
        try:
            temp = float(temp)
        except ValueError:
            print("Enter a valid weight.")
            self.inputWeight()  
            
        self._weights = np.append(self._weights, temp)
        
    #checks the current number of submissions
    def currNumSubmissions(self):
        print("There are currently ", self._numSubmissions, " progress submissions.")
        temp = input("Would you like to change the number of progress submissions? (y/n): ")
        if(temp.lower() == 'y'):
            self.changeNumSubmissions()
       
    #allows user to change the number of submissions 
    def changeNumSubmissions(self):
        temp = input("Enter new number of progress submissions: ")
        try:
            self._numSubmissions = int(temp)
        except ValueError:
            print("Enter a valid number of submissions.")
            self.changeNumSubmissions()   
    
    #user creates a new assignment
    def newAssignment(self):
        self.currNumSubmissions()
        #self.newGrade()
        self.inputProgSubmissions()
        self.calculateScore()
        print("What is the weight of the overall project?")
        super().inputWeight()
        self.calculateLetter()
        self.inputFeedback()
        
        
    #calculates total score based on prog submissions and weights
    def calculateScore(self):
        total = 0.0
        weight = 0.0
        for i in range(np.size(self._submissions)):
            total = total + self.weightedGrade(i)
            weight = weight + self._weights[i]
        
        self._score = total/weight
        
    #combines weight & grade
    def weightedGrade(self, position):
        return self._submissions[position] * self._weights[position]
        
    #display Assignment grade
    def display(self):
        super().display()
        print("Number of submissions: ",  self._numSubmissions)
        for i in range(np.size(self._submissions)):
            print("Submission", i + 1, ": ", self._submissions[i])
            print("Weight: ", self._weights[i], "%")
 
#Lab class definitions            
    
class Lab(Grade):
    #constructor
    def __init__(self):
        super().__init__()
        self._complete = False
        
    #user enters whether lab was completed
    def inputComplete(self):
        temp = input("Was this lab completed? y/n: ")
        if(temp.lower() == 'y'):
            self._complete = True
        elif(temp.lower() == 'n'):
            self._complete = False
        else:
            print("Please enter 'y' or 'n'.")
            self.inputComplete()
     
    #user enters a new lab grade        
    def newLab(self):
        self.inputComplete()
        
        #if lab is completed, grade is automatic 100
        if(self._complete == True):
            self._score = 100
            super().inputWeight()
            self._letter = 'A'
            super().inputFeedback()
        else:
            super().newGrade()
            
    #display Lab grade
    def display(self):
        super().display()
    
#Exam class definition
            
class Exam(Grade):
    #constructor
    def __init__(self):
        super().__init__()
        self._extraCredit = 0.0
        self._totalScore = 0.0
        
    #user enters extra credit amount
    def inputExtraCredit(self):
        temp = input("Enter extra credit: ")
        try:
            self._extraCredit = float(temp)
        except ValueError:
            print("Enter a valid number.")
            self.inputExtraCredit()
        
        if(self._extraCredit > 5.0 or self._extraCredit < 0.0):
            print("Enter valid amount of extra credit (0-5): ")
            self.inputExtraCredit()
            
    #calculate score w/ extra credit
    def totalScore(self):
        self._totalScore = self._score + self._extraCredit
    
    #input a new exam
    def newExam(self):
        self.newGrade()
        self.inputExtraCredit()
        self.totalScore()
        
        
    #display Exam grade
    def display(self):
        super().display()
        print("Extra credit points: ", self._extraCredit)
        print("Total score: ", self._totalScore)
        