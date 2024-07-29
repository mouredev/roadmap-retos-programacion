import Foundation

/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
 */

// Suma 
 func suma(a: Int, b: Int) -> Int {
    return a + b 
 }

print("El resultado de la suma 5 + 5 es: \(suma(a: 5, b: 5))")

// Test
func sumaTwoInts() {
    let result = suma(a: 5, b: 5) == 10
    assert(result, "El resultado de la suma de 5 + 5 deberia ser 10")
    print("El test del resultado de la suma de 5 + 5 ha pasado satisfactoriamente")
}

sumaTwoInts()