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
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
 */

const miFunc = async (time, nombre) => {
  console.log("Soy la función ", nombre);

  await new Promise((resolve) =>
    setTimeout(() => {
      console.log(`Me he ejecutado después de ${time} segundos`);
      console.log(`Ejecución finalizada`);
      resolve();
    }, time * 1000)
  );
};

const ejecucionParalela = async () => {

    await miFunc(3, "C");
    await miFunc(2, "B");
    await miFunc(1, "A");
    miFunc(1, "D");
};

ejecucionParalela();