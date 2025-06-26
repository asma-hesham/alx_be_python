from library_system import Book, EBook, printBook, Library

def main():
    my_library = Library()


    classic_book = Book("pride and prejudice", "jane Austen")
    digital_novel = EBook("snow crash", "Neal stephenson", 500)
    paper_novel = printBook("The catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()


if __name__=="__main__":
    main()
