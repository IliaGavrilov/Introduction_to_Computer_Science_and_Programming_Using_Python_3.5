# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 14:16:52 2017

@author: Gavrilov
"""

class fraction(object): 
    def __init__(self, numer, denom): 
        self.numer = numer 
        self.denom = denom 
    def __str__(self):
        return str(self.numer) + " / " + str(self.denom)
    
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    #"\" is a line continuation character
    def __add__(self, other): 
        numerNew = self.getNumer() * other.getDenom() \
        + other.getNumer() * self.getDenom()
        denomNew = self.getDenom() * other.getDenom()
        return fraction(numerNew, denomNew)
    def __sub__(self, other):
        numerNew = self.getNumer() * other.getDenom() \
        - self.getDenom() * other.getNumer()
        denomNew = self.getDenom() * other.getDenom()
        return fraction(numerNew, denomNew) 
    def convert(self):
        return self.getNumer() / self.getDenom()
        

oneHalf = fraction(1,2)
twoThirds = fraction(2,3)

print(fraction.__add__(oneHalf, twoThirds))