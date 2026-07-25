/*
  * EJERCICIO:
  * Explora el concepto de "decorador" y muestra cómo crearlo
  * con un ejemplo genérico.
*/

function withprintResult(func) {
  return function (...parameters) {
    console.log("Parámetros:", parameters)
    const result = func(...parameters)
    console.log("Resultado:", result)
    return result
  }
}

function sum(a, b) {
  return a + b
}

function multiply(a, b) {
  return a * b
}

const sumDecorator = withprintResult(sum)
const multiplyDecorator = withprintResult(multiply)

sumDecorator(2, 1)
multiplyDecorator(2, 3)

/*
  * DIFICULTAD EXTRA (opcional):
  * Crea un decorador que sea capaz de contabilizar cuántas veces
  * se ha llamado a una función y aplícalo a una función de tu elección.
*/

function counterDecorator(func) {
  let counter = 0;
  return function (...parameters) {
    counter++;
    console.log(`La función ha sido llamada ${counter} veces`)
    return func(...parameters)
  };
}

function firstFunction() {
  console.log("Función ejecutada")
}

const decoratedFunction = counterDecorator(firstFunction)

decoratedFunction()
decoratedFunction()
decoratedFunction()
