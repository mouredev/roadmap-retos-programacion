const DaysOfWeek = {
  Monday: 1,
  Tuesday: 2,
  Wednesday: 3,
  Thursday: 4,
  Friday: 5,
  Saturday: 6,
  Sunday: 7,
};

function getDayName(dayNumber) {
  switch (dayNumber) {
    case DaysOfWeek.Monday:
      return "Monday";
    case DaysOfWeek.Tuesday:
      return "Tuesday";
    case DaysOfWeek.Wednesday:
      return "Wednesday";
    case DaysOfWeek.Thursday:
      return "Thursday";
    case DaysOfWeek.Friday:
      return "Friday";
    case DaysOfWeek.Saturday:
      return "Saturday";
    case DaysOfWeek.Sunday:
      return "Sunday";
    default:
      return "Invalid day number";
  }
}

console.log(getDayName(1));
console.log(getDayName(3));
console.log(getDayName(7));
console.log(getDayName(8));

// Ejercicio extra

// Definición del "enum" para los estados del pedido
const OrderStatus = {
  PENDING: "Pendiente",
  SHIPPED: "Enviado",
  DELIVERED: "Entregado",
  CANCELED: "Cancelado",
};

class Order {
  constructor(id) {
    this.id = id;
    this.status = OrderStatus.PENDING;
  }

  // Método para enviar el pedido
  shipOrder() {
    if (this.status === OrderStatus.PENDING) {
      this.status = OrderStatus.SHIPPED;
      console.log(`Pedido ${this.id} ha sido enviado.`);
    } else {
      console.log(
        `Pedido ${this.id} no se puede enviar. Estado actual: ${this.status}.`
      );
    }
  }

  // Método para cancelar el pedido
  cancelOrder() {
    if (this.status === OrderStatus.PENDING) {
      this.status = OrderStatus.CANCELED;
      console.log(`Pedido ${this.id} ha sido cancelado.`);
    } else {
      console.log(
        `Pedido ${this.id} no se puede cancelar. Estado actual: ${this.status}.`
      );
    }
  }

  // Método para entregar el pedido
  deliverOrder() {
    if (this.status === OrderStatus.SHIPPED) {
      this.status = OrderStatus.DELIVERED;
      console.log(`Pedido ${this.id} ha sido entregado.`);
    } else {
      console.log(
        `Pedido ${this.id} no se puede entregar. Estado actual: ${this.status}.`
      );
    }
  }

  // Método para obtener la descripción del estado actual
  getStatusDescription() {
    return `El estado actual del pedido ${this.id} es: ${this.status}.`;
  }
}

// Crear algunos pedidos y mostrar cómo interactuar con ellos
const order1 = new Order(1);
console.log(order1.getStatusDescription());

order1.shipOrder();
console.log(order1.getStatusDescription());

order1.deliverOrder();
console.log(order1.getStatusDescription());

const order2 = new Order(2);
console.log(order2.getStatusDescription());

order2.cancelOrder();
console.log(order2.getStatusDescription());

order2.deliverOrder();
console.log(order2.getStatusDescription());
