// Ejercicio #18 - Conjuntos

function mostrarConjunto(set) {
    const ordenar = [...set].sort((a, b) => a - b)
    return `{${ordenar.join(',')}}`
}

function mostrar(set) {
    return `{${[...set].join(',')}}`
}

const conjunto = new Set([1, 2, 3, 4, 5, 6])
const conjunto2 = new Set([1, 2, 4, 5, 6, 8, 10])

console.log('A = ', mostrar(conjunto))
console.log('B = ', mostrar(conjunto2))
console.log('')

// Añadir valores a los conjuntos
conjunto.add(7)
console.log('Añadido el número 7 al conjunto A')
conjunto2.add(12)
console.log('Añadido el número 12 al conjunto B')
console.log('A = ', mostrar(conjunto))
console.log('B = ', mostrar(conjunto2))
console.log('')

// Añadir un elemento al final del conjunto A
console.log('Añadiendo el número 8 al final del conjunto A')
conjunto.add(8)
console.log(`A = ${mostrar(conjunto)}`)
console.log('')

// Eliminar un valor
conjunto2.delete(12)
console.log('Eliminado el número 12 del conjunto B')
console.log('')

console.log('El número 7 existe en el conjunto A: ', conjunto.has(7))
console.log('El número 12 existe en el conjunto B: ', conjunto2.has(12))
console.log('')

console.log('El conjunto A tiene: ', conjunto.size, 'elementos')
console.log('El conjunto B tiene: ', conjunto2.size, 'elementos')
console.log('')

console.log('Eliminado todo el contenido del conjunto A')
conjunto.clear()
console.log('')

console.log('El conjunto A tiene: ', conjunto.size, 'elementos')
console.log('El conjunto B tiene: ', conjunto2.size, 'elementos')
console.log('')

console.log('Añadiendo números al conjunto A')
conjunto.add(1)
conjunto.add(3)
conjunto.add(5)
conjunto.add(7)
conjunto.add(9)
console.log('')

console.log('Conjunto A = ', mostrarConjunto(conjunto))
console.log('Conjunto B = ', mostrarConjunto(conjunto2))
console.log('')

console.log('Unión de Conjuntos')
console.log('A ∪ B = ', mostrarConjunto(conjunto.union(conjunto2)))
console.log('')

console.log('Intersección de Conjuntos')
console.log('A ∩ B = ', mostrarConjunto(conjunto.intersection(conjunto2)))
console.log('')

console.log('Diferencia de Conjuntos')
console.log('𝐴 ∖ 𝐵 = ', mostrarConjunto(conjunto.difference(conjunto2)))
console.log('B ∖ A = ', mostrarConjunto(conjunto2.difference(conjunto)))
console.log('')

console.log('Diferencia simétrica de Conjuntos')
console.log('(𝐴∖𝐵) ∪ (𝐵∖𝐴) =', mostrarConjunto(conjunto.symmetricDifference(conjunto2)))
console.log('')
