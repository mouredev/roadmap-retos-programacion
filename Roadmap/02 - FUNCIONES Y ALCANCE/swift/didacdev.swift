import Foundation

// Funciones sin parámetros y valor de retorno
func hello() -> String {
    return "hello"
}

print(hello())

// Funciones con múltiples parámetros
func say(person: String, sentence: String) -> String {
    return "\(sentence) \(person)" 
}

print(say(person: "Diego", sentence: "hello"))

// Funciones sin valores de retorno
func greet(person: String) {
    print("hello \(person)")
}

// Funciones con varios valores de retorno
func sayHelloToTwo(personOne: String, personTwo: String) -> (helloOne: String, helloTwo: String) {

    return("hello \(personOne)", "hello \(personTwo)")
}

let greetings: (String, String) = sayHelloToTwo(personOne: "Diego", personTwo: "Pepe")
print(greetings.0)
print(greetings.1)

// Retorno implícito
func greet(for person: String) -> String {
    "hello \(person)"
}

print(greet(for: "Diego"))

// Especificar etiquetas en los argumentos
func greet(person: String, from hometown: String) -> String {
    return "hello \(person) for comming from \(hometown)"
}

print(greet(person: "Diego", from: "Madrid"))

// Omitir las etiquetas
func sumaDos(_ number: Int) -> Int {
    let result = number + 2
    return result
}

print(sumaDos(2))

// Parámetros con valor por defecto
func sayHello(person: String, greet: Bool = true) -> String{
    if greet {
        return "hello \(person)"
    } else {
        return "bye"
    }
}

print(sayHello(person: "Diego"))

// Parámetros variados
func greetToPeople(_ people: String...) -> [String] {
    var greet: [String] = []

    for person in people {
        greet.append("hello \(person)") 
    }

    return greet
}

print(greetToPeople("Diego", "Pepe"))

// Parámetros de entrada y salida
func sumaDos(_ number: inout Int) {
    number += 2
}

var number = 2
sumaDos(&number)
print(number)

// Funciones anidadas
func sumaDos(add: Bool) -> (Int) -> Int {

    func addTwo(number: Int) -> Int {
        let result = number + 2
        return result
    }

    func addOne(number: Int) -> Int {
        let result = number + 1
        return result
    }

    return add ? addTwo : addOne 
}

let suma = sumaDos(add: false)
print(suma(2))


// --------------------- Ejercicio ---------------------------
func times(textOne: String, textTwo: String) -> Int {
    
    var times = 0

    for number in 1...100 {


        if number % 3 == 0 {
            print(textOne)
            times += 1
        } else if number % 5 == 0 {
            print(textTwo)
            times += 1
        } else if number % 3 == 0 && number % 5 == 0 {
            print("\(textOne) \(textTwo)")
            times += 1
        } else {
            print(number)
        }
    }

    return times
}

print(times(textOne: "hola", textTwo: "adios"))