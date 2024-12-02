//#21 - CALLBACKS
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

//Bibliografy reference:
//Secrets of the JavaScript Ninja (John Resig, Bear Bibeault, Josip Maras) (z-lib.org)
//Eloquent Javascript A Modern Introduction to Programming by Marijn Haverbeke (z-lib.org)
//GPT

let log = console.log;

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #21.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #21. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #21'); 
});


/* Callbacks
One approach to asynchronous programming is to make functions that perform
a slow action take an extra argument, a callback function. The action is started,
and when it finishes, the callback function is called with the result.
As an example, the setTimeout function, available both in Node.js and in
browsers, waits a given number of milliseconds (a second is a thousand mil-
liseconds) and then calls a function.
setTimeout(() => console.log("Tick"), 500); */

/* Whenever we set up a function to be called at a later time, whether by the browser in
the event-handling phase or by other code, we’re setting up a callback. The term stems
from the fact that we’re establishing a function that other code will later “call back” at
an appropriate point of execution. */

const todayMenu = ['pizza', 'hamburger', 'paella', 'arabian food', 'posole', 'pastel azteca', 'carbonara past', 'napolitana past', 'fish', 'beaf'];

const orderConfirm = (order, cb) => {
    log(`The order: ${order} is confirmed. Tell you when it's ready.`);
   
    const processingTime = Math.floor(Math.random() * 10000) + 1000; 
    setTimeout(() => {
        cb(order);
    }, processingTime);
}

const orderReady = (order, cb) => {
    log(`The order: ${order} is ready. Waiting to deliver.`);
   
    const deliveryTime = Math.floor(Math.random() * 10000) + 1000; 
    setTimeout(() => {
        cb(order);
    }, deliveryTime);
}

const orderDeliver = (order) => {
    log(`Order: ${order} delivered.`);
}

const makeOrder = (listOrder) => {
    listOrder.forEach(order => {
        if (todayMenu.some(elm => elm.toLowerCase() === order.toLowerCase())) {
            orderConfirm(order, (confirmedOrder) => {
                orderReady(confirmedOrder, (readyOrder) => {
                    orderDeliver(readyOrder);
                });
            });
        } else {
            log(`The order: ${order} is not in today's menu. Please choose another dish.`);
        }
    });
}

let orderList1 = ['pastiche', 'hamburger', 'pizza'];
let orderList2 = ['arabian food', 'fish', 'pastel azteca'];

makeOrder(orderList1);
makeOrder(orderList2);

/* Output Example: The order: pastiche is not in today's menu. Please choose another dish.
21.js:42 The order: hamburger is confirmed. Tell you when it's ready.
21.js:42 The order: pizza is confirmed. Tell you when it's ready.
21.js:42 The order: arabian food is confirmed. Tell you when it's ready.
21.js:42 The order: fish is confirmed. Tell you when it's ready.
21.js:42 The order: pastel azteca is confirmed. Tell you when it's ready.
21.js:51 The order: pizza is ready. Waiting to deliver.
21.js:51 The order: pastel azteca is ready. Waiting to deliver.
21.js:51 The order: hamburger is ready. Waiting to deliver.
21.js:60 Order: pizza delivered.
21.js:60 Order: hamburger delivered.
21.js:51 The order: fish is ready. Waiting to deliver.
21.js:51 The order: arabian food is ready. Waiting to deliver.
21.js:60 Order: fish delivered.
21.js:60 Order: pastel azteca delivered.
21.js:60 Order: arabian food delivered. */