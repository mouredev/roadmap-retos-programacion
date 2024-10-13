#Solid

#Incorrect behaviour

class Invoice:
    def addInvoice(self):
        pass
    def removeInvoice(self):
        pass
    def generateInvoiceReport(self):
        pass
    def sendInvoiceEmail(self):
        pass

# Same using single responsability Principle

class Invoice:
    def addInvoice(self):
        pass
    def removeInvoice(self):
        pass

class InvoiceReport:
    def generateInvoiceReport(self):
        pass

class InvoiceEmail:
    def sendInvoiceEmail(self):
        pass

#Extra

class Library:
    def __init__(self):
       self.books = []
       self.users = []
       self.loan = []
    def addBook(self,title,author,units):
        new_book = {
            "title":title,
            "author": author,
            "units" : units
        }
        self.books.append(new_book)
    def addUser(self,name,id,email):
        new_user ={
            "name": name,
            "id" : id,
            "email": email
        }
        self.users.append(new_user)

    def add_loan(self,title,name):

        num_loans = 0
        for element in self.loan:
            if element["title"] == title:
                num_loans+=1
        stock = 0
        for book in self.books:
            if book["title"] == title:
                stock = book["units"]

        if num_loans + 1 <= stock:
            new_loan = {
                "title":title,
                "name":name
            }       
            self.loan.append(new_loan) 
            print(f'New loan {title} user {name}')
        else:
            print("Loan is not possible since there is not stock available")    
    def remove_loan(self,title,name):
        for element in self.loan:
            if element["title"] == title and element["name"] == name:
                self.loan.remove(element)      
                break
        print(self.loan)    

library = Library()
library.addUser("Raul","12345678N","raul@test.com")
library.addUser("Maria","23450098T","maria@test.com")
library.addUser("Pepe","12344500V","pepe@test.com")
library.addBook("Harry Potter","JK Rowling",2)
library.addBook("El quijote","Miguel de Cervantes",5)

library.add_loan("Harry Potter","Raul")
library.add_loan("Harry Potter","Maria")
library.add_loan("El quijote","Pepe")
library.remove_loan("El quijote","Pepe")
library.remove_loan("Harry Potter","Maria")
library.add_loan("Harry Potter","Pepe")

class Book:
    def __init__(self,title,author,units):
        self.title = title
        self.author = author
        self.units = units
    def getTitle(self):
        return self.title
    def getAuthor(self):
        return self.author
    def getUnits(self):
        return self.units    

class BooksDB:
    def __init__(self):
        self.books=[]
    def add_book_db(self,book:Book):
        self.books.append(book)
    def remove_book_db(self,book:Book):
        self.books.remove(book)  

class User:
    def __init__(self,name,id,email):
        self.name = name
        self.id = id
        self.email = email
    def getName(self):
        return self.name
    def getId(self):
        return self.id
    def getEmail(self):
        return self.email

class UserDB:
    def __init__(self):
        self.users = []    
    def addUserDB(self,user:User):
        self.users.append(user)   
       
class BookLoan:
    def __init__(self):
        self.loans = []
    def addLoand(self,book:Book,user:User):
        num_loans = 0
        for loan in self.loans:
            if loan[0].getTitle() == book.getTitle():
                num_loans+=1

        if num_loans + 1 <= book.getUnits():
            self.loans.append((book,user))
            print(f'New loan {book.getTitle()} to user {user.getName()}')
        else:
            print("Loan is not possible since there is not stock available")
    def removeLoan(self,book:Book,user:User):
        for loan in self.loans:
            if loan[0].getTitle() == book.getTitle() and user.getName()==loan[1].getName():
                print(f'Removing loan {loan[0].getTitle()} user {loan[1].getName()}')        
                self.loans.remove(loan)
dbUser = UserDB() 
dbBooks = BooksDB()   
loan_handler = BookLoan()
user1 = User("Raul","25350036B","raul@test.com")
dbUser.addUserDB(user1)
user2 = User("Maria","15233454T","maria@test.com")
dbUser.addUserDB(user2)
book = Book("Harry Potter","JK Rowling",2)
dbBooks.add_book_db(book)
book2 = Book("El Quijote","Miguel de Cervantes",5)
dbBooks.add_book_db(book2)
loan_handler.addLoand(book,user1)
loan_handler.addLoand(book,user2)
loan_handler.removeLoan(book,user1)