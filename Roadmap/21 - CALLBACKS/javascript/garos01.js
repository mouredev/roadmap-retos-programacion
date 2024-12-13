// Función que toma un número y un callback
function procesarNumero(numero, callback) {
  // Simulamos una operación asincrónica con setTimeout
  setTimeout(() => {
    let resultado = numero * 2;
    callback(resultado);
  }, 1000);
}

// Función callback que se ejecutará después de procesar el número
function mostrarResultado(resultado) {
  console.log("El resultado es:", resultado);
}

// Llamamos a la función procesarNumero y le pasamos 5 como número y mostrarResultado como callback
procesarNumero(5, mostrarResultado);

// Ejercicio extra

// Función que genera un tiempo aleatorio entre 1 y 10 segundos
function tiempoAleatorio() {
  return Math.floor(Math.random() * 10000) + 1000;
}

// Función que procesa pedidos
function procesarPedido(
  nombrePlato,
  callbackConfirmacion,
  callbackListo,
  callbackEntrega
) {
  console.log(`Pedido recibido: ${nombrePlato}`);

  // Confirmar el pedido
  setTimeout(() => {
    console.log(`Confirmación: El pedido de ${nombrePlato} está en proceso.`);
    callbackConfirmacion(nombrePlato);

    // Notificar que el plato está listo
    setTimeout(() => {
      console.log(`Listo: El plato ${nombrePlato} está listo.`);
      callbackListo(nombrePlato);

      // Notificar que el plato ha sido entregado
      setTimeout(() => {
        console.log(`Entrega: El plato ${nombrePlato} ha sido entregado.`);
        callbackEntrega(nombrePlato);
      }, tiempoAleatorio());
    }, tiempoAleatorio());
  }, tiempoAleatorio());
}

// Funciones callback
function confirmacionCallback(plato) {
  console.log(`Callback de confirmación: ${plato} está siendo preparado.`);
}

function listoCallback(plato) {
  console.log(`Callback de listo: ${plato} está listo para ser entregado.`);
}

function entregaCallback(plato) {
  console.log(`Callback de entrega: ${plato} ha sido entregado al cliente.`);
}

// Ejemplos
procesarPedido(
  "Pizza Carne",
  confirmacionCallback,
  listoCallback,
  entregaCallback
);
procesarPedido(
  "Ensalada",
  confirmacionCallback,
  listoCallback,
  entregaCallback
);
procesarPedido(
  "Tiramisú",
  confirmacionCallback,
  listoCallback,
  entregaCallback
);
