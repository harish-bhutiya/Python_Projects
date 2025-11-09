class Book:
    def __init__(self,title,author,available=True):
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self,title):
        #use lamda to search for books by title
        search_title = lambda book: book.title.lower() == title.lower()
        return list(filter(search_title,self.books))
    
    def search_by_author(self,author):
        search_author = lambda book: book.author.lower() == author.lower()
        return list(filter(search_author, self.books))
    
    def update_availability(self,title,available):
        #use lambda to update book availability
        update_book = lambda book: setattr(book,'available',available) if book.title.lower() == title.lower() else None
        list(map(update_book,self.books))

# Create instances of the book class
book1 = Book("Python programming","John Smith")
book2 = Book("Data Structures and Algorithms","Jane Doe")
book3 = Book("Web Development with Python","John Smith")

#Create an instance of the Library class
library = Library()

#add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Search for books by title
print("Books with title'Python Programming':")
for book in library.search_by_title("Python Programming"):
    print(f"-{book.title} by {book.author}")

#Search for books by author
print("\nBooks by author 'john Smith':")
for book in library.search_by_author("John Smith"):
    print(f"-{book.title} by {book.author}")

#Update book availability
library.update_availability("Data Structures and Algorithms",False)

#check updated availability
print("\nAvailability of 'Data Structures and Algorithms':")
for book in library.search_by_title("Data Structures and Algorithms"):
    print(f"- {book.title} is {'available' if book.available else 'not available'}")