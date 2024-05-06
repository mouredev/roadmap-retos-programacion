// Función sin parámetros ni retorno
function greet() {
  console.log("¡Hola!");
}

// Función con un parámetro y retorno
function squareOp(num) {
  return num * num;
}

// Función con varios parámetros y retorno
function sum(a, b) {
  return a + b;
}

// Función dentro de una función
function complexOperation() {
  function subtractionOp(a, b) {
    return a - b;
  }
  return subtractionOp(10, 5);
}

// Variable global
let globalMessage = "Hola desde la variable global";

function printGlobalMessage() {
  console.log(globalMessage);
}

// Variable local
function imprimirMensajeLocal() {
  let localMessage = "Hola desde la variable local";
  console.log(localMessage);
}

// Ejemplos de funciones ya creadas
greet();
console.log(squareOp(4));
console.log(sum(2, 3));
console.log(complexOperation());

// Probando variables global y local
console.log("Variable global:");
printGlobalMessage();

console.log("Variable local:");
imprimirMensajeLocal();

// Función con parámetros de texto y retorno de número
function printNumbersWithText(text1, text2) {
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(text1 + text2);
    } else if (i % 3 === 0) {
      console.log(text1);
    } else if (i % 5 === 0) {
      console.log(text2);
    } else {
      console.log(i);
    }
  }
  return 100; // Retorna el número de veces que se ha impreso el número
}

console.log(printNumbersWithText("Fizz", "Buzz"));
