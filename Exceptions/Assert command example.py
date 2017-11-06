# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 22:05:39 2017

@author: Gavrilov
"""
#"assert" statement to raise an error if some assumptions are not met.
#Could be on inputs, it could be in an intermediate state of the program
#where I want to check that I'm in the right place.
def average(grades):
    assert not len(grades) == 0, 'no grades data' #form of assert:
                                                  #assert <key word> not <logical not> 
                                                  #max_number !=0 <boolean expression> , <comma> 
                                                  #"Cannot divide by 0" <argument>
    return sum(grades) / len(grades)
L = [1,2,3,4]
print(average(L))  
