# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:28:27 2017

@author: Gavrilov
"""

class Coordinate(object): #keyword class is going to tell us we're about to create the definition of a new class
                          #Coordinate is a name each class definition is going to take one argument, 
                          #which is the parent class.
                          #Object as argument tells that class inherit from the underlying object class of Python
    def __init__(self, x, y): #data attributes
                              #immediately below that, I'm going to define the attributes of this class.
                              #first thing is define how I actually create instances of this object.
                              #special method to create an instance is keyword __init__
                              #self is first parameter of an argument self is going to refer to an instance of the class
                              #x, y parameters going to create instances the initial data.
        self.x = x #And the way we glue them together is we're going to actually create bindings for the names
                   #x and y to the values passed in.
        self.y = y #when we actually invoke the creation of an instance
                   #this will bind the variables x and y within that instance to the supplied values.
                   #This is typically the first method that we have inside of a class definition.
                   #Because we have to say, how am I going to create instances of this class?

c = Coordinate(3,4) #I can now create an instance.
                    #creates a new object of type Coordinate and pass in 3 and 4 to the __init__ method
origin = Coordinate(0,0) #each time I invoke coordinate, the name of a class, it's creating a new instance.
                         #it's calling that init method, and using that to create local bindings.
print(c.x) #print out the x-value value associated with c. C dot x is then interpreted as saying the following.
           #Get the value of c. Oh, that's a frame. And then inside of that frame, look up the value associated with x.
print(origin.x)