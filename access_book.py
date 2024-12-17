class Book:
    book_title = None
    _author = None
    __number_of_copies = None

    def __init__(self,book_title, author, number_of_copies):
        self.book_title = book_title
        self._author = author
        self.__number_of_copies = number_of_copies
# public member fn;
    def get_book_title(self):
        return self.book_title
#protected membr fn
    def get_author(self):
        return self._author
#prvt membr fn
    def get_number_of_copies(self):
        return self.__number_of_copies
    
    #issue book method
    def issue_book(self):
        self.__number_of_copies = int(self.__number_of_copies)-1
        print(f"{self.book_title} issued successfully!.., Number of copies left={self.__number_of_copies}")

    #return book method
    def return_book(self):
        print(f"{self.book_title} returned Successfully!..")
        self.__number_of_copies = int(self.__number_of_copies)+1
        print(f"Total available copies= {self.__number_of_copies}")

class Librarian(Book):
    def __init__(self, book_title, author, number_of_copies):
        super().__init__(book_title, author, number_of_copies)

    #display book details
    def display_bookDetails(self):
        print("Title :",self.get_book_title())
        print("Author :",self.get_author())
        print("No of Copies :",self.get_number_of_copies())

#instances of book class
lib = Librarian("One you cannot have","Preeti shenoy",300)
lib.display_bookDetails()
lib.issue_book()
lib.issue_book()
lib.issue_book()
lib.return_book()
lib.get_number_of_copies()


