class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author 
    def __str__(self):
        return f"Book: {self.title} by {self.author} "
book1=Book(1984,"George Orwell")

print(book1)