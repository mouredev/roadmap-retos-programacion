// Definimos una función sin parámetros ni retorno
function greeting(): void {
  console.log("¡Hola, mundo!");
}

// Definimos una función con parámetros y retorno
function adition(a: number, b: number): number {
  return a + b;
}

// Definimos una función que crea funciones dentro de funciones
function createFunctionWithinFunction(): void {
  function internalFunction(): void {
    console.log("¡Función interna ejecutada!");
  }

  internalFunction(); // Llamamos a la función interna
}

// Utilizamos una función ya creada en el lenguaje
const currentDate = new Date();
console.log("Fecha actual:", currentDate);

// Probamos el concepto de variable LOCAL y GLOBAL
let globalVariable = "Soy global";

function showLocalVariable(): void {
  let localVariable = "Soy local";
  console.log(localVariable); // Mostramos la variable local
  console.log(globalVariable); // Mostramos la variable global
}

showLocalVariable();

// Dificultad extra: función con dos parámetros de tipo cadena y retorno numérico
function printNumbers(text1: string, text2: string): number {
  let counter: number = 0;
  for (let i: number = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(text1 + text2);
    } else if (i % 3 === 0) {
      console.log(text1);
    } else if (i % 5 === 0) {
      console.log(text2);
    } else {
      console.log(i);
    }
    counter++;
  }
  return counter;
}

// Probamos la función con dos cadenas y mostramos el resultado
const result = printNumbers("Fizz", "Buzz");
console.log("La función ha impreso números " + result + " veces.");
