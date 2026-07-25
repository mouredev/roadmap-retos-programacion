/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#24 DECORADORES
---------------------------------------
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
*/
// ________________________________________________________
function myDecorator(func) {
    return function (...args) {
      console.log("\nAntes de que se llame a la función.");
      func(...args);
      console.log("Después de llamarla.");
    };
  }
  
  function sayHello(firstName, lastName) {
    console.log(`Hola, ${firstName} ${lastName}!`);
  }
  
  const decoratedSayHello = myDecorator(sayHello);
  decoratedSayHello("Zoe", "Roy");
  
  console.log("\n______________________");
  function classDecorator(Class) {
    return class extends Class {
      greet() {
        console.log("\nAntes de llamar al método");
        super.greet();
        console.log("Después de llamar al método");
      }
    };
  }
  
  // ________________________________________________________
  console.log("DIFICULTAD EXTRA");
  
  function countCalls(func) {
    const wrapper = function (...args) {
      wrapper.calls++;
      func(...args);
      console.log(`Ha sido llamada ${wrapper.calls} veces.`);
    };
    wrapper.calls = 0;
    return wrapper;
  }
  
  const functionA = countCalls(function (funcName) {
    console.log(`\nLa función '${funcName}':`);
  });
  
  const functionB = countCalls(function (funcName, example) {
    console.log(`\nLa función ${funcName} - ${example}:`);
  });
  
  functionA("A");
  functionA("A");
  functionA("A");
  
  functionB("B", "args");
  functionB("B", "args");
  