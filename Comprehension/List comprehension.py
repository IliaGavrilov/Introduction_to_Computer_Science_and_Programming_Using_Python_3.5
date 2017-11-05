# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 13:57:44 2017

@author: Gavrilov
"""

L = [1, 2, "3", 4, "five", 6, 7.5]
print([x+0.5 for x in L if type(x) == int or type(x)== float])
