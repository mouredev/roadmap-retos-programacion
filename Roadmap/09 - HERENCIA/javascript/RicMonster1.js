/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */

class Animal {
	constructor(nombre) {
		this.nombre = nombre;
	}
	sonido() {}
}

class Gato extends Animal {
	sonido() {
		console.log('miau');
	}
}

class Perro extends Animal {
	sonido() {
		console.log('Guau');
	}
}

let = emiteSonido = (Animal) => {
	Animal.sonido();
};

let miAnimal = new Animal('Ter');

miAnimal.sonido();

let miPerro = new Perro('Ferr');

miPerro.sonido();

let miGato = new Gato('Fran');

miGato.sonido();

emiteSonido(miAnimal);

emiteSonido(miPerro);

emiteSonido(miGato);

/* DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un especie.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

class Empleado {
	constructor(nombre, id) {
		this.nombre = nombre;
		this.id = id;
	}
}

class Gerente extends Empleado {
  coordinando(){
    console.log(`${this} coordina todos los proyectos`);
  }
}

class GerenteDeProyecto extends Empleado {
  coordinando(){
    console.log(`${this} coordina su proyecto`);
  }
}

class Programador extends Empleado {
  coordinando(){
    console.log(`${this} programa`);
  }
}
