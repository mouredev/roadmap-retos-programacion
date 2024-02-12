fun main() {

    // --------------------- Operadores -----------------------

    // Asignación
    val nombre = "Diego"
    var edad = 27
    println("$nombre tiene $edad años")

    // Artiméticos
    val suma = 1 + 2
    println("Suma: $suma")

    val resta = 3 - 2
    println("Resta: $resta")

    val multiplicacion = 3 * 2
    println("Multiplicación: $multiplicacion")

    val division = 10 / 2
    println("División: $division")

    val concatenacion = "hello " + "world"
    println(concatenacion)

    val resto = 9 % 8
    println("Resto: $resto")

    val tres = 3
    val negativo = -tres
    println("Negativo: $negativo")

    val cuatro = -4
    val positivo = +cuatro
    println("Positivo: $positivo")

    var compuesto = 2
    compuesto += 2
    println("Compuesto: $compuesto")

    // Comparación
    println(1 == 1)
    println(2 != 1)
    println(2 > 1)
    println(1 < 2)
    println(1 >= 1)
    println(2 <= 1)

    // if-else
    val resultado = if (2 + 1 == 3) true else false
    println(resultado)

    // Non-nullable
    var color: String? = null
    var colorCoche = if (color != null) "Es $color" else "Es nulo"
    println(colorCoche)

    println(color?.length)
    val colorString = color?.toString()
    println(colorString)

    colorCoche = color?.toString() ?: "Es nulo"
    println(colorCoche)    

    // println(color!!.toString())

    // Rango
    for (index in 1..5) {
        println(index)
    }

    for (index in 1 downTo 5) {
        println(index)
    }

    for (index in 1..5 step 2) {
        println(index)
    }

    for (index in 1 until 5) {
        println(index)
    }

    // ----------------------- Estructuras de control --------------------
    // Bucles for-in
    val nombres = listOf("Anna", "Alex", "Brian", "Jack")
    for (nombre in nombres) {
        println("Hola $nombre")
    }

    // Bucle while
    var numero = 0
    while (numero < 4) {
        println(numero)
        numero +=1
    }

    // Bucle do-while
    do {
        println(numero)
        numero += 1
    } while (numero < 8)

    // Condicional if
    if (numero == 7) {
        println("El número es 7")
    } else {
        println("No es 7")
    }

    // When
    when (numero) {
        7 -> println("Es 5")
        8 -> println("Es 8")
        else -> println("No es 7 ni 8")
    }

    // Transferencia de control
    for (index in 1..5) {
        if (index == 3) {
            continue
        }

        println(index)
    }

    for (index in 1..5) {
        if (index == 3) {
            break
        }

        println(index)
    }

    // Etiquetas
    mainLoop@ for (i in 1..5) {
        val letras = listOf("a", "b", "c")

        secondaryLoop@ for (letra in letras) {

            if (letra == "b") {
                break@secondaryLoop
            }
            println(letra)
        }
    }

    // Error Handling
    try {
        println(1 / 0)
    } catch (e: ArithmeticException) {
        println("Error: División por cero")
    } finally {
        println("Esto se imprime siempre")
    }

    // -------------------------- Ejercicio extra -------------------------
    for (index in 10..55) {

        if (index % 2 == 0) {

            if (index != 16 && index % 3 != 0) {
                println(index)
            }
        }
    }
}   
