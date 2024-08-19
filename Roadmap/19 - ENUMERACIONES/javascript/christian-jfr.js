// #19 ENUMERACIONES

/**
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 */
const weekDays = Object.freeze({
	MONDAY: 1,
	TUESDAY: 2,
	WEDNESDAY: 3,
	THURSDAY: 4,
	FRIDAY: 5,
	SATURDAY: 6,
	SUNDAY: 7,
});

function getDay(dayNumber) {
	if (dayNumber < 1 || dayNumber > 7) {
		console.log('Invalid day number. Please enter a number between 1 and 7.');
	} else {
		const dayEnum = Object.keys(weekDays)[dayNumber - 1];
		console.log(dayEnum);
	}
}

getDay(1); // -> MONDAY
getDay(8); // -> Invalid day number. Please enter a number between 1 and 7.
getDay(5); // -> FRIDAY

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

const Status = Object.freeze({
	PENDING: 'PENDING',
	SHIPPED: 'SHIPPED',
	CANCELED: 'CANCELED',
	DELIVERED: 'DELIVERED',
});

class Order {
	status = Status.PENDING;
	constructor(id) {
		this.id = id;
	}

	display_status() {
		console.log(`Order ${this.id} status: ${this.status}`);
	}

	ship() {
		if (this.status == Status.PENDING) {
			this.status = Status.SHIPPED;
			this.display_status();
		} else {
			console.log(
				`Order ${this.id} cannot be shipped because it is not pending.`
			);
		}
	}

	cancel() {
		if (this.status == Status.PENDING || this.status == Status.SHIPPED) {
			this.status = Status.CANCELED;
			this.display_status();
		} else {
			console.log(
				`Order ${this.id} cannot be canceled because it was already ${this.status}.`
			);
		}
	}

	deliver() {
		if (this.status == Status.SHIPPED) {
			this.status = Status.DELIVERED;
			this.display_status();
		} else {
			console.log(
				`Order ${this.id} cannot be delivered because it is not shipped.`
			);
		}
	}
}

let order10 = new Order(10);
let order20 = new Order(20);
let order30 = new Order(30);
let order40 = new Order(40);

order10.display_status(); // -> Order 10 status: PENDING
order10.deliver(); // -> Order 10 cannot be delivered because it is not shipped.
order10.ship(); // -> Order 10 status: SHIPPED
order10.deliver(); // -> Order 10 status: DELIVERED

order20.cancel(); // -> Order 20 status: CANCELED
order20.cancel(); // -> Order 20 cannot be canceled because it was already CANCELED.

order30.ship(); // -> Order 30 status: SHIPPED
order30.cancel(); // -> Order 30 status: CANCELED

order40.ship(); // -> Order 40 status: SHIPPED
order40.deliver(); // -> Order 40 status: DELIVERED
order40.cancel(); // -> Order 40 cannot be canceled because it was already DELIVERED.
