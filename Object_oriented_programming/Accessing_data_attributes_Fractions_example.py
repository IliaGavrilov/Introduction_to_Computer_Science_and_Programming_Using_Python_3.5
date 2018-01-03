# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 14:16:52 2017

@author: Gavrilov
"""
#ability to think about elements of this class and simply use them.
class fraction(object): #this is going to inherit from the underlying object class.
    def __init__(self, numer, denom): #I also need, as always, to define
                                      #what does it mean to create one of these objects.
                                      #So I've got an init method.
        self.numer = numer #And I'm just going to bind those locally
        self.denom = denom #within the frame associated with every instance of a class.
    def __str__(self):
        return str(self.numer) + " / " + str(self.denom)

    #These are often called getters.
    def getNumer(self): #Why am I creating those? Well those are going to be important
                        #because it's going to separate out accessing the internal representation
                        #from the actual use of the representation.
        return self.numer
    def getDenom(self):
        return self.denom
    
    #I can now use that to define things like how do I add fractions or how do I subtract fractions.
    def __add__(self, other): #It takes two arguments, the instance itself, and some other fraction.
        numerNew = self.getNumer() * other.getDenom() + other.getNumer() * self.getDenom()
        denomNew = self.getDenom() * other.getDenom()
        return fraction(numerNew, denomNew)
    def __sub__(self, other):
        numerNew = self.getNumer() * other.getDenom() - self.getDenom() * other.getNumer()
        denomNew = self.getDenom() * other.getDenom()
        return fraction(numerNew, denomNew) #having computed that numerator and denominator, I need to return an instance.
                                            #And I create one by calling Fraction with new values 
                                            #for the numerator and the denominator.
                                            #NB! is it the crucial point for making possible to use class objects as primitives?
                                                
    def convert(self): #Last thing I wanted to do is to be able to convert fractions into floats.
        return self.getNumer() / self.getDenom()
        

oneHalf = fraction(1,2)
twoThirds = fraction(2,3)

print(oneHalf)
print(twoThirds)

print(oneHalf.getNumer()) #one_half points to an instance. It's a frame somewhere.
                          #The dot says, get the binding for getNumer in that frame.
                          #that is the definition that I did of a method inside frame of fraction.
                          #But I inherit it because oneHalf is an instance of Fraction.
                          #() is that simply gives you back the procedure.
                          #And while it takes no arguments other than self, which is automatically provided, 
                          #I need to say open, close paren to actually invoke it.
print(oneHalf.getDenom())

new = oneHalf + twoThirds #we invoke __add__ by that?
                          #it is basically same as if we call fraction.__add__(oneHalf, twoThirds)
print(new) #this is an axample of how we treat objects as primitives as if they were provided to us

print(new.convert())
