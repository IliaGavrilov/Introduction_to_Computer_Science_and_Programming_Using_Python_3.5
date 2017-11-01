# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 13:11:20 2017

@author: Gavrilov
"""

mysum = 0
for i in range (5, 11, 2):
    mysum += i 
    if mysum == 5:
        break
print(mysum)