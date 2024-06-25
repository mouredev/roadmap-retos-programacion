// ** EJERCICIO 

const readline = require('node:readline');

function numeroAnos(callback) {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Por favor ingresa tu edad: ', (edad) => {
        callback(edad);
        rl.close();
    });
}

function cuandoNaciste(edad) {
    let actual = new Date();
    let anoNacimiento = actual.getFullYear() - edad;
    console.log('Naciste en el: ' + anoNacimiento + ' o ' + (anoNacimiento - 1));
}

// numeroAnos(cuandoNaciste)


// ** DIFICULTAD EXTRA ** ------------------------------------------------------------------------------------------------------------------------------------------------

function procesaPedido(nombrePlato, callbackConfirmacion, callbackListo, callbackEntrega) {
    console.log(`Iniciando pedido para ${nombrePlato}`);
    setTimeout(() => {
        callbackConfirmacion(nombrePlato);
        setTimeout(() => {
            callbackListo(nombrePlato);
            setTimeout(() => {
                callbackEntrega(nombrePlato);
            }, Math.random() * 9000 + 1000);
        }, Math.random() * 9000 + 1000); 
    }, Math.random() * 9000 + 1000); 
}

procesaPedido(
    'Pizza Margarita',
    (plato) => {
        console.log(`Confirmación recibida para ${plato}.`);
    },
    (plato) => {
        console.log(`${plato} está listo para ser entregado.`);
    },
    (plato) => {
        console.log(`${plato} ha sido entregado al cliente.`);
    }
);