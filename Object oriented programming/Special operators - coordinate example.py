# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:28:27 2017

@author: Gavrilov
"""
#associated methods - a class can implement certain operations that are invoked by special syntax
#Each one of these methods has a built-in name that I can use to override the underlying version of that.
class Coordinate(object): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def __str__(self): 
        return "<" + str(self.x) + ", " + str(self.y) + ">" 
    def __add__(self, other): #self + other
        return Coordinate(self.x + other.x, self.y - other.y)
    def __sub__(self, other): #self -other
                              #And what sub should do is, simply take the instance itself
                              #and another instance, subtract, coordinatewise, the x values,
                              #and then return a coordinate.
        return Coordinate(self.x - other.x, self.y - other.y) 
    def __eq__(self, other): #self == other
        return Coordinate(self.x == other.x, self.y == other.y)
    def __lt__(self, other): #self < other
        return Coordinate(self.x < other.x, self.y < other.y)
    def __len__(self): #len(self)
        return len(self.x) + len(self.y) #not sure that is correct

c = Coordinate(3,4) 
origin = Coordinate(4,2)
print(Coordinate.__add__(c, origin))
foo = c-origin
print(foo)
print(Coordinate.__sub__(c, origin)) 
print(Coordinate.__eq__(c, origin)) 
print(Coordinate.__lt__(c, origin))

z = Coordinate([1,2,3], [4,5,6,7])
print(Coordinate.__len__(z)) 
