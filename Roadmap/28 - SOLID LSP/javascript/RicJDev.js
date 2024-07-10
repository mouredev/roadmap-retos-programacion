//EJERCICIO
console.log('\nSin LSP');
class RectangleNoLSP {
	constructor(height, width) {
		this.height = height;
		this.width = width;
	}

	getArea() {
		return this.height * this.width;
	}

	rotateToVerticalPosition() {
		let changeValue = this.height;

		if (this.width > this.height) {
			this.height = this.width;
			this.width = changeValue;
		}
	}

	checkVerticalPosition() {
		if (this.height > this.width) {
			console.log('Está en posición vertical');
		} else {
			console.log('No está en posición vertical');
		}
	}
}

class SquareNoLSP extends RectangleNoLSP {
	constructor(side) {
		super(side, side);
	}
}

const rectangleNoLSP = new RectangleNoLSP(3, 4);
const squareNoLSP = new SquareNoLSP(5);

console.log('Área del círculo:', squareNoLSP.getArea());
console.log('Área del rectángulo:', rectangleNoLSP.getArea());

console.log(rectangleNoLSP.height);
rectangleNoLSP.checkVerticalPosition();

rectangleNoLSP.rotateToVerticalPosition();

console.log(rectangleNoLSP.height);
rectangleNoLSP.checkVerticalPosition();

console.log(squareNoLSP.height);
squareNoLSP.checkVerticalPosition();

squareNoLSP.rotateToVerticalPosition();

console.log(squareNoLSP.height);
squareNoLSP.checkVerticalPosition();

/*
En el ejemplo anterior vemos que, si bien un cuadrado podría ser similar a un rectángulo, no son exactamente lo mismo y no se comportan igual. Como esto no se ha tenido en cuenta para el diseño de las clases, al invocar los métodos para ponerlo en posición vertical y verificar si ya lo está, el programa no funciona como debería, lo que en un caso más complejo acarrearía problemas para la reutilización del código y su mantenimiento.
*/

console.log('\nCon LSP');
class Quadrilateral {
	constructor(height, width) {
		this.height = height;
		this.width = width;
	}

	getArea() {
		return this.height * this.width;
	}
}

class Rectangle extends Quadrilateral {
	constructor(height, width) {
		super(height, width);
	}

	rotateToVerticalPosition() {
		let changeValue = this.height;

		if (this.width > this.height) {
			this.height = this.width;
			this.width = changeValue;
		}
	}

	checkVerticalPosition() {
		if (this.height > this.width) {
			console.log('Está en posición vertical');
		} else {
			console.log('No está en posición vertical');
		}
	}
}

class Square extends Quadrilateral {
	constructor(side) {
		super(side, side);
	}
}

const quadrilateral = new Quadrilateral(12, 10);
const rectangle = new Rectangle(10, 23);
const square = new Square(10);

console.log('Área de un cuadrilátero abstracto:', quadrilateral.getArea());
console.log('Área de un rectángulo:', rectangle.getArea());
console.log('Área de un cuadrado:', square.getArea());

/*
"Si S es un subtipo de T, entonces los objetos de tipo T en un programa de computadora pueden ser sustituidos por objetos de tipo S, sin alterar ninguna de las propiedades deseables de ese programa."

En este caso, la capacidad de ponerse en posición vertical es única del rectángulo, y si fuera necesario sustituir un cuadrilátero cualquiera por un rectángulo, seguirán funcionando todos los métodos de la clase del cuadrilátero. Cierto que aquí solo se calcula el área de la figura, pero en un caso más complejo esto es de mucha ayuda y ahorra trabajo. 
*/

//EXTRA
console.log('\nJerarquía de vehículos');
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
