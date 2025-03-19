// #08 CLASES

/**
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 */

// sin inicializador constructor
class Class {
	sayHello() {
		console.log('Hello');
	}
}

const classInstance = new Class();
classInstance.sayHello(); // -> Hello

// con inicializador constructor
class User {
	// inicializador constructor
	constructor(name, id) {
		this.name = name;
		this.id = id;
	}

	// funcion imprimir
	print() {
		console.log(`Name: ${this.name}`);
		console.log(`Id: ${this.id}`);
	}

	// Modificar atributos
	editName(newName) {
		this.name = newName;
	}

	editId(newId) {
		this.id = newId;
	}
}

const user = new User('asdf', 99);
user.print(); // -> Name: asdf, Id: 99

user.editName('Christian');
user.editId(16);
user.print(); // -> Name: Christian, Id: 16

// herencia inheritance
class Teacher extends User {
	constructor(name, id, teaches) {
		super(name, id);
		this.teaches = teaches;
	}

	print() {
		super.print();
		console.log(`Teaches: ${this.teaches}`);
	}
}

const moure = new Teacher('Moure', 0, 'Cooking');
moure.print(); // -> Name: Moure, Id: 0, Teaches: Cooking

// encapsulamiento encapsulation
class Student extends User {
	constructor(name, id, grade) {
		super(name, id);
		this.grade = grade;
	}

	print() {
		super.print();
		console.log(`Grade: ${this.grade}`);
	}
}

const christian = new Student('Christian', 16, 10);
christian.print(); // -> Name: Christian, Id: 16, Grade: 10

/** DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 *
 */

// Pilas
class Stack {
	// inicializador constructor
	constructor() {
		this.stack = [];
	}
	// añadir elemento
	push(element) {
		this.stack.push(element);
		return this.stack;
	}
	// eliminar ultimo elemento en entrar
	pop() {
		return this.stack.pop();
	}
	// retornar ultimo elemento que entro
	peek() {
		return this.stack[this.stack.length - 1];
	}
	// ver el tamaño de la pila
	size() {
		return this.stack.length;
	}
	// imprimir contenido de la pila
	print() {
		console.log(this.stack);
	}
}

const colorStack = new Stack();

console.log(`Check stack size: ${colorStack.size()}`); // -> 0
console.log(`push element: ${colorStack.push('Yellow')}`); // -> ["Yellow"]
console.log(`push element: ${colorStack.push('Blue')}`); // -> ["Yellow", "Blue"]
console.log(`push element: ${colorStack.push('Red')}`); // -> ["Yellow", "Blue", "Red"]
console.log(`Check stack size: ${colorStack.size()}`); // -> 3
colorStack.print(); // -> ["Yellow", "Blue", "Red"]
console.log(`peek last element: ${colorStack.peek()}`); // -> "Red"
console.log(`pop last element: ${colorStack.pop()}`); // -> "Red"
console.log(`Check stack size: ${colorStack.size()}`); // -> 2
colorStack.print(); // -> ["Yellow", "Blue"]

// Colas
class Queue {
	// inicializador constructor
	constructor() {
		this.queue = [];
	}
	// añadir elemento a la cola
	enqueue(element) {
		this.queue.push(element);
		return this.queue;
	}
	// eliminar primer elemento de la cola
	dequeue() {
		return this.queue.shift();
	}
	// retornar primer elemento de la cola
	peek() {
		return this.queue[0];
	}
	// ver el tamaño de la cola
	size() {
		return this.queue.length;
	}
	// imprimir contenido de la cola
	print() {
		console.log(this.queue);
	}
	// verificar si la cola esta vacia
	isEmpty() {
		return this.queue.length === 0;
	}
}

const numbersQueue = new Queue();

console.log(`Empty queue? ${numbersQueue.isEmpty()}`); // -> true
console.log(`enqueue element: ${numbersQueue.enqueue(1)}`); // -> [1]
console.log(`enqueue element: ${numbersQueue.enqueue(2)}`); // -> [1, 2]
console.log(`enqueue element: ${numbersQueue.enqueue(3)}`); // -> [1, 2, 3]
console.log(`Check queue size: ${numbersQueue.size()}`); // -> 3
numbersQueue.print(); // -> [1, 2, 3]
console.log(`Empty queue? ${numbersQueue.isEmpty()}`); // -> false
console.log(`Check first element: ${numbersQueue.peek()}`); // -> 1
console.log(`dequeue first element: ${numbersQueue.dequeue()}`); // -> 1
console.log(`Check queue size: ${numbersQueue.size()}`); // -> 2
numbersQueue.print(); // -> [2, 3]
