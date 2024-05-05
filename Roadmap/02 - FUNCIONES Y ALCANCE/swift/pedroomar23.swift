import Foundation 

/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

// Funciones sin parametros ni retorno
func Greeting() {
    print("!Welcome to Hola Mundo Day!")
}

Greeting()

// Funiones con uno o varios para metros 
let nombres = ["Pedro", "Juan", "Oscar"] // Cadena de texto (String) 

// Ejemplo 1
func Perfil(nombres: String) {
    print("El perfil de las personas es \(nombres)")
}

let age = [20, 25, 30] // Cadena de enteros (Int)

// Ejemplo 2
func age(age: Int) {
    print("El array tiene una cadena de valores \(age)")
}

// Funciones con retorno
func suma(a: Int, b: Int) -> Int { // Ejemplo 1 Suma
    return a + b
}
print("El resultado de la suma 5 + 5 es \(suma(a: 5, b: 5))")

func resta(a: Int, b: Int) -> Int { // Ejemplo 2 Resta
    return a - b 
}
print("El resultado de las resta 10 - 5 es \(resta(a: 10, b: 5))")

func combinada(a: Int, b: Int, c: Int, d: Int) -> Int { // Ejemplo 3 Combinada 
    return a + b / c * d
}
print("El resultado de la combinada 15 - 5 / 2 * 4 es \(combinada(a: 1, b: 5, c: 2, d: 4))")

// Funciones dentro de funciones 
func MainActor() {
    print("Esta funcion va dirigida a la parte externa")

    func OtherAction() {
        print("Esta funcion va dirigida a la parte interna")

        OtherAction()
    }
}
MainActor()

// Variable Local
var numeros = 10
func LocalVar() {
    print(numeros)
}

// Variable Global
var numeros = 10

func GlobalVar(numeros: Int) {
   print(numeros)
}
GlobalVar(numeros: numeros)







