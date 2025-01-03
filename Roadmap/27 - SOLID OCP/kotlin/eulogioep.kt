/*
 * Principio Abierto-Cerrado (OCP) de SOLID
 * 
 * El principio OCP establece que las entidades de software (clases, módulos, funciones, etc.) 
 * deben estar abiertas para la extensión, pero cerradas para la modificación. Esto significa 
 * que debemos poder extender el comportamiento de una clase sin modificar su código existente.
 * 
 * En este ejemplo, demostraremos cómo aplicar el OCP en el diseño de una calculadora,
 * permitiendo agregar nuevas operaciones sin modificar el código existente.
 */

// Interfaz que define la operación matemática
interface Operation {
    fun execute(a: Double, b: Double): Double
}

// Implementaciones de las operaciones básicas
class Addition : Operation {
    override fun execute(a: Double, b: Double) = a + b
}

class Subtraction : Operation {
    override fun execute(a: Double, b: Double) = a - b
}

class Multiplication : Operation {
    override fun execute(a: Double, b: Double) = a * b
}

class Division : Operation {
    override fun execute(a: Double, b: Double): Double {
        if (b == 0.0) throw IllegalArgumentException("Cannot divide by zero")
        return a / b
    }
}

// Calculadora que utiliza el principio OCP
class Calculator {
    private val operations = mutableMapOf<String, Operation>()

    fun addOperation(name: String, operation: Operation) {
        operations[name] = operation
    }

    fun calculate(a: Double, b: Double, operationName: String): Double {
        val operation = operations[operationName] 
            ?: throw IllegalArgumentException("Operation not supported")
        return operation.execute(a, b)
    }
}

// Ejemplo de uso y prueba
fun main() {
    val calculator = Calculator()

    // Agregar operaciones básicas
    calculator.addOperation("add", Addition())
    calculator.addOperation("subtract", Subtraction())
    calculator.addOperation("multiply", Multiplication())
    calculator.addOperation("divide", Division())

    // Probar operaciones básicas
    println("5 + 3 = ${calculator.calculate(5.0, 3.0, "add")}")
    println("5 - 3 = ${calculator.calculate(5.0, 3.0, "subtract")}")
    println("5 * 3 = ${calculator.calculate(5.0, 3.0, "multiply")}")
    println("6 / 3 = ${calculator.calculate(6.0, 3.0, "divide")}")

    // Agregar una nueva operación (potencia) sin modificar el código existente
    class Power : Operation {
        override fun execute(a: Double, b: Double) = Math.pow(a, b)
    }
    calculator.addOperation("power", Power())

    // Probar la nueva operación
    println("2^3 = ${calculator.calculate(2.0, 3.0, "power")}")
}
