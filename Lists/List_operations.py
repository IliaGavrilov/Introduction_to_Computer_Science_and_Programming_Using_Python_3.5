# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 12:02:31 2017

@author: Gavrilov
"""

warm = ['red', 'yellow', 'orange']
print(warm)

cold = ['white']
print(cold)

colors = warm + cold #concatenate list
print(colors)

colors.append('pink') #given an object name, the dot says, get out some method
                   #and then call it, open print followed by close print
print(colors)

cold.extend(['blue', 'black'])
print(cold)

del(cold[2])
print(cold)

cold.remove('blue')
print(cold)

print(colors.pop(0))
