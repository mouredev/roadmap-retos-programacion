/*
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
*/

function time(nameTime, duration) {
  return new Promise((resolve) => {
    const startTime = new Date().toLocaleTimeString();
    console.log(`Function Name: ${nameTime}`);
    console.log(`Start Time: ${startTime}`);
    console.log(`Duration: ${duration / 1000} seconds`);
    setTimeout(() => {
      const endTime = new Date().toLocaleTimeString();
      console.log(`${nameTime} End Time: ${endTime}`);
      resolve();
    }, duration);
  });
}

/*
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

async function main() {
  const c = time('C', 3000);
  const b = time('B', 2000);
  const a = time('A', 1000);

  await Promise.all([c, b, a]);
  await time('D', 1000);
}

main();
