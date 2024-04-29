/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 */

//===CONCEPTO DE CLASE===//
console.log('\n-CREANDO UNA CLASE-');
class Estudiante {
	constructor(nombre, edad, carrera, semestre) {
		this.nombre = nombre;
		this.edad = edad;
		this.carrera = carrera;
		this.semestre = semestre;
	}

	muestraPropiedades() {
		console.log(
			`  Nombre: ${this.nombre}, edad: ${this.edad}, carrera: ${this.carrera}, semestre: ${this.semestre}.`
		);
	}
}

let estuadiante1 = new Estudiante(
	'Ricardo',
	21,
	'Ingieneria de sistemas',
	'primer semestre'
);

console.log(
	'*Aquí imprimimos el objeto creado a partir de la clase:\n',
	estuadiante1
);

console.log(
	'\n*Ahora utilizaremos el método de la clase para ver sus propiedades:'
);
estuadiante1.muestraPropiedades();

console.log(
	'\n*Aquí imprimimos una propiedad en específico antes de modificarla:'
);
console.log(`  Edad: ${estuadiante1.edad}`);

estuadiante1.edad = 22;
estuadiante1.semestre = 'tercer semestre';

console.log('\n*Aquí imprimimos la misma propiedad luego de modificarla:');
console.log(`  Edad: ${estuadiante1.edad}`);

console.log('\n*Utilizando el método se vería así:');
estuadiante1.muestraPropiedades();

console.log('\n*He actualizado el semestre también :D');

/*
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 *
 */

//===CREANDO CLASE PILA===//
console.log('\n-PILA-');
class Pila {
	constructor() {
		this.pila = [];
	}

	apilar(elemento) {
		this.pila.push(elemento);
	}

	desapilar() {
		if (this.pila.length > 0) {
			return this.pila.pop();
		} else {
			console.log('\nPila vacía');
		}
	}

	contar() {
		if (this.pila.length > 0) {
      return this.pila.length;
		} else {
			return '\nPila vacía';
		}
	}

	mostrar() {
		console.log(`\nContenido de la pila: \n${this.pila}`);
	}
}

console.log('\n*Ya hecha la clase y sus métodos, creamos una nueva pila y le apilamos elementos, cuya cantidad y contenido podemos mostrar en consola:');

let myStack = new Pila();

myStack.apilar(23);
myStack.apilar(43);
myStack.apilar(12);
myStack.apilar(98);
myStack.apilar(100);

console.log(`\nCantidad de elementos de la pila: ${myStack.contar()}`);

myStack.mostrar();

console.log('\n*Probamos desapilar elementos y volvemos a mostrar la cantidad y contenido:');

myStack.desapilar();

console.log(`\nCantidad de elementos de la pila: ${myStack.contar()}`);

myStack.mostrar();

console.log('\n*Creamos una nueva pila para que nos muestre este mensaje cuando esté vacía:');

let myStack2 = new Pila();

console.log(`\nCantidad de elementos de la nueva pila: ${myStack2.contar()}`);

//===CREANDO CLASE COLA===//
console.log('\n-COLA-');
class Cola {
	constructor() {
		this.cola = [];
	}

	encolar(elemento) {
		this.cola.push(elemento);
	}

	desencolar() {
		if (this.cola.length > 0) {
			return this.cola.shift();
		} else {
			console.log('\nCola vacía');
		}
	}

	contar() {
		if (this.cola.length > 0) {
      return this.cola.length;
		} else {
			return '\nCola vacía';
		}
	}

	mostrar() {
		console.log(`\nContenido de la cola: \n${this.cola}`);
	}
}

console.log('\n*Ya hecha la clase y sus métodos, creamos una nueva cola y encolamos elementos, cuya cantidad y contenido podemos mostrar en consola:');

let myQueue = new Cola();

myQueue.encolar(12);
myQueue.encolar(20);
myQueue.encolar(33);
myQueue.encolar(200);
myQueue.encolar(1);

console.log(`\nCantidad de elementos de la cola: ${myQueue.contar()}`);

myQueue.mostrar();

console.log('\n*Probamos desencolar elementos y volvemos a mostrar la cantidad y contenido:');

myQueue.desencolar();

console.log(`\nCantidad de elementos de la cola: ${myQueue.contar()}`);

myQueue.mostrar();

console.log('\n*Creamos una nueva cola para ver este mensaje si está vacía:');

let myQueue2 = new Cola();

console.log(`\nCantidad de elementos de la nueva cola: ${myQueue2.contar()}`);