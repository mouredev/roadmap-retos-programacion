/* Enumeraciones no existen como un tipo de valor especìfico en Javascript. Son objetos que nos permiten disponer diferentes opciones sobre un mismo elemento */

/* Generalmente se desea que las enumeraciones no cambien; entonces, usamos Object.freeze() para lograrlo */

const WEEKDAYS = Object.freeze({
  Monday: "Monday",
  Tuesday: "Tuesday",
  Wednesday: "Wednesday",
  Thursday: "Thursday",
  Friday: "Friday",
  Saturday: "Saturday",
  Sunday: "Sunday"
});

function getWeekdays(num) {
  switch (num) {
    case 1:
      console.log(WEEKDAYS.Monday);
      break;
    case 2:
      console.log(WEEKDAYS.Tuesday);
      break;
    case 3:
      console.log(WEEKDAYS.Wednesday);
      break;
    case 4:
      console.log(WEEKDAYS.Thursday);
      break;
    case 5:
      console.log(WEEKDAYS.Friday);
      break;
    case 6:
      console.log(WEEKDAYS.Saturday);
      break;
    case 7:
      console.log(WEEKDAYS.Sunday);
      break;
    default:
      console.log("Requerimiento inválido");
      break;
  }
}

getWeekdays(1);

//Extra

const ORDER_STATUS = Object.freeze({
  Pending: "Pending",
  Shipped: "Shipped",
  Delivered: "Delivered",
  Cancelled: "Cancelled"
});

class ORDER {
  status = ORDER_STATUS.Pending;
  constructor(id) {
    this.id = id;
  }
  display_status() {
    console.log(`El estado de la orden es: ${this.status}`); 
  }
  shipped() {
    if (this.status == ORDER_STATUS.Pending) {
      this.status = ORDER_STATUS.Shipped;
      this.display_status();
    } else {
      console.log("El pedido ya ha sido enviado o cancelado.");
    }
  }
  delivered() {
    if (this.status == ORDER_STATUS.Shipped) {
      this.status = ORDER_STATUS.Delivered;
      this.display_status();
    } else {
      console.log("El pedido necesita ser enviado antes de entregarse.");
    }
  }
  cancelled() {
    if (this.status != ORDER_STATUS.Delivered) {
      this.status = ORDER_STATUS.Cancelled;
      this.display_status();
    } else {
      console.log("El pedido no se puede cancelar ya que fue entregado.");
    }
  }
}

let pedido = new ORDER(2);
pedido.display_status();
pedido.delivered();
pedido.shipped();
pedido.delivered();
pedido.cancelled();