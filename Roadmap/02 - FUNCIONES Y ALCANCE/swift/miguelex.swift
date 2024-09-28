import Foundation

func holaMundo(){
    print("¡Hola, mundo!")
}

holaMundo()

func mostrarEdad(edad: Int){
    print("Tienes \(edad) años")
}

mostrarEdad(edad: 48)

func sumar(a: Int, b: Int) -> Int {
    return a + b
}

print("La suma de 5 + 3 es  \(sumar(a:5, b:3))")

func mainFunction(){
    print("Este mensaje se muestra desde al funcion más externa")
    func innerFunction(){
        print("Este mensaje se muestra desde la función interna")
    }
    innerFunction()
}

mainFunction()

let numeros = [1, 2, 3, 4, 5]

let pares = numeros.filter { $0 % 2 == 0 }
print("\nNumeros pares: \n\(pares)")

// Extra

func extra(param1: String, param2: String) -> Int {
    var numVeces = 0
    for i in 1...100 {
        if i % 15 == 0  {
            print("\(param1)\(param2)")
        } else if i % 3 == 0 {
            print("\(param1)")
        } else if i % 5 == 0 {
            print("\(param2)")
        } else {
            print(i)
            numVeces += 1
        }
    }
    return numVeces
}

print("La función ha impreso un total de \(extra(param1:"Fizz", param2:"Buzz")) numeros")



