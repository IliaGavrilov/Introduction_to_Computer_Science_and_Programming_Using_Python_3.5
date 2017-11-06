# -*- coding: utf-8 -*-
"""
Created on Mon May 16 22:41:46 2016

@author: ericgrimson
"""

def isPal(x):
    assert type(x) == list #assert statement at the start of a function checks for valid input
                           #after a function call it's checking for valid output.
    temp = x[:]
    print(temp, x) #I'm going to insert a print statement halfway through the code #bisection search
    temp.reverse()
    print(temp, x) #And I'm going to remove that print statement if I don't need it.
    if temp == x:
        return True
    else:
        return False

def silly(n):
    result = []
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
        print(result) #because of binary search, I know that at least one bug 
                      #must be present earlier in the code.
                      #So I want to add a second print in, this time, inside the loop
    if isPal(result):
        print('Yes')
    else:
        print('No')
silly(3)
