/*
  EJERCICIO:
  Empleando tu lenguaje, explora la definición del tipo de dato
  que sirva para definir enumeraciones (Enum).
  Crea un Enum que represente los días de la semana del lunes
  al domingo, en ese orden. Con ese enumerado, crea una operación
  que muestre el nombre del día de la semana dependiendo del número entero
  utilizado (del 1 al 7).
*/

console.log("\n+++++++++ DÍAS DE LA SEMANA +++++++++");

const weekDays = {
  lunes: 1,
  martes: 2,
  miercoles: 3,
  jueves: 4,
  viernes: 5,
  sabado: 6,
  domingo: 7,
}

function findDay(dayNumber) {
  return Object.keys(weekDays).find((key) =>
    weekDays[key] === dayNumber,
  );
}

console.log("El número de la semana ingresado corresponde a:", findDay(2));

/*
  DIFICULTAD EXTRA (opcional):
  Crea un pequeño sistema de gestión del estado de pedidos.
  Implementa una clase que defina un pedido con las siguientes características:
  - El pedido tiene un identificador y un estado.
  - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
  - Implementa las funciones que sirvan para modificar el estado:
    - Pedido enviado
    - Pedido cancelado
    - Pedido entregado
    (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
  - Implementa una función para mostrar un texto descriptivo según el estado actual.
  - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
*/
console.log("\n+++++++++ GESTIÓN DE PEDIDOS +++++++++");

class OrderStatus {
  constructor(id) {
    this.id = id;
    this.status = {
      pending: "Pendiente",
      send: "Enviado",
      delivered: "Entregado",
      cancelled: "Cancelado",
    };
  }

  get printStatus() {
    if (this.definedStatus !== "Error") {
      return `- El estado del pedido ${this.id} es: ${this.definedStatus}.`;
    } else {
      return `- El pedido ${this.id} no puede entregarse sin antes enviado.`;
    }
  }

  set setStatus(status) {
    if (status === this.status.pending) {
      this.definedStatus = this.pending();
    }

    if (status === this.status.send) {
      this.definedStatus = this.send();
      this.currentStatus = this.send();
    }

    if (status === this.status.delivered) {
      if (this.currentStatus === this.send()) {
        this.definedStatus = this.delivered();
        this.currentStatus = this.delivered();
      } else {
        this.definedStatus = this.send();
        this.definedStatus = "Error";
      }
    }

    if (status === this.status.cancelled) {
      this.definedStatus = this.cancelled();
    }
  }

  pending() {
    return this.status.pending;
  }

  send() {
    return this.status.send;
  }

  delivered() {
    return this.status.delivered;
  }

  cancelled() {
    return this.status.cancelled;
  }
}

const order1 = new OrderStatus(112314);
const order2 = new OrderStatus(223425);

order1.setStatus = order1.pending();
console.log(order1.printStatus);
order1.setStatus = order1.delivered();
console.log(order1.printStatus);
order1.setStatus = order1.send();
console.log(order1.printStatus);
order1.setStatus = order1.delivered();
console.log(order1.printStatus);
console.log("------------------------------------------------------");

order2.setStatus = order2.pending();
console.log(order2.printStatus);
order2.setStatus = order2.cancelled();
console.log(order2.printStatus);
