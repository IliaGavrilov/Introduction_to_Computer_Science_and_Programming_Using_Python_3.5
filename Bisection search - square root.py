# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 20:13:34 2017

@author: Gavrilov
"""

x = int(input("Enter int: "))
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low) / 2.0

while abs(ans**2 - x) >= epsilon:
    print("low = " + str(low) + " high = " + str(high) + " ans = " + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else: #if/elif ans**2 > x: 
        high = ans
    ans = (high + low) / 2.0
    
print("numGuesses = " + str(numGuesses))
print(str(ans) + " is close to square root of " + str(x))