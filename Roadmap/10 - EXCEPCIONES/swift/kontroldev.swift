import Foundation


/*
* EJERCICIO:
* Explora el concepto de manejo de excepciones según tu lenguaje.
* Fuerza un error en tu código, captura el error, imprime dicho error
* y evita que el programa se detenga de manera inesperada.
* Prueba a dividir "10/0" o acceder a un indice no existente
* de un listado para intentar provocar un error.
*
* DIFICULTAD EXTRA (opcional):
* Crea una función que sea capaz de procesar parámetros, pero que también
* pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
* corresponderse con un tipo de excepción creada por nosotros de manera
* personalizada, y debe ser lanzada de manera manual) en caso de error.
* - Captura todas las excepciones desde el lugar donde llamas a la función.
* - Imprime el tipo de error.
* - Imprime si no se ha producido ningún error.
* - Imprime que la ejecución ha finalizado.
*/


enum CustomError: Error {
    case divisionByZero
    case indexOutOfRange
}

func handleExceptions() {
    do {
        // División por cero
        let result = try divide(10, by: 0)
        print("El resultado de la división es:", result)
    } catch CustomError.divisionByZero {
        print("Error: División por cero")
    } catch {
        print("Se produjo un error inesperado:", error)
    }

    do {
        // Acceder a un índice no existente
        let array = [1, 2, 3]
        let value = try getValue(at: 4, from: array)
        print("El valor obtenido es:", value)
    } catch CustomError.indexOutOfRange {
        print("Error: Índice fuera de rango")
    } catch {
        print("Se produjo un error inesperado:", error)
    }
}

func divide(_ dividend: Int, by divisor: Int) throws -> Int {
    guard divisor != 0 else {
        throw CustomError.divisionByZero
    }
    return dividend / divisor
}

func getValue(at index: Int, from array: [Int]) throws -> Int {
    guard index >= 0 && index < array.count else {
        throw CustomError.indexOutOfRange
    }
    return array[index]
}

handleExceptions()
