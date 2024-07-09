/*
Liskov Sustitucion Principle
El Principio de Substitución de Liskov es uno de los principios SOLID y hace referencia a cómo usamos
la herencia de forma adecuada. El principio dice algo como lo siguiente si S es un subtipo de T , T
puede ser reemplazado con objetos de tipo S sin alterar el comportamiento esperado en el programa.
*/

// lo que no debe de hacer
open class BankAccount {
    private var balance = 0.0

    fun deposit(amount: Double){
        balance+=amount
    }
    open fun withdraw(amount: Double){
        balance-=amount
    }
    fun getBalance(): Double=balance
}

class NormalAccount: BankAccount()
// esta cuenta solo es de ahorro no permite hacer retiros por lo tanto
class SavingsAccount: BankAccount(){
    override fun withdraw(amount: Double) {
        throw Exception("Savings accounts cannot withdraw")
    }
}

// utilizando el principio de Liskov
// quitamos la clase witdraw de la clase BankAccount
open class BankAtm {
    protected var balance = 0.0

    fun deposit(amount: Double){
        balance+=amount
    }

    fun getBalanceAtm(): Double=balance
}
// delegamos la tarea a la cuenta corriente de poder hacer el deposito
class NormalAtm:BankAtm(){
    // nuevo objeto tipo S que no afecta el funcionamiento de la superclase
     fun withdraw(amount: Double){
        balance-=amount
    }
}
// ahora la cuenta de ahorro no necesita lanzar una excepcion
class SavingsAtm:BankAtm()


fun examplesLiskovSubstitution() {
    val account = NormalAccount()
    account.deposit(100.0)
    account.withdraw(50.0)
    println(account.getBalance())

    //val account2=SavingsAccount()
    //account2.withdraw(50.0)

    // nueva implementacion
    val atm = NormalAtm()
    atm.deposit(100.0)
    atm.withdraw(50.0)
    println(atm.getBalanceAtm())

    val atm2 = SavingsAtm()
    atm2.deposit(100.0)
    println(atm2.getBalanceAtm())
}

// ejercicio extra

open class Vehicle(protected val model:String,private val speed :Int){
    open fun accelerate(){
        println("$model accelerating at $speed km/h")
    }
    open fun brake(){
        println("brake $model")
    }
 }

// creando  subclases
 class Bus (model:String,speed:Int):Vehicle(model,speed){
     override fun accelerate(){
         super.accelerate()
     }
     override fun brake(){
         super.brake()
     }
 }
// el bote tiene una funcion para desanclar por lo tanto estamos agregando un objeto S sin afectar al
// comportamiento
class Boots(model:String,speed:Int):Vehicle(model,speed){
    override fun accelerate(){
        super.accelerate()
    }
    override fun brake(){
        super.brake()
    }
    fun anchorBoots(){
        println("anchor the boot $model")
    }
}
// el camion  de carga tambien necesita delegar el comportamiento a su clase y
// el objeto S no afecta el comportamiento
enum class Load{ COCONUTS,GRAVE,SUGAR}

class TruckLoad(model:String,speed:Int,val loadType:Load):Vehicle(model,speed){
    override fun accelerate(){
        super.accelerate()
    }
    override fun brake(){
        super.brake()
    }
    fun downLoad(){
        println("downloading $loadType")
    }
}

fun consumeVehicle(vehicle: Vehicle){
    vehicle.accelerate()
    vehicle.brake()
}

fun exampleLsp(){
    // crenado instancias
    val bus = Bus("Scania",120)
    val boot = Boots("Bayliner",250)
    val truck = TruckLoad("Kenworth",100,Load.GRAVE)
    // comprobando que el comportamiento no sea mutado
    consumeVehicle(bus)
    consumeVehicle(boot)
    consumeVehicle(truck)
    // llamndo objetos s particulares de cada  subclase
    truck.downLoad()
    boot.anchorBoots()
}


fun main() {
    examplesLiskovSubstitution()
    exampleLsp()
}