# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 23:41:42 2017

@author: Gavrilov
"""

L=[9,6,0,3]
print(sorted(L)) #returns sorted list, does not mutate L
                 #handy if I want to keep L around but I want a sorted version of it
print(L)
L.sort() #mutates L, but doesn't return anything
print(L)

L.reverse() #it will change l itself and create something in reverse order
print(L)
