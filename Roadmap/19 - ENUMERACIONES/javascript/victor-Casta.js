/*
  * Empleando tu lenguaje, explora la definición del tipo de dato
  * que sirva para definir enumeraciones (Enum).
  * Crea un Enum que represente los días de la semana del lunes
  * al domingo, en ese orden. Con ese enumerado, crea una operación
  * que muestre el nombre del día de la semana dependiendo del número entero
  * utilizado (del 1 al 7).
*/

const DAYS_OF_WEEK = Object.freeze({
  'Monday': 1,
  'Tuesday': 2,
  'Wednesday': 3,
  'Thursday': 4,
  'Friday': 5,
  'Saturday': 6,
  'Sunday': 7
})

function getDay(numberOfDay) {
  let value
  for (let item in DAYS_OF_WEEK) {
    if (DAYS_OF_WEEK[item] === numberOfDay) {
      value = item
    }
  }
  return value
}

console.log(getDay(1))

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

const ORDER_STATE = Object.freeze({
  'SENT': 1,
  'PENDING': 2,
  'DELIVERED': 3,
  'CANCELED': 4
});

class ORDER {
  constructor(id) {
    this.id = id;
    this.state = ORDER_STATE.PENDING;
  }

  shipped() {
    if (this.state === ORDER_STATE.PENDING) {
      this.state = ORDER_STATE.SENT;
    }
  }

  delivered() {
    if (this.state === ORDER_STATE.SENT) {
      this.state = ORDER_STATE.DELIVERED;
    }
  }

  canceled() {
    if (this.state !== ORDER_STATE.SENT && this.state !== ORDER_STATE.DELIVERED && this.state !== ORDER_STATE.CANCELED) {
      this.state = ORDER_STATE.CANCELED;
    } else {
      console.log('El pedido no se puede cancelar');
    }
  }

  getStateName() {
    return Object.entries(ORDER_STATE).find(([key, value]) => value === this.state)?.[0] || 'Estado desconocido';
  }

  viewState() {
    const stateName = this.getStateName();
    console.log(`El estado del pedido #${this.id} es ${stateName}`);
  }
}

const order1 = new ORDER(1);
order1.viewState()
order1.shipped()
order1.viewState()
order1.delivered()
order1.viewState()
order1.canceled()
order1.viewState()
