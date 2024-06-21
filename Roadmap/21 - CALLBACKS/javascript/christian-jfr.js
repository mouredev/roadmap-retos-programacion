// #21 CALLBACKS
/**
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 */
function double(number, callback) {
	const result = number * 2;
	callback(`${number} x 2 = ${result}`);
}

double(5, console.log); // 5 x 2 = 10
double(7, console.log); // 7 x 2 = 14

/**
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
 */

function rng() {
	const SIMULATE_TIME_IN_MS = Math.floor(Math.random() * 10 + 1) * 1000;
	return SIMULATE_TIME_IN_MS;
}

function processOrders(dish, confirm_cb, ready_cb, deliver_cb) {
	confirm_cb(dish);
	setTimeout(() => {
		ready_cb(dish);
		setTimeout(() => {
			deliver_cb(dish);
		}, rng());
	}, rng());
}

function confirm(dish) {
	console.log(`Your ${dish} order has been confirmed.`);
}

function ready(dish) {
	console.log(`Your ${dish} order is ready.`);
}

function deliver(dish) {
	console.log(`Your ${dish} order has been delivered`);
}

processOrders('Spaghetti Carbonara', confirm, ready, deliver);
processOrders('Veggie Pizza', confirm, ready, deliver);
processOrders('Bacon Burger', confirm, ready, deliver);
