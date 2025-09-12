import Foundation



// Función sin parametros
print("\nFucnción Sin Parametros")
func helloWorld() {
    print("Hola mundo")
}
helloWorld()



// Fución con un parametro
print("\nFunción Con Un Parametro")
func greet(to name: String) {
    print("Hola \(name)")
}
greet(to: "Alberto")



// Fución con multiples parametros
print("\nFunción Con Multiples Parametros")
func personInfo(of firstName: String, secondName: String, age: Int, jobPosition: String) {
    print("La persona seleccionada es: \(firstName) \(secondName) tiene \(age) años y trabaja de \(jobPosition)")
}
personInfo(of: "Ricardo", secondName: "Fernandez", age: 30, jobPosition: "Jardinero")



// Función con retorno
print("\nFunción Con Retorno")
func greet(person: String) -> String {
    let name: String = person
    return "Hola \(name) que tal estas"
}
print(greet(person: "Yaiza"))



// Función con parametros varialbes
print("\nFunción Con Parametros Variables")
func swapTwoInts(a: inout Int, b: inout Int) -> (a: Int, b: Int) {
    let temporaryA: Int = a
    a = b
    b = temporaryA
    return (a, b)
}
var integer: Int = 33
var anotherInteger: Int = 10
print("La variable a vale: \(swapTwoInts(a: &integer, b: &anotherInteger).a), la variable b vale: \(swapTwoInts(a: &anotherInteger, b: &integer).b)")



// Fución dentro de una función
print("\nFunción Dentro De Una Función")
func firstFunction() {
    print("Soy la primera función")

    func secondFunction() {
        print("Soy la segunda función")
    }
    secondFunction()
}
firstFunction()



// Función con función en parametro
print("\nFunción Con Función En Parametro")
func addFunction(a: Int, b: Int) -> Int {
    return a + b
}
func arithmeticFunction(numA: Int, numB: Int, function: (Int, Int) -> Int) {
    print("El resultado de la operacion es: \(function(numA, numB))")
}
arithmeticFunction(numA: 2, numB: 2, function: addFunction)



// Variable local
print("\nVariable Local")
func useLocalVariable() {
    var localVariable = ""
    localVariable = "Soy una variable local"
    print(localVariable)
}
useLocalVariable()



// Variable global
print("\nVariable Global")
var globalVariable: String = ""
globalVariable = "Soy una variable global"
func useGlobalVariable(str: String) {
    print(str)
}
useGlobalVariable(str: globalVariable)



// Funciones del lenguaje
print("\nFunción Del Lenguaje")
print("Potenciacion 2^3 = \(pow(2.0, 3.0))")



// Dificultad extra
func printNumbersOrStrings(str1: String, str2: String) -> Int {
    var counter: Int = 0

    for n in 1...100 {
        if n % 5 == 0 && n % 3 == 0 {
            print(str1 + " " + str2)
            continue
        } else if n % 5 == 0 {
            print(str1)
            continue
        } else if n % 3 == 0 {
            print(str2)
        }
        print(n)
        counter += 1
    }
    return counter
}
print("\nDificultas Extra")
let howManyNumbers: Int = printNumbersOrStrings(str1: "Hola", str2: "Mundo")
print("Se han impreso: \(howManyNumbers) numeros")

