fun main() {
    printNumbers()
    println("Introduce un numero para calcular su factorial")
    var i = readln()
    var x = i.toInt()
    factorial(x)
    println("El factorial de $x es ${factorial(x)}")
    println("Escribe el numero de la posicion en la succesion de Fibonacci que quieras saber ")
    var z = readln()
    var posicion = z.toInt()
    println("Fibonnacci en posicion $posicion es ${fibonacci(posicion)}")

}

//Funcion de recursividad que imprime numeros de 1 al 100
fun printNumbers(n: Int = 1) {
    if (n > 100) return
    println(n)
    printNumbers(n + 1)
}

//Dificultad Extra
//Calcular el factorial de un numero
fun factorial(i: Int): Long {
    if (i <= 1) {
        return 1
    } else {
        return i * factorial(i - 1)
    }
}

//Calcular el valor en la posicion de fibonacci
fun fibonacci(posicion: Int): Long {
    return when (posicion) {
        0 -> 0
        1 -> 1
        2 -> 1
        else -> fibonacci(posicion - 1) + fibonacci(posicion - 2)
    }
}