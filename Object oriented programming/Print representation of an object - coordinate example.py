# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:28:27 2017
@author: Gavrilov
"""

class Coordinate(object): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def distance(self, other):  
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return(x_diff_sq + y_diff_sq)**0.5 
    def __str__(self): #another special method called the string method
                       #Whenever I ask to print an instance of any kind of data object,
                       #Python calls the __str__ method when used with print on your class object
        return "<" + str(self.x) + ", " + str(self.y) + ">" #you choose what it does!
                                                            #all I require is that, how ever I want to define it, 
                                                            #it must return a string.
    def __repr__(self):
        return "Coordinate(" + str(self.x) + "," + str(self.y) +")" #printable representation of the object
                                               #__repr__ is more for developers while __str__ is for end users.
    
c = Coordinate(3,4) 
origin = Coordinate(0,0) 

print(c) #It prints out a much better representation of the coordinate, something that I can recognize
print(type(c)) #It says C is an instance of a class, and the class type is coordinate.
               #The .main just tells me it was defined up in that overall environment to which I interact
print(Coordinate, type(Coordinate)) 
print(isinstance(c, Coordinate)) #One of the other things I might want to do is to know what kind of thing is this.
                                 #Do I have something that is an instance of a coordinate?
print(Coordinate.__repr__(c))
