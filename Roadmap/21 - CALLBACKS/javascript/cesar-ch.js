/*
    * #21 CALLBACKS
*/

function greet(name, callback) {
    console.log("Hello, " + name + "!");
    callback();
}

function sayGoodbye() {
    console.log("Goodbye!");
}

greet("Mouredev", sayGoodbye);

/*
    * DIFICULTAD EXTRA
*/

function procesarPedido(plato, confirmacionCallback, listoCallback, entregaCallback) {
    console.log(`Procesando pedido para: ${plato}`);
    confirmacionCallback(plato);

    const tiempoPreparacion = Math.floor(Math.random() * 10) + 1;
    console.log("Tiempo de preparacion es: " + tiempoPreparacion)
    setTimeout(() => {
        listoCallback(plato);

        const tiempoEntrega = Math.floor(Math.random() * 10) + 1;
        console.log("Tiempo de entrega es: " + tiempoEntrega)
        setTimeout(() => {
            entregaCallback(plato);
        }, tiempoEntrega);
    }, tiempoPreparacion);
}

function confirmarPedido(plato) {
    console.log(`Pedido confirmado para: ${plato}`);
}

function platoListo(plato) {
    console.log(`El plato ${plato} está listo para ser entregado.`);
}

function entregarPedido(plato) {
    console.log(`El plato ${plato} ha sido entregado.`);
}

procesarPedido("Pizza", confirmarPedido, platoListo, entregarPedido);
