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


// Funcion sin parametros:
function noParametros() {
    return 'No parametro'
}

// Con uno o varios parametros:
function dosParametros(uno, dos) {
    console.log(`${uno} y ${dos}`)
}

// Con uno o varios parametros y con retorno:
function dosParametros(uno = 1, dos = 2) {
    return (uno + dos)
}

// Funcion dentro de otra funcion:
function funcUno(param1, param2) {
    let result = 0

    function funcDos() {
        result = param1 + param2
    }

    if (param1 && param2) {
        funcDos(param1, param2)
    }

    return result
}
funcUno(1, 2)


// Funcion Flecha
const funcionFlecha = (a) => {
    return a
}

// Funciones ya creadas en el Lenguaje
let hola = 'hola como estas'

let upperCase = hola.toUpperCase()
let lowerCase = hola.toUpperCase()
let slice = hola.slice(1, 2)
let length = hola.length
let split = hola.split(' ')

// Funciones (Metodos) de Arrays en Javascript
let test = ['uno', 'dos', 'tres']
const filter = test.filter(a => {
    return a === 'dos'
})
const map = test.map(x => x === 'tres')
const forEach = test.forEach(x => { })
const find = test.find(x => x === 'tres')
const some = test.some(x => x == 'uno')
const every = test.every(x => x == 'uno')

// concepto de variable GLOBAL.
let global = 0  // <-- variable global
function increment() {
    return global++
}

// concepto de variable LOCAL.
function decrement() {
    let local = 0  // <-- vairable local
    return local
}



// Comprobacion en consola

console.log(noParametros(), '   <-- noParametros')
console.log(dosParametros(), '  <-- dosParametros')

console.log(`

    Funciones ya creadas en el lenguaje
    ${hola.toUpperCase()}   <-- toUpperCase
    ${hola.toLowerCase()}   <--toLowerCase
    ${hola.slice(1, 2)}     <-- slice
    ${hola.length}          <-- length
    ${hola.split(' ')}      <-- split
    `)

console.log(filter, '   <-- Filter')
console.log(map, '  <-- map')
console.log(find, '  <-- find')
console.log(some, '  <-- some')
console.log(every, '  <-- every')
console.log(increment() + '.. resultado:  ' + global, ' <-- VARIABLE GLOBAL')
console.log(decrement(), '      <-- VARIABLE LOCAL')



//     * DIFICULTAD EXTRA(opcional):


function difExtra(arg1, arg2) {
    let counter = 0

    for (let i = 0; i < 100; i++) {
        if (i % 5 == 0 && i % 3 == 0) {
            console.log(arg1 + 2)
        } else if (i % 3 === 0) {
            console.log(arg1)
        } else if (i % 5 == 0) {
            console.log(arg2)
        } else {
            console.log(i)
            counter++
        }
    }

    console.log('Numero de veces Numeros Impresos: ', counter)
}
// difExtra('gracias ', 'mouredev')