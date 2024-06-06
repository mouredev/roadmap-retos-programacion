fun main() {

    numberPrinter(100)

    println()

    val number = 6
    val factorial = factorialNumber(number)
    println("El factorial de $number es: $factorial")

    val fibonacciSequence = fibonacci(8)
    println(fibonacciSequence)
}

// 100 -> 100 - 1 = 99 ...
fun numberPrinter(value: Int){

    if(value >= 0){
        print("$value ")
        numberPrinter(value - 1)
    }
}

// 6!=1x2x3x4x5x6 = 720
//6x5 = 30 -> 30x4 = 120 -> 120x3 = 360 -> 360x2 = 720
fun factorialNumber(number: Int): Int{

    if (number != 0) {
        return number * factorialNumber(number - 1)
    } else {
        return 1
    }
}
// 0,1,1,2,3,5,8,13,21...
fun fibonacci(n: Int): Int {
    if (n <= 1) {
        return n
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2)
    }
}