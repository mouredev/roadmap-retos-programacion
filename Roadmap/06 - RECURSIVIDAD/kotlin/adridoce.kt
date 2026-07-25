fun main() {
    println(funcionRecursiva(100))
    println(factorial(5))
    println(fibonacci(20))
}

fun funcionRecursiva(n: Int){
    if(n > 0) funcionRecursiva(n-1)
}

fun factorial(n: Int):Int {
    return if (n == 0) 1 else n * factorial(n-1)
}

fun fibonacci(n: Int): Int {
    return if (n <= 1) n else fibonacci(n - 1) + fibonacci(n - 2)
}