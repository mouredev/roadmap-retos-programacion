fun main () {

    // Operadores aritmeticos

    val a = 3
    val b = 2

    println("a + b = ${a + b}")
    println("a - b = ${a - b}")
    println("a * b = ${a * b}")
    println("a / b = ${a / b}")
    println("a % b = ${a % b}")

    // Operadores de asignacion

    var c = 5
    println("El valor de c es $c")
    c += 2
    println("El valor de c += 2 es $c")
    c -= 2
    println("El valor de c -= 2 es $c")
    c *= 2
    println("El valor de c *= 2 es $c")
    c /= 2
    println("El valor de c /= 2 es $c")
    c %= 2
    println("El valor de c %= 2 es $c")

    // Operadores de comparacion

    println("a == b es ${a == b}")
    println("a != b es ${a != b}")
    println("a > b es ${a > b}")

    // Operadores logicos

    val x = true
    val y = false

    println("x && y es ${x && y}")
    println("x || y es ${x || y}")
    println("!x es ${!x}")

    // Operadores bits

    val m = 12
    val n = 25

    println("m and n es ${m and n}")
    println("m or n es ${m or n}")
    println("m xor n es ${m xor n}")

    // Operadores de desplazamiento
    println("m shl 3 es ${m shl 3}")
    println("m shr 3 es ${m shr 3}")
    println("m ushr 3 es ${m ushr 3}")

    // if else

    val edad = 18
    if (edad >= 18) {
        println("Eres mayor de edad")
    } else {
        println("Eres menor de edad")
    }

    // when

    val calificacion = 5
    when (calificacion) {
        10 -> println("Excelente")
        9 -> println("Muy bien")
        8 -> println("Bien")
        7 -> println("Regular")
        6 -> println("Suficiente")
        else -> println("Insuficiente")
    }

    // for

    val frutas = listOf("Manzana", "Pera", "Fresa", "Uva")
    for (fruta in frutas) {
        println(fruta)
    }

    // while
    var contador = 0
    while (contador < 5) {
        println("El contador es $contador")
        contador++
    }

    // do while

    var contador2 = 0
    do {
        println("El contador2 es $contador2")
        contador2++
    } while (contador2 < 5)

    // foreach
    val numeros = listOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    numeros.forEach {
        println(it)
    }

    // break
    for (i in 1..10) {
        if (i == 5) {
            break
        }
        println(i)
    }

    // continue 
    for (i in 1..10) {
        if (i % 2 == 0) {
            continue
        }
        println(i)
    }

    // Extra

    for (i in 10..55) {
        if (i % 2 == 0 && i != 16 && i % 3 == 0)
            println(i)
    }






}