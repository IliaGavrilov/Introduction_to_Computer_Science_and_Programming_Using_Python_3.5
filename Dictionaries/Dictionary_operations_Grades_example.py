# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 19:33:02 2017

@author: Gavrilov
"""

my_dict = {}
grades = {"Anna":"B", "John":"A+", "Denise":"A", "Katy":"A"} #I'm going to index into the dictionary
                                                             #by the key element of the entry
print(grades["Anna"])

grades["Ilia"]="A++" #I can add an entry, it's mutable.
print(grades["Ilia"])
print("Ilia" in grades, "Helga" in grades) #test if key in dictionary

del(grades["Anna"]) #delete entry
print(grades)

print(grades.keys()) #get an iterable that acts like a tuple of all keys
print(grades.values()) #get an iterablethat acts like a tuple of all values
