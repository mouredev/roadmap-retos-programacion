/*
  EJERCICIO:
  Explora el concepto de callback en tu lenguaje creando un ejemplo
  simple (a tu elección) que muestre su funcionamiento.
*/

function phrase(message, callback) {
  const fullMessage = "¡Me gusta " + message;

  callback(fullMessage);
}

function complement(complementaryMessage) {
  console.log(complementaryMessage);
}

phrase("la leche, la carne y el pan!", complement);

/*
  DIFICULTAD EXTRA (opcional):
  Crea un simulador de pedidos de un restaurante utilizando callbacks.
  Estará formado por una función que procesa pedidos.
  Debe aceptar el nombre del plato, una callback de confirmación, una
  de listo y otra de entrega.
  - Debe imprimir un confirmación cuando empiece el procesamiento.
  - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
    procesos.
  - Debe invocar a cada callback siguiendo un orden de procesado.
  - Debe notificar que el plato está listo o ha sido entregado.
*/

function confirmation(receive, confirmationCallback) {
  setTimeout(() => {
    console.log(receive);

    confirmationCallback();
  }, Math.random() * 1000);
}

function ready(process, readyCallback) {
  setTimeout(() => {
    console.log(process);

    readyCallback();
  }, Math.random() * 1000);
}

function delivery(finish) {
  setTimeout(() => {
    console.log(finish);
  }, Math.random() * 1000);
}

function orders(saucer, confirmation, ready, delivery) {
  const confirmationMessage = `1. Recibimos la orden para preparar "${saucer}".`;
  const readyMessage = `2. Ya estamos preparando "${saucer}". En unos momentos estará listo su platillo.`;
  const deliveryMessage = `3. Hemos entregado su "${saucer}". ¡Buen provecho!`;

  confirmation(confirmationMessage, () => {
    ready(readyMessage, () => {
      delivery(deliveryMessage);
    });
  });
}

orders("Quesadilla de chicharrón prensado", confirmation, ready, delivery);
