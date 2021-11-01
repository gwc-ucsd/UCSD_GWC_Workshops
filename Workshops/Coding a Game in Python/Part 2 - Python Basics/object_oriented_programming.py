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
print(sum_two_numbers(1,4))

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
# unchangeable. (Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been 
# created.)

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

# Lists: A list used to store multiple items in a single variable. List items are ordered, changeable, and allow 
# duplicate values.

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "cherry"]

# list indexing
print(list1[0])
print(list2[3])

# list slicing
# start is the index of the first element to include, and stop is the index of the item to stop at without including 
# it in the slice
list4[0:3]

### LOOPS ---------------------------------------------------------------------------------------------------------------- 
# for loop: used to repeat a specific block of code a known number of times.
for i in range(0,5):
    print('happy halloween!')

for i in list4:
    print(i)

# nested loop: one loop inside of another
for i in list4:
    for x in list1: 
        if i == x:
            print(i)

# while loop: used to execute a set of statements as long as a condition is true
i = 1
while i < 6: 
    print(i)
    i += 1 # have to change i, otherwise the loop will continue forever

### TRY/EXCEPT STATEMENTS ------------------------------------------------------------------------------------------------
# Defintion: The try-except block can handle exceptions. This prevents abrupt exits of the program on error. In the 
# example below we purposely raise an exception.

try: 
    1 / 0
except ZeroDivisionError: 
    print('Divided by zero')

print('Should reach here')


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