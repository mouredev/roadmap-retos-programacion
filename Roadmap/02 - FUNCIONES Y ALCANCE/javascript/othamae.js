/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */


// FUNCTIONS:
// 1. Function without parameters and return
function helloWord(){
    console.log("Hello World!")
}

helloWord()

// 2. Function with parameter and return

function helloName(name){
    return `Hello ${name}!`
}

console.log(helloName('Moure'))

// 3. Function with more parameters and return

function helloNameAndLanguage(name, language){
    return `Hello ${name} from ${language}!`
}

console.log(helloNameAndLanguage('Moure', 'JavaScript'))

// 4. Arrow functions
// without parameters and return
const sayHello = () => console.log('Hello World from an arrow function!')
sayHello()

// with parameters and return
const sayHelloWithReturn = (name) => `Hello ${name} from an arrow function!`

console.log(sayHelloWithReturn('Moure'))

// 5. Nested functions
function helloNameFromNestedFunction(name){
    return function nested(type){
        return `Hello ${name} from a ${type} function!`    
    }
}

console.log(helloNameFromNestedFunction('Moure')('nested'))

// 6. Arrow functions in nested functions
function helloNameFromArrowInNestedFunction(name){
    return (type)=>`Hello ${name} from an arrow function in a ${type} function!`      
}

console.log(helloNameFromArrowInNestedFunction('Moure')('nested'))

// 7. Built-in functions examples
const string= '60' 
const n = parseInt(string) // To parse a string in Number
console.log(`Type of ${n} is: ${typeof parseInt(string)}`)

// 8. Global and local variables

const globalVariable = 'I am a global variable'

function localAndGlobal(){
    const localVariable = 'I am a local variable'
    console.log(globalVariable)
    console.log(localVariable)
}

localAndGlobal() 

try {
    console.log(localVariable)     
} catch (error) {
    console.log('Error: ' + error)
}


// EXTRA TASK:
function printFrom1to100(param1, param2){
    let counter = 0
    for(let i = 1; i<=100; i++){
        if (i%3==0 && i%5==0) console.log(param1 + param2)            
        else if (i%3==0) console.log(param1)           
        else if (i%5==0) console.log(param2)          
        else {
            console.log(i)
            counter++
        }
    }
    return counter
}
const counter = printFrom1to100('Fizz', 'Buzz')
console.log({counter})