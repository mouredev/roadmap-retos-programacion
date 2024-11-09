/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
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

const diasDeLaSemana = Object.freeze({
  LUNES: 1,
  MARTES: 2,
  MIERCOLES: 3,
  JUEVES: 4,
  VIERNES: 5,
  SABADO: 6,
  DOMINGO: 7,
});

const getDayFromNumber = (number) => {
  let day = Object.keys(diasDeLaSemana).find(
    (key) => diasDeLaSemana[key] === number
  );
  console.log(day);
};

getDayFromNumber(2);

console.log("---------------DIFICULTAD EXTRA----------------");

const statusEnum = Object.freeze({
  PENDIENTE: 0,
  ENVIADO: 1,
  ENTREGADO: 2,
  CANCELADO: 4,
});

class Order {
  constructor(id, state) {
    this.id = id;
    this.status = state;
  }

  order() {
    this.status = statusEnum.PENDIENTE;
    console.log("El pedido se ha creado con id: ", this.id);
  }

  send() {
    if (!this.checkIsCanceled('enviar')) {
      return false;
    } else if (this.status === 0) {
      console.log("El pedido se está enviando");
      this.status = statusEnum.ENVIADO;
    } else if (this.status === statusEnum.ENVIADO) {
      console.log("El pedido ya se ha enviado o ha sido cancelado");
    } else {
      console.log("No se puede enviar un envío inexistente");
    }
  }

  deliver() {
    if (!this.checkIsCanceled('entregar')) {
      return false;
    } else if (this.status > 2) {
      this.status = statusEnum.ENTREGADO;
      console.log("El pedido se está entregando");
    } else {
      console.log(
        "No se puede entregar un envío que no se ha creado y/o mandado"
      );
    }
  }

  cancel() {
    if (this.status < 2) {
      this.status = statusEnum.CANCELADO;
      console.log("El pedido se ha cancelado");
    } else {
      console.log(
        "No se puede entregar un envío que no se ha creado y/o mandado"
      );
    }
  }

  checkStatus() {
    console.log(
      "El estado del pedido es: ",
      Object.keys(statusEnum).find((key) => statusEnum[key] === this.status)
    );
  }

  checkIsCanceled(operacion) {
    if (this.status === statusEnum.CANCELADO) {
      console.log("El pedido ha sido cancelado, no se puede realizar la operación: ", operacion);
      return false;
    }
    return true;
  }
}

const order1 = new Order('001');
order1.order();
order1.checkStatus();
order1.send();
order1.checkStatus();

const order2 = new Order('002');
order2.order();
order2.checkStatus();
order2.cancel();
order2.send();