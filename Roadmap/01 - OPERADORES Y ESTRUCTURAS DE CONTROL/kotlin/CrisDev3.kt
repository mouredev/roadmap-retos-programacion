fun main() {
    /* Operadores unarios, representan si un numeros es
negativo o positivo
 */
    var positiveNum = +3
    var negativeNum = -3

// Operadores aritmeticos
    var sum = 42 + 33
    println(sum)

    var sustraction = 3 - 1
    println(sustraction)

    var multiplication = 2 * 2
    println(multiplication)

    var division = 6 / 3
    println(division)

    var mod = 6 % 3
    println(mod)

// Operador de asignación simple
    var val1 = "hello world"
    println(val1)

// Operadores de asignacion aumentada
    var a += b
    println("+= $a")

    var a -= b
    println("-= $a")

    var a *= b
    println("*= $a")

    var a /= b
    println("/= $a")

    var a %= b
    println("%= $a")

// Operadores logicos
    val entrada = 10
    var resto: Boolean

    val mayorQueCero = input > 0
    val esPar = input % 2 == 0

// Operador and
    resto = mayorQueCero && esPar
    println("Es mayor que cero y par:$resto")

// Operador or
    resto = mayorQueCero || esPar
    println("Es mayor que cero o par:$resto")

// Operador not
    resto = mayorQueCero && !esPar
    println("Es mayor que cero e impar:$resto")

// Operadores relacionales
    val first = 12
    val second = 42

    println("$first es igual a $second: ${first == second}")
    println("$first es diferente a $second: ${first != second}")
    println("$first es menor que $second: ${first < second}")
    println("$first es mayor que $second: ${first > second}")
    println("$first es menor o igual que $second: ${first <= second}")
    println("$first es mayor o igual que $second: ${first >= second}")

// Operadores de incremento ++ y decremento --
    var a = 2
    println(a)
    ++a
    println(a)
    a++
    println(a)
    --a
    println(a)
    a--
    println(a)

// Operador de rangos

    val b = 1..3
    val c = 1 until 8
    println(b)
    println(c)

// Operador in

    /* 3 in numeros. Esta expresión evalúa si el número 3 está
    presente en el array numeros y almacena el resultado en la
    variable estaPresente */
    val numeros = arrayOf(1, 2, 3, 4, 5)
    val estaPresente = 3 in numeros
    println("¿El número 3 está presente en la lista? $estaPresente")

// Operadores de acceso a indices
    val cadena = "Hola"
    println(cadena[1]) // accede al caracter en la posicion 1 que es la 'o'

    /* Operador de llamada segura !!, esto fuerza al programa a
    acceder a una propiedad o llamar a un método en una variable
    que puede ser nula
     */
    val cadena1: String? = null
    val longitud = cadena1!!.length
    println(longitud)

    /* Operador de llamada segura ?, se utiliza para acceder
     a las propiedades o métodos de un objeto de manera
     segura, evitando que se produzca una excepción NullPointerException
     si el objeto es nulo.
     */
    val d: String? = null
    println(d)

    /* Operador Elvis ?:, es una forma concisa de manejar valores nulos. Se
     utiliza como una expresión que devuelve el valor de la izquierda si no
     es nulo, y si es nulo, devuelve el valor de la derecha.
     */
    val cadena2: String? = null
    val longitud: Int = cadena2?.length ?: -1
    println("Longitud de la cadena: $longitud") // Imprime: Longitud de la cadena: -1

// Estructuras de control en kotlin

// Estructuras iterativas

// for loop
    val nombress = listOf(
        "Dalmata",
        "Husky",
        "Chihuahua",
        "Pitbull"
    )
    for (nombre in nombres) {
        val n = nombre.replaceFirstChar { it.lowercase() }
        println(n)

// while loop
        var variable1 = 1
        while (variable1 <= 5) {
            println("Númber: $variable1")
            ++variable
        }

// do-While loop
        var j = 1
        do {
            println(j)
            j++
        } while (j <= 5)

// Estructuras condicionales

// Sentencia if
        val isAdult: Boolean? = null
        if (isAdult == true) {
            println("Es verdadero")
        } else {
            println("Es falso o nulo")
        }

// Sentencia when
        val dia = 3
        val nombreDia = when (dia) {
            1 -> "Lunes"
            2 -> "Martes"
            3 -> "Miércoles"
            4 -> "Jueves"
            5 -> "Viernes"
            6 -> "Sábado"
            7 -> "Domingo"
            else -> "Día inválido"
        }
        println("Hoy es $nombreDia")

// Excepciones
        /* Try catch, Se utiliza para manejar excepciones en Kotlin.
         El bloque try contiene el código que puede generar una
         excepción, mientras que el bloque catch se utiliza para manejar
         la excepción si ocurre.
         */
        val cadenaNumero = "abc"
        try {
            val numero = cadenaNumero.toInt()
            println("Número: $numero")
        } catch (excepcion: NumberFormatException) {
            println("Error: No se pudo convertir la cadena a número")
        }

        /* Throw, Se utiliza para lanzar manualmente una excepción en un
         punto específico del código.
         */
        val valor = -10
        if (valor < 0) {
            throw IllegalArgumentException("El valor no puede ser negativo")
        }
        println("El valor es $valor")


// DIFICULTAD EXTRA (opcional):
// * Crea un programa que imprima por consola todos los números comprendidos
// * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
        for (i in 10..55) {
            if (i % 2 == 0 && (i != 16) && (i % 3 != 0)) {
                println(i)
            }

        }
 }


