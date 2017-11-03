# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 11:44:21 2017

@author: Gavrilov
"""
#I evaluate this sequence of expressions.
def f (x): #any time I do an invocation of a function, I create a new frame.
#There is that formal parameter.
    x==x+1
    print("in f(x): x =",x)
    return x
x = 3 #So in the global scope, x has a binding to the value of 3.
z = f(x) #There's the actual parameter I'm going to use,
#I evaluate that, and in that global frame,
#I create a set of bindings.
#First one is evaluating that definition
#binds the variable name f to something.