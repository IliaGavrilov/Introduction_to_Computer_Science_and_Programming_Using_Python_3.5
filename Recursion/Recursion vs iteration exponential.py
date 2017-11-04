# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 21:50:16 2017

@author: Gavrilov
"""

def mult(base,exp):
    """
    base == int or float, exp == int
    """
    result=1
    while exp>0:
        result=result*base
        exp=exp-1
    return result
print(mult(float(input("Enter int or float: ")), int(input("Enter int: "))))

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp==1:
        return base
    elif exp==0:
        return 1.0000
    else:
        return base*recurPower(base, exp-1)
print(recurPower(float(input("Enter int or float: ")), int(input("Enter int: "))))
