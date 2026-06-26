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

 // Función sin parámetros ni retorno
func saludar() {
    print("Bonjour, world!")
} 
saludar()

// Función con un parámetro y sin retorno
func saludar1(_ nombre: String) {
    print("Bonjour, \(nombre)!")
}   
saludar1("Yang")

// Función con varios parámetros y sin retorno
func saludar2(_ nombre: String, _ apellido: String) {
    print("Bonjour, \(nombre) \(apellido)!")
}
saludar2("Yang", "Shao")

// Función con un parámetro y con retorno
func saludar3(_ nombre: String) -> String {
    return "Bonjour, \(nombre)!"
}
let saludo = saludar3("Yang")
print(saludo)   

// Función con varios parámetros y con retorno
func saludar4(_ nombre: String, _ apellido: String) -> String {
    return "Bonjour, \(nombre) \(apellido)!"
}
let saludoCompleto = saludar4("Yang", "Shao")
print(saludoCompleto)   

// Función sin parámetros y con retorno
func obtenerSaludo() -> String {
    return "Bonjour, world!"
}
let saludoMundo = obtenerSaludo()
print(saludoMundo)  

// Función dentro de otra función
func externa() {
    func interna() {
        print("Bonjour, Paris!")
    }
    interna()
}
externa()

// Función dentro de otra función con retorno
func externa2() -> String {
    func interna2(_ nombre: String) -> String {
        return "Bonjour, \(nombre)!"
    }
    let saludoInterno = interna2("Madrid")
    return saludoInterno
}
let sayHiToACity = externa2()
print(sayHiToACity) 

// utilizando una función ya creada en el lenguaje
print(max(5, 10))
print(min(5, 10))
print(abs(-5))
print("Bonjour".uppercased())   
print("Bonjour".lowercased())
print("Bonjour".count)
print([1, 2, 3].contains(2))

// Variable global
var cuidad = "Paris"
func saludarCiudad() {
    // Variable local
    let cuidadLocal = "Madrid"
    print("Bonjour, \(cuidad)!")
    print("Bonjour, \(cuidadLocal)!")
}
saludarCiudad() 
print("Bonjour, \(cuidad)!")
// print("Bonjour, \(cuidadLocal)!") da error porque la variable cuidadLocal es local a la función saludarCiudad

// Dificultad extra
func imprimirNumerosConTexto(_ texto1: String, _ texto2: String) -> Int {
    var contador = 0 
    for i in 1...100 {
        if i % 3 == 0 && i % 5 == 0 {
            print("\(texto1) \(texto2)")
        } else if i % 3 == 0 {
            print(texto1)
        } else if i % 5 == 0 {
            print(texto2)
        } else {
            print(i)
            contador += 1
        }
    }
    return contador
}
let veces = imprimirNumerosConTexto("Fizz", "Buzz")
print("Se han impreso \(veces) números en lugar de los textos.")