/*Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 */

function doSomethingAsyn (callback) {
    console.log("Inicio de la operación asíncrona...")
    setTimeout(() => {
        console.log("Operación asíncrona completada.");
        callback();
    }, 2000);
}

function complete () {
    console.log("Callback ejecutado: Operació finalizada.");
}

doSomethingAsyn(complete);

/*EXTRA
Crea un simulador de pedidos de un restaurante utilizando callbacks.
* Estará formado por una función que procesa pedidos.
* Debe aceptar el nombre del plato, una callback de confirmación, una
* de listo y otra de entrega.
* - Debe imprimir un confirmación cuando empiece el procesamiento.
* - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
*   procesos.
* - Debe invocar a cada callback siguiendo un orden de procesado.
* - Debe notificar que el plato está listo o ha sido entregado.
*/

function getRandomTime() {
    return Math.floor(Math.random() * 1000) + 1000;
}

function procesarPedido(plato, confirmación, listo, entrega) {
    console.log(`Procesando el pedido de ${plato}`);
    setTimeout(() => {
        confirmacion(plato);
            setTimeout(() => {
                listo(plato);
                    setTimeout(() => {
                        entrega(plato);
                    }, getRandomTime());
            }, getRandomTime());
    }, getRandomTime());
}

function confirmacion(plato) {
    console.log(`Pedido de ${plato} confirmado.`)
}
function listo(plato) {
    console.log(`Pedido de ${plato} listo.`)
}
function entrega (plato) {
    console.log(`El plato de ${plato} ha sido entregado.`)
}

procesarPedido('Macarrones con tomate', confirmacion, listo, entrega);