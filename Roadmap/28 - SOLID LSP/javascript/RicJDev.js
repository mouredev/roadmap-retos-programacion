/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
 */
//EJERCICIO

/*

"Si S es un subtipo de T, entonces los objetos de tipo T en un programa de computadora pueden ser sustituidos por objetos de tipo S, sin alterar ninguna de las propiedades deseables de ese programa."

*/
class GeometricShape {
	constructor() {
		this.area = this.getArea();
	}

	getArea() {
		return 1;
	}
}

class Rectangle extends GeometricShape {
	constructor(height, width) {
		super();
		this.height = height;
		this.width = width;
		this.area = this.getArea();
	}

	getArea() {
		return this.height * this.width;
	}
}

class Square extends GeometricShape {
	constructor(height) {
		super();
		this.height = height;
		this.area = this.getArea();
	}

	getArea() {
		return this.height ** 2;
	}
}

class Circle extends GeometricShape {
	constructor(radius) {
		super();
		this.radius = radius;
		this.area = this.getArea();
	}

	getArea() {
		return this.radius * 2 * Math.PI;
	}
}

function displayArea(shape) {
	console.log(shape.area);
}

let square = new Square(12);

displayArea(square);

//EXTRA
class Vehicle {
	constructor() {
		this.speed = 0;
	}

	accelerate(amount) {
		this.speed += amount * 1.2;
	}

	brake(amount) {
		this.speed -= amount * 0.8;

		if (this.speed < 0) {
			this.speed = 0;
		}
	}
}

class Motorcycle extends Vehicle {
	constructor() {
		super();
	}

	accelerate(amount) {
		this.speed += amount * 1.5;
	}

	brake(amount) {
		this.speed -= amount * 1.2;

		if (this.speed < 0) {
			this.speed = 0;
		}
	}
}

class Car extends Vehicle {
	constructor() {
		super();
	}

	accelerate(amount) {
		this.speed += amount * 1.6;
	}

	brake(amount) {
		this.speed -= amount * 1.3;

		if (this.speed < 0) {
			this.speed = 0;
		}
	}
}

class SciFiTurboCar extends Vehicle {
	constructor() {
		super();
	}

	accelerate(amount) {
		this.speed += amount * 3;
	}

	brake(amount) {
		this.speed -= amount * 2.5;

		if (this.speed < 0) {
			this.speed = 0;
		}
	}
}

function checkLSP(vehicle) {
	if (!vehicle.accelerate || !vehicle.brake) {
		throw new Error('El objeto no cumple con la interfaz de Vehículo');
	}

	vehicle.accelerate(78);
	vehicle.brake(4);

	console.log(vehicle);
}

const vehicle = new Vehicle();
const toyota = new Car();
const jaguar = new Motorcycle();
const hypercar3000 = new SciFiTurboCar();

checkLSP(vehicle);
checkLSP(toyota);
checkLSP(jaguar);
checkLSP(hypercar3000);
