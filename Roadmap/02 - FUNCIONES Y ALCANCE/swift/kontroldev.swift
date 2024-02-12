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


func saludar() {
    print("¡Hola, mundo!")
}
saludar()

func saludar(nombre: String) {
    print("¡Hola, \(nombre)!")
}
saludar(nombre: "Juan")

func sumar(a: Int, b: Int) -> Int {
    return a + b
}
let resultado = sumar(a: 3, b: 4)
print("El resultado de la suma es \(resultado)")

func funcionExterna() {
    func funcionInterna() {
        print("Esta es una función interna")
    }
    funcionInterna()
}
funcionExterna()

let numeros = [1, 2, 3, 4, 5]
let numerosPares = numeros.filter { $0 % 2 == 0 }
print(numerosPares)

var variableGlobal = 10

func funcionConVariableLocal() {
    let variableLocal = 5
    print("La variable local es \(variableLocal)")
}

funcionConVariableLocal()
print("La variable global es \(variableGlobal)")

func imprimirNumeros(texto1: String, texto2: String) -> Int {
    var contador = 0
    for i in 1...100 {
        if i % 3 == 0 && i % 5 == 0 {
            print("\(texto1)\(texto2)")
            contador += 1
        } else if i % 3 == 0 {
            print("\(texto1)")
            contador += 1
        } else if i % 5 == 0 {
            print("\(texto2)")
            contador += 1
        } else {
            print(i)
        }
    }
    return contador
}

let vecesImpreso = imprimirNumeros(texto1: "Hola", texto2: "Mundo")
print("La función ha impreso \(vecesImpreso) veces")
