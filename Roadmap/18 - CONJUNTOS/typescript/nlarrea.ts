/*
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */


const data: (number | string | any[])[] = [1, 2, 3, 4, 5]

// Añadir elemento al final
data.push('end')
console.log(data)  // [ 1, 2, 3, 4, 5, 'end' ]

// Añadir elemento al principio
data.unshift('start')
console.log(data)  // [ 'start', 1, 2, 3, 4, 5, 'end' ]

// Añade varios elementos en bloque al final
data.push(['more', 'elements', 3])
console.log(data)  // [ 'start', 1, 2, 3, 4, 5, 'end', [ 'more', 'elements', 3 ] ]

// Añade varios elementos en bloque en una posición concreta
data.splice(2, 0, ['position', 2])
console.log(data)
// ['start', 1, [ 'position', 2 ], 2, 3, 4, 5, 'end', [ 'more', 'elements', 3 ]]

// Elimina un elemento en una posición concreta
data.splice(1, 1)
console.log(data)
// ['start', [ 'position', 2 ], 2, 3, 4, 5, 'end', [ 'more', 'elements', 3 ]]

// Actualiza el valor de un elemento en una posición concreta
data[1] = 1
console.log(data)  // [ 'start', 1, 2, 3, 4, 5, 'end', [ 'more', 'elements', 3 ] ]

// Comprueba si un elemento está en un conjunto
console.log(data.includes('start'))  // true
console.log(data.includes('bbb'))  // false

// Elimina todo el contenido del conjunto
data.splice(0)
console.log(data)  // []


/*
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */


const d1: number[] = [...Array(4).keys()]  // d1 = [0, 1, 2, 3]
const d2: number[] = [1, 2, 3, 4, 5, 6, 7]

const dataUnion: number[] = [...new Set([...d1, ...d2])]
console.log(dataUnion)
// [ 0, 1, 2, 3, 4, 5, 6, 7 ]

const dataIntersection: number[] = d1.filter(item => d2.includes(item))
console.log(dataIntersection)
// [ 1, 2, 3 ]

const difference12: number[] = d1.filter(item => !d2.includes(item))
console.log(difference12)
// [  0 ]
const difference21: number[] = d2.filter(item => !d1.includes(item))
console.log(difference21)
// [ 4, 5, 6, 7 ]

const symmetricDifference: number[] = [
    ...new Set([...difference12, ...difference21])
]
console.log(symmetricDifference)
// [ 0, 4, 5, 6, 7 ]