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

// --- Variable Global ---
var globalVar = "Soy una variable global"

print("===> Funciones básicas <===")

// Sin parámetros ni retorno
func greet() {
    print("Hola, Swift!")
}
greet()

// Con un parámetro. Por defecto, Swift usa el nombre del parámetro como etiqueta en la llamada.
func greetPerson(name: String) {
    print("Hola, \(name)!")
}
greetPerson(name: "Wilmer")

// Con varios parámetros
func add(a: Int, b: Int) {
    print("La suma de \(a) y \(b) es \(a + b)")
}
add(a: 5, b: 3)

// Con retorno
func multiply(a: Int, b: Int) -> Int {
    return a * b
}
let result = multiply(a: 5, b: 3)
print("El resultado de la multiplicación es \(result)")

// Con parámetros por defecto
func greetDefault(name: String, greeting: String = "Hola") {
    print("\(greeting), \(name)!")
}
greetDefault(name: "MoureDev")
greetDefault(name: "Wilmer", greeting: "Hello")

// Con parámetros de longitud variable (variadic)
// El _ omite la etiqueta del argumento en la llamada para una sintaxis más limpia.
func printArgs(_ args: Any...) {
    print("Argumentos variables (variadic):")
    for arg in args {
        print("- \(arg)")
    }
}
printArgs(1, "texto", true, 12.5)


print("\n===> Funciones dentro de funciones <===")
func outerFunction() {
    print("Esta es la función externa.")
    func innerFunction() {
        print("Esta es la función interna.")
    }
    innerFunction()
}
outerFunction()


print("\n===> Funciones de la Librería Estándar de Swift <===")
let myList = [1, 2, 3, 4, 5]
print("Usando la propiedad .count de un Array: El array tiene \(myList.count) elementos.")
// .max() devuelve un valor opcional, por eso se usa `!` para desempaquetarlo de forma forzada para este ejemplo.
print("Usando .max(): El valor máximo es \(myList.max()!).")


print("\n===> Variable LOCAL y GLOBAL <===")
func myFunctionScope() {
    let localVar = "Soy una variable local"
    print(globalVar) // Acceso directo a la variable global
    print(localVar)
}
myFunctionScope()

func modifyGlobal() {
    globalVar = "He modificado la variable global"
}

print("Antes de modificar: \(globalVar)")
modifyGlobal()
print("Después de modificar: \(globalVar)")


/*
 * DIFICULTAD EXTRA (opcional):
 */
print("\n====> DIFICULTAD EXTRA <====")
func fizzBuzzExtra(text1: String, text2: String) -> Int {
    var count = 0
    for i in 1...100 { // El rango ... es inclusivo en ambos extremos
        let isMultipleOf3 = (i % 3 == 0)
        let isMultipleOf5 = (i % 5 == 0)

        if isMultipleOf3 && isMultipleOf5 {
            print("\(text1)\(text2)")
        } else if isMultipleOf3 {
            print(text1)
        } else if isMultipleOf5 {
            print(text2)
        } else {
            print(i)
            count += 1
        }
    }
    return count
}

let timesPrintedNumber = fizzBuzzExtra(text1: "Fizz", text2: "Buzz")
print("\nEl número se imprimió un total de \(timesPrintedNumber) veces.")
