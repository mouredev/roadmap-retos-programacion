//: [Previous](@previous)

/*
 * EJERCICIO 01: 18miguelgalarza.swift
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

import Foundation

func operadorAritmetico(_ valor1:Int, _ valor2:Int, _ operacion:String) -> Double{

    switch operacion {
    case "suma":
        return Double(valor1 + valor2)
    case "resta":
        return Double(valor1 - valor2)
    case "multiplicacion":
        return Double(valor1 * valor2)
    case "division":
        return Double(valor1 / valor2)
    case "modulo":
        return Double(valor1 % valor2)
    default:
        return Double(-500)
    }

}

func operadorLogico(_ valor1:String?, _ valor2:String?, _ operacion:String) -> String{

    switch operacion {
    case "AND":
        
        if valor1  != nil && valor2 != nil {
            return "Las variables no son nulas"
        }else {
            return "existe almenos una variable nula"
        }
        
    case "OR":
        
        if valor1  != nil || valor2 != nil {
            return "existe almenos una variable nula"
        }else {
            return "Las variables no son nulas "
        }
    case "NOT":
        return String(-500)

    default:
        return String(-500)
    }

}


func operadorComparacion(_ valor1:Int, _ valor2:Int, _ operacion:String) -> String{

    switch operacion {
    case "comparacion":
        if valor1 > valor2 {
            return "\(valor1) es mayor que \(valor2)"
        }else {
            return "\(valor1) es menor que \(valor2)"
        }

    default:
        return String(-500)
    }

}

func buscaNumeroEnArreglo (_ arreglo:[Int], _ valor:Int) -> Bool {
    
    for num in arreglo {
        if num == valor{
            return true
        }
    }
return false

}

print("********************* 00 Control de excepciones ***********************")

enum MiError: Error {
    case miError
    case ErrorConocido
}

func funcionQueLanzaError() throws {
    throw MiError.miError
}

do {
    try funcionQueLanzaError()
}catch MiError.miError{
    print("Se produjo un error de tipo MiError.miError.")
}catch {
    print("Se produjo un error.")
}
    
print("********************* 01 Aritmético y Asignacion ***********************")

print("\u{2713} El resultado de la suma es: \(Int(operadorAritmetico(2,5,"suma")))")
print("\u{2713} El resultado de la resta es: \(Int(operadorAritmetico(2,5,"resta")))")
print("\u{2713} El resultado de la multiplicación es: \(operadorAritmetico(2,5,"multiplicacion"))")
print("\u{2713} El resultado de la división es: \(operadorAritmetico(10,2,"division"))")
print("\u{2713} El resultado de la división es: \(operadorAritmetico(5,3,"modulo"))")

//suma y asignación

var numero = 5
    numero += 3

print("\u{2713} El resultado del suma y asignación es: \(numero) ")

//resta y asignación

var numero1 = 5
    numero -= 3

print("\u{2713} El resultado del resta y asignación es: \(numero1) ")

//multiplicación y asignación

var numero2 = 5
    numero *= 3

print("\u{2713} El resultado del multiplicación y asignación es: \(numero2) ")

//división y asignación

var numero3 = 5
    numero /= 3

print("\u{2713} El resultado del división y asignación es: \(numero3) ")

//módulo y asignación

var numero4 = 5
    numero /= 3

print("\u{2713} El resultado del módulo y asignación es: \(numero4) ")

//Asignacion de tipo  "??"
let nombre: String? = nil
let nombreDefecto = nombre ?? "Usuario"


print("********************* 02 Comparacion ***********************")

print("\u{2713} Ejemplo de operador lógico AND (Los números no deben ser nulos) : \(operadorLogico("1","1","AND"))")
print("\u{2713} Ejemplo de operador lógico OR (Debe haber almenos un variable nulo) : \(operadorLogico(nil,"1","OR"))")
print("\u{2713} Ejemplo de operador comparación (Qué variable es mayor?) : \(operadorComparacion(10,11,"comparacion"))")


// Guard : usado para validaciones tempranas, puedes condicionar, iterar de forma rapida, esto ayuda a optimizar los recursos.
let patinetas = ["skateboard", "longboards","penny"]

guard let patin = patinetas.last else {
    
    print("No existe patineta")
    throw MiError.ErrorConocido
}

print("\u{2713} Ejemplo de guard para buscar : \(patin)")

// Defer
var score = 1
if score < 10 {
    defer {
        print(score)
    }
    score += 5
}



print("********************* 03 Identidad ***********************")

class pruebaIdentidad{
/**
 Clase para hacer la prueba de refereia al mismo objeto de memoria
 */
}

let objeto1 = pruebaIdentidad()
let objeto2 = objeto1

if objeto1 === objeto2 {
    print("objeto1 y objeto2 hacen referencia al mismo objeto en memoria.")
} else {
    print("objeto1 y objeto2 no hacen referencia al mismo objeto en memoria.")
}

print("********************* 04 Iterar ***********************")
// se incluye Condicionales ternarias

let arregloDeNumeros = [1,2,3,4,5,6,7,8,9]
//func output: bool
print("\u{2713} Ejemplo de buscar numero en arreglo : \( String(buscaNumeroEnArreglo(arregloDeNumeros,2) ? "existe" : "no existe" ))")

// While
var cont = 0

while cont < 5 {
print("Iterando con While  \(cont)")
    cont += 1
}

// Repeat-While
var cont01 = 0

repeat {
print("Iterando con Repeat While  \(cont01)")
    cont01 += 1
} while cont01 < 5
print("\n")


print("********************* 05 DIFICULTAD EXTRA (opcional): ***********************")

/*
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
func dificultadExtra (){
    
    for numero in 10...55 {
      
        if (numero % 2 ) == 0 &&  (numero % 3 ) != 0 && numero != 16 {
            print("El número \(numero) es par, no es múltiplo de 3 y no es 16")
        }
    }
    
}

dificultadExtra ()

