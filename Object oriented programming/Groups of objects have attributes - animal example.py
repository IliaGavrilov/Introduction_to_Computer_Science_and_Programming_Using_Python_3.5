# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 12:16:06 2017

@author: Gavrilov
"""

class Animal(object):
    def __init__(self, age): #recap: self is a variable to refer to an instance of the class
        self.age = age
        self.name = None #I can define not only bindings for data attributes that are passed in (age)
                         #but I can also define data attributes that I'm just going to set up internally,
                         #init is going to create a binding for both age and name inside every instance.
                         #and initially, name is simply set to none.
    
    def getAge(self): #I need methods to get out values. I'm going to have something
                      #that gets out the age, something that gets out the name.
        return self.age
    def getName(self): #That makes sense because those were the two attributes I defined, 
                       #even though I didn't pass in an initial value for name.
        return self.name
      
    #But I also want to have another kind of method here, and we call those setters.
    #And those are methods that can change the binding for internal data attributes.    
    def setAge(self, new_age):
        self.age = new_age #So if I want to change the age, I can change the binding for age.
                           #I can rebind it to a new value.
    def setName(self, new_name = ""): #Default arguments for formal parameters are used if no actual argument is given
                                      #my version of setting the name is not only
                                      #the name of the variable, but I'm going to have 
                                      #a default binding, which is the empty string 
        self.name = new_name #if I don't give it an argument, I'm just going to redefine it 
                             #to be the empty string, or a string of nothing, 
                             #as opposed to that separate symbol, none.
    
    def __str__(self):
        return "animal: " + str(self.name) + ":" + str(self.age)
        
myAnimal=Animal(3) #one instance #mapped to self.age in class def
print(myAnimal)
myAnimal.setName("foobar") #call of setter #getters and setters should always be used 
                           #outside of the class to access the data attributes. 
print(myAnimal)

print(myAnimal.getAge()) #call of getter
print(myAnimal.age) #another way to call a variable #I'd really rather use the getter.
                    #because I want to separate the internal representation from access to that representation.
