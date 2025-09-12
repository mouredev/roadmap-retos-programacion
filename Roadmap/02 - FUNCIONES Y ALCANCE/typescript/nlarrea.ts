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


// BASIC FUNCTIONS

function noParamsNoReturn() {
    console.log('Hello there!')
}

noParamsNoReturn() // Hello there


function paramsNoReturn(name: string) {
    console.log(`Hello, ${name}`)
}

paramsNoReturn('Naia')  // Hello, Naia


function paramsReturn(name: string, surname: string): string {
    return `${name} ${surname}`
}

console.log(paramsReturn('John', 'Smith'))  // John Smith


// FUNCTIONS INSIDE FUNCTIONS

function printFullName(name: string, surname: string): void {
    function getFullName() {
        return `${name} ${surname}`
    }

    console.log(getFullName())
}

printFullName('John', 'Smith')  // John Smith


// BUILTIN FUNCTIONS

console.log(typeof parseInt('101'))  // number


// LOCAL AND GLOBAL VARIABLES

// Global variables
var counter: number = 0

function globalVariables() {
    counter++
    console.log(counter)  // 1
    counter++
}

globalVariables()
console.log(counter)  // 2

// Local variables

function localCounter() {
    let counterTwo: number = 0
    counterTwo++
    console.log(counterTwo)
}

localCounter()  // 1
// console.log(counterTwo)  // Error: Cannot find name 'counterTwo'


/*
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 */

function printNumbers(textOne: string, textTwo: string): number {
    let counter: number = 0;

    for (let num: number = 1; num <= 100; num++) {
        if (num % 3 === 0 && num % 5 === 0) {
            console.log(`${textOne}${textTwo}`);
        } else if (num % 3 === 0) {
            console.log(textOne);
        } else if (num % 5 === 0) {
            console.log(textTwo);
        } else {
            console.log(num);
            counter++;
        }
    }

    return counter;
}

console.log(printNumbers('fizz', 'buzz'));  // 53