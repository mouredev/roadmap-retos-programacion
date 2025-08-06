// Aritméticos 
// Suma
console.log(`Suma 1 + 2 = ${1 + 2}`) // 3
console.log(`Resta 1 - 2 = ${1 - 2}`) // -1
console.log(`Multiplicación 27 * 3 = ${27 * 3}`) // 81
console.log(`División 3 / 4 = ${3 / 4}`) // 0.75
console.log(`Residuo 10 % 2 = ${10 % 2}`) // 0
console.log(`Exponencial 10 ** 3 = ${10 ** 3}`) // 1000

// Comparación
console.log(`Igualdad: 10 === 3: ${10 === 3}`) // false
console.log(`Diferentes: 10 !== 3: ${10 !== 3}`) // true
console.log(`Mayor que: 10 > 3: ${10 > 3}`) // true
console.log(`Mayor o igual que: 10 > 3: ${10 >= 3}`) //true
console.log(`Menor que: 10 < 3: ${10 < 3}`) // false
console.log(`Menor o igual que: 10 < 3: ${10 <= 3}`) // false

// Lógicos
console.log(`AND (&&): false && true =  ${false && true}`) // false
console.log(`OR (||): false || true = ${false || true}`) // true
console.log(`NULLISH (??): null && 'This is a default value' = ${undefined ?? 'This is a default value'}`) // This is a default value
console.log(`NOT (!): !false = ${!false}`) // true

// Operadores de asignación
let a = 5
console.log(`Asignación simple (=): a = 5 → a = ${a}`) // 5
console.log(`Suma y asigna (+=): a += 3 → a = ${a += 3}`) // 8
console.log(`Resta y asigna (-=): a -= 2 → a = ${a -= 2}`) // 6
console.log(`Multiplica y asigna (*=): a *= 4 → a = ${a *= 4}`) // 24
console.log(`Divide y asigna (/=): a /= 6 → a = ${a /= 6}`) // 4
console.log(`Módulo y asigna (%=): a %= 3 → a = ${a %= 3}`) // 1
console.log(`Exponente y asigna (**=): a **= 4 → a = ${a **= 4}`) // 1

// Operadores de pertenencia
const persona = { nombre: 'Santi', edad: 25 }
console.log(`'nombre' in persona: ${'nombre' in persona}`) // true
console.log(`'apellido' in persona: ${'apellido' in persona}`) // false

console.log(``)

class Animal {
  name: string
  constructor(name: string) {
    this.name = name
  }
}
class Cat extends Animal {
  color: string
  constructor(name: string, color: string) {
    super(name)
    this.color = color
  }
}
const morgan = new Cat('Morgan', 'white')
console.log(`Morgan es intancia de Animal? ${morgan instanceof Animal}`) // true

// Estructuras de control
// Condicionales
const newName = 'rendonnm'
if (newName === 'rendonnm') {
  console.log('Nice name')
} else if (newName === 'another name') {
  console.log('ok ok')
} else {
  console.log('MMMM')
}

// Iterativas
for (let i = 1; i < 11; i++) {
  console.log(`Iterando: Número ${i}`)
}

let iterator = 0
while (iterator < 11) {
  console.log(`Iterando while: Número ${iterator}`)
  iterator++
}

// Manejo de excepciones
try {
  // Intentar hacer algo...
} catch (err) {
  console.error(`Ha ocurrido un error ${err}`)
}

// DIFICULTAD EXTRA (opcional)
// Crea un programa que imprima por consola todos los números comprendidos
// entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3

for (let i = 10; i < 56; i++) {
  if (i % 2 !== 0 || i === 16 || i % 3 === 0) continue
  console.log(i)
}