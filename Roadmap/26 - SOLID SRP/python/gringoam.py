

"""
Extra
"""

""" class Library:
    def __init__(self):
        self.books=[]
        self.users=[]
        self.loans=[]
    
    
    def addBook(self, title, author, copies):
        self.books.append({"Title":title, "Author": author, "Copies":copies})

    def addUser(self, name, id_user, mail):
        self.users.append({"name":name, "id usuer": id_user, "e-mail":mail})

    def loan_book(self, title_book, id_user):
        for book in self.books:
            if book["Title"]== title_book and book["Copies"]> 0:
                self.loans.append({"id_user": id_user, "Title book": title_book})
                book["Copies"]-=1
                return True
        return False

    def return_book(self, title_book, id_user):
        for loan in self.loans:
            if loan["Title book"]== title_book and loan["id_uaser"]== id_user:
                self.loans.remove(loan)
                for book in self.books: 
                    if book["Title"]== title_book:
                        book["Copies"]+=1
                    return True
        return False   """

#Correcto

class Book:
    def __init__(self, title, author, copies): 
        self.title= title
        self.author=author
        self.copies=copies
    
class User:
      def __init__(self, name, id, mail): 
        self.name= name
        self.id=id
        self.mail= mail

class Loan:
     
     def __init__(self):
        self.loans = []

     def loan_book(self, book, user):
        if book.copies> 0:
            self.loans.append({"id_user": user.id , "Title book": book.title})
            book.copies-=1
            return True
        return False
     
     def return_book(self, book, user):
        for loan in self.loans:
            if loan["Title book"]== book.tilte and loan["id_uaser"]== user.id:
                self.loans.remove(loan)
                book.copies+=1
                return True
        return False
       
     def see_loans(self):
        print(self.loans)
    
class Library:

    def __init__(self):
        self.books=[]
        self.users=[]
        self.loans_service= Loan()
    

    def addBook(self, book):
        self.books.append(book)

    def addUser(self, user):
        self.users.append(user)


    def loan_book(self, user_id, book_title):
        user= next((u for u in self.users if user_id == u.id), None)
        book= next((b for b in self.books if book_title == b.title), None)
        if user and book:
            return self.loans_service.loan_book(book, user)
        return False  

    def return_book(self, user_id, book_title):
        user= next((u for u in self.users if user_id == u.id), None)
        book= next((b for b in self.books if book_title == b.title), None)
        if user and book:
            return self.loans_service.return_book(book, user)
        return False    
    
    


book= Book("Progamador", "Diego", 2)
user= User("Ariel", 1, "ari@hot.com")

library= Library()

library.addBook(book)
library.addUser(user)
library.loan_book(user.id, book.title)
#library.loans_service.see_loans()

book1= Book("Desarrollador", "Ariel", 3)
user1= User("Diego", 2, "ari@hot.com")

library.addBook(book1)
library.addUser(user1)
library.loan_book(user1.id, book1.title)
library.loans_service.see_loans()

library.loans_service.see_loans()
