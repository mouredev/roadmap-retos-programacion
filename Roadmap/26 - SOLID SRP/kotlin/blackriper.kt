import io.github.oshai.kotlinlogging.KotlinLogging
import java.lang.System.exit
import java.util.UUID

/*
Single Responsibility Principle
establece que cada módulo o clase debe tener responsabilidad sobre una sola parte de la funcionalidad proporcionada por el software
y esta responsabilidad debe estar encapsulada en su totalidad por la clase. Todos sus servicios deben estar estrechamente alineados
con esa responsabilidad. Este principio está incluido en el acrónimo mnemotécnico SOLID. Robert C. Martin expresa el principio de la siguiente forma:


Una clase debe tener solo una razón para cambiar.

*/

// lo que no debe de hacerce
class AutoWash(var nameCar:String, private var registrationNumber: String) {
    private val costWashing=135.34

    fun startWashing(){
        println("Car ${nameCar} with registration number ${registrationNumber} was washed")
    }

    fun recivedPaymented(moneyRecived:Double) {
        println("the total cost of washing car ${nameCar} with registration number ${registrationNumber} was ${costWashing + moneyRecived}")
    }
}

// lo que debe de hacerce

// separamos las funcionalidades en  varias clases
data class Car(var nameCar:String,var registrationNumber:String){
    fun startWashing(){
        println("Car ${nameCar} with registration number ${registrationNumber} was washed")
    }
}


class Payment{
    private val costWashing=135.34
    fun recivedPaymented(car : Car,moneyRecived:Double) {
        val(nameCar,registrationNumber)=car
        println("the total cost of washing car ${nameCar} with registration number ${registrationNumber} was ${costWashing + moneyRecived}")
    }
}

// podemos usar una clase manager
class AutoWashSRP{
   private lateinit var car:Car
   private val payment=Payment()


    fun reciveCar(nameCar:String ,registrationNumber:String){
        car=Car(nameCar,registrationNumber)
        car.startWashing()
    }

    fun recivedPaymented(moneyRecived:Double){
        payment.recivedPaymented(car, moneyRecived)
    }
}

fun exampleSRP(){
    //antes
    val autoWash1=AutoWash("Nissan","ABC123")
    autoWash1.startWashing()
    autoWash1.recivedPaymented(155.34)
    // despues
    val autoWash=AutoWashSRP()
    autoWash.reciveCar("Ferrari","ABC1456")
    autoWash.recivedPaymented(455.34)
}

//ejercicio extra

//1.- defnir identidades
data class Book(
    val title: String,
    val author: String,
    var numCopies: Int
)

data class UserLib(
    val idUserLib: String,
    val name: String,
    val email: String
)

data class Loan(
    val idLoan:String,
    val nameUser:String,
    val nameBook:String
)

val logging= KotlinLogging.logger {  }


//2.-Crear clase monolito
class Library{
    private val books= mutableListOf<Book>()
    private val users= mutableListOf<UserLib>()
    private val loans= mutableListOf<Loan>()

   fun showMenu(){
      var option:Int=0
     while (option!=5) {
         println("1. Add book")
         println("2. Add user")
         println("3. Create loan")
         println("4. Return loan")
         println("5. Exit")
         println("Choose an option:")
          option = readLine()!!.toInt()
         when (option) {
             1 -> registerBook()
             2 -> registerUser()
             3 -> createLoan()
             4 -> returnLoan()
             else -> println("exit")
         }
     }
    }

   private fun registerBook(){
        println("title of the book:")
        val title= readLine()!!.toString()
        println("author of the book:")
        val author= readLine()!!.toString()
        println("number of copies:")
        val numCopies= readLine()!!.toInt()
        val book=Book(title,author,numCopies)
        books.add(book)
        logging.info {  "The book ${book.title} was added successfully"}
    }

    private fun registerUser(){
        println("name of the user:")
        val name= readLine()!!.toString()
        println("email of the user:")
        val email= readLine()!!.toString()
        val id=UUID.randomUUID().toString().substring(0, 8)
        val user=UserLib(id,name,email)
        users.add(user)
        logging.info {  "The user ${user.name} was added successfully"}
    }

   private  fun createLoan(){
        println("name of the user:")
        val nameUser= readLine()!!.toString()
        val existUser=users.find { it.name==nameUser }

        if(existUser==null){
          logging.warn { "user ${nameUser} not found" }
           println("user not found, please register first")
           return
        }
        var idx=1
        books.forEach {
            println("${idx}-${it.title}")
            idx++
        }

        println("choose de book to loan:")
        val bookIndice= readLine()!!.toInt()
        val book=books[bookIndice-1]
       if (book.numCopies>0) {
           val id = UUID.randomUUID().toString().substring(0, 8)
           val loan = Loan(id, nameUser, book.title)
           book.numCopies -= 1
           loans.add(loan)
           logging.info { "The loan ${loan.nameUser} was added successfully" }
       }else{
           logging.warn { "The book ${book.title} is not available" }
           println("The book ${book.title} is not available")
           return
       }
    }

   private  fun returnLoan() {
        println("name of the user:")
        val userName= readLine()!!.toString()
        val loan=loans.find { it.nameUser==userName }
        println("The book ${loan?.nameBook} was returned")
        logging.info { "The book ${loan?.nameBook} was returned" }
        val book=books.find { it.title==loan?.nameBook }
        book?.numCopies?.let { it + 1 }
        loan?.let { loans.remove(it) }

    }

}

// refactorizando codigo

//1.- vamos a definir el comportamiento que van a tener nuestras clases de acuerdo a su funcionalidad

enum class CopiesStatus{
    MINUS,PLUS
}


