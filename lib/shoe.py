#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand, size, can_coble, coble_makes):
        self.brand = brand
        self.size = size
        self.can_cobble = can_coble
        self.cobble_makes = coble_makes

    def brand (self):
        return self.brand
    
    def size (self):
        return self.size
    
    def can_cobble (self):
        #print("the shoe has been repaired.")
        return self.can_cobble
    
    def cobble_makes (self):
        return self.cobble_makes
    
    def set_size (self, new_size):
        if isinstance ( new_size, int):
            print(new_size)
            self.size = new_size
        else: 
            print ("size must be an integer")  

    new_size = property(size, set_size,)        
   
    
    def cobble_makes_new (self, new_condition):
        if new_condition in "repaired":
            print("Your shoe is as good as new!")
            self.cobble_makes = new_condition
        else: 
            print ("The shoe has not been repaired!")  

    new_condition = property(cobble_makes, cobble_makes_new,)         
            

shoe = Shoe("Adidas", 9, "The shoe has been repaired", "not repaired")
print(shoe.brand)
print(shoe.size)  
print (shoe.can_cobble)
shoe.new_size = "eight"  
shoe.new_condition= "repaired"   