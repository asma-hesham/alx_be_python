#base class
class Book:
    def __init_(self, title:str , author:str ):
        self.title = title
        self.author = author


    def get_details(self):
        return f"Book: {self.title} by {self.author}"


#derived class
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        return f"Book: {self.title} by {self.author} file size {self.file_size}"   


#derived class 
class printBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        return f"Book: {self.title} by {self.author} and page count {self.page_count} "
    

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
     self.books.append(book)


     def List_books(self):
         for book in self.books:
             print(self.get_details()) 
            
=======
#base class
class Book:
    def __init_(self, title:str, author:str ):
        self.title = title
        self.author = author


    def get_details(self):
        return f"Book: {self.title} by {self.author}"


#derived class
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        return f"Book: {self.title} by {self.author} file size: {self.file_size}"   


#derived class 
class printBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        return f"Book: {self.title} by {self.author} and page count {self.page_count} "
    

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
     self.books.append(book)


     def List_books(self):
         for book in self.books:
             print(self.get_details()) 
