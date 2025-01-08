var a = 1
var b = 2

fun main(){
    // Operadores aritméticos
    println("Operadores de aritmeticos")
    println(1+1)
    println(1-1)
    println(2*5)
    println(6/2)
    println(1%1)

    // Operadores lógicos
    println("Operadores lógicos")
    println(a < b && b > a)
    println(a < b || b > a)
    println(!true)

    // operadores de comparación
    println("Operadores de comparación")
    println(a == b)
    println(a != b)
    println(a < b)
    println(a > b)
    println(a <= b)
    println(a >= b)

    // operadores de asignación
    println("Operadores de asignación")
    var c = 1
    println(c)
    c += 1
    println(c)
    c -= 1
    println(c)
    c *=8
    println(c)
    c /= 2
    println(c)
    c %= 5
    println(c)

    // Operadores de pertenencia
    println("Operadores de pertenencia")
    println(2 in 1..10)
    println(2 !in 1..10)

    // Operadores de bits
    println("Operadores de bits")
    println(a and b)
    println(a or  b)
    println(a xor b)
    println(a.inv())
    println(a shl b)
    println(a shr b)
    println(a ushr b)

    //Estructuras de control
    println("Estructuras de control")

    // IF
    println("IF")
    if (a < b)
        println("$a es mas pequeño que $b")
    else
        println("$b es mas grande que $a")

    // WHEN
    println("WHEN")
    when (a){
        1 -> println("a es 1")
        2 -> println("a es 2")
        else -> println("a no es 1 ni tampoco 2")
    }

    // FOR
    println("FOR")
    for (i in 1..10){
        println(i)
    }

    // WHILE
    println("WHILE")
    var d = 1
    while (d <= 5){
        println(d)
        d++
    }

    // DO WHILE
    println("DO WHILE")
    d = 1
    do {
        println(d)
        d++
    } while (d <= 5)

    // FOREACH
    println("FOREACH")
    val nombres = arrayOf("Isaac", "Sergi", "Gerrard", "Eric", "Pol")
    for (nombre in nombres)
        println(nombre)

    // TRY CATCH
    println("TRY CATCH")
    try {
        val valor = 20/0
    } catch (e: ArithmeticException){
        println("Excepción aritmética")
    }

    // Reto extra
    println("Reto extra")
    retoExtra()
}

fun retoExtra() {
    for (numero in 10..55){
        if (numero%2 == 0 && numero != 16 && numero%3 != 0)
            println(numero)
    }
}
