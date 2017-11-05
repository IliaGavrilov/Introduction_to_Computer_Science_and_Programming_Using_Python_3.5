# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 13:06:52 2017

@author: Gavrilov
"""

#aliases - multiple variables pointing to the same list
warm = ['red', 'yellow', 'orange']
hot = warm #points to the same variable in global frame
print(warm)
print(hot)

hot.append('pink') #both warm and hot structures mutated
print(warm)

#different structures
cool = ['blue', 'green', 'grey']
chill = ['blue', 'green', 'grey'] 
print(cool)
print(chill)
chill[2]='blue'
print(cool)
print(chill)

#Cloning lists is really useful when
#I want to do something with a list that involves mutation,
#but I don't want to, in fact, change the original list.
cool = ['blue', 'green', 'grey']
chill = cool[:] #cloning through slicing   
                #I can simply say I want chill to be a clone of cool
chill.append('black')
print(cool)
print(chill)