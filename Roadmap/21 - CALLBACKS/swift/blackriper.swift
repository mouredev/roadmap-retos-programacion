import Foundation

/*
 un callback es una funcion que se pasa como argumento a otra funcion y se ejecuta en la misma 
 al igual que en kotlin  estas funciones se pueden simplificar con closures.
 */


func exampleWithCallback(callback: ([Int]) -> [Int]) {
    let numbers = [1, 2, 3, 4, 5]
    let result = callback(numbers)
    print(result)
}

// estamos pasando una closure como argumento
exampleWithCallback { numbers in
    return numbers.map({ $0 * 2 })
}

//ejercicio extra

func confirmOrder(_ dishName: String) async  throws {
    let duration = Double.random(in: 1...10)
    print("ordering \(dishName)")
   try await Task.sleep(for: .seconds(duration))
}

func readyOrder(_ dishName: String) async throws{
    let duration = Double.random(in: 1...10)
    try await Task.sleep(for: .seconds(duration))
    print("ready \(dishName)")
}

func recivedOrder(_ dishName: String) async throws{
    let duration = Double.random(in: 1...10)
    try await Task.sleep(for: .seconds(duration))
    print("recived \(dishName)")
}
    
// creamos un tipo personalido para no tener que escribir el tipo de callback
typealias Callback = (String) async throws -> Void

func restaurantOrder(confirm: Callback, ready: Callback, recived: Callback) async throws {
   print("What would you like to order?") 
   let dishName = readLine() ?? "Tacos"

   try await confirm(dishName)
   try await ready(dishName)
   try await recived(dishName)
 }

 try await restaurantOrder(confirm: confirmOrder, ready: readyOrder, recived: recivedOrder)


