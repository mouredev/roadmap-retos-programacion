import Foundation

/*
 Single Responsability Principle (SRP):

establece que cada módulo o clase debe tener responsabilidad sobre una sola parte de la funcionalidad
proporcionada por el software y esta responsabilidad debe estar encapsulada en su totalidad por la clase. 

En programación orientada a objetos, se suele definir como principio de diseño que cada clase debe tener una única responsabilidad, y que esta debe estar contenida únicamente en la clase. Así:

Una clase debería tener solo una razón para cambiar
Cada responsabilidad es el eje del cambio
Para contener la propagación del cambio, debemos separar las responsabilidades.
Si una clase asume más de una responsabilidad, será más sensible al cambio.
Si una clase asume más de una responsabilidad, las responsabilidades se acoplan.
*/

// forma incorrecta
 class CheckingHours{
    private var horaries:[String:[[String:String]]] = ["Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[]]

    func registerEmployee(name:String,day:String){
        horaries[day]?.append([UUID().uuidString:name])
    }

    func changeDay(day:String,name:String,oldDay:String){
        horaries[day]?.append([UUID().uuidString:name])
        horaries[oldDay]?.removeAll(where: {$0.values.contains(name)})
    }

    func showHorary(){
        print("Horaries Empleoyee")
        horaries.forEach { day in
            print(day.key)
            print("_____________")
            day.value.forEach { employee in
                employee.values.forEach{
                        print($0)
                    }            
        }
    }
  }
}

let checking = CheckingHours()
checking.registerEmployee(name: "John", day: "Monday")
checking.registerEmployee(name: "blackriper", day: "Friday")
checking.showHorary()
checking.changeDay(day: "Monday", name: "blackriper", oldDay: "Friday")
checking.showHorary()


// forma correcta
struct Empleoyee{
        let id:String=UUID().uuidString
        let name:String 

        func getInfo()->String{
            return "\(id) \(name)"
                
        }
 }

 enum Day{
    case Monday
    case Tuesday
    case Wednesday
    case Thursday
    case Friday
 }

 class ManagerHours{
      private var hours:[Day:[Empleoyee]] = [.Monday:[],.Tuesday:[],.Wednesday:[],.Thursday:[],.Friday:[]]

      func registerEmployee(emp:Empleoyee,day:Day){
          hours[day]?.append(emp)
      }

      func changeDay(empleoyee:Empleoyee,day:Day,oldDay:Day){
          hours[day]?.append(empleoyee)
          hours[oldDay]?.removeAll(where: {$0.id == empleoyee.id})
      }


      func showHorary(){
          hours.forEach { day in
              print(day.key)
              print("_____________")
              day.value.forEach { employee in
                  print(employee.getInfo())
              }
          }
      }
 }

let checkSRP = ManagerHours()
let emp1=Empleoyee(name: "John")
let emp2=Empleoyee(name: "blackriper")

checkSRP.registerEmployee(emp: emp1, day: .Monday)
checkSRP.registerEmployee(emp: emp2, day: .Friday)
print("Horaries Empleoyee 1")
checkSRP.showHorary()
checkSRP.changeDay(empleoyee: emp2, day: .Tuesday, oldDay: .Friday)
print("Horaries Empleoyee 2")
checkSRP.showHorary()

// ejercicio extra

//generar fechas 
func generateDate()->String{
 let format=DateFormatter()
 format.dateFormat="dd/MM/yyyy"
 let date=Date()
 return  format.string(from: date)
 }



struct Book{
    let title:String
    let author:String
    var numCopies:Int

}


struct User{
    let userId:String=UUID().uuidString.substring(to: 8)
    let name:String
    let email:String
 }

struct Loan{
   let id:String=UUID().uuidString.substring(to: 8)
   let dateLoan:String=generateDate()
   let nameUser:String
   let numUser:String
   let titleBooks:[String]
 }

class Library{
    private var books:[Book] = []
    private var users:[User] = []
    private var loans:[Loan] = []

    private func registerBook(){
        print("Enter book title")
        let title=readLine()!
        print("Enter book author")
        let author=readLine()!
        print("Enter number of copies")
        let numCopies=readLine() ?? "1"
        let book=Book(title: title, author: author, numCopies: Int(numCopies) ?? 1)
        books.append(book)
    }

   private  func registerUser(){
        print("Enter user name")
        let name=readLine()!
        print("Enter user email")
        let email=readLine()!
        let user=User(name: name, email: email)
        users.append(user)
    }


   private func registerLoan(){

        var titlesBooks:[String] = []
        var option:String=""

        print("Enter username or  userId")
        let input=readLine()!
        guard let user=users.first(where: {$0.name == input || $0.userId == input}) else{
            print("User not found")
            return
        }
        while option != "n"{
        var idx=1             
        books.forEach{ book in 
            print("\(idx)   \(book.title)")
            idx+=1
        }
        print("Enter book number")
        let inputBook=Int(readLine()!) ?? 0
        var book=books[inputBook-1] 

          titlesBooks.append(book.title)
          book.numCopies-=1
          print("Do you want to add another book? (y/n)")
          option=readLine() ?? "n"
        }

        let loan=Loan(nameUser: user.name, numUser: user.userId, titleBooks: titlesBooks)
        loans.append(loan)

    }

   private func returnigBooks(){
        print("Enter username or  userId")
        let input=readLine()!
        guard let user=users.first(where: {$0.name == input || $0.userId == input}) else{
            print("User not found")
            return
        }

        guard let loan=loans.first(where: {$0.nameUser == user.name}) else{
            print("Loan not found")
            return
        }

        loan.titleBooks.forEach{ (title) in
            guard var book=books.first(where: {$0.title == title}) else{
                print("Book not found")
                return
            }
            book.numCopies+=1
        }
        loans.removeAll(where: {$0.id == loan.id})
        print("Loans \(loan.id) returned successfully")
    
    }

    func showMenu(){
        var option:Int = 0 
        while option != 5{
             print("Library Menu")
             print("_________________")
             print("1. Register book")
             print("2. Register user")
             print("3. Register loan")
             print("4. Returnig books")
             print("5. Exit")

             print("Enter option")
             option=Int(readLine() ?? "5") ?? 5
             if option == 1{
                registerBook()
             }else if option == 2{
                registerUser()
             }else if option == 3{
                registerLoan()
             }else if option == 4{
                returnigBooks()
             }

        }
    }

}

//let library=Library()
//library.showMenu()

// aplicando el principio de responsabilidad unica

//1.- Creamos un mock de pruebas  opcional
var books: [Book] = [
    Book(title: "El Señor de los Anillos", author: "J.R.R. Tolkien", numCopies: 10),
    Book(title: "Cien Años de Soledad", author: "Gabriel García Márquez", numCopies: 15),
    Book(title: "One Piece", author: "Eiichiro Oda", numCopies: 20), 
    Book(title: "Dragon Ball", author: "Akira Toriyama", numCopies: 30),
    Book(title: "Fundación", author: "Isaac Asimov", numCopies: 5)
]

var users: [User] = [
    User(name: "John", email: "pNzJG@example.com"),
    User(name: "blackriper", email: "pNzJG@example.com")
]

//2.- delegar responsabilidades a las estructuras  de datos y controlar comportamientos con protocols
 
protocol ForBooks{
   func insertBooks()
   func showAllBooks()
   func findBook(filter:(Book) ->Bool)->Book
   func findBookByIndex(index:Int)->Book
}

protocol ForUsers{
   func insertUsers() 
   func findUser(value:String)->User
 }

protocol ForLoans{
   func insertLoans(nameUser:String,numUser:String,titleBooks:[String]) 
   func showLoans()
   func findLoan(filter:(Loan) ->Bool)->Loan
   func deleteLoan(idLoan:String)
  }


  class BookRepository:ForBooks{
   
    func insertBooks() {
        print("Enter book title")
        let title=readLine()!
        print("Enter book author")
        let author=readLine()!
        print("Enter number of copies")
        let numCopies=readLine() ?? "1"
        let book=Book(title: title, author: author, numCopies: Int(numCopies) ?? 1)
        books.append(book) 
   }

    func showAllBooks() {
        var idx=1
        books.forEach{ book in 
            print("ID:\(idx) Title: \(book.title) Author: \(book.author) Copies: \(book.numCopies)")
            idx+=1
        }
   }

    func findBook(filter: (Book) -> Bool) -> Book {
           guard let book=books.first(where: filter ) else{
            print("Book not found")
            return Book(title: "", author: "", numCopies: 0)
        }
         return book
   }

    func findBookByIndex(index: Int) -> Book {
       return books[index-1]
   }
 }


 class UserRepository:ForUsers{
     
       func insertUsers() {
        print("Enter user name")
        let name=readLine()!
        print("Enter user email")
        let email=readLine()!
        let user=User(name: name, email: email)
        users.append(user)
        print("User with id \(user.userId) created successfully")
        
     }

      func findUser(value:String )-> User {
       guard let user = users.first(where: {$0.name == value || $0.userId == value}) else{
           print("User not found")
           return User(name: "", email: "")
       }
       return user
     }
 }

 class LoanRepository:ForLoans{
    private var loans:[Loan] = []

    func insertLoans(nameUser: String, numUser: String, titleBooks: [String]) {
      let loan=Loan(nameUser: nameUser, numUser:numUser, titleBooks: titleBooks)
      loans.append(loan) 
    }

    func showLoans() {
        loans.forEach{ loan in
            print("ID: \(loan.id) Date: \(loan.dateLoan) User: \(loan.nameUser) Books: \(loan.titleBooks)")
        }
    }

    func findLoan(filter: (Loan)  -> Bool) -> Loan {
        guard let loan=loans.first(where: filter ) else{
           print("Loan not found")
           return Loan(nameUser: "", numUser: "", titleBooks: [])
       }
        return loan
    }

     func deleteLoan(idLoan: String) {
        loans.removeAll(where: {$0.id == idLoan})
    }

 }

 class SRPLibrary{
    private var bookRepository=BookRepository()
    private var userRepository=UserRepository()
    private var loanRepository=LoanRepository()

   private func lendBooks(){
        var titlesBooks:[String] = []
        var option:String=""

        print("Enter username or  userId")
        let input=readLine()!
        let user = userRepository.findUser(value: input)
        if user.name == ""{
            return
         }
        
         while option != "n"{
            bookRepository.showAllBooks()
            print("Enter book number")
            let inputBook=Int(readLine()!) ?? 0
            var book=bookRepository.findBookByIndex(index: inputBook)
            titlesBooks.append(book.title)
            book.numCopies-=1
            books[inputBook-1]=book

            print("Do you want to add another book? (y/n)")
            option=readLine() ?? "n"
        }
        loanRepository.insertLoans(nameUser: user.name, numUser: user.userId, titleBooks: titlesBooks)
    }

   private  func returnigBooks(){
        print("Enter username or  userId")
        let input=readLine()!
        let loan=loanRepository.findLoan(filter: {$0.nameUser == input || $0.numUser == input})
        if loan.nameUser == ""{
            return
        }
        retryBooks(titleBooks: loan.titleBooks)
        loanRepository.deleteLoan(idLoan: loan.id)
        print("Loans \(loan.id) returned successfully")

     }

     func showMenu(){
        var option:Int = 0 
        while option != 6{
             print("Library Menu")
             print("_________________")
             print("1. Register book")
             print("2. Register user")
             print("3. Register loan")
             print("4. Show loans")
             print("5. Returnig books")
             print("6. Exit")

             print("Enter option")
             option=Int(readLine() ?? "6") ?? 6
             switch option {
             case 1:
                bookRepository.insertBooks()
             case 2:
                userRepository.insertUsers()
             case 3:
                lendBooks()
             case 4:
                loanRepository.showLoans()
             case 5:
                returnigBooks()
             default:
                break
             }
        }
    }

   private func retryBooks(titleBooks :[String]){
       Task{
         titleBooks.forEach{ (title) in
            var book=bookRepository.findBook(filter: {$0.title == title})
             book.numCopies+=1
      }
    }
  }
 }

 let library=SRPLibrary()
 library.showMenu()
