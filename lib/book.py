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
        if isinstance(count, int) and (count > 50):
            print(f"the count is { count }")
            self.page_count = count
        else:
            print("Flipping the page...wow, you read fast!")    
    


book= Book("And Then There Were None", 272) 
print(book.title) 
print(book.page_count)      
    
        