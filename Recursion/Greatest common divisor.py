# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:33:59 2017

@author: Gavrilov
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Base case is when b = 0
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)
print(gcdRecur(24, 52))