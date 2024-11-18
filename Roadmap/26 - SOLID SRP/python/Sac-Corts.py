# Incorrecto
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate_report(self):
        return f"Title: {self.title}\nContent: {self.content}"

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(self.generate_report())

report = Report("Monthly Report", "This is the content of the monthly report.")
print(report.generate_report())
report.save_to_file("report.txt")

# Correcto
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate_report(self):
        return f"Title: {self.title}\nContent: {self.content}"

class ReportSaver:
    @staticmethod
    def save_to_file(report, filename):
        with open(filename, 'w') as file:
            file.write(report.generate_report())

report = Report("Monthly Report", "This is the content of the monthly report.")
print(report.generate_report())
ReportSaver.save_to_file(report, "report.txt")

### Ejercicio Extra ###

# Incorrecto

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def register_book(self, title, author, copies):
        self.books[title] = {'author': author, 'copies': copies}

    def register_user(self, user_id, name, email):
        self.users[user_id] = {'name': name, 'email': email}

    def borrow_book(self, user_id, title):
        if title in self.books and self.books[title]['copies'] > 0:
            self.books[title]['copies'] -= 1
            self.loans.append({'user_id': user_id, 'title': title})
        else: 
            print("Book not available")

    def return_book(self, user_id, title):
        for loan in self.loans:
            if loan['user_id'] == user_id and loan['title'] == title:
                self.books[title]['copies'] += 1
                self.loans.remove(loan)
                break
        else:
            print("Loan record not found")

# Correcto

class BookManager:
    def __init__(self):
        self.books = {}

    def register_book(self, title, author, copies):
        self.books[title] = {'author': author, 'copies': copies}

    def is_book_available(self, title):
        return title in self.books and self.books[title]['copies'] > 0

    def borrow_book(self, title):
        if self.is_book_available(title):
            self.books[title]['copies'] -= 1
        else:
            raise ValueError("Book not available")

    def return_book(self, title):
        if title in self.books:
            self.books[title]['copies'] += 1
        else:
            raise ValueError("Book not found")
        
class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, user_id, name, email):
        self.users[user_id] = {'name': name, 'email': email}

    def is_user_registered(self, user_id):
        return user_id in self.users
    
class LoanManager:
    def __init__(self, book_manager, user_manager):
        self.book_manager = book_manager
        self.user_manager = user_manager
        self.loans = []

    def borrow_book(self, user_id, title):
        if self.user_manager.is_user_registered(user_id):
            self.book_manager.borrow_book(title)
            self.loans.append({'user_id': user_id, 'title': title})
        else:
            raise ValueError("User not registered")
        
    def return_book(self, user_id, title):
        for loan in self.loans:
            if loan['user_id'] == user_id and loan['title'] == title:
                self.book_manager.return_book(title) 
                self.loans.remove(loan)
                return
        raise ValueError("Loan record not found")


book_manager = BookManager()
user_manager = UserManager()
loan_manager = LoanManager(book_manager, user_manager)

book_manager.register_book("The Great Gatsby", "F. Scott Fitzgerald", 5)

user_manager.register_user(1, "Isaac", "isaacgeo125@gmail.com")

loan_manager.borrow_book(1, "The Great Gatsby")
loan_manager.return_book(1, "The Great Gatsby")