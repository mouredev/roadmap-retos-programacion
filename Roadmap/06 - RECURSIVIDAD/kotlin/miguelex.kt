import kotlin.io.println

fun sumaRecursiva(a: Int, b: Int): Int = if (b == 0) a else 1 + sumaRecursiva(a, b - 1)

fun potenciaRecursiva(base: Int, exponente: Int): Int = if (exponente == 0) 1 else base * potenciaRecursiva(base, exponente - 1)

fun factorialRecursivo(n: Int): Int = if (n == 0) 1 else n * factorialRecursivo(n - 1)

fun fibonacciRecursivo(n: Int): Int {
    return if (n <= 1) n else fibonacciRecursivo(n - 1) + fibonacciRecursivo(n - 2)
} 

fun decremento(n: Int): Int {
    if (n == 0) 
        return 0 
    else 
        print(n.toString() + " ") 
        return decremento(n - 1)
}

fun main() {
    print("Los númeos de 100 a 1  de forma recursica: ")
    decremento(100)
    println()
    println("La suma recursiva de 3 + 5 es: ${sumaRecursiva(3, 5)}")
    println("La potencia recursica de 2^3 es: ${potenciaRecursiva(2, 3)}")
    println("El valor de 5! es: ${factorialRecursivo(5)}")
    println("El 10º numero de Fibonacci es: ${fibonacciRecursivo(10)}")

    println("Introduzca el numero del que queire calcular el factorial: ")
    val numero = readLine()!!.toInt()
    println("El factorial de $numero es: ${factorialRecursivo(numero)}")

    println("Introduzca el numero del que quiere calcular el fibonacci: ")
    val numeroFib = readLine()!!.toInt()
    println("El $numeroFib º numero de Fibonacci es: ${fibonacciRecursivo(numeroFib)}")


}
