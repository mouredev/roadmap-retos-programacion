// 02-Javascript

/*
 * EJERCICIO:
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

// Function
function santaClaus(name) {
    let localVar = 'Kittens'
    console.log('Ho ho ho! Merry Christmas!')

    function greetings(name) {
        console.log(`Hello ${name}`)
    }
    greetings(name)
}
santaClaus('Dorothy')
// console.log(localVar) 


// Exercise

let count = 0
function printNumbers(string1, string2, i) {
    if (i % 3 == 0 && i % 5 == 0) {
        console.log(string1 + string2)
        count ++
    } else if (i % 3 == 0) {
        console.log(string1)
        count ++
    } else if (i % 5 == 0) {
        console.log(string2)
        count ++
    } else {
        console.log(i)
    }
}

for (let i = 1; i <= 100; i++) {
    printNumbers('First', 'Second', i)
}

console.log(`Amount of strings: ${count}`)



