# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:48:45 2017

@author: Gavrilov
"""

nameHandle = open ("Kids", "r")
for line in nameHandle:
    print(line)
nameHandle.close()
