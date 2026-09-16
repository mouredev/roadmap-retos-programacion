/*
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
*/

function registrar(callback,user) {
    console.log("Se esta registrando")
    callback(user)
}

function registroFin(user) {
    console.log(`¡Registro terminado! \n User: ${user}\nPassword: ********`)
}

//registrar(registroFin, "pacoPE")

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



function procesarPedido(pedido, confirmacionCallback, listoCallback,  entregaCallback) {

    // TODA LA LÓGICA EN procesarPedido Y EL RESTO DE FUNCIONES HACEN SU COMETIDO PERO procesarPedido DECIDE COMO HACERLO,
    // ESTO ES SEPARACIÓN DE RESPONSABILIDAD.

    // 1. Confirmación incial
    confirmacionCallback(pedido)

/*
    Los setTimeout no "espera" bloqueando la ejecución como un bucle tradicional; en su lugar, programa una tarea para el futuro en el bucle de eventos (Event Loop) de JavaScript.

    Al anidar un setTimeout dentro de otro (creando el famoso fenómeno conocido como Callback Hell o infierno de callbacks), lo que haces es:

    Se ejecuta la confirmación inicial de forma inmediata.

    Se programa el primer temporizador (tiempoAleatorio).

    Cuando ese tiempo termina, se ejecuta listoCallback e inmediatamente se programa otro temporizador independiente para la entrega.
*/
    setTimeout(() => {
        // 2. El pedido se prepara y está listo.
        listoCallback(pedido)
        setTimeout(() => {
            // 3. El pedido se entrega al cliente.
            entregaCallback(pedido)
        }, tiempoAleatorio());
    }, tiempoAleatorio());

}

function confirmacionOrden(pedido) {
    console.log(`Tu pedido ${pedido} se esta preparando.`)
}

function pedidoListo(pedido) {
    console.log(`Tu pedido ${pedido} está listo para ser servido`)
}

function pedidoEntrega(pedido) {
    console.log(`Tu pedido ${pedido} ha sido entregado al cliente, ¡ buen provecho!`)
}


const tiempoAleatorio  = () => Math.floor(Math.random()* 10 +1) * 1000;


procesarPedido("Pizza Barbacoa", confirmacionOrden, pedidoListo,  pedidoEntrega)
procesarPedido("Hamburguesa", confirmacionOrden, pedidoListo,  pedidoEntrega)
procesarPedido("Bocadillo", confirmacionOrden, pedidoListo,  pedidoEntrega)
procesarPedido("Arroz con lentejas", confirmacionOrden, pedidoListo,  pedidoEntrega)
procesarPedido("Tallarines", confirmacionOrden, pedidoListo,  pedidoEntrega)