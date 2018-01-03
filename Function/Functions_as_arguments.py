# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 18:36:41 2017

@author: Gavrilov
"""
#not only can parameters have numerical values,
#they could also have another values,
#including being a function.
def func_a():
    print("inside func_a")
def func_b(y):
    print("inside func_b")
    return y
def func_c(z):
    print("inside func_c")
    return z() #it called a return of calling z with no arguments
               #function A then said print out inside function A
               #Return nothing, because there is no return statement
print(func_a()) #open and close paren to tell me there are no parameters
print(5 + func_b(2)) #In this case, I'm going to give it a number
print(func_c(func_a)) #is going to take in one parameter, but in this case it's another function
