# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 19:00:10 2017

@author: Gavrilov
"""

def applyToEach(L,f):
    '''assumes L is list, f a function
       mutates L by replacing each element,
       e, of L by f(e)'''
    for i in range(len(L)):
        L[i] = f(L[i]) #1) for each index that goes into the list, get out the element of the list,
                       #2) applying function to each element of the list
                       #3) and then put that back in that spot inside of the list.
    return L
L = [1, -2, 3.4]

applyToEach(L, abs)
print(L)

applyToEach(L, int)
print(L)

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
applyToEach(L, fact)
print(L)

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
applyToEach(L, fib)
print(L)