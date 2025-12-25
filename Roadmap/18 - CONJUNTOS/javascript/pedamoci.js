let conjunto = ['sada', 75654, 21, 3347, 'asd', 'adsd']

// añadiendo elemento al final del conjunto
conjunto.push('último elemento')
console.log(conjunto)

// añadiendo elemento al principio del conjunto
conjunto.splice(0,0,'primer elemento')
console.log(conjunto)

// añadiendo varios elementos en bloque al final
conjunto = conjunto.concat([['eB1', 'eB2', 'eB3']])
console.log(conjunto)

// añadiendo varios elementos en bloque en una posición concreta
conjunto.splice(3, 0, ['eB1', 'eB2', 'eB3'])
console.log(conjunto)

// eliminando un elementos en una posición concreta
conjunto.splice(5, 1)
console.log(conjunto)

// actualizando el valor de un elementos en una posición concreta
conjunto.splice(7, 1, 'ya no soy el último elemento')
console.log(conjunto)

// comprobando si un elementos esta en el conjunto
console.log(conjunto.includes(21))

// eliminando todo el contenido conjunto
conjunto.splice(0, conjunto.length)
console.log(conjunto)

// --------------------------------------- DIFICULTAD EXTRA ---------------------------------------
let arrConjunto1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let arrConjunto2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

// Unión
let union = arrConjunto1.concat(arrConjunto2)
console.log(`La unión de los dos conjuntos es ${union}`)

// intersección
let interseccion = []
arrConjunto1.forEach((e) => {if (arrConjunto2.includes(e)) interseccion.push(e)})
console.log(interseccion)

// Diferencia en arrConjunto1
let difArrConjunto1 = []
arrConjunto1.forEach((e) => {if (!arrConjunto2.includes(e)) difArrConjunto1.push(e)})
console.log(difArrConjunto1)

// Diferencia en arrConjunto2
let difArrConjunto2 = []
arrConjunto2.forEach((e) => {if (!arrConjunto1.includes(e)) difArrConjunto2.push(e)})
console.log(difArrConjunto2)

// Diferencia simétrica
let diferenciaSimetrica = []
arrConjunto1.forEach((e) => {if (!arrConjunto2.includes(e)) diferenciaSimetrica.push(e)})
arrConjunto2.forEach((e) => {if (!arrConjunto1.includes(e)) diferenciaSimetrica.push(e)})
console.log(diferenciaSimetrica)