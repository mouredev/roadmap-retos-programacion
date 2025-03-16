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


function greeting(user, callback) {
    console.log('This is the greeting process...');
    callback(user);
}


function greetUser(user) {
    console.log(`Welcome ${user}!`);
}


greeting('nlarrea', greetUser);


/*
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


function orderProcess(
    dish, confirmCallback, readyCallback, deliveredCallback
) {
    const randTime = (min, max = 0) => {
        [min, max] = [Math.min(min, max), Math.max(min, max)];
        return Math.floor(Math.random() * (max - min) + min) * 1000;
    };

    setTimeout(() => {
        confirmCallback(dish);
        
        setTimeout(() => {
            readyCallback(dish);

            setTimeout(() => {
                deliveredCallback(dish);
            }, randTime(1, 5));
        }, randTime(1, 5));
    }, randTime(1, 5));
}


function orderConfirmation(dish) {
    console.log(`The order '${dish}' is confirmed.`);
}


function orderReady(dish) {
    console.log(`The order '${dish}' is ready.`);
}


function orderDelivered(dish) {
    console.log(`The order '${dish}' has been delivered.`);
}


orderProcess(
    'Tonkotsu Ramen', orderConfirmation, orderReady, orderDelivered
);