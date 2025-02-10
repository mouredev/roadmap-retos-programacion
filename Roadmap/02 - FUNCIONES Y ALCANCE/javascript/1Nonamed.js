// FUNCIONES -- FUNCTIONS
console.log("Funciones\n");
// FUNCIÓN POR DEFINICIÓN -- Function Declaration
function greet() {
  // Función sin retorno
  console.log("Hi from function declaration");
}

// FUNCIÓN POR EXPRESIÓN -- Function Expression
// Puede ser una función anónima (lambda) o tener nombre

// Función anónima (lambda)
const greeting = function () {
  // Función con retorno, en este caso, un string
  return "Hello from fn expression";
};

// Función con nombre
const sum = function sum(a, b) {
  console.log(`La suma de a + b es = ${a + b}`);
};
//

// FUNCIÓN AUTOINVOCADA - Immediately Invoked Function Expression (IIFE)

// IIFE imprimiendo en consola
(function (name) {
  console.log(`*** IIFE Saludo autoinvocado de ${name}`);
})("Daniel");

// IIFE con return y guardando su valor en una variable
const greetFromIIFE = (function (name) {
  return `Saludo autoinvocado de ${name}`;
})("Pablo");
console.log(`*** IIFE: ${greetFromIIFE}`);

// CLAUSURAS -- Closures
// Funciones dentro de otras ✅
function squares(a, b) {
  // La función interna (square) puede acceder al scope y variables de la función que la contiene (squares) pero no pasa lo contrario
  function square(x) {
    // Aquí se forma el Closure
    return x * x;
  }
  console.log(square(a) + square(b));
  return square(a) + square(b);
}

// ARROW FUNCTIONS
// Siempre son anónimas
// No tienen this
const myArrowFn = () => console.log("Log from Arrow Function");

// CALLBACKS
const myCallback = () => console.log("Log desde callback function");

const mainFunction = (cb) => cb();

// HOF -- High Order Functions
// Funciones que reciben por parámetro otra función y/o devuelven una función mediante el return.
function doubleOperationHOF(arr, operation) {
    return arr.map(operation)
}

const double = function (number) {
    return number * 2
};

const numbers = [1, 2, 3, 4, 5];
const doubledNumbers = doubleOperationHOF(numbers, double)


// EJECUCIÓN DE FUNCIONES -- Function execution
console.log('\nFunction Logs\n')
greet();
greeting(); 
sum(2, 8);
squares(2, 3);
myArrowFn();
mainFunction(myCallback);
console.log(doubledNumbers)

// VARIABLES
console.log("\nVariables\n");

let myGlobal = "Pedro";

const myFn = () => {
  let myLocal = "David";
  console.log(`** Esta es mi variable global: ${myGlobal}`);
  console.log(`** Esta es mi variable local dentro de myFn: ${myLocal}`);
};

myFn();

// RETO EXTRA
console.log("\n------ RETO EXTRA ------");

const challengeFn = (arg1, arg2) => {
  let counter = 0;
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) console.log(`${i} es ${arg1} y ${arg2}`);
    else if (i % 3 === 0) console.log(`${i} es ${arg1}`);
    else if (i % 5 === 0) console.log(`${i} es ${arg2}`);
    else {
      console.log(i);
      counter++;
    }
  }
  console.log(`\nLas veces que se imprimió un número fue de: ${counter}`);
  return counter;
};

challengeFn("multiplo de 3", "multiplo de 5");
