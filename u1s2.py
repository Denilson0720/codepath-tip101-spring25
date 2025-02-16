print('UNIT 1 SESSION 2 PROBLEMS')
'''
Problem 1: Print List
Write a function print_list() that takes in a list lst as a parameter and prints out each item in the list.

def print_list(lst):
    pass
Example Input: lst = ["squirtle", "gengar", "charizard", "pikachu"]
Example Output:

squirtle
gengar
charizard
pikachu
UNDERSTAND
    what is a list?
    what are the different ways/formats we can print out the list?
    is there a difference between 
    squirtle                AND            ['squirtle','gengar']
    gengar 

    how can we iterate through each value of the list?
PLAN    
    use a for loop to iterate over each item in the list.
    print out each item
IMPLEMENT
'''
def print_list(lst):
    for n in lst:
        print(n)

lst = ["squirtle", "gengar", "charizard", "pikachu"]
print_list(lst)
print('END OF QUESTION 1')

'''
Problem 2: Print Doubled List
Write a function doubled() that takes in a list of integers lst as a parameter and prints each item in the list multiplied by two.

def doubled(lst):
    pass
Example Input: lst = [1,2,3]
Example Output:

2
4
6
UNDERSTAND
    what can we reuse from the previous problem to help us out in this problem?
    is it possible to edit each item in the list? if so, how?
PLAN
    iterate through each item in the list using a for loop
    multiply the item by 2, print out the item
IMPLEMENT
'''
def doubled(lst):
    for n in lst:
        double = n*2
        print(double)
doubled([1,2,3])
print('END OF QUESTION 2')
'''
Problem 3: Return Doubled List
Modify the function doubled() so that instead of printing the items, it returns a new list of the doubled numbers.

Example Usage:

lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)
Example Output:

[2, 4, 6]
UNDERSTAND
    is it asking to edit the given list OR make a entirely list?

    how do we append values to a list?

    how can we go about reassigning/assigning a value to a list index?
        ex: lst[2] = 'something'
    what does the previous for loops weve been working with not allow us to do here?

    do we need to just read the list items,would it be beneficial to use an indexed for loop instead?

PLAN
    PLAN TO MAKE NEW LIST AND RETURN NEW LIST
        make new empty list, new_list
        iterate through lst using for loop and n
        calculate new value,
            new_val = n*2
        append new_val to new_list using .append() function
        return new_list

    PLAN TO EDIT LIST
    - using an indexed for loop iterate throguht the list
        for i in range(len(lst)):
    - calculate new value to be replaced with
        newValue = lst[i]*2
    - reassign list at index value with new vaue
        lst[i] = newValue
    - return lst
    
IMPLEMENT
'''
def doubled(lst):
    for i in range(len(lst)):
        lst[i] = lst[i]*2
    return lst
print(doubled([1,2,3]))
# OR
def doubled(lst):
    new_lst = []
    for i in lst:
        val = i*2
        new_lst.append(val)
    return new_lst
print(doubled([1,2,3]))

print('END OF QUESTION 3')
'''
Problem 4: Flip Signs
Write a function flip_sign() that takes in a list of integers lst as a parameter and returns a new list where each number in the original list has been multiplied by -1.

def flip_sign(lst):
    pass
Example Usage:

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)
Example Output:

[-1, 2, 3, -4]
UNDERSTAND
    are we supposed to edit the given list OR make a new one?
    how can we have access to each item in lst?
PLAN
    make a new empty list, new-list
    iterate through lst
        for n in lst:
    calculate value of n flipped, n*-1
    append calculated flipped value to new-list
    return new-list
IMPLEMENT
'''
def flip_sign(lst):
    new_list = []
    for n in lst:
        val = n*-1
        new_list.append(val)
    return new_list

lst = [-1, 2, 3, -4]
print(flip_sign(lst))
print('END OF QUESTION 4')
'''
Problem 5: Max Difference
Write a function max_difference() that takes in a list of integers lst and returns the difference between the smallest and largest value in the list.

def max_difference(lst):
    pass
Example Usage:

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)
UNDERSTAND
    how do we find out the max and min of the list?
    would it be beneficial for us to sort the list first?
    what is a builtin function to sort that we can use here?
PLAN    
    sort the list
    return difference between last and first index of lst
IMPLEMENT
'''
def max_difference(lst):
    lst.sort()
    print(lst)
    return lst[-1] - lst[0]
lst = [5,22,8,10,2]
print(max_difference(lst))
print('END OF QUESTION 5')