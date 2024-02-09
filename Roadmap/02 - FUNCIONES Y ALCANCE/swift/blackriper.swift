/*
  Convenciones del lenguaje Swift
1. Nombres:

Los nombres de variables, constantes, funciones, tipos y métodos deben ser descriptivos y en minúscula.
Se pueden usar guiones bajos para separar palabras en nombres compuestos.
Los nombres de tipo deben comenzar con una letra mayúscula.
Las constantes deben tener un nombre en mayúscula con guiones bajos.
2. Sangrías:

Se debe usar una sangría de 4 espacios para las indentaciones.
Las llaves de apertura y cierre deben estar en la misma línea que la instrucción que controlan.
3. Espacios en blanco:

Se debe usar un espacio después de las comas, puntos y comas.
Se debe usar un espacio antes y después de los operadores.
4. Comentarios:

Los comentarios se pueden agregar usando // para comentarios de una sola línea o /* ... */ para comentarios de varias líneas.
5. Enumeraciones:

Los casos de enumeración deben estar en minúscula y separados por comas.
El último caso de enumeración no debe tener una coma al final.
6. Funciones:

Los argumentos de las funciones deben estar en minúscula y separados por comas.
El tipo de retorno de la función debe estar antes del nombre de la función.
7. Clases:

Los nombres de las clases deben comenzar con una letra mayúscula.
Las propiedades y métodos de las clases deben ser públicos o privados.
8. Protocolos:

Los nombres de los protocolos deben comenzar con una letra mayúscula.
Los métodos de los protocolos deben ser públicos.
9. Extensiones:

Las extensiones se pueden usar para agregar métodos a tipos existentes.
El nombre de la extensión debe comenzar con un guión bajo.
10. Importaciones:

Se deben usar importaciones para acceder a los tipos y funciones de otros módulos.
Se debe usar la importación import para importar módulos completos.
Se debe usar la importación import . para importar miembros específicos de un módulo.
*/

// ejemplos de funciones 

//sin parametros y sin retorno
func helloWorld() {
    print("Hello, World!")
}

// con parametros y con retorno
func sum(a: Int, b: Int) -> Int {
    return a + b
}

print("La suma de 5 + 3 es \(sum(a: 5, b: 3))")


// retorno multiple como una tupla 
func rest(a: Int, b: Int) -> (resta: Int, multiplicacion: Int) {
    let resta = a - b
    let multiplicacion = a * b
    return (resta, multiplicacion)
}

let results=rest(a: 4, b: 5)
print("La resta de 4 - 5 es \(results.resta) y la multiplicación es \(results.multiplicacion)")

// cuando solo se va retornar un valor se puede hacer sin la palabra return 
func suma2(a: Int, b: Int) -> Int {
    a + b
}
print("La suma de 5 + 3 es \(suma2(a: 5, b: 3))")

// funcion con argumental label 
func greeting(person: String , from hometown: String) {
    print("Hello \(person)! Glad you could visit from \(hometown).")
}
greeting(person: "Diego", from: "Madrid")

// funcion con argumental label y sin argumental label
func greet(_ person: String, from hometown: String) {
    print("Hello \(person)! Glad you could visit from \(hometown).")
}
greet("Diego", from: "Madrid")

// funcion con parametros con valor por defecto
func greet2(_ person: String, from hometown: String = "Madrid") {
    print("Hello \(person)! Glad you could visit from \(hometown).")
}
greet2("Diego")

// funcion con parametros sin especificar el numero del mismo
func showNumbers(_ numbers: Int...) {
    for number in numbers {
        print(number)
    }
}
showNumbers(1, 2, 3, 4, 5)

// funcion dentro de otra funcion
func chooseStepFunction(backward: Bool) -> (Int) -> Int {
    func stepForward(input: Int) -> Int { return input + 1 }
    func stepBackward(input: Int) -> Int { return input - 1 }
    return backward ? stepBackward : stepForward
}
var currentValue = -4
let moveNearerToZero = chooseStepFunction(backward: currentValue > 0)
// moveNearerToZero now refers to the nested stepForward() function
while currentValue != 0 {
    print("\(currentValue)... ")
    currentValue = moveNearerToZero(currentValue)
}
print("zero!")


// ejercicio extra 
func printerNumbers(text1:String,text2:String)->Int{
    var numRep=0
    for num in 1...100{
        if num % 5 == 0 && num % 3 == 0{
            print("\(text1) \(text2)")
        }else if num % 5 == 0{
            print("\(text2)")
        }else if num % 3 == 0{
            print("\(text1)")
            
        }else{
            numRep+=1
        }
        
    }
    return numRep
}

let num=printerNumbers(text1: "Hulk", text2: "aplasta!!")
print("\(num) es el total de numeros que se imprimen")