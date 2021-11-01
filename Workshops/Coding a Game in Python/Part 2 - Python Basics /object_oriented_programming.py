import pygame # Open-source cross-platform library for the development of multimedia applications like video games using python
import random # Implements pseudo-random number generators for various distributions
import numpy as np

### GLOBAL VARIABLES ---------------------------------------------------------------------------------------------------
# Definition: Global variables, as the name implies, are variables that are accessible globally, or everywhere 
# throughout the program. Once declared, they remain in memory throughout the runtime of the program. This means that 
# they can be changed by any function at any point and may affect the program as a whole.

club = "UCSD_GWC"
ucsd_student = True

def myfunc():
    club = "UCI_GWC" # can change the global variable by adding the global keyword
    print("I am a member of " + club)

myfunc()
print("I'm a member of " + club)

### HELPER FUNCTIONS -----------------------------------------------------------------------------------------------------
# Definition: Helper functions are used to make your programs easier to read by giving descriptive names to computations.

def sum_two_numbers(a,b):
    """Returns the sum of two numbers"""
    return a+b

# Output: 10
print(sum(1,4))

### IF/ELSE STATEMENTS ---------------------------------------------------------------------------------------------------
# Defintion: The if statement executes a statement if a specified condition is true. If the condition is false, another 
# statement can be executed

holiday = "halloween"

if holiday == "new year's":
    print("happy new year's!!!!")
elif holiday == "christmas":
    print("jingle bells")
elif holiday == "halloween":
    print("BOO!")
else:
    print("no holiday today :(")


### DATA STRUCTURES ------------------------------------------------------------------------------------------------------
# Tuples: A tuple is used to store multiple items in a single variable. It's also a collection which is ordered and 
# unchangeable.



# Lists: 

### LOOPS ---------------------------------------------------------------------------------------------------------------- 
# for loop/nested loop
# while loop

### TRY/EXCEPT STATEMENTS ------------------------------------------------------------------------------------------------
# try/except


### CLASSES ------------------------------------------------------------------------------------------------------------
# Definition: Used to create objects (object has state (data) and behavior (code)) and define a type
# More information here: https://realpython.com/lessons/classes-python/

# (__init__)

class Person:
    "This is a person class"
    age = 20

    def greet(self):
        "This function will return a greeting"
        print('Hello')

# Output: 20
print(Person.age)

# Output: <function Person.greet>
print(Person.greet)

# Output: "This is a person class"
print(Person.__doc__)





