/*
# #19 ENUMERACIONES
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 */

//No existen los ENUM en javascript
const Semana = {
  LUNES: 1,
  MARTES: 2,
  MIERCOLES: 3,
  JUEVES: 4,
  VIERNES: 5,
  SABADO: 6,
  DOMINGO: 7,
};
Object.freeze(Semana);

console.log(Semana);

function showDiaSemana(num) {
  if (!num || num <=0 || num >7) {
    return "Error: El número debe ser del 1 al 7";
  }
  return Object.keys(Semana)[num-1];
}
console.log("Día de la semana 0: ", showDiaSemana(0));
console.log("Día de la semana 1: ", showDiaSemana(1));
console.log("Día de la semana 3: ", showDiaSemana(3));
console.log("Día de la semana 5: ", showDiaSemana(5));
console.log("Día de la semana 8: ", showDiaSemana(8));

/*
* DIFICULTAD EXTRA (opcional):
* Crea un pequeño sistema de gestión del estado de pedidos.
* Implementa una clase que defina un pedido con las siguientes características:
* - El pedido tiene un identificador y un estado.
* - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
* - Implementa las funciones que sirvan para modificar el estado:
*   - Pedido enviado
*   - Pedido cancelado
*   - Pedido entregado
*   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
* - Implementa una función para mostrar un texto descriptivo según el estado actual.
* - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
*/

console.log("\n\n* DIFICULTAD EXTRA (opcional):")

const EstadoPedido = {
  PENDIENTE: 1,
  ENVIADO: 2,
  ENTREGADO: 3,
  CANCELADO: 4,
};

console.log(EstadoPedido);

function obtenerEstadoPedido(num) {
  if (!num || num <=0 || num >4) {
    return "Error: El número debe0 ser del 1 al 4";
}
  return Object.keys(EstadoPedido)[num-1];
}

let pedidoA = { id: 1, estado: 1}
let pedidoB = { id: 2, estado: 2}
let pedidoC = { id: 2, estado: 4}

console.log("El pedidoA está en estado: ", obtenerEstadoPedido(pedidoA.estado));
console.log("El pedidoB está en estado: ", obtenerEstadoPedido(pedidoB.estado));
console.log("El pedidoC está en estado: ", obtenerEstadoPedido(pedidoC.estado));

function modificarEstadoPedido(pedido, nuevoEstado) {
  if (pedido.estado == 2 && nuevoEstado == 4) {
    console.log('No se puede cambiar el estado de un pedido ENVIADO a CANCELADO');
    return;
  }
  if (pedido.estado == 4 && nuevoEstado == 2) {
    console.log('No se puede cambiar el estado de un pedido CANCELADO a ENVIADO');
    return;
  }
  pedido.estado = nuevoEstado;
}
console.log('\nCambiar pedidoA a estado CANCELADO');
modificarEstadoPedido(pedidoA, 4);
console.log("El pedidoA está ahora en estado: ", obtenerEstadoPedido(pedidoA.estado));

console.log('\nCambiar pedidoB a estado CANCELADO');
modificarEstadoPedido(pedidoB, 4);
console.log("El pedidoB está ahora en estado: ", obtenerEstadoPedido(pedidoB.estado));

console.log('\nCambiar pedidoC a estado ENVIADO');
modificarEstadoPedido(pedidoC, 2);
console.log("El pedidoC está ahora en estado: ", obtenerEstadoPedido(pedidoC.estado));