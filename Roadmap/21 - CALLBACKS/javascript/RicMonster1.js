/*
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
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
 */

//EJERCICIO
function callbackFunction1(callback) {
	callback();
	console.log('\nSe ejecuta la primera función');
}

callbackFunction1(() => {
	console.log('\nSe ejecuta la primera callback');
});

function callbackFunction2(callback) {
	console.log('\nSe ejecuta la segunda función');
	callback();
}

callbackFunction2(() => {
	console.log('\nSe ejecuta la segunda callback');
});

//EXTRA
