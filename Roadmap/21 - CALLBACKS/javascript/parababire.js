//Ejercicio

/* Las callback brillan en el mundo real cuando son usadas por funciones asyncronas */

/* function myFunction() {
  console.log('Hello World');
}*/
/* La función setTimeout nos permite emular un proceso asyncrono que al finalizar llama a nuestra callback */
/*setTimeout(myFunction, 3000); */

//Extra

function orderProcess(dishName, confirmCallbak, readyCallback, deliveredCallback) {
  confirmCallbak(dishName);
  readyCallback();
  deliveredCallback();
}

async function confirmOrder(orden) {
  let pedidoRecibido = new Promise(function(resolve) {
    setTimeout(function() {
      resolve(`Orden de ${orden} Recibida`);
    }, 1000);
  })
  console.log(await pedidoRecibido);
}

async function orderReady() {
  let ordenLista = new Promise(function(resolve) {
    setTimeout(function() {
      resolve('Orden lista');
    }, 3000);
  })
  console.log(await ordenLista);
}

async function orderDelivered() {
  let ordenEntregada = new Promise(function(resolve) {
    setTimeout(function() {
      resolve('Orden Entregada');
    }, 5000);
  })
  console.log(await ordenEntregada);
}

orderProcess('Salmón con ensalada', confirmOrder, orderReady, orderDelivered);