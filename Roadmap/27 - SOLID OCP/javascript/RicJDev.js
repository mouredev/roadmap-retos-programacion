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
		return false;
	}
}

class Rectangle extends GeometricShape {
	constructor(height, width) {
		super();
		this.height = height;
		this.width = width;
	}

	getArea() {
		return this.height * this.width;
	}
}

class Square extends GeometricShape {
	constructor(height) {
		super();
		this.height = height;
	}

	getArea() {
		return this.height ** 2;
	}
}

class Circle extends GeometricShape {
	constructor(radius) {
		super();
		this.radius = radius;
	}

	getArea() {
		return this.radius * 2 * Math.PI;
	}
}

class AreaCalculator {
	calculateArea(shape) {
		return shape.getArea();
	}
}

class App {
	rectangle = new Rectangle(12, 20);
	square = new Square(20);
	circle = new Circle(5);

	areaCalc = new AreaCalculator();

	displayAreas() {
		console.log('Rectángulo:', this.areaCalc.calculateArea(this.rectangle));
		console.log('Cuadrado:', this.areaCalc.calculateArea(this.square));
		console.log('Círculo:', this.areaCalc.calculateArea(this.circle));
	}
}

const app = new App();

app.displayAreas();

//EXTRA
console.log('\nCalculadora');
class Operation {
	calculate(a, b) {
		throw new Error('operación no soportada');
	}
}

class Add extends Operation {
	calculate(a, b) {
		return a + b;
	}
}

class Susbtract extends Operation {
	calculate(a, b) {
		return a - b;
	}
}

class Multiply extends Operation {
	calculate(a, b) {
		return a * b;
	}
}

class Divide extends Operation {
	calculate(a, b) {
		return a / b;
	}
}

class Calculator {
	operations = {
		add: new Add(),
		substract: new Susbtract(),
		multiply: new Multiply(),
		divide: new Divide(),
	};

	calculate(operationType, a, b) {
		let operation = this.operations[operationType] || new Operation();

		try {
			return operation.calculate(a, b);
		} catch (error) {
			console.log(`Se produjo un error: ${error.message}`);
			return NaN;
		}
	}
}

const calculator = new Calculator();

let result = calculator.calculate('add', 12, 10);
console.log('Suma:', result);

result = calculator.calculate('substract', 10, 2);
console.log('Resta:', result);

result = calculator.calculate('multiply', 10, 2);
console.log('Multiplicación:', result);

result = calculator.calculate('divide', 10, 2);
console.log('División:', result);

result = calculator.calculate('exponent', 10, 2);
console.log('Potencia:', result);

class Exponent extends Operation {
	calculate(a, b) {
		return a ** b;
	}
}

calculator.operations.exponent = new Exponent();

result = calculator.calculate('exponent', 10, 2);
console.log('Potencia:', result);
