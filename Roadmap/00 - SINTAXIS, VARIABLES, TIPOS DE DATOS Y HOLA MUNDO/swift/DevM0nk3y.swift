/*
* EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */

import Foundation

// sitio web oficial de swift https://www.swift.org

//comentario de una linea

/*
 comentarios
 de multiples
 lineas
 */

/*
 /* comentario anidado */
*/

var myVariable = "Im a variable"
let myConstant = "Im a constant"

//Int: Un entero con signo, que puede ser positivo, negativo o cero. Su tamaño depende de la plataforma (32 o 64 bits).
var myInt = 1

//UInt: Un entero sin signo, que solo puede ser positivo o cero.
var myUInt = 100

//Float: Número de punto flotante de precisión simple (32 bits).
var myFloat = 1.12345

//Double: Número de punto flotante de precisión doble (64 bits). Se usa cuando necesitas más precisión que Float.
var myDouble = 1.1234567890

//Boolean: Valores que representan verdadero o falso (true o false).
var myBool = true

//String: Tipo de dato que almacena texto.
var myString = "Swift"

//Character: Almacena un solo carácter.
var myChar = "a"

print("¡Hola, \(myString)!")
