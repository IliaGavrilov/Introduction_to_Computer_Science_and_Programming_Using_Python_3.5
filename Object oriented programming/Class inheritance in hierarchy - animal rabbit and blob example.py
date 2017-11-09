# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 18:40:51 2017

@author: Gavrilov
"""
#I can inherit methods from higher in the hierarchy, something higher in the hierarchy 
#cannot access a method of a subclass.
#I use the appropriate method by letting the instance tell me what kind of method I should look up.
class Animal(object): #object is underlying class, animal is parent class
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
    
class Cat(Animal): #children subclass
    def speak(self): #new functionality via new methods
        print("meow")
    def __str__(self): 
        return "Cat: " + str(self.name) + ":" + str(self.age) 

class Rabbit(Animal): #children subclass
    def speak(self):
        print("meep")
    def __str__(self):
        return "Rabbit: " + str(self.name) + ":" + str(self.age) 

jelly = Cat(1)
jelly.setName("JellyBelly")      
print(jelly.speak()) #There is one speak() method associated with cats,
                     #Now I didn't define speak() inside the instance, but because this is an instance, 
                     #I know it's a kind of Cat. I look up the speak() method inside of Cat, which is why it does the right thing.
peter = Rabbit(5)
print(peter.speak()) #and another speak method associated with rabbits

blob = Animal(3)
#print(blob.speak()) #AttributeError because there is no speak() method associated with Animal.
                     #Blob is an instance of Animal. Look up an Animal. 
                     #The definition for a method for speak() - there isn't one.
