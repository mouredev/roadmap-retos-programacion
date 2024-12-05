// Función sin parámetros ni retorno
function saludo() {
  console.log("Hola, mundo!");
}
saludo();

// Función con un parámetro
function saludar(nombre) {
  console.log("Hola, " + nombre + "!");
}
saludar("Juan");

// Función con varios parámetros
function sumar(a, b) {
  return a + b;
}
console.log(sumar(5, 3));

// Función dentro de una función
function operacion(a, b) {
  function multiplicar(x, y) {
      return x * y;
  }
  return multiplicar(a, b);
}
console.log(operacion(4, 5));

// Ejemplo de función ya creada en el lenguaje
console.log(Math.max(10, 20, 30));

// Variables LOCAL y GLOBAL
var globalVar = "Soy una variable global";

function mostrarVariables() {
  var localVar = "Soy una variable local";
  console.log(globalVar);
  console.log(localVar);
}
mostrarVariables();
// console.log(localVar); // Esto dará un error porque localVar no está definida en el ámbito global

// DIFICULTAD EXTRA
function imprimirNumeros(cadena1, cadena2) {
  let contador = 0;
  for (let i = 1; i <= 100; i++) {
      if (i % 3 === 0 && i % 5 === 0) {
          console.log(cadena1 + cadena2);
      } else if (i % 3 === 0) {
          console.log(cadena1);
      } else if (i % 5 === 0) {
          console.log(cadena2);
      } else {
          console.log(i);
          contador++;
      }
  }
  return contador;
}
console.log("Número de veces que se ha impreso el número: " + imprimirNumeros("Fizz", "Buzz"));
