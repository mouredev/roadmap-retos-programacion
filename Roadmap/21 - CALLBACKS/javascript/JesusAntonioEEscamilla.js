/** #21 - JavaScript ->Jesus Antonio Escamilla */

/**
 * Una función de callback es una función que se pasa a otra función como un argumento, que luego 
    se invoca dentro de la función externa para completar algún tipo de rutina o acción.
 * Es aquella que es pasada como argumento a otra función para que sea "llamada de nuevo" (call back)
    en un momento posterior. 
*/

//---EJERCIÓ---
// Aquí podemos ver un ejemplo con tiempo
// Hacemos una función que retorne en consola
function saludar(data) {
    console.log(data);
}

// Creamos el CALLBACK que retornara un texto para imprimirlo en consola
function fetchData(name ,callback) {
    setTimeout(() => {
        const responder = `Hola soy, ${name}`;
        callback(responder);    //Aquí vemos como retorna la función CallBack
    }, 2000);
}

// Aquí solo llamamos el CALLBACK
fetchData('Jesus Antonio', saludar);


// También podemos crear primero el Callback con una suma de números
function sum(a, b, callback) {
    const resultado = a + b;
    callback(resultado);    //Aquí vemos como retorna la función CallBack
}

// Después el torno del Callback a la consola
function printSum(resultado) {
    console.log('El resultado es:', resultado)
}

// Aquí solo llamamos el CALLBACK
sum(3,6,printSum);



/**-----DIFICULTAD EXTRA-----*/

//  Una función que represente los tiempo aleatorio
function getRandomTime() {
    return Math.floor(Math.random() * 10000) + 1000;
}

//  La función del Callback donde tiene los 3 segmentos de 
function processOrder(namePlatillo, confirmCallback, readyCallback, deliveryCallback) {
    console.log(`Procesando la orden: ${namePlatillo}\n`);

    // Confirmación del pedido
    setTimeout(() => {
        console.log('Preparando orden');
        confirmCallback(namePlatillo);

        // Simula el tiempo de preparación del plato
        setTimeout(() => {
            console.log('Preparando orden para enviar');
            readyCallback(namePlatillo);

            // Simula el tiempo de entrega del plato
            setTimeout(() => {
                console.log('Preparando orden para entregar');
                deliveryCallback(namePlatillo);

            }, getRandomTime());
        }, getRandomTime());
    }, getRandomTime());
}

//  Callback de confirmación
function orderConfirmed(namePlatillo) {
    console.log(`Orden confirmado del pedido: ${namePlatillo}\n`);
}

//  Callback de plato listo
function orderReady(namePlatillo) {
    console.log(`Orden listo de: ${namePlatillo}\n`);
}

//  Callback de entrega
function orderDelivered(namePlatillo) {
    console.log(`Orden entregado: ${namePlatillo}\n`);
}

//  Ejemplo de uso de pedidos de restaurante
processOrder('Pizza la Italiana', orderConfirmed, orderReady, orderDelivered);
processOrder('Patas boloñesa', orderConfirmed, orderReady, orderDelivered);
processOrder('Albóndigas con arroz', orderConfirmed, orderReady, orderDelivered);

/**-----DIFICULTAD EXTRA-----*/