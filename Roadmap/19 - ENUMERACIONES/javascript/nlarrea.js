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


// In JS there are no Enums -> we create one
class Enum {
    object = {};

    add(key, value) {
        this.object[key] = value;
    }

    getById(valueId) {
        const keys = Object.keys(this.object);
        if (typeof keys[valueId - 1] === 'undefined') {
            throw new Error('Value Not Found');
        }

        return keys[valueId - 1];
    }
}


class WeekDay extends Enum {
    constructor () {
        super();
    }

    object = {
        MONDAY: 1,
        TUESDAY: 2,
        WEDNESDAY: 3,
        THURSDAY: 4,
        FRIDAY: 5,
        SATURDAY: 6,
        SUNDAY: 7
    };
};
    

const weekdays = new WeekDay();
console.log(weekdays.getById(5));  // friday


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


class OrderStatus extends Enum {
    constructor () {
        super();
    }

    object = {
        PENDING: 1,
        SHIPPED: 2,
        DELIVERED: 3,
        CANCELED: 4
    }
};


class Order {
    constructor (orderId) {
        this.orderId = orderId;
        this.state = new OrderStatus().getById(1);

        console.log(`\nThe order '${this.orderId}' is ${this.state}`);
    };

    updateState() {
        if (this.state == 'CANCELED' || this.state == 'DELIVERED') {
            // If order is canceled or delivered -> maintain the state as it is
            return;
        } else if (this.state == 'PENDING') {
            this.state = new OrderStatus().getById(2);
        } else if (this.state == 'SHIPPED') {
            this.state = new OrderStatus().getById(3);
        }
    }

    cancelOrder() {
        if (this.state != 'DELIVERED') {
            this.state = new OrderStatus().getById(4);
        }
    }

    printCurrentState() {
        console.log(`The order '${this.orderId}' is ${this.state}`);
    }
}

const order1 = new Order('1234');  // The order '1234' is PENDING
order1.updateState();
order1.printCurrentState();  // shipped
order1.updateState();
order1.printCurrentState();  // delivered
order1.cancelOrder();  // it won't work because it's delivered already
order1.printCurrentState();  // delivered

const order2 = new Order("5678");  // pending
order2.updateState();
order2.printCurrentState();  // shipped
order2.cancelOrder();
order2.printCurrentState();  // canceled
order2.updateState();  // it won't work because it's canceled
order2.printCurrentState();  // canceled

const order3 = new Order("1290");  // pending
order3.cancelOrder();
order3.printCurrentState();  // canceled
