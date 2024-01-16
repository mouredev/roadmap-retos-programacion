

import Foundation
//Sin parametro ni retorno
func Hola(){
    print("Hola")
}

//con parametro

func Adios(usuario: String){
    print("Adios \(usuario)")
}

let usuario: String = "David"

Adios(usuario: usuario)

//Con varios parametros

func Suma(n1: Int, n2: Int){
    let suma = n1 + n2
    print("La suma es: \(suma)")
}

//con Parametro y retorno

func Potencia(n1: Int) -> Int {
    return n1 * n1 
}

let Cuadrado = Potencia(n1: 5)
print("\(Cuadrado)")

//Funcion dentro de funcion

func BienvenidaC(){
    print("Hola")

    func Adios(){
        print("Adios")
    }

    Adios()
}

BienvenidaC()
//Adios() --> No se puede llamar fuera Pero si adentro.

//Funciones dentro de swift:
let funcion = "Hola como estan :D"

print(funcion)

let contarfuncion = funcion.count

let funcionMayus = funcion.uppercased()

let funcionMinus = funcion.lowercased()

//...etc

print("\(contarfuncion) \(funcionMayus) \(funcionMinus)" )

//Variable local y global

let variableGlob = "Global"

func variableLoc(){
    let variableLoc = "Local"
    print(variableGlob)
    print(variableLoc)
}
//print(variableLoc) --> No se le puede llamar a variable local fuera de la funcion

variableLoc()

//Dificultad Extra

func DExtra(var1: String, var2: String ) -> Int {
    var contador: Int = 0
    for numero in 1...100 {
        if (numero % 15 == 0){
            print("\(var1)\(var2)")
        }
        else if (numero % 3 == 0){
            print(var1)
        }else if (numero % 5 == 0){
            print(var2)
        }
        else {
            print(numero)
            contador += 1
        }

    }

    return contador
}



var a = DExtra(var1: "A", var2: "B")
print("Las veces que se imprimio un numero fueron: \(a)")