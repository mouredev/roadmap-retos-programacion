@file:Suppress("DIVISION_BY_ZERO")

fun main() {
    //operadores de comparacion
    val a = 10
    val b = 5
    println(a > b)
    println(a < b)
    println(a >= b)
    println(a <= b)
    println(a == b)
    println(a != b)

    //operadores logicos
    println(a > b && a < b)
    println(a > b || a < b)
    println(!true)

    //operadores de asignacion
    var c = 10
    println(c)
    c += 5
    println(c)
    c -= 5
    println(c)
    c *= 5
    println(c)
    c /= 5
    println(c)
    c %= 5
    println(c)

   //operadores de pertenecia
    println(5 in 1..10)
    println(5 !in 1..10)

   // operadores de bits
    println(5 and 10)
    println(5 or 10)
    println(5 xor 10)
    println(5 shl 1)
    println(5 shr 1)
    println(5 ushr 1)
    println(5 and 10)
    println(5 or 10)
    println(5 xor 10)

    // condicional if
    if (a > b) {
        println("a es mayor que b")
    } else {
        println("a no es mayor que b")
    }

    //when
    when (a) {
        1 -> println("a es 1")
        2 -> println("a es 2")
        else -> println("a no es ni 1 ni 2")
    }

    //loop for
    for (i in 1..10) {
        println(i)
    }
    for (i in 10 downTo 1) {
        println(i)
    }
    for (i in 1..10 step 2) {
        println(i)
    }
    for (i in 10 downTo 1 step 2) {
        println(i)
    }

    // loop while
    var i = 1
    while (i <= 10) {
        println(i)
        i++
    }

    // loop do while
    do {
        println(i)
        i++
    } while (i <= 10)

    //break y continue
    for (d in 1..10) {
        if (d == 5) {
            break
        }
    }

    for (f in 1..10) {
        if (f == 5) {
            continue
        }
    }

    // exception
    try {
        val x = 10 / 0
    } catch (e: ArithmeticException) {
        println("No se puede dividir entre 0")
    }

    // extra reto
    extraReto()
}

fun extraReto(){
    for (i in 10..55){
        if(i%2==0 && i!=16 && i%3!=0 ){
            println(i)
        }

    }
}