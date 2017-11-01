# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:38:50 2017

@author: Gavrilov
"""
x = int(input("Enter an integer: ")) #print out message, then read, convert it into an integer
ans = 0 #I'm going to have a little loop: 
while ans**3 < x: #less than I'm trying to find the cube of
    ans += 1 #I'm just going to increment-- add 1 to it.
if ans**3 != x: #did I actually get the cube, by doing a test.
    print(str(x)+ " is not a perfect cube")
else:
    print(("Cube root of ") + str(x) + " is " + str(ans))
    
