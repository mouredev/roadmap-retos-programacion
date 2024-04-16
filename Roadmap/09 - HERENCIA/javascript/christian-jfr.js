// #09 HERENCIA

/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */
class Animal {
	constructor(name) {
		this.name = name;
	}
}

class Dog extends Animal {
	constructor(name) {
		super(name);
	}

	bark() {
		return `${this.name} woof woof!`;
	}
}

class Cat extends Animal {
	constructor(name) {
		super(name);
	}

	meow() {
		return `${this.name} meow!`;
	}
}

const myDog = new Dog('Fido');
const myCat = new Cat('Garfield');

console.log(myDog.bark()); // -> Fido woof woof!
console.log(myCat.meow()); // -> Garfield meow!

/**
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

class Employee {
	constructor(id, name) {
		this.id = id;
		this.name = name;
		this.employees = [];
	}

	assignEmployee(employee) {
		this.employees.push(employee);
	}

	underSupervision() {
		console.log(
			`${this.name} has ${this.employees.length} employees under his supervision.`
		);
	}
}

class Manager extends Employee {
	constructor(id, name) {
		super(id, name);
	}

	hireEmployees() {
		const rng = Math.floor(Math.random() * 10 + 1);
		console.log(
			`${this.name} is hiring ${rng} efficient employees and delegating work.`
		);
	}
}

class ProjectManager extends Employee {
	constructor(id, name) {
		super(id, name);
	}

	projectPlanning() {
		console.log(
			`${this.name}  is defining project scope, objectives, and deliverables.`
		);
	}
}

class Programmer extends Employee {
	constructor(id, name, language) {
		super(id, name);
		this.language = language;
	}

	code() {
		console.log(`${this.name} is writing code in ${this.language}`);
	}

	assignEmployee() {
		console.log(`${this.name} does not have permissions to assign employees.`);
	}
}

const luke = new Programmer('2', 'Luke Skywalker', 'TypeScript');
console.log(luke.code()); // -> Luke is writing code in TypeScript
console.log(luke.assignEmployee()); // -> Luke does not have permissions to assign employees
console.log(luke.underSupervision()); // -> Luke has 0 employees under his supervision.

const vader = new Manager('1', 'Darth Vader');
console.log(vader.underSupervision()); // -> Darth Vader has 0 employees under his supervision.
console.log(vader.assignEmployee(luke)); // -> Darth Vader is hiring 1 efficient employees and delegating work.
console.log(vader.underSupervision()); // -> Darth Vader has 1 employee under his supervision.
console.log(vader.hireEmployees()); // -> Darth Vader is hiring 8 efficient employees and delegating work.

const han = new ProjectManager('3', 'Han Solo');
console.log(han.underSupervision()); // -> Han Solo has 0 employees under his supervision.
console.log(han.assignEmployee(luke)); // -> Han Solo is hiring 1 efficient employees and delegating work.
console.log(han.underSupervision()); // -> Han Solo has 1 employee under his supervision.
console.log(han.projectPlanning()); // -> Han Solo is defining project scope, objectives, and deliverables.
