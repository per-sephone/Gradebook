'''
Nora Luna
CS 202
Project 5
main.py

This file contains the main file. This file acts a gradebook. The user can add a student
to the gradebook, the add any grades needed for that student. The user can remove, search for,
and display all students. 
'''


from Grade import Grade
from Student import Student
from BST import TreeNode, BST

def menu():
    print()
    print("---------Gradebook Main Menu----------")
    print("a. Add a new student to the gradebook")
    print("b. Search for a student in the gradebook")
    print("c. Remove a student from the gradebook")
    print("d. Display all students in the gradebook")
    print("e. Exit Gradebook")
    print()

def main():
    
    print("Welcome to the gradebook application!")
    menu()
    key = input("Select from above options: ")
    tree = BST()
    key = key.lower()
    while(key == 'a' or key == 'b' or key == 'c' or key == 'd'):
        if(key == 'a'):
            #insert new student
            newStudent = Student()
            newStudent.studentMenu()
            tree.insert(newStudent)
        elif(key == 'b'):
            #search for a student by name
            search = input("Enter the name to search for: ")
            tree.search(search)
        elif(key == 'c'):
            #remove student by name
            remove = input("Enter the name to remove: ")
            tree.remove(remove)
        elif(key == 'd'):
            #display all students
            tree.display()
        elif(key == 'e'):
            pass
        else:
            print("Please select a, b, c, d, or e")
            
        menu()
        key = input("Select from above options: ")
        
    print("Thank you for using my gradebook!")    
    
if __name__=="__main__":
    main()