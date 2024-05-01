const letters = ['a', 'b', 'c', 'd']
console.log('Original', letters)
// Añade un elemento al final.
letters.push('e')
console.log('Añade un elemento al final', letters)

// Añade un elemento al principio.
letters.unshift('-')
console.log('Añade un elemento al principio', letters)

// Añade varios elementos en bloque al final.
const newLetters = ['x', 'y', 'z']
letters.push(...newLetters)
console.log('Añade varios elementos en bloque al final', letters)

// Añade varios elementos en bloque en una posición concreta.
const newLetters2 = ['f', 'g', 'h']
letters.splice(6, 0, ...newLetters2)
console.log('Añade varios elementos en bloque en una posición concreta', letters)

// Elimina un elemento en una posición concreta.
letters.splice(5, 1)
console.log('Elimina un elemento en una posición concreta', letters)

// Actualiza el valor de un elemento en una posición concreta.
letters[1] = '#'
console.log('Actualiza el valor de un elemento en una posición concreta', letters)

// Comprueba si un elemento está en un conjunto.
const isAinArray = letters.find(letter => letter === 'a' ? true : false)
console.log(' Comprueba si el elemento -a- está en el conjunto letters', isAinArray)
const isXinArray = letters.find(letter => letter === 'x' ? true : false)
console.log(' Comprueba si el elemento -x- está en el conjunto letters', isXinArray)

// Elimina todo el contenido del conjunto.
letters.length = 0
console.log('Elimina todo el contenido del conjunto', letters)


// DIFICULTAD EXTRA

// Union de conjuntos
const first = [1, 2, 3, 4]
const second = [3, 4, 5, 6]
const union = new Set()

first.forEach(number => union.add(number))
second.forEach(number => union.add(number))

console.log('Union', union)

// Interseccion
const interseccion = new Set()
first.forEach(n1 => {
  second.forEach(n2 => {
    if(n1 === n2){
      interseccion.add(n1)
    }
  })
})

console.log('Interseccion', interseccion)

// Diferencia
const diferencia = new Set()
first.forEach(number => diferencia.add(number))
second.forEach(number => {
  if (diferencia.has(number)){
    diferencia.delete(number)
  }
})
console.log('Diferencia', diferencia)


// Diferencia simetrica
const simetrica = new Set()
first.forEach(number => simetrica.add(number))
second.forEach(number => {
  if(simetrica.has(number)){
    simetrica.delete(number)
  }else{
    simetrica.add(number)
  }
})
console.log('Diferencia simetrica', simetrica)
