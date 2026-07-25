/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#21 CALLBACKS
---------------------------------------
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
*/
// ________________________________________________________
function sumNumbers(a, b, callback) {
    if (typeof a === "number" && typeof b === "number") {
      const result = a + b;
      callback(`${a} + ${b}`, result);
    }
  }
  
  function myCallback(summands, result) {
    if (typeof summands === "string" && typeof result === "number") {
      console.log(`La suma de ${summands} es: ${result}`);
    }
  }
  
  sumNumbers(6, 6, myCallback);
  sumNumbers(5, 2, myCallback);
  
  // ________________________________________________________
  console.log("\nDIFICULTAD EXTRA");
  
  function timeRandom() {
    return Math.floor(Math.random() * 10) + 1;
  }
  
  function confirmOrder(name) {
    return new Promise((resolve) => {
      const time = timeRandom();
      console.log(`* Confirmando ${name}, espere ${time} segundos.`);
      setTimeout(() => {
        console.log(`- '${name}', ha sido confirmado.\n`);
        resolve();
      }, time * 1000);
    });
  }
  
  function prepareOrder(name) {
    return new Promise((resolve) => {
      const time = timeRandom();
      console.log(`* Preparando ${name}, espere ${time} segundos.`);
      setTimeout(() => {
        console.log(`- '${name}', está listo.\n`);
        resolve();
      }, time * 1000);
    });
  }
  
  function servingOrder(name) {
    return new Promise((resolve) => {
      const time = timeRandom();
      console.log(`* Sirviendo ${name}, espere ${time} segundos.`);
      setTimeout(() => {
        console.log(`- '${name}', ha sido entregado.\n`);
        resolve();
      }, time * 1000);
    });
  }
  
  async function processOrder(name) {
    console.log(`-----\n* Procesando: '${name}' \n-----\n`);
    await confirmOrder(name);
    await prepareOrder(name);
    await servingOrder(name);
  }
  
  async function ordersList() {
    await processOrder("Baleadas");
    await processOrder("Tamales");
    await processOrder("Enchiladas");
  }
  
  ordersList();
  