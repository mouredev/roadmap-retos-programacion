import Foundation

func factorial(number: Int) -> Int{

    if number == 0 {
        return 1
    } else {
        let i = factorial(number: number - 1)

        return number * i
    }
}

let number = 5
print("El factorial de \(number) es \(factorial(number: number))")

func fibonacci(position: Int) -> Int {

    if position <= 2 {
        return 1
    } else {
        let i = fibonacci(position: position - 1)
        let j = fibonacci(position: position - 2)
        return j + i
    }
}

let position = 4
print("El valor de la posición \(position) en la secuencia de Fibonacci es \(fibonacci(position: position))")

