# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 11:44:02 2017

@author: Gavrilov
"""
#iteration as base for recursion
def mult_iter(a, b):
    result = 0
    while b > 0:
        b -= 1
        result += a
    print(result)    
    return result
mult_iter(int(input("Enter a: ")),int(input("Enter b: ")))

def mult_recur(a, b):
    if b == 1: #1 or more base cases 
               #base must be a test which stops recursion
        return a
    else:
        return a + mult_recur(a, b-1) #recurcive step 
                                      #invoking function inside function makes recursion
print(mult_recur(int(input("Enter a: ")), int(input("Enter b: "))))
