/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */



// #01 OPERADORES Y ESTRUCTURAS DE CONTROL
fun main() {
    //definición de variables
    val a = 10
    val b = 5



    //Tipos de operadores en kotlin

    println("Operadores aritméticos")
    println("Suma: ${a + b}")
    println("Resta: ${a - b}")
    println("Multiplicación: ${a * b}")
    println("División: ${a / b}")
    println("Módulo: ${a % b}")

    println("Operadores de comparación")
    println("Igual: ${a == b}")
    println("Desigual: ${a != b}")
    println("Menor: ${a < b}")
    println("Menor igual: ${a <= b}")
    println("Mayor: ${a > b}")
    println("Mayor igual: ${a >= b}")

    println("Operadores lógicos")
    val isTrue = true
    val isFalse = false

    println("$isTrue && $isFalse es ${isTrue && isFalse}")
    println("$isTrue || $isFalse es ${isTrue || isFalse}")
    println("!$isTrue es ${!isTrue}")

    println("Operadores de asignación")
    var c = 5 //Asignación simple
    println("c = $c")
    c += 2 //Suma y asignación
    println("c += 2 es $c")
    c -= 2 //Resta y asignación
    println("c -= 2 es $c")
    c *= 2 //Multiplica y asignación
    println("c *= 2 es $c")
    c /= 2 //Divide y asignación
    println("c /= 2 es $c")
    c %= 2 //Módulo y asignación
    println("c %= 2 es $c")
    
    println("Operadores de rango")

    val numbers = 1..10 //Incluyendo 1 y 10
    println(numbers)
    val letters = 'a'..'z' //Letras de la 'a' a la 'z'
    println(letters)
    val even_numbers = 2 until 10 //Numeros pares del 2 al 9 (excluyendo el 10)
    println(even_numbers)

    println("Operadores de bits")

    val bin_1 = 10 //1010 en binario
    val bin_2 = 5  //0101 en binario

    println("Operador de bits AND: ${bin_1 and bin_2}")
    println("Operador de bits OR: ${bin_1 or bin_2}")
    println("Operador de bits XOR: ${bin_1 xor bin_2}")
    println("Operador de bits desplazamiento a la izquierda: ${bin_1 shl 1}")
    println("Operador de bits desplazamiento a la derecha: ${bin_1 shr 1}")
    println("Operador de bits desplazamiento a la derecha sin signo: ${bin_1 ushr 1}")

    //Estructuras de control

    println("Estructuras de control")

    //Condicionales
    println("If:")

    val x = 10
    val y = 5

    if (x > y) {
        println("$x es mayor que $y")
    } else {
        println("$x es menor que $y")
    }

    //When
    println("When:")

    val day = "Monday"

    when(day) {
        "Monday" -> println("It's monday")
        "Tuesday" -> println("It's tuesday")
        "Wednesday" -> println("It's wednesday")
        "Thursday" -> println("It's thursday")
        "Friday" -> println("It's friday")
        else -> println("Weekend!")
    }

    //Iterativas

    println("Iterativas")

    //For

    println("For")
    for (i in 1..10) {
        println(i)
    }

    //While

    println("While")

    var w_i = 0

    while (w_i < 10) {
        println(w_i)
        w_i++
    }

    //Do-While

    println("Do-While")

    var j = 0

    do {
        println(j)
        j++
    } while (j < 10)

    //Excepciones

    // println("Excepciones")

    // try {
    //     val z = 10 / 0
    // } catch (e: Exception) {
    //     println("Error: ${e.message}")
    // }

    //Break

    println("Break")

    for (i in 1..10) {
        if (i == 5) {
            break
        }
        print(i)
    }

    //Continue

    println("Continue")

    for (i in 1..10) {
        if (i % 2 == 0) {
            continue
        }
        print(i)
    }

    //Ejercicio extra

    println("Ejercicio extra")

    for (i in 10..55) {
        if (i % 2 == 0 && i % 3 != 0) {
            print("$i ")
        }
        if (i == 16) {
            continue
        }
    }


}