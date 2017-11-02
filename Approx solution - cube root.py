# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 16:07:23 2017

@author: Gavrilov
"""
x = int(input("Type int: "))
epsilon = 0.01
guess = 0.0
increment = 0.01
num_guess = 0
while abs(guess**3 - x) >= epsilon and guess <= x:
    guess += increment
    num_guess += 1
print ("num_guess =", num_guess)
if abs(guess**3 - x) >= epsilon:
    print("Failed on cube root of", x)
else:
    print(guess, "is close to the cube root of", x)