import Foundation

// RETO #02 FUNCIONES Y ALCANCE

// Función sin parámetros
print("\nEsto es una función sin parámetros: ")

func helloWorld() {
    print("Hello, World!")
}

helloWorld()

// Función con un parámetro
print("\nEsto es una función con un parámetro: ")

func squared(num:Int){
    let squareNum = num * num

    print(squareNum)
}

squared(num: 5)

// Función con múltiples parámetros y valor de retorno
print("\nEsto es una función con múltiples parámetros y valor de retorno: ")

func cube(num: Int) -> Int {
    return num * num * num
}

let resultCube = cube(num:5)
print("El resultado de cube³ es: \(resultCube)")

// Función dentro de función
print("\nEsto es una función dentro de una función: ")

func myFirstFunc(){
    print("Un gran poder, conlleva")

    func mySecondFunc(){
        print("una gran responsabilidad")
    }
    mySecondFunc()
}
myFirstFunc()

// Variable local
print("\nVariables locales")

func localVarFunc() {
    var localVar = 15

    print("El valor de la variable local es: \(localVar)") 
}
localVarFunc()

// Variable global
print("\nVariables globales")

var globalVar: Int = 150
func globalVarFunc(integer: Int) {
    print(integer)

}
globalVarFunc(integer: globalVar)


/* DIFICULTAD EXTRA:
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/

func printNum(str1: String, str2: String) -> Int {
    var counter = 0
    for i in 1...100 {
        if i % 3 == 0 && i % 5 == 0 {
            print("\(str1)\(str2)")
            counter += 1
        } else if i % 3 == 0 {
            print("\(str1)")
            counter += 1
        } else if i % 5 == 0 {
            print("\(str2)")
            counter += 1
        } else {
            print(i)
        }
    }
    return counter
}

let printedNum = printNum(str1: "Hello", str2: "World!")
print("\(printedNum) times has been printed")

