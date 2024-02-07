fun main() {
    var number = 10
    var a = 10
    var b = 20
    var x = 10

    println("Original number: $number")
    println("a = $a, b = $b")


    // ------------- TIPOS DE OPERADORES ----------------

    // Unary plus
    number = +number
    println("Number after unary plus: $number")

    // Unary minus
    number = -number
    println("Number after unary minus: $number")

    // Increment
    number++
    println("Number after increment: $number")

    // Decrement
    number--
    println("Number after decrement: $number")

    // Not operator
    var flag = true
    println("Original flag: $flag")
    flag = !flag
    println("Flag after NOT operator: $flag")

    // Addition
    var result = a + b
    println("a + b = $result")

    // Subtraction
    result = a - b
    println("a - b = $result")

    // Multiplication
    result = a * b
    println("a * b = $result")

    // Division
    result = a / b
    println("a / b = $result")

    // Modulus
    result = a % b
    println("a % b = $result")

    // Greater than
    val isGreater = a > b
    println("a > b = $isGreater")

    // Less than
    val isLess = a < b
    println("a < b = $isLess")

    // Greater than or equal to
    val isGreaterOrEqual = a >= b
    println("a >= b = $isGreaterOrEqual")

    // Less than or equal to
    val isLessOrEqual = a <= b
    println("a <= b = $isLessOrEqual")

    // Equal to
    val isEqual = a == b
    println("a == b = $isEqual")

    // Not equal to
    val isNotEqual = a != b
    println("a != b = $isNotEqual")

    // And
    val andResult = a > b && a > 0
    println("a > b && a > 0 = $andResult")

    // Or
    val orResult = a > b || a > 0
    println("a > b || a > 0 = $orResult")

    // In operator
    val numbers = listOf(1, 2, 3, 4, 5)
    if (3 in numbers) {
        println("3 is in the list")
    } else {
        println("3 is not in the list")
    }

    // Indexing operator
    val letters = mutableListOf("a", "b", "c", "d", "e")
    println("The second element is ${letters[1]}")
    letters[1] = "f"
    println("After modification, the second element is ${letters[1]}")

    // Augmented assignments
    x += 5
    println("x = $x")
    x -= 3
    println("x = $x")
    x *= 2
    println("x = $x")
    x /= 4
    println("x = $x")
    x %= 2
    println("x = $x")

    // Equality and inequality operators
    val c = 10
    println("a == b is ${a == b}")
    println("a != b is ${a != b}")
    println("a == c is ${a == c}")
    println("a != c is ${a != c}")

    // Comparison operators
    println("a > b is ${a > b}")
    println("a < b is ${a < b}")
    println("a >= b is ${a >= b}")
    println("a <= b is ${a <= b}")


    // ------------- ESTRUCTURAS DE CONTROL -------------

    // if-else
    if (a > b) {
        println("a es mayor que b")
    } else {
        println("a no es mayor que b")
    }

    // when
    x = 1
    when (x) {
        1 -> println("x es 1")
        2 -> println("x es 2")
        else -> println("x no es ni 1 ni 2")
    }


    // for
    for (i in 1..5) {
        println("Número: $i")
    }

    // while
    var i = 1
    while (i <= 5) {
        println("Número: $i")
        i++
    }

    // do-while
    var j = 1
    do {
        println("Número: $j")
        j++
    } while (j <= 5)

    // try-catch-finally
    try {
        val arr = arrayOf(1, 2, 3)
        println(arr[5]) // Esto lanzará una excepción
    } catch (e: ArrayIndexOutOfBoundsException) {
        println("Índice fuera de los límites del array")
    } finally {
        println("Este bloque se ejecuta independientemente de si se produjo una excepción o no")
    }


    // ------------- DESAFÍO ----------------
    /** Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
     */
    for (i in 10..55 step 2) {
        if (i != 16 && i % 3 == 0) {
            println(i)
        }
    }
}