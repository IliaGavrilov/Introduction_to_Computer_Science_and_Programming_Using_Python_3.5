# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 19:56:00 2017

@author: Gavrilov
"""
#basically, that type of recursion called factorial recursion
def factorial(n):
    '''
    Calculates factorial for positive int
    such is that n! = n*(n-1)*(n-2)*(n-3)* ... * 
    '''
    if n == 1: #base case
        return n
    else:
        return n * factorial(n - 1) #recursion step 
                                #I need to make sure that I'm
                                #changing the parameter
print(factorial(5))