# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 21:24:19 2017

@author: Gavrilov
"""
#rabbits
def fib(x):
    """
    assumes xan int >= 0 returns Fibonacci of x
    """
    if x == 0 or x == 1: #two base cases 
        return 1
    else:
        return fib(x-1) + fib(x-2) #two recursive cases
    #so basically if there are two base cases then I need two recursive cases
print(fib(7))