# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 18:40:51 2017

@author: Gavrilov
"""
#What I'm doing here (in person class) is explicitly inheriting the __init__() method 
#of the superclass to create the instance
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
    
class Person(Animal): #children subclass (subclass of an animal)
    def __init__(self, name, age):
        Animal.__init__(self, age) #I'm going to now use the underlying Animal method to create the instance.
                                   #I'm going to say, take Animal, the name of a class. 
                                   #Get the __init__() method associated with that, and call it to create the actual instance.
        Animal.setName(self, name) #I'm also going to use the underlying setName() method of Animal 
                                   #to change the name associated with this instance of a Person.
        self.friends = [] #finally, I'm going to simply define friends in this instance directly.
    def getFriends(self):
        return self.friends
    def addFriend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print ("hello")
    def ageDiff(self,other):
        #alternative way: diff = self.age - other age
        diff = self.getAge() - other.getAge()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
    def __str__(self):
        return "person: "+ str(self.name) + ":" + str(self.age)

eric = Person("Eric", 45)
john = Person("John", 55)
print(eric.speak())
print(eric.ageDiff(john)) #alternative way: print(Person.ageDiff(eric, john))