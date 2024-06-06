import Foundation

// variable por valor

var name = "Migue" 
var nombre = name 

print("Antes de cambiar el nombre:")
print(name)
print(nombre)

name = "Miguel Angel"

print("Despues de cambiar el nombre:")
print(name)
print(nombre)

// variable por referencia

class Persona {
    var nombre: String
    init(nombre: String) {
        self.nombre = nombre
    }
}

var p1 = Persona(nombre: "Juan")
var p2 = p1 // p2 es una referencia a la misma instancia que p1

print("Antes de cambiar el nombre:")
print(p1.nombre)
print(p2.nombre)

p1.nombre = "Pedro" // cambiamos el nombre de p1

print("Después de cambiar el nombre:")
print(p1.nombre)
print(p2.nombre)

// Funcion con paso por valor

func incrementar(_ n: Int) -> Int {
    return n + 1
}

var a = 100

var b = incrementar(a)

print(a)
print(b)

// Extra

let num1, num2, num3, num4: Int

func intercambiarPorValor(_ x: Int, _ y: Int) -> (Int, Int) {
    return (y, x)
}

num1 = 10
num2 = 5

(num3, num4) = intercambiarPorValor(10, 5)
print("Despues de llamar a la funcion, tenemos los valores:")
print(num1)
print(num2)
print(num3)
print(num4)

// parámetros por referencia. Intercambio de array

func intercambiarPorReferencia(_ x: inout [Int], _ y: inout [Int]) -> ([Int], [Int]) {
    let temp = x
    x = y
    y = temp
    return (x, y)
}

var arr1 = [1, 2, 3]
var arr2 = [4, 5, 6]

print("Antes del intercambio:")
print("arr1 = \(arr1)")
print("arr2 = \(arr2)")

var (arr3, arr4) = intercambiarPorReferencia(&arr1, &arr2)

print("\nDespués del intercambio:\n")
print("arr1 = \(arr1)")
print("arr2 = \(arr2)")
print("arr3 = \(arr3)")
print("arr4 = \(arr4)")





