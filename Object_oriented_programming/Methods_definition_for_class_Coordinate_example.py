# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:28:27 2017

@author: Gavrilov
"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other): #methods ways of manipulating attributes
                               #we need to have the first argument be self,
                               #because it's going to refer to a particular instance.
                               #other is another parameter
                               #the “.” operator is used to access any attribute
                               #think of it as a function call
        x_diff_sq = (self.x - other.x)**2 #other.x saying, get the value of other, it points to a frame, 
                                          #because it's an instance of a coordinate, and in that frame,
                                          #I defined variable bindings for x and y
        y_diff_sq = (self.y - other.y)**2
        return(x_diff_sq + y_diff_sq)**0.5 #**0.5 is same as square root
   
c = Coordinate(3,4)
origin = Coordinate(0,0)

print(c.distance(origin)) #conventional way: object on which to call a method, name of the method
                          #parameters not including self (self is implied to be c)
                          #Python automatically provides C as the first argument to this distance function.
                          #because value of distance is a method __init__
print(Coordinate.distance(c, origin)) #different way: using the class to get to the method
                                      #name of a class, name of method, parameters including an object 
                                      #on which to call the method representing self
