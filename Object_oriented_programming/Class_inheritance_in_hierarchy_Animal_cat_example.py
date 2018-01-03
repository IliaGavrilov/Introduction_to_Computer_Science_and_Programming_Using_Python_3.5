# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 18:40:51 2017

@author: Gavrilov
"""
#First, key advantage is that we cluster common behaviors together around instances of a class (which may vary?).
#Second, I can have hierarchies of classes but each one could be a separate class.
#Thus, And I'd like to build classes that reflect exactly that hierarchy, sharing the properties 
#and the methods that are common, but having distinct properties, attributes, methods when appropriate.
class Animal(object): #object is underlying class, animal is parent class
                      #That means it inherits all of the pieces inside of Python.
    def __init__(self, age):
        self.age = age
        self.name = None
    def getAge(self): #I've got getters.
        return self.age
    def getName(self):
        return self.name
    def setAge(self, newAge): #I've got setters.
        self.age = newAge
    def setName(self, newName=""):
        self.name = newName
    def __str__(self): #I got a way of printing them out
        return "Animal: " + str(self.name) + ":" + str(self.age)
    
class Cat(Animal): #children subclass, which inherit the behaviors and data 
                   #of the parents unless I explicitly override them.
                   #It have its own properties on top of it.
                   #An instance of type Cat can be called with its methods.
    def speak(self): #new functionality via new methods
        print("meow")
    def __str__(self): #I also want to override the print() method, because I want to know that it is a Cat.
        return "Cat: " + str(self.name) + ":" + str(self.age) 

jelly = Cat(1)
jelly.setName("JellyBelly")
print(jelly.getName())
print(jelly) #as a consequence, if I print Jelly, it will inherit from the string method
             #of a parent class associated with an instance of a Cat. So that string method 
             #is shadowing the Animal string method. This is a version of an Animal,
             #but it doesn't use the Animal string method when I use this.
print(Animal.__str__(jelly)) #Jelly will only see the method associated with Cat.
                             #I can still get to that underlying method if I really wanted to use it.
                             #and here, I'm going to say, take the Animal class, get the string method 
                             #associated with Animal, and apply it to Jelly.
