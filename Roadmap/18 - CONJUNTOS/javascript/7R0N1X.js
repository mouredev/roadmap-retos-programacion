let data = [1, 2, 3]

data.push(4)
console.log(`Añade un elemento al final: ${data}`)

data.unshift(0)
console.log(`Añade un elemento al principio: ${data}`)

data = data.concat([5, 6])
console.log(`Añade varios elementos en bloque al final: ${data}`)

data.splice(0, 0, [-1, -2])
console.log(`Añade varios elementos en bloque en una posición concreta: ${data}`)

data.splice(1, 1)
console.log(`Elimina un elemento en una posición concreta: ${data}`)

data[4] = -4
console.log(`Actualiza el valor de un elemento en una posición concreta: ${data}`)

console.log(`Comprueba si un elemento está en un conjunto: ${data.includes(0)}`)

data = []
console.log(`Elimina todo el contenido del conjunto: ${data}`)


// DIFICULTAD EXTRA
const set1 = new Set([1, 2, 3, 7, 8])
const set2 = new Set([1, 2, 3, 4, 5, 6])

console.log('---  UNIÓN ---')
console.log(set1.union(set2))

console.log('---  INTERSECCIÓN ---')
console.log(set1.intersection(set2))

console.log('---  DIFERENCIA ---')
console.log(set1.difference(set2))

console.log('---  DIFERENCIA ASIMÉTRICA ---')
console.log(set1.symmetricDifference(set2))