interface ForBooks{
    fun registerBook()
    fun selectedBooks():Book
    fun findBook(title: String):Book?
    fun updateCopies(title: String,op: CopiesStatus)
}

interface ForUsers{
  fun registerUser()
  fun findUser(name: String):UserLib?
}

interface ForLoans{
    fun createLoan(nameUser:String,title:String):Boolean
    fun getAllLoans():List<Loan>
    fun deleteLoan(repo:ForBooks)
}



//1.1.- Definir fake data pero esto es opcional y funcion auxiliar para ids

val generateIds={UUID.randomUUID().toString().substring(0, 8)}


var mockBooks= mutableListOf(
    Book("El principito","Antoine de Saint-Exupery",10),
    Book("El señor de los anillos","JRR Tolkien",5),
    Book("El Código da Vinci","Dan Brown",3),
    Book("Don Quijote de la Mancha","Miguel de Cervantes",2),
    Book("Harry Potter ","J.K. Rowling",1),
    Book("El resplandor","Stephen King",3),
    Book("El Alquimista","Paulo Coelho",4),
)

var mockUsers= mutableListOf(
    UserLib(generateIds(),"blackriper","XHqKm@example.com"),
    UserLib(generateIds(),"hdeleon","XHqKm@net.com"),
  )

//2.- Crear nuevas clases

class BookRepository:ForBooks{
    override fun registerBook() {
        println("title of the book:")
        val title= readLine()!!.toString()
        println("author of the book:")
        val author= readLine()!!.toString()
        println("number of copies:")
        val numCopies= readLine()!!.toInt()
        val book=Book(title,author,numCopies)
        mockBooks.add(book)
        logging.info {  "The book ${book.title} was added successfully"}
    }

    override fun selectedBooks():Book {
        var idx=1
        mockBooks.forEach {
            println("${idx}-${it.title}")
            idx++
        }

        println("choose de book to loan:")
        val bookIndice= readLine()!!.toInt()
        val book= mockBooks[bookIndice-1]
        logging.trace { "The book ${book.title} selected successfully"}
        return book
    }

    override fun findBook(title: String): Book? {
        val book= mockBooks.find { it.title==title }
        logging.info { "The book ${book?.title} was found successfully" }
        return book

    }

    override fun updateCopies(title: String, op: CopiesStatus) {
       val bookFind=findBook(title)?:return
         when(op){
            CopiesStatus.PLUS ->{
                bookFind.numCopies+=1
                logging.info { "The book ${bookFind.title} has ${bookFind.numCopies}" }
            }
            CopiesStatus.MINUS -> {
                bookFind.numCopies-=1
                logging.info { "The book ${bookFind.title} has ${bookFind.numCopies}" }
            }
        }
    }

}

class RepositoryUser:ForUsers{
     override fun registerUser() {
        println("name of the user:")
        val name= readLine()!!.toString()
        println("email of the user:")
        val email= readLine()!!.toString()
        val user=UserLib(generateIds(),name,email)
        mockUsers.add(user)
        logging.info {  "The user ${user.name} was added successfully"}
    }

    override fun findUser(name: String): UserLib? {
        val user= mockUsers.find { it.name==name }
        logging.info { "The user ${user?.name} was found successfully" }
        return user
    }

}


class RepositoryLoans:ForLoans{
    private val loans= mutableListOf<Loan>()

    override fun createLoan(nameUser: String, title: String):Boolean {
        val loan = Loan(generateIds(), nameUser, title)
        loans.add(loan)
        logging.info { "The loan ${loan.nameUser} was added successfully" }
        return true
    }

    override fun getAllLoans(): List<Loan> = loans

    override fun deleteLoan(repo:ForBooks) {
        println("name of the user:")
        val userName= readLine()!!.toString()
        loans.find { it.nameUser==userName }.let {
            println("The book ${it?.nameBook} was returned")
            logging.info { "The book ${it?.nameBook} was returned" }
            repo.updateCopies(it?.nameBook!!, CopiesStatus.PLUS)
            loans.remove(it)
        }
    }

}

 class LibrarySRP {
     // hacemos la instancia de cada clase
     private val bookRepo = BookRepository()
     private val userRepo = RepositoryUser()
     private val loanRepo = RepositoryLoans()

     fun showMenu() {
         var option: Int = 0
         while (option != 6) {
             println("1. Add book")
             println("2. Add user")
             println("3. Create loan")
             println("4. Return loan")
             println("5.-List loans")
             println("6. Exit")
             println("Choose an option:")
             option = readLine()!!.toInt()
             when (option) {
                 1 -> bookRepo.registerBook()
                 2 -> userRepo.registerUser()
                 3 -> createLoan()
                 4 -> loanRepo.deleteLoan(bookRepo)
                 5 -> showLoans()
                 else -> println("exit")
             }
         }
     }

     private fun createLoan() {
         println("name of the user:")
         val nameUser = readLine()!!.toString()
         val existUser = userRepo.findUser(nameUser)
         if (existUser == null) {
             logging.error { "The user ${nameUser} not found" }
             return
         }
         val book = bookRepo.selectedBooks()
         if (book.numCopies > 0) {
             loanRepo.createLoan(existUser.name, book.title).run {
                 if (this) bookRepo.updateCopies(book.title, CopiesStatus.MINUS)
             }
         } else {
             logging.warn { "The book ${book.title} is not available" }
             println("The book ${book.title} is not available")
             return
         }
     }

     private fun showLoans() {
         loanRepo.getAllLoans().forEach {
             println("id: ${it.idLoan} - User: ${it.nameUser} - Book: ${it.nameBook}")
         }
     }
 }

fun main() {
   exampleSRP()
  // val library=Library()
   //library.showMenu()
    val library=LibrarySRP()
    library.showMenu()
}
