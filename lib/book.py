#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def title (self):
        return self.title
    
    def page_count (self):
        return self.page_count
    
    def set_count (self, count):
        if isinstance(count, int) and (count > 1):
            print("Flipping the page...wow, you read fast!")
            self.page_count = count
        else:
            print("page_count must be an integer")  

    count = property(page_count, set_count,)          
    


book= Book("And Then There Were None", 272) 
print(book.title) 
print(book.page_count)      
book.count = "twenty"    
        