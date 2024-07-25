// Ejecicio

// El decorador es una función que modifica la funcionalidad de otra función sin alterar su código.
// Un decorador implementa una función 'print_call()' que ejecute la lógica.

function decorator(func) {
  function print_call() {
    console.log(`La función ${func.name} ha sido llamada.`)
    return func;
  }
  return print_call();
}

function example() {
}
function example_2() {
}
function example_3() {
}

decorator(example)
decorator(example_2)
decorator(example_3)

// Extra

/* Aun JS no soporta decoradores, el código funciona con Typescript */

function Log(target, {kind, name}) {
  function counter_function(...args) {
    counter_function.call_count += 1
    console.log(`inside ${name}, ${kind} log, se ha llamado ${counter_function.call_count} vez/veces`)
    return target(args)
  }
  counter_function.call_count = 0
  return counter_function
}

class MyClass {

  @Log
  mymethod(arg) {
    console.log('arg', arg)
  }
  @Log
  othermethod() {
    console.log('Hola España');
  }
}

let x

x = new MyClass()
x.mymethod(true)
x.mymethod(false)
x.mymethod(44)
x.othermethod()
x.mymethod('Ángel')
x.othermethod()