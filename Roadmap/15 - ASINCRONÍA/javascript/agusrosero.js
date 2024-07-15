/*
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 */

const asyncFunction = async (name, seconds) => {
  console.log(`Inicio de la ejecucion ${name}`);
  console.log(`Duracion de ${name}: ${seconds} segundos..`);

  await new Promise((res) => {
    setTimeout(res, seconds * 1000);
  });

  console.log(`Fin de la ejecucion: ${name}`);
};

const main = async () => {
  const promise1 = asyncFunction("Funcion 1", 2);

  await Promise.all([promise1]);
};

// main();

/* DIFICULTAD EXTRA (opcional):
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
const funcionC = async () => {
  await setTimeout(() => {
    console.log("función C");
  }, 3000);
};

const funcionB = async () => {
  await setTimeout(() => {
    console.log("función B");
  }, 2000);
};

const funcionA = async () => {
  await setTimeout(() => {
    console.log("función A");
  }, 1000);
};

const funcionD = async () => {
  await setTimeout(() => {
    console.log("función D");
  }, 1000);
};

const main2 = async () => {
  const res1 = funcionC();
  const res2 = funcionB();
  const res3 = funcionA();

  await Promise.all([res1, res2, res3]);

  const res4 = await funcionD();
};

main2;
