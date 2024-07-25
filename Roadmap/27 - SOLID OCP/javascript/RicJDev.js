//EJERCICIO
/*
Incorrecto ❎

Dado a que no se ha diseñado siguiendo el principio, habría que modificar clases para que el sistema de cálculo de áreas pueda soportar otras figuras geométricas. En un caso más complejo este sería un problema, ya que dificulta el agregar funcionalidades o realizar cambios.

*/
console.log('\nSin OCP');
class RectangleNoOCP {
	constructor(height, width) {
		this.height = height;
		this.width = width;
	}
}
class AreaCalculatorNoOCP {
	calculateArea(rectangle) {
		let area = rectangle.height * rectangle.width;

		return area;
	}
}

class AppNoOCP {
	rectangle = new RectangleNoOCP(12, 20.33);
	square = new RectangleNoOCP(21, 21);

	areaCalc = new AreaCalculatorNoOCP();

	displayAreas() {
		console.log('Rectangulo:', this.areaCalc.calculateArea(this.rectangle));
		console.log('Cuadrado:', this.areaCalc.calculateArea(this.square));
	}
}

const appNoOCP = new AppNoOCP();
appNoOCP.displayAreas();

/*
Correcto ✅

"Las entidades de software (clases, módulos, funciones, etc) deben de estar abierta para su extensión, pero cerradas para su modificación."

Diseñado de esta manera resulta más fácil añadir figuras geométricas al sistema de cálculo de áreas. Este ejemplo abstrae el método getArea y lo hace común para cada figura, pero cada una cuenta con su propio método concreto para calcular el área.

*/
console.log('\nCon OCP');

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

class App {
	rectangle = new Rectangle(12, 20);
	square = new Square(20);
	circle = new Circle(5);

	calculateArea(geometricShape) {
		return geometricShape.area;
	}

	displayAreas() {
		console.log('Rectángulo:', this.calculateArea(this.rectangle));
		console.log('Cuadrado:', this.calculateArea(this.square));
		console.log('Círculo:', this.calculateArea(this.circle));
	}
}

const app = new App();

app.displayAreas();

//EXTRA
console.log('\nCalculadora');
class Operation {
	calculate(a, b) {
		throw new Error('Operación no soportada');
	}
}

class Addition extends Operation {
	calculate(a, b) {
		return a + b;
	}
}

class Substraction extends Operation {
	calculate(a, b) {
		return a - b;
	}
}

class Multiplication extends Operation {
	calculate(a, b) {
		return a * b;
	}
}

class Division extends Operation {
	calculate(a, b) {
		return a / b;
	}
}

class Calculator {
	operations = {};

	addOperation(name, operation) {
		this.operations[name] = operation;
	}

	calculate(operation, a, b) {
		let op = this.operations[operation] || new Operation();

		try {
			return op.calculate(a, b);
		} catch (error) {
			console.log(`Se produjo un error. ${error.message}: ${operation}`);
			return NaN;
		}
	}
}

const calculator = new Calculator();
calculator.addOperation('Addition', new Addition());
calculator.addOperation('Substraction', new Substraction());
calculator.addOperation('Multiplication', new Multiplication());
calculator.addOperation('Division', new Division());

let result = calculator.calculate('Addition', 12, 10);
console.log('Suma:', result);

result = calculator.calculate('Substraction', 10, 2);
console.log('Resta:', result);

result = calculator.calculate('Multiplication', 10, 2);
console.log('Multiplicación:', result);

result = calculator.calculate('Division', 10, 2);
console.log('División:', result);

result = calculator.calculate('Pow', 10, 2);
console.log('Potencia:', result);

class Pow extends Operation {
	calculate(a, b) {
		return a ** b;
	}
}

calculator.addOperation('Pow', new Pow());

result = calculator.calculate('Pow', 10, 2);
console.log('Potencia:', result);
