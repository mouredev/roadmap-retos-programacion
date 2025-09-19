console.clear()

/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

const myName = "Jesus" // Asignación de constante
let myNum = 5 // Asignación de variable tipo number y valor 5
let myStringNum = "5" // Asignación de variable tipo string y valor 5
console.log(myName == "Jesus") 
console.log(myNum == myStringNum) // Compara valores
console.log(myNum === myStringNum) // Compara valores y tipos

//Asignación de mismo valor para 3 variables con let
let one = two = three = 1 
// de esta manera 1 se asigna a three, three se asigna a two y two se asigna a one en ese orden

console.log(one, two, three, four) //four no está inicializada aun pero al declararse con var posteriormente devuelve undefined
//let two = 2, esto me da error porque no puedo reasignar otro valor a las variables asignadas en bloque con let 
// volviéndola a declarar como let

//Asignación de mismo valor para 3 variables de manera individual en una línea con var
var four = 4, five = 4, six = 4 
console.log(four, five, six)

// Reasignación de todas las variables y asignación de nuevas (seven, eight, nine) en una sola línea, todas se asignan como let
zero = 0, two = 2, three = 3, five = 5, six = 6, seven = 7, eight = 8, nine = 9 

// Asignación de variables let con valores diferentes por desectructuración
let [ten, eleven, twelve] = [10, 11, 12]

console.log(zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve)

if (four + one == myNum){ // condicional en base a una operación con variables de tipo number
    console.log(`El resultado es ${five}`)
}

let myNumbers = [zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve]

console.log(typeof(myNumbers)) // JS interpreta un array como un tipo object

let printBuilder = ''
for (num of myNumbers){ // For each que recorre cada elemento del array
    printBuilder += num + ' ' //concatenación con un espacio para formar el string
}
console.log(printBuilder) // para hacer una impresión sin saltos de línea se puede "construir" un string

try{
    console.log(twelve / two) // La operación es correcta e imprime el resultado
    console.log(twelve / zero) // La operación es incorrecta por división entre 0 pero imprime Infinity
    console.log("twelve" / "zero") // La operación es incorrecta al intentar dividir entre 2 strings pero imprime NaN
    console.log(thirteen * fourteen) //En este caso al intentar operar con 2 variables no declaradas la ejecución se va al catch
}catch{
    console.error("Error de operación") 
}

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */

printBuilder = ''
for (let i = 10; i < 56; i++){
    if (i % 3 == 0 ||i % 2 != 0 || i == 16){ // For por índices
        continue
    }
    printBuilder += i + ' '
    
}
console.log(printBuilder.trim() + "\n")
