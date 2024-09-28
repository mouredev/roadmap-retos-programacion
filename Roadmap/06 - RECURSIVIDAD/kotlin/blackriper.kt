/*  una funcion recursiva es aquella que puede llmarse  asi misma para realizar un proceso  */


fun exmapleRecursive(num:Int ){
     println(num)
    if(num>0) exmapleRecursive(num-1)

}


fun numberFactorial(number: Int): Int {
    return if (number == 1) number
    else number * numberFactorial(number - 1)
}


fun fibonacci(number: Int): Int {
    return if (number == 1 || number == 2) 1
    else fibonacci(number - 1) + fibonacci(number - 2)
}



fun main(){
    exmapleRecursive(100)
    numberFactorial(6).let { println(it) }
    fibonacci(20).let { println(it) }
}