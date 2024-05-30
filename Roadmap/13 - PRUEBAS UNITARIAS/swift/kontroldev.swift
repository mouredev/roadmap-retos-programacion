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


import Foundation
import XCTest

// Definición de la función sumar
func sumar(_ a: Int, _ b: Int) -> Int {
    return a + b
}

// Clase de prueba para la función sumar
class SumarTests: XCTestCase {
    
    func testSumar() {
        // Caso de prueba 1: 2 + 3 = 5
        XCTAssertEqual(sumar(2, 3), 5)
        
        // Caso de prueba 2: -1 + 1 = 0
        XCTAssertEqual(sumar(-1, 1), 0)
        
        // Caso de prueba 3: 0 + 0 = 0
        XCTAssertEqual(sumar(0, 0), 0)
        
        // Caso de prueba 4: 123 + 456 = 579
        XCTAssertEqual(sumar(123, 456), 579)
        
        // Caso de prueba 5: -123 + (-456) = -579
        XCTAssertEqual(sumar(-123, -456), -579)
    }
}

// Ejecutar las pruebas
SumarTests.defaultTestSuite.run()


/// **Dificultad EXTRA**


// Definición del diccionario con los datos requeridos
let myInfo: [String: Any] = [
    "name": "Tu nombre",
    "age": "Tu edad",
    "birth_date": "Tu fecha de nacimiento",
    "programming_languages": ["Swift", "Python", "JavaScript"] // Ejemplo de lenguajes de programación
]

// Clase de prueba para el diccionario
class MyInfoTests: XCTestCase {
    
    func testFieldsExistence() {
        // Verificar que existen todas las claves
        XCTAssertNotNil(myInfo["name"])
        XCTAssertNotNil(myInfo["age"])
        XCTAssertNotNil(myInfo["birth_date"])
        XCTAssertNotNil(myInfo["programming_languages"])
    }
    
    func testCorrectData() {
        // Verificar que los valores de las claves son correctos
        XCTAssertEqual(myInfo["name"] as? String, "Tu nombre")
        XCTAssertEqual(myInfo["age"] as? String, "Tu edad")
        XCTAssertEqual(myInfo["birth_date"] as? String, "Tu fecha de nacimiento")
        
        // Verificar que los lenguajes de programación son correctos
        let expectedLanguages = ["Swift", "Python", "JavaScript"]
        XCTAssertEqual(myInfo["programming_languages"] as? [String], expectedLanguages)
    }
}

// Ejecutar las pruebas
MyInfoTests.defaultTestSuite.run()
