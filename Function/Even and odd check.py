# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 21:46:36 2017

@author: Gavrilov
"""

def even(x):
    '''
    x: int

    returns: True if x is even, False otherwise
    '''
    z=x%2==0 
    return(z)
print(even(4))

def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    z=x%2!=0 
    return(z)
print(odd(5))
