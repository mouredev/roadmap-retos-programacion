import "./style.css";

/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */

class Animal {
	constructor(sound) {
		this.sound = sound;
	}

	makeSound() {
		console.log(this.sound);
	}
}

class Perro extends Animal {
	constructor() {
		super("Guau");
	}
}

class Gato extends Animal {
	constructor() {
		super("Miau");
	}
}

const perro = new Perro();
const gato = new Gato();
perro.makeSound();
gato.makeSound();

/*
* DIFICULTAD EXTRA (opcional):
* Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
* pueden ser Gerentes, Gerentes de Proyectos o Programadores.
* Cada empleado tiene un identificador y un nombre.
* Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
* actividad, y almacenan los empleados a su cargo.
*/

class Empleado {
	constructor(id, nombre) {
		this.id = id;
		this.nombre = nombre;
	}
}

class Gerente extends Empleado {
	constructor(id, nombre) {
		super(id, nombre);
		this.empleados = [];
	}

	addEmpleado(empleado) {
		this.empleados.push(empleado);
	}
}

class GerenteProyecto extends Gerente {
	projects = [];

	constructor(id, nombre) {
		super(id, nombre);
	}

	assignProject(project) {
		this.projects.push(project);
	}
}

class Programador extends Empleado {
	constructor(id, nombre) {
		super(id, nombre);
	}

	develop() {
		console.log("Desarrollando...");
	}
}

const gerente = new Gerente(1, "Gerente");
const gerenteProyecto = new GerenteProyecto(2, "Gerente de Proyecto");
const programador = new Programador(3, "Programador");

gerente.addEmpleado(gerenteProyecto);
console.log(gerente);

gerenteProyecto.assignProject("Proyecto 1");
gerenteProyecto.addEmpleado(programador);
console.log(gerenteProyecto);

programador.develop();