import kotlin.math.pow

fun main() {
    //Forma incorrecta

    class Specie {

        fun specifySpecie(specie: String) {
            when (specie) {
                "humano" -> println("Hola soy un humano")
                "perro" -> println("Hola soy un perro")
                "gato" -> println("Soy un gato")
            }
        }
    }
    val subject1 = Specie()
    subject1.specifySpecie("humano")
    val subject2 = Specie()
    subject2.specifySpecie("perro")
    /*
    Esta forma es incorrecta para el OCP porque si hay que añadir especies hay que ir retocando la clase,
    lo que es lo contrario al principio Open/Closed
     */

    //Forma correcta
    abstract class Speciee {
        abstract fun identifySpecie(): String
    }

    class Humano(): Speciee() {
        override fun identifySpecie() = "Soy un humano con OCP"
        }
    class Perro(): Speciee() {
        override fun identifySpecie() = "Soy un perro con OCP"
        }
    class Gato(): Speciee() {
        override fun identifySpecie() = "Soy un gato con OCP"
        }
    val human = Humano()
    println(human.identifySpecie())
    val dog = Perro()
    println(dog.identifySpecie())
    val cat = Gato()
    println(cat.identifySpecie())

    /*
    Esta sí es buena forma de aplicar el OCP, pues enemos la clase base, con las funciones y ya
    a cada especie le crearíamos su clase con sus atributos y sobreescribiendo los métodos comunes
    que queramos.
    Estamos añadiendo funcionalidades sin tener que modificar la clase
     */

    println("\n ${"*".repeat(7)} EJERCICIO EXTRA ${"*".repeat(7)}")
    fun calculator() {
        print("Ingrese el primer número: ")
        val num1 = readln().toDouble()
        println("¿Qué operación quieres realizar con esos números?\n" +
                "Suma(+)\n" +
                "Resta(-)\n" +
                "Multiplicación(*)\n" +
                "División(/)" +
                "Exponente(**)")
        val operation = readln()
        when (operation) {
            "+" -> {val op = Sum()
                println(op.operation(num1))
            }
            "-" -> {val op = Subst()
                println(op.operation(num1))
            }
            "*" -> {val op = Mult()
                println(op.operation(num1))
            }
            "/" -> {val op = Div()
                println(op.operation(num1))
            }
            "**" -> {val op = PowMat()
                println(op.operation(num1))
            }
            else -> println("Opción no válida. Elige una de las disponibles")

        }
    }
    calculator()
}


interface Calculator {
    fun operation(num1: Double): Double
}

class Sum: Calculator{
    override fun operation(num1: Double): Double {
        print("Elige un segundo número: ")
        val num2 = readln().toInt()
        return num1 + num2
    }
}

class Subst: Calculator {
    override fun operation(num1: Double): Double {
        print("Elige un segundo número: ")
        val num2 = readln().toInt()
        return num1 - num2
    }
}
class Mult: Calculator {
    override fun operation(num1: Double): Double {
        print("Elige un segundo número: ")
        val num2 = readln().toInt()
        return num1 * num2
    }
}
class Div: Calculator {
    override fun operation(num1: Double): Double {
        print("Elige un segundo número: ")
        val num2 = readln().toInt()
        return num1 / num2
    }
}

class PowMat: Calculator {
    override fun operation(num1: Double): Double {
        print("A qué potencia quieres elevarlo? : ")
        val exp = readln().toDouble()

        return num1.pow(exp)
    }
}
