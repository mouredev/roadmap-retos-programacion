// Función sin argumento
function helloWorld() {
  console.log("Hello world!")
}

// Función con argumento
function helloWord(word) {
  console.log(`Hello ${word}!`)
}

// Función con argumentos
function sumAll(...args) {
  let sum = 0
  for (let element of args) {
    sum += element
  }
  console.log(sum)
}

// Función recursiva
function power(base, exponent) {
  if (exponent == 0) {
    return 1;
  } else {
    return base * power(base, exponent - 1);
  }
}

// Arrow functions
const arrow = () => {
  console.log("Hello arrow function!")
}

helloWorld()
helloWord("there")
sumAll(2, 6)
power(2, 3)
arrow()

// Dificultad extra

function exercise(threeMultiplier, fiveMultiplier) {
  let counter = 0
  
  for (i = 1; i <= 100; i++) {
    let output = ""
    if(i % 3 == 0) {output += threeMultiplier}
    if(i % 5 == 0) {output += fiveMultiplier}
    if (!output) {counter++}
    console.log(output || i)
  }
  
  return counter
}

exercise("three", "five")
