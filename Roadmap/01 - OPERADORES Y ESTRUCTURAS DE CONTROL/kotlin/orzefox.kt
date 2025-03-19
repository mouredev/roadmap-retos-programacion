import java.lang.ArithmeticException

fun main() {
    var a = 2
    var b = 3

    // Operadores Aritmeticos
    println(a + b)
    println(a - b)
    println(a * b)
    println(a / b)
    println(a % b)

    // Operadores Logicos
    println(a < b && a > b)
    pritnln(a < b || a > b)
    printls(!true)

    //Operadores de comparacion
    println(a == b)
    println(a != b)
    println(a < b)
    println(a > b)
    println(a >= b)
    println(a <= b)

    // Operadores de Asignacion
    var c = 1
    println(c)
    c += 1
    println(c)
    c -= 2
    println(c)
    c *= 3
    println(c)
    c /= 4
    println(c)
    c %= 5
    println(c)

    // Operadores de pertenencia
    println(15 in 1..35)
    println(25 !in 1..10)

    // Operadores de Bits

    println(a and b)
    println(a or b)
    println(a xor b)
    println(a shl 2)
    println(a shr 1)
    println(a ushr b)

    // Condicionales

    // if
    if(a == b)
        println("$a es igual a $b")
    else
        println("$a es diferente a $b")

    // when

    when (a)
    {
        2 -> println("Es dos")
        3 -> println("Es tres")
        else -> println("No es ni dos ni tres")
    }

    // while

    while (a < 5)
    {
        println("La variable a es $a")
        contador++
    }

    // do while

    do
    {
        println("La variable b es $b")
        b--
    }
    while (b > 0)

    // for

    for (i in 0 until 10)
        println("valor del indice es $i")

    // try catch

    try
    {
        val d = b / 0
        println("el resultado es : $d")
    }
    catch (e: ArithmeticException)
    {
        println("ERROR ARITMETICO")
    }

    retroExtra()
}

fun retroExtra()
{
    var ind = 10
    while (ind != 55)
    {
        if (ind % 2 == 0 && ind != 16 && !(ind % 3 == 0)
            println(ind)
        ind++
    }
}