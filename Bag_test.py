#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:38:56 2018

@author: joelpendery
"""

# creates a bag to hold items (uses a )
class Bag1():
    def __init__(self, size):
        self.inventory = [""]*size # creates a list the length of "size" (size is a value you pass in when creating the instance)
        self.itemName = [""]*size
        self.maxItems = size
        
    def add(self, item):
        for ii in range(self.size()):   # for loop to search through the inventory
            if self.inventory[ii] == "":    # if there is no object in the list, add the object to the inventory
                self.inventory[ii] = item   # adds object to inventory
                self.itemName[ii] = item.name
                break   # stop looking through the list because you just added the object
    
    def remove(self, item):
        # find item within list
        if item in self.itemName:
            # if in bag
            for ii in range(self.maxItems):
                if (self.itemName[ii]) == item:
                    # set whatever to item in bag
                    self.inventory[ii] = ""     # deletes item within inventory
                    self.itemName[ii] = ""      # deletes item name from item name list
                    break
        else:
            # item not in bag
            print("You don't have that dude")
        
    def size(self):
        return(len(self.inventory)) # finds the size of your bag
        
class MagicBag():
    def __init__(self, size):
        self.inventory = {}     # create an empty dictionary to hold the items and number of items
        self.maxItems = size    # maximum number of unique items that can be held
        
    def add(self, item):    # add an object to the inventory
        if item in self.inventory:  # if the item is there
            self.inventory[item] += 1   # add an additional item to the bag (increase count by 1)
        elif len(self.inventory) < self.maxItems:   # if item is not already in bag and there is space
            self.inventory[item] = 1    # add the item and set the number to 1
        else:
            print "Sorry dude, no more space"   # if there is no space, tell the player
 
    # not using yet       
    def equip(self):
        goodInd = []
        for ii in range(self.size()):
            if (self.inventory[ii].name == 'equipment'):
                goodInd.extend([ii])
        print goodInd
        #add helmet
        
    def remove(self, item): # remove an item from the bag
        if item in self.inventory:  # if the item is in the bag
            if self.inventory[item] == 1:   # if there is only one item
                del self.inventory[item]    # remove the item from the dictionary
            elif self.inventory[item] > 1:  # if there are more than one of those items
                self.inventory[item] -= 1   # reduce the number of that item by one
        else:
            print "You don't have that item bro"    # if the item is not in the bag, you can't remove it
  
#    def remove(self, item, num):
#        if item in self.inventory:
#            if self.inventory[item] == 1:
#                del self.inventory[item]
#            elif self.inventory[item] > 1:
#                self.inventory[item] -= 1
        
    
    def size(self):
        return(len(self.inventory)) # lets player know how many items they can carry
        
    
class WeirdBag():
    def __init__(self):
        self.inventory = []
        self.numOfItems = len(self.inventory)
        
    def add(self, item):
        if item in self.inventory:
            print "Already have one of those items"
        else:
            (self.inventory).extend([item])
            self.numOfItems = len(self.inventory)
            print "You saved that item"
            
    def remove(self, item):
        print item
        item 
        if item in self.inventory:
            # remove item
            (self.inventory).remove(item)
        else:
            print "You don't have that item"
          
        
# a helmet object
class Helmet():
    def __init__(self):
        self.name = 'helmet'
        self.hp = 10
        self.mp = 5
        
# an apple object
class Apple():
    def __init__(self):
        self.name = 'apple'
        self.hp = 4
        
# a vest object
class Vest():
    def __init__(self):
        self.name = 'vest'
        self.type = 'equipment'
        self.location = 'body'
        self.hp = 15
        self.mp = 10
        
# a vest object
class Watch():
    def __init__(self):
        self.name = 'watch'
        self.hp = 15
        self.mp = 10
        
#a = Bag1(10)    # creates a bag1 object of size 10
##aa = Bag1(20)   # upgrade bag
##aa.add(a.remove())  # remove items from small bag and put into larger bag
#
## add items
#print a.inventory
#a.add(Helmet())
#print a.inventory
#a.add(Apple())
#print a.inventory
#a.add(Vest())
#print a.inventory
#
## remove vest item
#print("remove item")
#a.remove("helmet")
#print a.inventory
#
### to show that with the first bag class, you can mix different types of 
### objects (strings, ints, whatever)
#a.add(Watch())  # adds a string to bag1
#a.add(Watch())
#a.remove("vest")
#print a.inventory
        
b = WeirdBag()
# adds 5 of the following items: spears, potions and vests
# only one item of each will be added in the weird bag
for ii in range(5):
    b.add("Spears") 
    b.add("Potions")
    b.add("Vest")
    
b.add("Helmet") # add a helmet to the bag because there is not a helmet in there already
b.add("Spears") # can't add another spear to the bag because one is already in there
    
print b.inventory   # print the inventory of the weird bag

for ii in range(2):     # remove 2 of the following items from the bag: spears, potions
    b.remove("Spears")
    b.remove("Potions")
    
b.remove("Potions") # remove another potion from the bag
print b.inventory   # check the inventory again. we should have 5 vests, 3 spears and 2 potions and no helmets


#b = MagicBag(3) # creates a magic bag with 3 slots for items
# adds 5 of the following items: spears, potions and vests
#for ii in range(5):
#    b.add("Spears") 
#    b.add("Potions")
#    b.add("Vest")
#    
#b.add("Helmet") # tries to add a helmet but can't because it would be 4 items
#b.add("Spears") # adds another spear (can do this because there is already a spear there)
#    
#print b.inventory   # print the inventory of the magic bag
#
#for ii in range(2):     # remove 2 of the following items from the bag: spears, potions
#    b.remove("Spears")
#    b.remove("Potions")
#    
#b.remove("Potions") # remove another potion from the bag
#print b.inventory   # check the inventory again. we should have 5 vests, 3 spears and 2 potions and no helmets