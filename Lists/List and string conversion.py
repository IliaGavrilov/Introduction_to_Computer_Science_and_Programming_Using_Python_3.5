# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 21:37:57 2017

@author: Gavrilov
"""

s = 'qwerty asdfg'
print(s)

l = list(s) #procedure or function to convert every char as separate str of list
print(l)

sNew = s.split() #split a string on a character parameter
          #on spaces if called without a parameter
print(sNew) #It has literally broken it up into two parts

sNewTwo = ''.join(sNew) #turn a list of characters into a string
print(sNewTwo)

sNewThree = '_'.join(sNew) #can give a character in quotes to add char between every element
print(sNewThree)