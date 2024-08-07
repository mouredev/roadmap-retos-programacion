
// operadores aritmeticos 

let a = 5
let b = 3
print("Aritmeticos:")
print("5 + 3 = \(a + b)")
print("5 - 3 = \(a - b)")
print("5 * 3 = \(a * b)")
print("5 / 3 = \(5 / 3)")
print("5 % 3 = \(5 % 3)")

// operadores de comparacion
print("\nDe comparacion:")
print("5 == 5 --> \(5 == 5)")
print("10 != 5 --> \(10 != 5)")
print("8 > 3 --> \(8 > 3)")
print("2 < 7 --> \(2 < 7)")

// operadores de asignacion
var edad = 48
print("\nDe asignacion:")
print("Mi edad actual: \(edad)")
print("Mi edad el año que viene: \(edad + 1)")

// operadores de identidad  
let objeto1 = "Hola"
let objeto2 = "Hola"
let sonIguales = objeto1 == objeto2
print("\nDe identidad:")
print("Objetos iguales: \(sonIguales)")

//operadores logicos

let and: Bool = true == true && false == false
let or: Bool = 1 > 11 || "or" == "or"
let not: Bool = !false
print("\nOperadores logicos:")
print("AND: \(and)")
print("OR: \(or)")
print("NOT: \(not)")


//estructuras de control

let c = 5
let d = 3
print("\nEstructuras de control:")
if c == d {
    print("a es igual a b")
} else {
    print("a no es igual a b")
}

var heroe="Flash"

switch(heroe) {
    case "Flash":
        print("Flash")
    case "Batman":
        print("Batman")
    case "Superman":
        print("Superman")
    default:
        print("No se reconoce")
}

// estructuras de repeticion 

print("bucle for")

for i in 1...5 {
    print(i)
}

print("bucle while")
var i=0
while i<5 {
    print(i)
    i+=1
}

print("bucle repeat while")
var j=0
repeat {
    print(j)
    j+=1
} while j<5

// excepciones 
enum ErrorPersonalizado: Error {
    case errorPersonalizado
}

func lanzarExcepcion() throws {
    throw ErrorPersonalizado.errorPersonalizado
}

print("Reto adicional")
// reto adicional
for i in 10...55{
    if i % 2 == 0 && i != 16 && i % 3 != 0 {
        print(i)
    }
}