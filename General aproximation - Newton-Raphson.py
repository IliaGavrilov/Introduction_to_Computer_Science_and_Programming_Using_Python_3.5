# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 19:17:57 2017

@author: Gavrilov
"""

epsilon = 0.01
y = 8.0
guess = y/2.0
numGuesses = 0

while (abs(guess*guess - y)) >= epsilon: #going to 0 through guesess 
    numGuesses += 1
    guess = guess-(((guess**2)-y)/(2*guess)) #newton-rapson finding root #parening is crutial
print("NumGuesses = " + str(numGuesses))
print("Square root of "+ str(y) + " is about " + str(guess))
