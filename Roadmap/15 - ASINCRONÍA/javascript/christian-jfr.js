// #15 ASINCRONÍA

/**
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 */

async function asyncTask(name, seconds) {
	console.log(
		`starting ${name}, at: ${new Date().toLocaleTimeString()}, duration: ${seconds} seconds`
	);

	await new Promise((resolve) => {
		setTimeout(() => {
			let end = `finished ${name}, at: ${new Date().toLocaleTimeString()}`;
			resolve(end);
			console.log(end);
		}, seconds * 1000);
	});
}

asyncTask('test-1', 5);

/**
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

async function extra() {
	await Promise.all([asyncTask('C', 3), asyncTask('B', 2), asyncTask('A', 1)]);
	await asyncTask('D', 1);
}

extra();
