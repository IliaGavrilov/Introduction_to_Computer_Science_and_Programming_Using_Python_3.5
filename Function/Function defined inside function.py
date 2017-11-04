# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 20:08:37 2017

@author: Gavrilov
"""

def g(x):
    def h(): #internal or helper function #Only when I'm inside of g can I use h
        x = "abc"
    x += 1
    print("in g(x): x =", x)
    h()
    return x
x=3
z=g(x)

