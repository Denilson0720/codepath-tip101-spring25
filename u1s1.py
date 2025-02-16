
print('UNIT 1 SESSION 1 PROBLEMS')
'''
Problem 1: Hello World!
Given the following lines of code, work with your group members to place the lines in order and write and call your first Python function!

a. print("Hello world!")
b. def hello_world():
c. hello_world()

Understand
- what is a python function and how do you make specific code pertain to it?
- what could be the main objective of the lines of code above? whats it trying to do?

Plan
    Make print statement belong to the function by indenting it inside.
    Call hello_world()
Implement
'''
def hello_world():
    print('hello world!')
hello_world()
print('END OF PROBLEM 1')

'''
Problem 2: Today's Mood
The following function uses a variable, mood to print out "Today's mood: 😎". Copy this code to your Replit and update the mood variable to print out your mood for today.

def todays_mood():
    mood = "😎"
    print("Today's mood: " + mood)

todays_mood()

Example Output: Today's mood: 🥱

UNDERSTAND
    what is a variable in python?
    Is the value the print statement has for mood the same value as above?
PLAN
    manually change the value of mood to 😁
IMPLEMENT
'''
def todays_mood():
    mood = '😁'
    print('Todays mood: ' + mood)
todays_mood()
print('END OF QUESTION 2')
'''
The following function accepts one parameter menu. Copy this code to your Replit and add a function call so that "Lunch today is: 🍕" is printed to the console.

def print_menu(menu):
    print("Lunch today is: " + menu)
Example Output: Lunch today is: 🍜

UNDERSTAND
    what is the menu parameter allowing the function to do?
    how do we pass parameter values to a function?
    what values can be passed into the parameters of print_menu()?
PLAN
    call print_menu() and pass in '🍕' as the menu parameter
IMPLEMENT
'''
def print_menu(menu):
    print('Lunch today is: ' + menu)
print_menu('🍕')
print('END OF QUESTION 3')
'''
Problem 4: Sum of Two Integers
The following function returns the sum of two integers: a and b.

def sum(a, b):
    return a + b
Use the sum() function to calculate the sum of 13 and 27. Then, double the calculated sum and print the result to the console.

Example Input: 20 and 8
Example Output: 56

UNDERSTAND
    do we need to modify the sum function?
    what is returned from the sum function?
PLAN
    saved return of sum(a,b)
    modify the returned value by multiplying it by 2 and print
IMPLEMENT
'''
def sum(a,b):
    return a+b
summed = sum(20,8)
print(2*summed)
print('END OF QUESTION 4')
'''
Problem 5: Product of Two Integers
Write a function product() that returns the product of two integers, a and b.

Example Input: 22 and 7
Example Result: 154
UNDERSTAND
    what is meant by product of two integers?
    what parameters should our function receive?
    what python operator can be used to multiply two integers?
PLAN
    return a*b
IMPLEMENT
'''
def product(a,b):
    return a*b
print(product(22,7))
print(product(22,2))


