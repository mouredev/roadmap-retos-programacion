// Value assignment
let value = 'Hello'


let number = 1

function valueFunction (number) {
    number = 2
    return number
}

// console.log(valueFunction(number))


// Reference Assignment
let letter = 'a'


let array = ['a', 'e']

function referenceFunction (array) {
    array.push('hello')
    return array
}

// console.log(referenceFunction(array))


/* - Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
   - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.

   - Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
          se asigna a dos variables diferentes a las originales. 
   - Imprime el valor de las variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
   - Comprueba también que se ha conservado el valor original en las primeras.
*/

let aux = ''

function valueProgram (value, number) {
    aux = value
    value = number
    number = aux
    return[`New value: ${value}, New number: ${number}`]
}

function referenceProgram (letter, array) {
    aux = letter
    letter = array
    array = aux
    return [`New letter: ${letter}, New array: ${array}`]
}

console.log(valueProgram(value, number))
console.log(`Original value: ${value}`)
console.log(`Original number: ${number}`)

console.log(referenceProgram(letter, array))
console.log(`Original letter: ${letter}`)
console.log(`Original array: ${array}`)

