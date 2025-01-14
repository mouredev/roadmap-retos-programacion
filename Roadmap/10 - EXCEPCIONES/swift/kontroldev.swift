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

//MARK: - Extra
enum StrTypeError: Error {
    case invalidType
}

func processParams(_ parameters: [Any]) {
    guard parameters.count >= 3 else {
        print("El número de elementos de la lista debe ser mayor que dos.")
        return
    }
    
    guard let divisor = parameters[1] as? Int, divisor != 0 else {
        print("El segundo elemento de la lista no puede ser un cero.")
        return
    }
    
    guard !(parameters[2] is String) else {
        print("El tercer elemento no puede ser una cadena de texto.")
        return
    }
    
    print(parameters[2])
    print(parameters[0] as! Int / divisor)
    print((parameters[2] as! Int) + 5)
}

do {
    try processParams([1, 2, 3, 4])
} catch StrTypeError.invalidType {
    print("El tercer elemento no puede ser una cadena de texto.")
} catch let error as NSError {
    print("Se ha producido un error inesperado: \(error.localizedDescription)")
} catch {
    print("Se ha producido un error inesperado.")
} finally {
    print("El programa finaliza sin detenerse.")
}

