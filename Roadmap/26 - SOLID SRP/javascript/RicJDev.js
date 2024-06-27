//EJERCICIO
//Código sin seguir el principio de Responsabilidad Única
class CarNoSRP {
	constructor(model, year, price) {
		this.model = model;
		this.year = year;
		this.price = price;

		this.stock = 2;
		this.status = this.setStatus();
	}

	//Esta sería la simulación de una lógica que le muestre información al cliente y le permita adquirir un carro
	describe() {
		console.log(`${this.model} (${this.year}): $${this.price.toLocaleString()}`);
	}

	getStatus() {
		console.log(`El modelo ${this.model} está ${this.status}`);
	}

	buyCar(payment) {
		if (this.status === 'disponible') {
			if (this.validatePayment(payment)) {
				console.log(`Felicidades! Ha adquirido un ${this.model} totalmente nuevo!`);
				this.stock--;
				this.setStatus();
			} else {
				console.log('Debe abonar el monto total del modelo para comprarlo');
			}
		} else {
			console.log('Modelo no disponible');
		}
	}

	/*
	Esta sería la simulación de una lógica que procese los pagos, gestione inventarios
	o realice cualquier otra función que no interesa o no conviene que sepa el cliente
	*/
	validatePayment(payment) {
		return payment >= this.price;
	}

	setStatus() {
		if (this.stock > 0) {
			this.status = 'disponible';
		} else {
			this.status = 'agotado';
		}

		return this.status;
	}

	getStock() {
		console.log(`Inventario actual del modelo ${this.model}: ${this.stock}`);
	}
}

/*
Esto está mal por varias razones:

- Se complica la tarea de implementar procesos en otras clases si los necesitan.
- De la misma manera la clase vendrá con procesos que no necesita en todos los casos que será implementada.
- Complica el mantenimiento, al juntar demasiados procesos.
- Hace más difícil definir los test unitarios.
- El código es algo más ilegible, pues no queda claro para qué es la clase.

En general, el principio de responsabilidad única busca simplificar y facilitar el desarrollo,
lo cual es todavía más útil si se trabaja con código que luego será leído y editado por otras personas.
*/

let car1 = new CarNoSRP('Chevrolet Tracker', 2022, 20190);
car1.describe();
car1.getStatus();
car1.buyCar(20000);
car1.buyCar(20200);
car1.getStock();
car1.buyCar(20190);
car1.getStock();
car1.buyCar(30000);
car1.buyCar(30000);
car1.getStock();

//Código siguiendo el principio de Responsabilidad Única
//Lógica de negocio
console.clear();

const Inventory = {
	list: [],

	search: function (itemName) {
		let result = undefined;

		this.list.forEach((element) => {
			if (element[itemName]) {
				result = element;
			}
		});

		return result;
	},

	displayInventory: function () {
		console.log('\nINVENTARIO');
		this.list.forEach((element) => {
			console.log(element);
		});
	},
};

class Item {
	constructor(itemName, quantity = 0) {
		this[itemName] = quantity;
		Inventory.list.push(this);
	}

	addQuantity(itemName, addNum) {
		return (this[itemName] = +addNum);
	}

	substractQuantity(iteName, substractNum) {
		return (this[iteName] = -substractNum);
	}
}

class Car {
	constructor(model, year, price) {
		this.model = model;
		this.year = year;
		this.fullName = `${model} ${year}`;
		this.price = price;
		this.stock = new Item(this.fullName, 5);
	}
}

new Car('Ram Pickup', 2021, 40150);
new Car('Chevrolet Silverado', 2022, 43990);

console.log(Inventory.search('Ram Pickup 2021'));
//Lógica de cliente

/*
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
 * manejar diferentes aspectos como el registro de libros, la gestión de Users
 * y el procesamiento de préstamos de libros.

 * Requisitos:
 * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con
 * información básica como título, autor y número de copias disponibles.
 * 2. Registrar Users: El sistema debe permitir agregar nuevos Users con
 * información básica como name, número de identificación y correo electrónico.
 * 3. Procesar préstamos de libros: El sistema debe permitir a los Users
 * tomar prestados y devolver libros.

 * Instrucciones:
 * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
 * los tres aspectos mencionados anteriormente (registro de libros, registro de
 * Users y procesamiento de préstamos).
 * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
 * siguiendo el Principio de Responsabilidad Única.
 */
