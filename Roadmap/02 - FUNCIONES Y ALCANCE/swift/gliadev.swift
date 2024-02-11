import Foundation

// Ejemplo de una función sin parámetros ni retorno
func imprimirMensaje() {
    print("Esta es una función sin parámetros ni retorno")
}
imprimirMensaje() // Llamada a la función

// Ejemplo de una función con un parámetro
func saluda(nombre: String) {
    print("Hola, \(nombre)!")
}
saluda(nombre: "Adolfo") // Llamada a la función con un parámetro

// Ejemplo de función con varios parámetros
func suma(a: Int, b: Int) {
    print("La suma de \(a) y \(b) es \(a + b)")
}
suma(a: 5, b: 3) // Llamada a la función con múltiples parámetros

// Ejemplo de función con retorno
func multiplica(a: Int, b: Int) -> Int {
    return a * b
}
print("El resultado de multiplicar 4 y 5 es \(multiplica(a: 4, b: 5))")

// Función dentro de función
func operacionesCompuestas() {
    func resta(a: Int, b: Int) -> Int {
        return a - b
    }
    print("El resultado de restar 5 de 10 es \(resta(a: 10, b: 5))")
}
operacionesCompuestas() // Llamada a la función contenedora

// Variable global y local
var variableGlobal = 10 // Variable global

func probarVariables() {
    let variableLocal = 5 // Variable local
    print("Variable global: \(variableGlobal), Variable local: \(variableLocal)")
}
probarVariables()

// Función con dificultad extra
func imprimirNumeros(cadena1: String, cadena2: String) -> Int {
    var contador = 0
    for numero in 1...100 {
        if numero % 3 == 0 && numero % 5 == 0 {
            print("\(cadena1)\(cadena2)")
        } else if numero % 3 == 0 {
            print(cadena1)
        } else if numero % 5 == 0 {
            print(cadena2)
        } else {
            print(numero)
            contador += 1
        }
    }
    return contador
}

let contador = imprimirNumeros(cadena1: "Fizz", cadena2: "Buzz")
print("Se imprimieron \(contador) números en lugar de textos.")
