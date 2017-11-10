# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 11:14:45 2016

@author: ericgrimson
"""
#class variables belong to the class and therefore is shared among all objects or instances of that class.
#a variable defined inside the class definition, but outside of any of the methods, so outside of init.
class Animal(object):
    def __init__(self, age):
        self.age = age #these are instance variables. Age and name are things that are created
        self.name = None #whenever I call init, which means whenever I create an instance.
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)

class Rabbit(Animal): #subclasses inherit all the data attributes and methods of a parent class.
    tag = 1 #I'm going to create a class variable.
    #And notice in particular, it is outside of the init definition.
    #So when I create the class of Rabbit, it is going to create within that frame associated
    #with Rabbit a binding for tag, initially set to 1. And that tag is going to allow me
    #to give a unique ID to every new rabbit that I create.
    def __init__(self, age, parent1=None, parent2=None): #my initialization method for Rabbit
                                          #is a little bit different. In particular I'm going to 
                                          #ask to pass in, potentially, two other arguments.
        Animal.__init__(self, age) #I'm still going to initialize an instance using
                                   #the underlying animal init method, as I did before.
        self.parent1 = parent1 #But now I'm also going to set, within that instance,
        self.parent2 = parent2 #parameters or bindings for parent1 and parent2.
        self.rid = Rabbit.tag #I'm going to create a local rabbit ID tag or an rid for this rabbit 
                              #by accessing rabbit.tag. first time I call this instance,
                              #that instance is going to have, as a local variable, rid.
                              #And it's going to be the value 1, because that's the current value of the tag.
        Rabbit.tag += 1 #And then the last thing I'm going to do is having called that instance, I'm
                        #going to increase it by 1 to 2. And that means that the class is keeping track of the tag.
                        #And this is a place where I've got data attributes associated with the class, not with the instance.
    #having done that, there's a couple of other things I can do with the rabbit.
    def get_rid(self): #the getter methods will include now getting out the ID
        return str(self.rid).zfill(3) #technique to make sure that everything prints out to the same size.
                                      #In this case, it will be 001 rather than 1 so that things look and print similarly.
  
    def get_parent1(self): #the getter methods will include now getting out the names of the parents.
        return self.parent1
    def get_parent2(self):
        return self.parent2
    
    # define + operator between two rabbit instances 
    def __add__(self, other): #I can define inherent add method here.
        # returning object of same type as this class
        return Rabbit(0, self, other) #recall Rabbit’s __init__(self... where 
                                      #age=0, self= parent1=None, other= parent2=None)
        #And I'm going to create a new rabbit with that call to Rabbit, with parent1 (self) and parent2 (other).

        #I can use that idea of those tags to actually define what it means to compare two rabbits.
    def __eq__(self, other): #I'm going to define an override of the eq method, a built in method.
        parents_same = self.parent1.rid == other.parent1.rid \
                       and self.parent2.rid == other.parent2.rid #I'm going to decide that two rabbits 
                                                                 #are equal if they have the same parents.
                                                                 #I'm simply going to look at the tag associated
                                                                 #with the instance for each parent,
        parents_opposite = self.parent2.rid == other.parent1.rid \
                       and self.parent1.rid == other.parent2.rid #or they could be the other direction.
        return parents_same or parents_opposite #And I'm going to return true if one of those cases is true.

peter = Rabbit(2)
peter.set_name('Peter')
hopsy = Rabbit(3)
hopsy.set_name('Hopsy')
cotton = Rabbit(1, peter, hopsy) #I'm going to now create another rabbit, Cotton, that has two parents.
cotton.set_name('Cottontail')
print(cotton) #if I want to look at things about Cotton, i will see that
              #I've inherited all the behaviors I would have wanted before.
print(cotton.get_parent1()) #If I ask Cotton to get the first parent, I can print that out.

mopsy = peter + hopsy #I'm using rabbit addition (+ operator). I'm creating a new instance of a Rabbit (= operator).
mopsy.set_name('Mopsy')
print(mopsy.get_parent1()) #And now I can say what's the parrot of Mopsy?
print(mopsy.get_parent2()) #And I can say what's the other parrot of Mopsy? And I get out Hopsy.

print(mopsy==cotton) #I'm relying on the fact that I built a unique tag with each instance of a Rabbit.
#now I've got an example of using a class variable to gather information that I can associate with instances
#in a way that lets me keep track of the information that belongs to each instance but is defined within the class.