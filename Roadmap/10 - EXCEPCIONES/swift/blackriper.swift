import Foundation
/* las excepciones se usan para manejar errores  en swift 
   se pueden manejar de la siguiente manera
   do {
    
   } catch error {
    
   }
    las funciones , clases pueden tener excepciones para agregar alguna 
    se hace de la siguiente manera:

    func getResponde() throws  ->String

    esto quiere decir que la funcion puede retornar un error

    para crear uno o mas errores personalizados usamos el enum este debe implementar el protocolo Error

    enum MiError: Error {
        case ErrorConocido
    }
 */
  
enum ArithmeticError: Error {
    case divideByZero
    case moduloByZero
}

func divide(_ dividend: Int, by divisor: Int) throws -> Int {
    if divisor == 0 {
        throw ArithmeticError.divideByZero
    }
    return dividend / divisor
}

func modulo(_ dividend: Int, by divisor: Int) throws -> Int {
    if divisor == 0 {
        throw ArithmeticError.moduloByZero
    }
    return dividend % divisor
}

do {
    let result = try divide(10, by: 0)
    print(result)
} catch ArithmeticError.divideByZero {
    print("No se puede dividir por 0")
}

do {
    let result = try modulo(10, by: 0)
    print(result)
} catch ArithmeticError.moduloByZero {
    print("No se puede dividir por 0")
}

//ejercicio extra

enum ProductError: Error {
    case outOfStock
    case notFoundProduct
    case nillStock
}

struct Product {
    var id :UUID
    var name: String
    var stock: Int?
}

let products = [
          Product(id: UUID(), name: "iPhone15pro", stock: 10),
          Product(id: UUID(), name: "Samsung s24", stock: 0),
          Product(id: UUID(), name: "Xiaomi", stock: nil)]


func buy(nom: String,cantity: Int) throws {
    guard let product = products.first(where: {$0.name==nom}) else {
        throw ProductError.notFoundProduct
    }
    
    guard let stock = product.stock else {
        throw ProductError.nillStock
    }
    
    if stock < cantity {
        throw ProductError.outOfStock
    }
    
}

do {
    //try buy(nom: "Motorola", cantity: 10)
    //try buy(nom: "Samsung s24", cantity: 10)
    try buy(nom: "Xiaomi", cantity: 14)
} catch ProductError.outOfStock {
    print("out of stock")
} catch ProductError.notFoundProduct {
    print("product not found")
} catch ProductError.nillStock {
    print("stock not available")
}
