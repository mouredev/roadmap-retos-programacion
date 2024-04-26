import Foundation

// Array para iterar.
var numbers = [1, 2, 3, 4, 5, 5, 7, 8, 9, 10]


// Función recursiva con numeros.
print("\nFunción recursiva con numeros.")
func printNumbers(_ n: Int) {
    if n > 0 {
        printNumbers(n - 1)
        
        print(n)
    }
}
printNumbers(10)


// Función recursiva con array.
print("\nFunción recursiva con array.")
func printArray(_ a: inout [Int]) {
    var b: [Int] = a
    
    if !b.isEmpty {
        print(b[0])
        
        b.removeFirst()
        
        printArray(&b)
    }
}
printArray(&numbers)


// Metodo map, imprime los números del array.
print("\nMetodo map.")
let map: [()] = numbers.map { n in
    print(n)
}


// Metodo forEach, imprime los números del array.
print("\nMetodo forEach.")
numbers.forEach { n in
    print(n)
}




// DIFICULTAD EXTRA
print("\nDIFICULTAD EXTRA.")


// Clouser que imprime los caracteres de un string.
print("\nClosure imprime caracteres.")
var string = ""
let closurePrint: (String) -> Void = { str in
    string = str
    if !str.isEmpty {
        print(str[string.startIndex])
        string.removeFirst()
        closurePrint(string)

    }
}
closurePrint("Hello")


// Metodo filter, imprime los números del array que sean multiplos de 2.
print("\nMetodo filter")
let filter = numbers.filter { n in
    if n % 2 == 0 {
        print(n)
    }
    return true
}



// Metodo reduce, sume 10 a cada uno de los números del array y los imprime.
print("\nMetodo reduce.")
let reduce = numbers.reduce(into: 10) { n1, n2 in
    print(n1 + n2)
}


// Metodo sequencee, inicia una secuencia en 10 y le eleva al cubo tantas veces como sea indicado.
print("\nMetodo sequence.")
let seq = sequence(first: 10) { n in
    pow(n, 3)
}
// Se eleva 4 veces al cubo el numero 10 e imprime los números.
let firstFour: [()] = Array(seq.prefix(4)).map { n in
    print(n)
}


// Metodo sort, ordena de mayor a menor e imprime los numeros.
print("\nMetodo sort.")
numbers.sort { n1, n2 in
    n1 > n2
}
numbers.forEach { n in
    print(n)
}

