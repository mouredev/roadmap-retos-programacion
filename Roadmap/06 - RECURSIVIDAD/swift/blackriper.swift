
func counterReversed(n: Int){
    if n > 0 {
        print(n)
        counterReversed(n: n - 1)
    }
}
counterReversed(n: 100)

func factorialNumber(n: Int) -> Int {
    if n == 0 {
        return 1
    }
    return n * factorialNumber(n: n - 1)
}
print(factorialNumber(n: 5))


func fibonacciNumber(n: Int) -> Int {
    if n == 0 || n == 1 {
        return 1
    }
    return fibonacciNumber(n: n - 1) + fibonacciNumber(n: n - 2)
}
print(fibonacciNumber(n: 5))