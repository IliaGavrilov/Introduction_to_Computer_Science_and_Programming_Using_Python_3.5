# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:48:45 2017

@author: Gavrilov
"""

nameHandle = open ("Kids", "w") #the way that is done is by using the special command open
                                #and giving it the name of a file and giving it a command
                                #And I've bound that to a name so I can refer to it
for i in range(2): #That allows me then to use it.
                   #loop says to the user, type in a name, and write it into that file.
    name = input("Enter name: ")
    nameHandle.write(name + "\n") #using name handle and the dot and then the write command
                                  #"\n" string says do a carriage return 
                                  #or start a new line after the end of this right
nameHandle.close() #When I'm done, I close the file handle by invoking the method close
                   #with name handle, open close paren to say that it's actually
                   #an invoking of a function that closes up the file