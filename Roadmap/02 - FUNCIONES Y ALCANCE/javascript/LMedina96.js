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

const a = 2
const b = 4
const arrayValues = ['Hola Mundo', 'Soy un Array', 2024]

//Funcion normal sin parametros
function saludar() {
    console.log('Funcion normal sin parametros: Hola Mundo')
}
console.log()

//Función normal con parametros
function sumarParams(a, b) {
    console.log('Funcion normal sin return: ',a + b);
}
sumarParams(a, b)
console.log()

//Funcion normal con return
function sumarReturn(a, b) {
    return a + b
}
console.log('Funcion normal con return: ', sumarReturn(a, b))
console.log()

//arrow function sin parametros
const arrowSaludo = () => {
    console.log('Function arrow sin parametros: Hola Mundo')
}
arrowSaludo()
console.log()

//Arrow function con parametros
const arrowSumarParams = (a, b) => {
    console.log('Funcion normal sin return: ',a + b);
}
arrowSumarParams(a, b)
console.log()

//Arrow function con return
const arrorSumarReturn = (a, b) => {
    return a + b
}
console.log('Funcion normal con return: ', arrorSumarReturn(a, b))
console.log()

//Función dentro de otra función
const externFunction = () => {
    const internFunction = () => {
        console.log('Esta es una función dentro de otra función')
    }
    internFunction()
}
externFunction()
console.log()

//Ejemplos de funciones ya creadas
console.log('Función length(): ', arrayValues.length)
console.log('Función toString(): ', arrayValues.toString())
console.log('Función reverse(): ', arrayValues.reverse())
console.log()

//Variables Locales y Globales
const varGlobal = 'Hola Variable Global'

const callVarGlobal = () => {
    console.log('Puedo llamar a la variable Global: ', varGlobal)
}
callVarGlobal()

const varLocal = () => {
    const varLocal = 'Hola Variable Local'
}
console.log('No puedo llamar a la variable Local: ', varLocal)
console.log()

//Dificultad Extra:

/* 
    * DIFICULTAD EXTRA (opcional):
    * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos. 
*/

const string1 = 'Soy la primer cadena'
const string2 = 'Soy la segunda cadena'

const extraDifficult = (string1, string2) => {
    let numbers = []

    for (let i = 0; i <= 100; i++) {
        i % 3 == 0 && i % 5 == 0 ? console.log(string1.concat(' ', string2)) :
        i % 3 == 0 ? console.log(string1) :
        i % 5 == 0 ? console.log(string2) :
        numbers.push(i)
    }

    return numbers
}

console.log(extraDifficult(string1, string2))