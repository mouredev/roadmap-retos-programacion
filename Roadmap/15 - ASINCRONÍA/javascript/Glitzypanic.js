/*
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han
 *   finalizado.
 */

// const cafeFiltrado = async (nombre, segundos) => {
//   console.log(`Metodo de filtrado: ${nombre}`);
//   console.log(`Duración: ${segundos} segundos`);

//   const inicio = new Date();

//   await new Promise((resolve) => setTimeout(resolve, segundos * 1000));

//   const termino = new Date();

//   console.log(`Cafe listo con el metodo: ${nombre}`);
//   console.log(`Tiempo transcurrido: ${(termino - inicio) / 1000} segundos`);
// };

// cafeFiltrado("v60", 5);

// Ejercicio extra

const funcionC = async (nombre, segundos) => {
  console.log(`Nombre: ${nombre}`);
  console.log(`Duración: ${segundos}`);

  await new Promise((resolve) => setTimeout(resolve, segundos * 1000));

  console.log(`Terminado en: ${segundos}s`);
};

funcionC("Cafe", 3);

const funcionB = async (nombre, segundos) => {
  console.log(`Nombre: ${nombre}`);
  console.log(`Duración: ${segundos}`);

  await new Promise((resolve) => setTimeout(resolve, segundos * 1000));

  console.log(`Terminado en: ${segundos}s`);
};

funcionB("Pastel", 2);

const funcionA = async (nombre, segundos) => {
  console.log(`Nombre: ${nombre}`);
  console.log(`Duración: ${segundos}`);

  await new Promise((resolve) => setTimeout(resolve, segundos * 1000));

  console.log(`Terminado en: ${segundos}s`);
};

funcionA("Pan", 1);

const funcionD = async (nombre, segundos) => {
  console.log(`Nombre: ${nombre}`);
  console.log(`Duración: ${segundos}`);

  await new Promise((resolve) => setTimeout(resolve, segundos * 1000));

  console.log(`Terminado en: ${segundos}s`);
};

funcionD("mantequilla", 1);

const cafeteria = async () => {
  await Promise.all([funcionC(), funcionB(), funcionA()]);

  await funcionD();
};
