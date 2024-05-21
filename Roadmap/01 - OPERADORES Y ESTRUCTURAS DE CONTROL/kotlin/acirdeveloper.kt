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


fun main() {

    //* Operadores

    // Operadores aritméticos
    println("Operadores aritméticos")
    println("Suma: ${10 + 15}")
    println("Resta: ${10 - 15}")
    println("Multiplicación: ${10 * 15}")
    println("División: ${10 / 3}")
    println("Módulo: ${10 % 15}")

    // Operadores de comparación
    println("Operadores de comparación")
    println("Igualdad: ${10 == 3}")
    println("Desigualdad: ${10 != 3}")
    println("Mayor que: ${10 > 3}")
    println("Menor que: ${10 < 3}")
    println("Mayor o igual que: ${10 >= 10}")
    println("Menor o igual que: ${10 >= 3}")

    // Operadores lógicos
    println("Operadores lógicos")
    println("AND &&: 10 + 3 == 13 && 5 - 1 == 4 es: ${10 + 3 == 13 && 5 - 1 == 4}")
    println("OR ||: 10 + 3 == 13 || 5 - 1 == 4 es: ${10 + 3 == 13 || 5 - 1 == 4}")
    println("NOT !: !(10 + 3) == 13) es: ${!(10 + 3 == 13)}")

    // Operadores de asignación
    println("Operadores de asignación")
    var myNumber = 77
    myNumber += 5
    println("suma y asignación: " + myNumber)
    myNumber -= 5
    println("resta y asignación: " + myNumber)
    myNumber *= 5
    println("multiplicación y asignación: " + myNumber)
    myNumber /= 5
    println("Divisió y asignación: " + myNumber)
    myNumber %= 2
    println("Módulo y asignación: " + myNumber)

    // Operadores de identidad
    var myNewNumber = myNumber
    println("Operadores de identidad")
    println("myNumber === myNewNumber es: ${myNumber === myNewNumber}")
    println("myNumber !== myNewNumber es: ${myNumber !== myNewNumber}")

    // Operadores de pertenencia
    println("Operadores de pertenencia")
    val names = listOf("Ana", "Juan", "Pedro")

    if ("Juan" in names) {
        println("Juan está en la lista de nombres")
    } else {
        println("Juan no está en la lista de nombres")
    }

    if ("Marta" !in names) {
        println("Marta no está en la lista de nombres")
    } else {
        println("Marta está en la lista de nombres")
    }

    // Operadores de bit
    println("Operadores de bit")
    val a = 12   // 1100 en binario
    val b = 10   // 1010 en binario

    println("a and b = ${a and b}") // and bit a bit
    println("a or b = ${a or b}") // or bit a bit
    println("a xor b = ${a xor b}") // xor bit a bit
    println("a shl b = ${a shl b}") // Desplazamiento de bits a la izquierda
    println("a shr b = ${a shr b}") // Desplazamiento de bits a la derecha
    println("a ushr b = ${a shr b}") // Desplazamiento de bits a la derecha sin signo
    println("a.inv = ${a.inv()}") // not bit a bit

    /* Estructuras de control */

    // Condicional
    var myString = "Chanchitos"

    if(myString == "Acirdev") {
        println("Si es")
    } else if (myString == "Chanchito") {
        println("Feliz")
    } else {
        println("No es ni Feliz ni nada")
    }

    // Iterativas, bucles
    val rango = 0..9
    for(number in rango) {
        print("${number} ")
    }
    println("")

    // Manejo de excepciones
    println("Manejo de excepciones")
    try {
        println(10/0)
    } catch(e: Exception) {
        println("Se ha producido un error: ${e.message}")
    } finally {
        println("Ha finalizado el manejo de excepciones")
    }

    // EXTRA
    val range = 10..55
    for(num in range) {
        if(num % 2 == 0 && num != 16 && num % 3 != 0) {
            print("${num} ")
        }
    }
}