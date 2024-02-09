import Foundation
// Reto #06 RECURSIVIDAD

// Función recursiva que imprima nº del 100 al 0
func printNum(_ num: Int) {
    if num >= 0 {
        print(num, terminator: " ")
        printNum(num - 1)
    }
}

print("Print numbers 100-0 with recursive function: ")
printNum(100)

// 🧩 DIFICULTAD EXTRA 🧩
// Calcular el factorial de un número concreto
func factorialNum(num: Int) -> Int {
    if num == 0 {
        return 1
    } else {
        return num * factorialNum(num: num - 1)
    }
}

print("The factorial of 18 using recursion is = " +  String(factorialNum(num: 8)))

// Cálculo de un valor concreto (según posición) en la serie Fibonacci
func recursiveFibonacci(position: Int) -> Int {
    if position == 0 {
        return 0
    } else if position == 1 {
        return 1
    } else {
        return recursiveFibonacci(position: position - 1) + recursiveFibonacci(position: position - 2)
    }
}

print("The value of the sixth position of the Fibonacci series using recursion is: = " +  String(recursiveFibonacci(position: 6)))

// 1-1-2-3-5-8