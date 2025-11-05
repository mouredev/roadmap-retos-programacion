// Incorrecto
// class User {
//   String name;
//   String email;

//   User(this.name, this.email);

//   void saveToDatabase(String name, String email) {
//     print('User $name with email $email saved to database.');
//   }

//   void sendWelcomeEmail(String email) {
//     print('Welcome email sent to $email');
//   }

// }

// Corecto

class User {
  String name;
  String email;

  User(this.name, this.email);
}

class UserSeervice {
  void saveToDatabase(String name, String email) {
    print('User $name with email $email saved to database.');
  }
}

class EmailService {
  void sendWelcomeEmail(String email) {
    print('Welcome email sent to $email');
  }
}

// Ejercicio de biblioteca

// Icorrecto
// class Biblioteca {
//   List<Map<String, dynamic>> books = [];
//   List<Map<String, dynamic>> users = [];
//   List<String> loans = [];

//   void addBook(String title, String author, int copies) {
//     books.add({'title': title, 'author': author, 'copies': copies});
//     print('Book "$title" added to the library.');
//   }

//   void addUser(String name, String userId, int email) {
//     users.add({'name': name, 'userId': userId, 'email': email});
//     print('User "$userId" added to the database.');
//   }

//   void loanBook(String userId, String bookTitle) {
//     var user = users.firstWhere((u) => u['userId'] == userId, orElse: () => {});
//     var book = books.firstWhere((b) => b['title'] == bookTitle, orElse: () => {});

//     if (user.isEmpty) {
//       print('User not found.');
//       return;
//     }

//     if (book.isEmpty || book['copies'] <= 0) {
//       print('Book not available.');
//       return;
//     }

//     book['copies'] -= 1;
//     loans.add('User $userId loaned "$bookTitle"');
//     print('Book "$bookTitle" loaned to user $userId.');
//   }

//   void returnBook(String userId, String bookTitle) {
//     var book = books.firstWhere((b) => b['title'] == bookTitle, orElse: () => {});

//     if (book.isEmpty) {
//       print('Book not found in the library.');
//       return;
//     }

//     book['copies'] += 1;
//     loans.remove('User $userId loaned "$bookTitle"');
//     print('Book "$bookTitle" returned by user $userId.');
//   }
// }

// Correcto 
class Book {
  String title;
  String author;
  int copies;

  Book(this.title, this.author, this.copies);
}

class LibraryUser {
  String name;
  String userId;
  String email;

  LibraryUser(this.name, this.userId, this.email);
}

class Loan {
  List<Map<String, dynamic>> loans = [];

  void loanBook(LibraryUser user, Book book) {
    if (book.copies <= 0) {
      print('Book not available.');
      return;
    }

    book.copies -= 1;
    loans.add({'userId': user.userId, 'bookTitle': book.title});
    print('Book "${book.title}" loaned to user ${user.userId}.');
  }

  void returnBook(LibraryUser user, Book book) {
    book.copies += 1;
    loans.removeWhere((loan) => loan['userId'] == user.userId && loan['bookTitle'] == book.title);
    print('Book "${book.title}" returned by user ${user.userId}.');
  }
}

class Library {
  List<Book> books = [];
  List<LibraryUser> users = [];
  Loan loanService = Loan();

  void addBook(Book book) {
    books.add(book);
    print('Book "$book.title" added to the library.');
  }

  void addUser(LibraryUser user) {
    users.add(user);
    print('User "${user.userId}" added to the database.');
  }

  loanBook(LibraryUser user, Book book) {
    loanService.loanBook(user, book);
  }

  returnBook(LibraryUser user, Book book) {
    loanService.returnBook(user, book);
  }
}