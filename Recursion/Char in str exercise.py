# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 13:44:56 2017

@author: Gavrilov
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr)<1:
        return False
    elif char==aStr[0]: #recursive base
       return True
    else:
        return isIn(char, aStr[1:]) #recursive step #function call inside function
print(isIn('z', 'artz'))