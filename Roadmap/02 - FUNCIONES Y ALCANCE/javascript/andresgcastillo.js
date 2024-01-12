// Function without parameters and return value
function sayHello() {
  console.log("Hello!");
}

sayHello();

// Function with parameters and return value
function addNumbers(a, b) {
  return a + b;
}

console.log(addNumbers(23, 32));

// Function within a function
function outerFunction() {
  console.log("Outer function");

  function innerFunction() {
    console.log("Inner function");
  }

  innerFunction();
}

outerFunction();

// Using built-in functions
console.log(Math.random());

// Local and global variables
function localAndGlobal() {
  var localVariable = "I am a local variable";
  globalVariable = "I am a global variable";

  console.log(localVariable);
  console.log(globalVariable);
}

localAndGlobal();
console.log(globalVariable);

// Arrow functions

// Function without parameters and return value
const sayHello2 = () => console.log("Hello!");
sayHello2();

// Function with parameters and return value
const addNumbers2 = (a, b) => a + b;
console.log(addNumbers2(23, 32));

// Function within a function
const outerFunction2 = () => {
  console.log("Outer function");

  const innerFunction2 = () => console.log("Inner function");

  innerFunction2();
};

outerFunction2();

// Local and global variables
const localAndGlobal2 = () => {
  const localVariable2 = "I am a local variable";
  globalVariable2 = "I am a global variable";

  console.log(localVariable2);
  console.log(globalVariable2);
};

localAndGlobal2();
console.log(globalVariable2);

//Dificultad Extra
function imprimirNumerosYTextos(cadena1, cadena2) {
  let contador = 0;
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(cadena1 + " " + cadena2);
    } else if (i % 3 === 0) {
      console.log(cadena1);
    } else if (i % 5 === 0) {
      console.log(cadena2);
    } else {
      console.log(i);
      contador++;
    }
  }
  return "\nCantidad de veces que se imprimio numeros: " + contador;
}

console.log(imprimirNumerosYTextos("Ludwig", "Wolfgang"));
