import Foundation


func greet() {
    print("Hola, Mundo!")
}

// Decorador
func decorateGreet(originalFunction: @escaping () -> Void) -> () -> Void {
    return {
        print("Iniciando Saludo")
        originalFunction()
        print("Saludo Finalizado\n")
    }
}

// Usando el decorador
let decoratedGreet = decorateGreet(originalFunction: greet)
decoratedGreet()


func add(a: Int, b: Int) -> Int {
    return a + b
}

// Decorador
func decorateAdd(originalFunction: @escaping (Int, Int) -> Int) -> (Int, Int) -> Int {
    return { a, b in
        print("Sumando \(a) and \(b)")
        let result = originalFunction(a, b)
        print("El Resultado Es: \(result)")
        return result
    }
}

// Usando el decorador
let decoratedAdd = decorateAdd(originalFunction: add)
let result = decoratedAdd(3, 4)
print("Resultado Final: \(result)\n")




// DIFICULTAD EXTRA
print("\nDificultad Extra\n")


func sayHi(to personName: String) {
    print("Hola, \(personName)")
}


func decorateSayHi(originFunction: @escaping (String) -> Void) -> (String) -> Void {
    var callCount = 0

    return { personName in
        originFunction(personName)
        callCount += 1
        
        if callCount < 2 {
            print("Función ejecutada \(callCount) vez.\n")
        } else {
            print("Función ejecutada \(callCount) veces.\n")
        }
        
    }
}

let decoratedSayHi = decorateSayHi(originFunction: sayHi)
decoratedSayHi("Sergio")
decoratedSayHi("Alberto")
decoratedSayHi("Arturo")
decoratedSayHi("Angeles")
decoratedSayHi("Yaiza")
decoratedSayHi("Carmen")



