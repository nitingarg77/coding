

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
        return f"{self.title} by {self.author}"



book1 = Book("a", "x", 250)        
book2 = Book("b", "y", 150)   
book3 = Book("c", "w", 340)   
book4 = Book("d", "z", 600)



print(book1)

print(f"{book1.pages + book2.pages}")