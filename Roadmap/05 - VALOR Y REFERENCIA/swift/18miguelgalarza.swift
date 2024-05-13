//: [Previous](@previous)


/* 18miguelgalarza.swift Release #05 - swift
 * EJERCICIO: #05 VALOR Y REFERENCIA
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato. .......ok
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */


import Foundation

var greeting = "Hello, playground"

//Asignacion por valor
// Tipo de dato: Int (tipo primitivo)
var numero1 = 10
var numero2 = numero1 // Asignación por valor, se crea una copia independiente de numero1

numero1 = 20 // Cambiar el valor de numero1 no afecta a numero2

print(numero1) // Salida: 20
print(numero2) // Salida: 10 (se mantiene igual)


//Asignacion por referencia

class Persona {
    var nombre: String
    
    init(nombre: String) {
        self.nombre = nombre
    }
}

// Crear dos instancias de la clase Persona
let persona1 = Persona(nombre: "Juan")
let persona2 = persona1 // Asignación por referencia, persona2 apunta a la misma instancia que persona1

// Modificar el nombre de persona1
persona1.nombre = "Pedro"

// Imprimir los nombres de ambas personas
print("Nombre de persona1:", persona1.nombre) // Output: Pedro
print("Nombre de persona2:", persona2.nombre) // Output: Pedro, ya que ambas variables apuntan a la misma instancia

// FUNCIONES


// Función variable por valor 01
func concatenar(_ subcadena: String) -> String {
    subcadena + " birthday"
}
// Asigna el retorno de la función a la variable valueVariable3
var variable = concatenar(_: "Happy")
// Imprime el valor de la variable valueVariable1
print(variable)



/** DIFICULTAD EXTRA (opcional):
* Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
* - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
*   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
*   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
*   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
*   Comprueba también que se ha conservado el valor original en las primeras.
*/

// Asignación por valor 02
func setValues(x: String, y: String) -> (String, String){
    return (y, x)
}

var input = "morning"
var input0 = "night"
var (output, output1) = setValues(x: input, y: input0)
print("original values \(input) and \(input0)")
print("new values \(output) and \(output1)")

//Asignación por referencia
func intercambioPorReferencia(x: inout String, y: inout String) -> (String, String){
    let temporal = x
    x=y
    y=temporal
    return (x,y)
}

var v1 = "morning"
var v2 = "night"
var (v3, v4) = intercambioPorReferencia(x: &v1, y: &v2)
print("original values \(v1) and \(v2)")
print("new values \(v3) and \(v4)")




