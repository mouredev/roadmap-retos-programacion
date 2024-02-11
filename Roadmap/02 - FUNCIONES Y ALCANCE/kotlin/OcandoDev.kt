// Variable global
const val username  = "OcandoDev"

//funcion simple
fun greeting(){
    println("Hola $username!")
}

//funcion con parametros
fun sum(a: Int, b: Int): Int{
    return a + b
}

//funcion con argumentos por defecto
fun calculateArea(width: Int, height: Int = 10): Int{
    return width * height
}

//funcion de Unit
fun printMessage(message: String){
    println(message)
}

//funcion de orden superior
fun operation(a: Int, b: Int, operation: (Int, Int) -> Int): Int{
    return operation(a, b)
}

//funcion con extension
fun String.inUpperCase(): String{
    return this.uppercase()
}

//funcion anonima
val havingFun = fun(a: Boolean): String{
    return when (a) {
        true -> "Super! :D"
        false -> "You should practice more to have fun :)"
        else -> "Sorry! I don't get it"
    }
}

//funcion infija
infix fun String.sameAs(txt: String): Boolean {
    return this == txt
}

// ---Ejercicio---
fun fizzbuzz(fizz: String, buzz: String): Int {
    var count = 0
    for (i in 1..100) {

        when {
            i % 3 == 0 && i % 5 == 0 -> {
                print("$fizz$buzz ")
            }

            i % 3 == 0 -> {
                print("$fizz ")
            }

            i % 5 == 0 -> {
                print("$buzz ")
            }

            else -> {
                print("$i ")
                count++
            }
        }
    }
    println()
    return count
}

    fun main(){
        greeting()

        //Variable local
        val result = sum(4, 4)
        println(result)

        val area = calculateArea(2)
        println(area)

        printMessage("This is a unit function!")

        //funcion de order superior
        val substraction = {a: Int, b: Int -> a - b }
        val substraction_result = operation(6, 3, substraction)
        println(substraction_result)

        val numberList = listOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        //funcion lambda
        val evenNumbers = numberList.filter {it % 2 == 0}
        print("$evenNumbers ")

        println()

        val usernameUpperCase = username.inUpperCase()
        println(usernameUpperCase)

        //funcion local
        fun farewell(name: String): String{
            return "Bye $name!"
        }
        println(farewell(username))

        val status = havingFun(true)
        println(status)

        val person1 = "Alejandro"
        val person2 = "Alejandro"

        val samePerson = person1 sameAs person2
        println(samePerson)

        println("EJERCICIO EXTRA!")
        println(fizzbuzz("fizz", "buzz"))
    }