/*
Interface Segregation Principle

Este principio nos dice que una clase nunca debe extender de interfaces con métodos que no usa,
por el principio de segregación de interfaces busca que las interfaces sean lo más pequeñas
y específicas posible de modo que cada clase solo implemente los métodos que necesita.

errores comunes con este principio

- Estaremos violando este principio si Tenemos clases que implementan métodos de interfaces que no se usan.

- Definimos interfaces con parámetros que no se van a utilizar en todas las clases

-cuando tenemos interfaces muy grandes y métodos que no son genéricos y que otras clases que implementen esta interfaz no puedan usar

*/

//ejemplo de lo que no debe de hacerce


interface Bank {
    fun deposit(amount: Double)
    fun withdraw(amount: Double)
    fun getBalance()
}

class AccountNormal(private var balance: Double):Bank{
    override fun deposit(amount: Double) {
        balance+=amount
    }

    override fun withdraw(amount: Double) {
        balance-=amount
    }

    override fun getBalance() {
        println("the balance is $balance")
    }

}
// esta cuenta solo es de imversion y esta no pueda hacer retiros por lo tanto rompe este principio
// porque solo retornamos el error
class InterestAccount(private var balance: Double):Bank {
    override fun deposit(amount: Double) {
        balance += amount
    }

    override fun withdraw(amount: Double) {
        throw Exception("not allowed this operation")
    }

    override fun getBalance() {
        println("the balance is $balance")
    }
}

// lo que debe de hacerce

// quitamos el metodo que solo se permite  en las dos clases
interface LspBank{
    fun deposit(amount: Double)
    fun getBalance()
}
//las inferfaces pueden extender de otras interfaces ahora este inferfaz hija herera los metodos del padre
// pero agrega la fucnionalidad de withdraw
interface LspNormalBank : LspBank{
    fun withdraw(amount: Double)
}

class NormalAccountLsp(private var balance: Double):LspNormalBank {
    override fun withdraw(amount: Double) {
        balance -= amount
    }

    override fun deposit(amount: Double) {
        balance += amount
    }

    override fun getBalance() {
        println("the balance is $balance")
    }
}

class InterestAccountLsp(private var balance: Double):LspBank {
    override fun deposit(amount: Double) {
        balance += amount
    }

    override fun getBalance() {
        println("the balance is $balance")
    }
}

fun exmapleLsp(){
    val normal = NormalAccountLsp(100.0)
    normal.deposit(100.0)
    normal.getBalance()
    normal.withdraw(50.0)
    normal.getBalance()

    val inv = InterestAccountLsp(100.0)
    inv.deposit(100.0)
    inv.getBalance()

    println("violation this principle")
    // clase  que  viola esta principio
    val interest = InterestAccount(100.0)
    interest.deposit(100.0)
    interest.getBalance()
    // me veo forzado a chacar el error
    runCatching { interest.withdraw(50.0)}.let { println(it.exceptionOrNull()?.message) }
    interest.getBalance()
}

//ejercicio extra

enum class ColorPrint{
    BLACK_AND_WHITE,
    COLOR
}

interface Printer{
    fun print(document:String)
}

// aplicando el principio de ISP para crear una nueva interfaz cuando esta tenga multiples funciones
interface MultiFunctionPrinter : Printer{
    fun sendFax(document:String):Boolean
    fun scan(document:String)
}

class NormalPrinter(val color:ColorPrint):Printer{
    override fun print(document: String) {
        println("Printing $document in color: $color")
    }

 }

class MultiFuncPrinter(val color:ColorPrint):MultiFunctionPrinter {
    override fun sendFax(document: String): Boolean {
        if (document.isNotEmpty()){
            println("Sending $document by fax")
            return true
        }
        return false
    }

    override fun scan(document: String) {
        document.isNotEmpty().run {
            println("Scanning $document")
        }
    }

    override fun print(document: String) {
        println("Printing $document in color: $color")
    }
}

fun pritingDocument(printer:Printer, document:String){
    printer.print(document)
}

fun examplePrinter(){
    val normalPrinter = NormalPrinter(ColorPrint.BLACK_AND_WHITE)
    pritingDocument(normalPrinter,"Hello World")
    val multiFuncPrinter = MultiFuncPrinter(ColorPrint.COLOR)
    pritingDocument(multiFuncPrinter,"Kotlin is son of Java")
    multiFuncPrinter.sendFax("Hello Comunity")
    multiFuncPrinter.scan("Hello World")
}


fun main() {
    exmapleLsp()
    examplePrinter()
}