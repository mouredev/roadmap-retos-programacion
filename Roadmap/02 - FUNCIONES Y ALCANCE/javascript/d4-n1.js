// Función sin argumento
function helloWorld() {
  console.log("Hello world!")
}

// Función con argumento
function helloWord(word) {
  console.log(`hello ${word}!`)
}

// Función con argumentos
const sumAll = function(...args) {
  for (let i = 0; i < args.length; i++ ) {
    let x = 0
    x += args.value
    return x
  }
}

// Función recursiva

// Arrow functions

helloWorld()
helloWord("there")
sum(2, 3)