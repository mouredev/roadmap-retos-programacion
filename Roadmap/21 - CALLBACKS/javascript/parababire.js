//Ejercicio

/* Las callback brillan en el mundo real cuando son usadas por funciones asyncronas */

function myFunction() {
  console.log('Hello World');
}
/* La función setTimeout nos permite emular un proceso asyncrono que al finalizar llama a nuestra callback */
setTimeout(myFunction, 3000);

//Extra

async function orderProcess(dishName, confirmCallback, readyCallback, deliveredCallback) {
  await confirmCallback(dishName).then(orderHandle);
  await readyCallback(dishName).then(orderHandle);
  await deliveredCallback(dishName).then(orderHandle);
}

function orderHandle(result) {
  return console.log(result);
}

async function confirmOrder(order) {
  return new Promise(function(resolve) {
    resolve(`Orden de ${order} Recibida`);
  })
}

async function orderReady(order) {
  return new Promise(function(resolve) {
    setTimeout(function() {
      resolve(`${order} lista`);
    }, Math.floor((Math.random() * 10000) + 1000));
  })
}

async function orderDelivered(order) {
  return new Promise(function(resolve) {
    setTimeout(function() {
      resolve(`${order} entregada`);
    }, Math.floor((Math.random() * 10000) + 1000));
  })
}

orderProcess('Pizza Margarita', confirmOrder, orderReady, orderDelivered);
orderProcess('Pizza 4 Quesos', confirmOrder, orderReady, orderDelivered);
orderProcess('Pizza Napolitana', confirmOrder, orderReady, orderDelivered);
orderProcess('Pizza Fungi', confirmOrder, orderReady, orderDelivered);