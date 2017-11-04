# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:54:19 2017

@author: Gavrilov
"""

import circle #the usage here is if I can invoke the command import circle
              #it goes and finds that file and reads all of the statements, 
              #including the definitions and assignments inside that file
              #in python path
pi = 3 #I could redefine Pi to be 3
print(pi)
print(circle.pi) #I could print out the value of Pi that was defined in the module circle
print(circle.area(3)) #function call defined in circle
print(circle.circumference(3))