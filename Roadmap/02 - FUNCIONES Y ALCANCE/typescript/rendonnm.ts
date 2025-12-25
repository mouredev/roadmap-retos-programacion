// Función declarada
// Se hoistea
function greet() {
  console.log('Hello world')
}

// Función expresada
// No se hoistea
const greet2 = function () {
  console.log('Hello world')
}

// Arrow function
// No tiene this, común en callbacks
const greetArrow = () => {
  console.log('Hello world')
}

// Con argumentos/parámetros y return
const greetName = (name: string = 'Friend') => {
  return `Hello ${name}`
}

console.log(greetName('Santiago'))

// Múltiples parámetros, se recomienda utilizar objetos
const personalizedGreet = ({ greet, name }: { greet: string, name: string }) => {
  return `${greet} ${name}!`
}

personalizedGreet({ name: 'Santi', greet: 'Oe' })

// Funciones de orden súperior
// Funciones que reciben una una función cómo callback o retornan una función
const runOnce = (fn: () => void) => {
  return () => {
    // Hacer algo...
    fn()
  }
}

// Variables locales y globales
let usuario = "Santi" // variable global

function saludar() {
  let saludo = `Hola, ${usuario}` // variable local
  console.log(saludo)
}

saludar()
console.log(usuario) // ✅ Santi

// console.log(saludo) ❌ Error: 'saludo' is not defined

// Closures 
const createCounter = () => {
  let counter = 0
  return () => {
    console.log(`Aumentamos contador: ${++counter}`)
  }
}

const counter = createCounter()
counter()
counter()
counter()

/* DIFICULTAD EXTRA (opcional):
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

const newF = (a: string, b: string): number => {
  let counter = 0
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(`${a}${b}`)
    } else if (i % 3 === 0) {
      console.log(a)
    } else if (i % 5 === 0) {
      console.log(b)
    } else {
      console.log(i)
      counter++
    }
  }
  return counter
}