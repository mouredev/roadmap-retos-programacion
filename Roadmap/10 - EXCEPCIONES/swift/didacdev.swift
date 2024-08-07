import Foundation

enum MyError: Error {
    case errorEmptyList
}

func divideBy(numbers: [Int], divisor: Int, size: Int) throws {

    guard numbers.count != 0 else {
        throw MyError.errorEmptyList
    }

    guard divisor != 0 else {
        throw fatalError("Divisor can't be 0")
    }

    guard numbers.count == size else {
        throw fatalError("Size should be numbers.count")
    }

    for index in 0..<size {
        print(numbers[index] / divisor)
    }

    print("Ejecución finalizada sin errores")
}

do {
    try divideBy(numbers: [], divisor: 2, size: 4)
} catch MyError.errorEmptyList{
    print("The list is empty")
} catch {
    print("Error \(error.localizedDescription)")
} 
defer {
    print("Ejecución finalizada")
}