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
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

// Function 
// Without parameters
function greeting () {
    console.log ('Hello Wolrd')
}

greeting ();

// With one parameter

function greetingPerson(name) {
    console.log (`Hello ${name}`)    
}

greetingPerson('Jose');

// With two parameters and return
function addition (a,b) {
    return a + b
}

console.log (addition (1,3))

// arrow funtion within a basic function, with a language function

function outer () {
    console.log ('This Basic Function is runnig')
    const inner = () => {
        console.log ("This is a nested function executed by a language function")
    }
    setTimeout(inner, 1500) // this is a language function
}

outer();

let myVarGlobal = 'This is a global variable'

function testScope () {
let myVarLocal = 'This is a local variable'
    console.log (myVarLocal)
}

testScope ();

console.log (myVarGlobal)
// console.log (myVarLocal) no se puede acceder a esta variable, porque existe solo en la funcion testScope 

// * DIFICULTAD EXTRA (opcional):
// * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
// * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
// *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
// *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
// *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
// *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.


function isMultipleOf (param1, param2){
    let counter = 0

    for (let i = 1; i <= 100; i++ ) {
        if (i % param1 === 0 && i % param2 === 0) {
            console.log (`${i} is multiple of ${param1} and ${param2}`)
        } else if (i % param1 === 0) {
            console.log (`${i} is multiple of ${param1}`) 
        } else if (i % param2 === 0){
            console.log (`${i} is multiple of ${param2}`) 
        } else {
            counter++
            console.log (i)
        }
    } console.log (`In this loop, ${counter} number not divisible between ${param1} and ${param2} were counted`)
}

isMultipleOf(3, 5); // Funciona para cualquier parametros numericos