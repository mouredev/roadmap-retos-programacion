
fun main () {
// Variables with data types & initialized:
    val a: Int = 3
    val b: Byte = 127
    val c: Long = 100_000_000_000_000L
    val d: Float = 1.25f
    val e: Double = 3.23
    val f: String = "myString "
    val g: String = "anotherString"

// Operaciones aritmeticas con las variables previas:
    val sum: Int = b + a
    val sum2: String = f + g
    val rest = c - b
    val mult = d * e
    val div = b / a
    val aRem2 = a % 2
    val bRem2 = b % 2

// Operadores Lógicos
    val myTrue: Boolean = true
    val myFalse: Boolean = false
    val isAEven: Boolean = aRem2 == 0
    val isAOdd: Boolean = bRem2 != 0

// Valores de las constantes
    println(a)
    println(b)
    println(c)
    println(d)
    println(e)
    println(f)
    println(g)
    println()
// Operaciones aritmeticas
    println(sum)
    println(sum2)
    println(rest)
    println(mult)
    println(div)
    println()
// Operaciones lógicas
    println(isAEven)
    println(isAOdd)
    println(myTrue || myFalse)
    println(myTrue && myFalse)
    println(!myTrue)
    println()
// Operaciones de comparación
    println(b > a)
    println(b < a)
    println(myTrue == myTrue)
    println(!myTrue)
    println()

// Operadores de asignación


//  Estructuras de control = Control flow
// If expression
    if (a > b) {
        println("$a is bigger than $b")
    } else {
        println("$a is not bigger than $b")
    }
    println()

// When else expression
    val temp = 9
    val description = when {
        // If temp < 0 is true, sets description to "very cold"
        temp < 0 -> "very cold"
        // If temp < 10 is true, sets description to "a bit cold"
        temp < 10 -> "a bit cold"
        // If temp < 20 is true, sets description to "warm"
        temp < 20 -> "warm"
        // Sets description to "hot" if no previous condition is satisfied
        else -> "hot"
    }
    println(description)
    println()

// For loops & ranges
    for (number in 1..5) {
        println(number)
    }
    println()
    for (number in 1..<5) {
        println(number)
    }
    println()
    for (number in 10 downTo 5) {
        println(number)
    }
    println()
    for (number in 0..<28 step 2) {
        println(number)
    }
    println()
    val cakes = listOf("carrot", "cheese", "chocolate")
    for (cake in cakes) {
        println("Yummy, it´s a $cake cake!")
    }


// While loops
    /* Using a when expression, update the following program so that when you input
     the names of GameBoy buttons, the actions are printed to output.
*/
    println()
    val button = "X"
    println(
        when (button) {
            "A" -> "Yes"
            "B" -> "No"
            "X" -> "Menu"
            "Y" -> "Nothing"
            else -> "There is not such a button"
        }
    )
    // Do + While. Program that counts pizza slices until there’s a whole pizza with 8 slices.
    println()
    var pizzaSlices = 0
    pizzaSlices++

    do {
        println("There's only $pizzaSlices slice/s of pizza :(")
        pizzaSlices++
    } while (pizzaSlices <= 8)
    println("Hooray! We have a whole pizza! :D")

    // Fizz buzz
    for (i in 1..100) {
        println(
            when {
                i % 15 == 0 -> "fizzbuzz"
                i % 3 == 0 -> "fizz"
                i % 5 == 0 -> "buzz"
                else -> i.toString()
            }
        )
    }
    // For and if to print only the words that start with the letter l (from a list)
    println()
    val words = listOf("dinosaur", "limousine", "magazine", "language")
    for (word in words) {
        if (word.startsWith("l"))
            println(word)
    }


// Break and continue loops

//Ejercicio extra
    println()
    for (i in 10..55) {
        if (i % 2 == 0 && i != 16 && i % 3 != 0) {
            println(i)
        }
    }
}


