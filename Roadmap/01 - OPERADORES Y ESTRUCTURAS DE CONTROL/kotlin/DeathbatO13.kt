/**
 * @author Daniel Torres
 */

import java.util.Scanner

object Ejercicio01 {
    @JvmStatic
    fun main(args: Array<String>) {
        // Declaración de variables que se usarán en el código
        val sc = Scanner(System.`in`)
        var a: Int
        var b: Int
        var c: Int
        var d: Int
        var t: Int
        var x: Int
        var k: Int
        var num: Int
        var bite1: Boolean
        var bite2: Boolean
        var vocal: Char

        ////-------- Operadores ---------////

        //-- Aritméticos --//
        a = 5
        b = 10
        val sum = a + b
        val res = a - b
        val mult = a * b
        val div = a / b
        val mod = a % b
        /* Con el siguiente print se podrá visualizar el resultado de cualquier
        operación realizada en esta sección reemplazando la que está como ejemplo */
        println("Ejemplo de Operador Aritmético: $mult")

        //-- Comparación --//
        c = 5
        d = 9
        val opIgual = c == d
        val opDesigualdad = c != d
        val opMayorQue = c > d
        val opMenorQue = c < d
        val opMayorOIgual = c >= d
        val opMenorOIgual = c <= d
        /* Con el siguiente print se podrá visualizar el resultado de cualquier
        operación realizada en esta sección reemplazando la que está como ejemplo */
        println("Ejemplo de Operador de Comparación (Mayor): $opMayorQue")

        //-- Lógicos --//
        bite1 = true
        bite2 = false
        val operadorAnd = bite1 && bite1
        val operadorOr = bite1 || bite2
        val operadorNot = !bite1
        /* Con el siguiente print se podrá visualizar el resultado de cualquier
        operación realizada en esta sección reemplazando la que está como ejemplo */
        println("Ejemplo de Operador Lógico (Not): $operadorNot")

        //-- Asignación --//
        // Asignación simple
        t = 100 // se asigna un valor de 100 a la variable 't'
        // Asignación de suma
        t += 2 // Toma el valor que ya tenía y le suma 2
        // Asignación de resta
        t -= 2 // Toma el valor que ya tenía y le resta 2
        // Asignación de multiplicación
        t *= 2 // Toma el valor que ya tenía y le multiplica 2
        // Asignación de división
        t /= 2 // Toma el valor que ya tiene y lo divide entre 2
        // Asignación de módulo
        t %= 2 // Toma el valor que ya tiene y hace la operación de módulo
        // Asignación de desplazamiento a la izquierda
        t = t shl 2 // Toma el valor que ya tiene y multiplica por 2 elevado a la 2

        //-- Bits --//
        val opBitAnd = bite1 and bite2
        val opBitOr = bite1 or bite2
        val opBitXor = bite1 xor bite2
        val opBitNot = !bite1
        /* Con el siguiente print se podrá visualizar el resultado de cualquier
        operación realizada en esta sección reemplazando la que está como ejemplo */
        println("Ejemplo de Operador de Bits (Xor): $opBitXor")

        ////-------- Estructuras de Control ---------////

        //-- Condicionales --//
        print("Por favor digita un número entero para compararlo con 20: ")
        x = sc.nextInt(); sc.nextLine()
        when {
            x > 20 -> println("\nEl número es mayor a 20")
            x < 20 -> println("\nEl número es menor a 20")
            else -> println("\nEl número es 20")
        }

        println("\nAhora por favor digita una vocal: ")
        vocal = sc.nextLine().uppercase().first()

        when (vocal) {
            'A' -> println("Vocal A")
            'E' -> System.err.println("Vocal E")
            'I' -> println("Vocal I")
            'O' -> println("Vocal O")
            'U' -> println("Vocal U")
            else -> println("Eso no es una vocal")
        }

        //-- Iterativas --//

        // Imprime los números pares desde el 0 hasta el 12
        for (i in 0..12) {
            if (i % 2 == 0) {
                print("$i ")
            }
        }
        println()

        // Imprime los números múltiplos de 3 desde el 0 hasta el 15
        k = 0
        while (k <= 15) {
            if (k % 3 == 0) {
                print("$k ")
            }
            k++
        }
        println()

        //-- Excepciones --//

        try {
            print("Por favor ingrese un número entero: ")
            num = sc.nextInt()
            println("\nEl número que ingresó es la mitad de: ${num * 2}\n")
        } catch (e: Exception) {
            println("ERROR---. Eso no era un número\n")
        } finally {
            sc.close()
        }

        ////-------- Reto Extra ---------////

        //-- Ejercicio con For --//

        println("Ejercicio con For")
        for (i in 10..55) {
            if (i % 2 == 0 && i != 16 && i % 3 == 0) {
                print("$i ")
            }
        }
        println()

        //-- Ejercicio con While --//

        println("Ejercicio con While")
        k = 10
        while (k <= 55) {
            if (k % 2 == 0 && k != 16 && k % 3 == 0) {
                print("$k ")
            }
            k++
        }
    }