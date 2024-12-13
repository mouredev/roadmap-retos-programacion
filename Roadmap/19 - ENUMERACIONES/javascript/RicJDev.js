//EJERCICIO
class Enum {
	object = {};

	add(key, value) {
		this.object[key] = value;
	}

	getById(valueId) {
		const values = Object.keys(this.object);
		if (typeof values[valueId - 1] === 'undefined') {
			throw new Error('Valor inexistente');
		}
		return values[valueId - 1];
	}
}

const weekDays = new Enum('weekDays');

weekDays.add('lunes', 1);
weekDays.add('martes', 2);
weekDays.add('miercoles', 3);
weekDays.add('jueves', 4);
weekDays.add('viernes', 5);
weekDays.add('sabado', 6);
weekDays.add('domingo', 7);

console.log(`\nDía de la semana: ${weekDays.getById(2)}`);

//EXTRA
let cancelledOrders = [];

class Order extends Enum {
	constructor(identifier) {
		super();
		this.identifier = identifier;
		this.status = this.getById(1);
	}

	object = {
		pending: 1,
		sent: 2,
		delivered: 3,
		cancelled: 4,
	};

	sendOrder() {
		if (this.status === 'pending') {
			console.log('\nEnviando...');
			return (this.status = this.getById(2));
		} else {
			console.log('\nEl pedido debe estar pendiente para poder enviarlo');
		}
	}

	deliverOrder() {
		if (this.status === 'sent') {
			console.log('\nEntregando...');
			return (this.status = this.getById(3));
		} else {
			console.log('\nEl pedido debe haber sido enviado para poder entregarlo');
		}
	}

	cancelOrder() {
		if (this.status === 'delivered') {
			console.log('\nNo se puede cancelar un pedido entregado');
		} else {
			console.log('\nCancelando...');
			cancelledOrders.push(this.identifier);
			return (this.status = this.getById(4));
		}
	}

	showStatus() {
		console.log(`\nEstado actual del pedido ${this.identifier}:`);
		switch (this.status) {
			case 'pending':
				console.log('Pendiente. Envíe cuando guste');
				break;
			case 'sent':
				console.log('Enviado. En cualquier momento se entregará');
				break;
			case 'delivered':
				console.log('Entregado. Puede realizar más pedidos si quiere');
				break;
			case 'cancelled':
				console.log('Cancelado. La vida es impredecible');
				break;
		}
	}
}

let myOrder = new Order(1434343);

myOrder.showStatus();

myOrder.sendOrder();
myOrder.showStatus();

myOrder.deliverOrder();
myOrder.showStatus();

myOrder.cancelOrder();

let myPizzaOrder = new Order(1223456);

myPizzaOrder.showStatus();

myPizzaOrder.deliverOrder();
myPizzaOrder.sendOrder();
myPizzaOrder.showStatus();

myPizzaOrder.cancelOrder();
myPizzaOrder.showStatus();

let myShoesOrder = new Order(4546066)

myShoesOrder.showStatus();

myShoesOrder.cancelOrder();
myShoesOrder.showStatus();

console.log('\n- Lista de pedidos cancelados 😭:');
cancelledOrders.forEach(element => {
	console.log(element);
});