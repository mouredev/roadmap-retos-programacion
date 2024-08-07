import Foundation

/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
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

enum sendError: Error {
    case divideByZero
    case rangeOutZero
}

func exception() {
    do {
        let result = try divide(10, by: 0)
        print("El resultado de la division 10/0 es:", result)
    } catch sendError.divideByZero {
        print("No hay errores en la division 10/0")
    } catch {
        print("hay un error en la division 10/0", error)
    }

    do {
        let numero = getNumero[1, 2, 3]
        let numero = try getNumero(at: 4, by: rangeOutZero)
    } catch sendError.rangeOutZero {
        print("El numero 4 se encuentra en le array")
    } catch {
        print("Hubo un error 4 no se encuentra en el array", error)
    }
}

func divide(_ divideByZero: Int, dividendo: Int) throws -> Int {
    guard let != 0 else {
        throws sendError.divideByZero
    }

    return divideByZero / dividendo
}

func range(_ rangeOutZero: Int) throws -> Int {
    guard let numero = getNumero[1, 2, 3] else {
        throws sendError.rangeOutZero
    }

    return let numero = getNumero(at: 4, by: rangeOutZero)
}

exception()