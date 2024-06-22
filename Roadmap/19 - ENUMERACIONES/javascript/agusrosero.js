/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 */
const diasSemana = Object.freeze({
  LUNES: "Lunes",
  MARTES: "Martes",
  MIERCOLES: "Miercoles",
  JUEVES: "Jueves",
  VIERNES: "Viernes",
  SABADO: "Sabado",
  DOMINGO: "Domingo",
});
console.log(diasSemana);

function getWeekdays(num) {
  switch (num) {
    case 1:
      console.log(diasSemana.LUNES);
      break;
    case 2:
      console.log(diasSemana.MARTES);
      break;
    case 3:
      console.log(diasSemana.MIERCOLES);
      break;
    case 4:
      console.log(diasSemana.JUEVES);
      break;
    case 5:
      console.log(diasSemana.VIERNES);
      break;
    case 6:
      console.log(diasSemana.SABADO);
      break;
    case 7:
      console.log(diasSemana.DOMINGO);
      break;
  }
}

getWeekdays(5);

/**
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
const estados = Object.freeze({
  PENDIENTE: "Pendiente",
  ENVIADO: "Enviado",
  ENTREGADO: "Entregado",
  CANCELADO: "Cancelado",
});

class GestionEstadoPedidos {
  constructor(id) {
    this.id = id;
    this.estado = estados.PENDIENTE;
  }

  pedidoEnviado() {
    if (this.estado === estados.ENVIADO) {
      console.log("Pedido enviado con exito");
    } else {
      console.log("Error en el envio del pedido");
    }
  }

  pedidoCancelado() {
    if (this.estado === estados.CANCELADO) {
      console.log("Pedido cancelado");
    } else {
      console.log("Error al cancelar el pedido");
    }
  }

  pedidoEntregado() {
    if (this.estado === estados.ENTREGADO) {
      console.log("Pedidos entregado correctamente");
    } else {
      console.log("Error al entregar el pedido");
    }
  }

  textoDescriptivo() {
    console.log(`Estado del pedido: ${this.estado}`);
  }
}

const pedido1 = new GestionEstadoPedidos();
pedido1.textoDescriptivo();
pedido1.pedidoEnviado();

const pedido2 = new GestionEstadoPedidos();
pedido2.textoDescriptivo();
pedido2.pedidoCancelado();
