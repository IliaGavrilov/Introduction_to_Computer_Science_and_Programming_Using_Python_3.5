# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 19:44:35 2017

@author: Gavrilov
"""

def ApplyFuns(L,x): #I could apply a list of functions to a number
    for f in L:
        print(f(x))

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
    
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
    
ApplyFuns([abs, int, fact, fib], 4)
