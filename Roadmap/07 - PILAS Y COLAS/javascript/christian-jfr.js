// #07 PILAS Y COLAS

/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 */

/** === PILAS ===
 * Convencion para nombrar metodos:
 * push: Agrega un nuevo valor a la pila, ubicándolo al final de ésta.
 * pop: Retorna el último valor ingresado a la pila, sacándolo de ésta.
 * peek: Retorna el último valor ingresado a la pila, sin sacarlo de ésta.
 * size: Retorna el número de elementos que contiene la pila.
 * print: Muestra el contenido de la pila.
 */

// PILA con Array
class StackOnArray {
	constructor() {
		this.stack = [];
	}

	push(element) {
		this.stack.push(element);
		return this.stack;
	}

	pop() {
		return this.stack.pop();
	}

	peek() {
		return this.stack[this.stack.length - 1];
	}

	size() {
		return this.stack.length;
	}

	print() {
		console.log(this.stack);
	}
}

const colorStack = new StackOnArray();

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

// PILA con Objeto
class StackOnObject {
	constructor() {
		this.stack = {};
		this.top = 0;
	}

	push(element) {
		this.stack[this.top] = element;
		this.top++;
		return this.stack;
	}

	pop() {
		const element = this.stack[this.top - 1];
		delete this.stack[this.top - 1];
		this.top--;
		return element;
	}

	peek() {
		return this.stack[this.top - 1];
	}

	size() {
		return this.top;
	}

	print() {
		console.log(this.stack);
	}
}

const userStack = new StackOnObject();

console.log(`Check stack size: ${userStack.size()}`); // 0
console.log(`push element: ${userStack.push('John')}`); // -> { '0': 'John' }
console.log(`push element: ${userStack.push('Jane')}`); // -> { '0': 'Jane' }
console.log(`push element: ${userStack.push('Jim')}`); // -> { '0': 'Jim' }
userStack.print(); // -> { '0': 'John', '1': 'Jane', '2': 'Jim' }
console.log(`peek last element: ${userStack.peek()}`); // -> 'Jim'
console.log(`pop last element: ${userStack.pop()}`); // -> 'Jim'
console.log(`Check stack size: ${userStack.size()}`); // -> 2
userStack.print(); // -> { '0': 'John', '1': 'Jane' }

/**
 * === COLAS ===
 * Convencion para nombrar metodos:
 * enqueue: Agrega un nuevo elemento a la cola, situándolo al final de ésta.
 * dequeue: Retorna el primer elemento de la cola, quitándolo de ésta.
 * peek: Retorna el primer elemento de la cola, sin quitarlo de ésta.
 * size: Retorna el número de elementos que contiene la cola.
 * print: Muestra el contenido de la cola.
 * **isEmpty: Verifica si la cola está vacía.**
 */

// Cola con Array
class QueueOnArray {
	constructor() {
		this.queue = [];
	}

	enqueue(element) {
		this.queue.push(element);
		return this.queue;
	}

	dequeue() {
		return this.queue.shift();
	}

	peek() {
		return this.queue[0];
	}

	size() {
		return this.queue.length;
	}

	print() {
		console.log(this.queue);
	}

	isEmpty() {
		return this.queue.length === 0;
	}
}

const numbersQueue = new QueueOnArray();

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

// DIFICULTAD EXTRA (opcional):

/**
 * Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 * de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 * que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 * Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 * el nombre de una nueva web.
 */
// Solucion con entorno NodeJS
import { createInterface } from 'readline';

const rl = createInterface({
	input: process.stdin,
	output: process.stdout,
});

class BrowserHistory {
	constructor() {
		this.history = ['Home'];
		this.forwardStack = [];
	}

	push(url) {
		this.history.push(url);
		console.log(`Navigated to ${url}`);
	}

	pop() {
		const prevUrl = this.history.pop();
		if (prevUrl) {
			this.forwardStack.push(prevUrl);
			console.log(`Navigated back from ${prevUrl}`);
		} else {
			console.log('No backward history available.');
		}
		return prevUrl;
	}

	forward() {
		const nextUrl = this.forwardStack.pop();
		if (nextUrl) {
			this.history.push(nextUrl);
			console.log(`Navigated forward to ${nextUrl}`);
		} else {
			console.log('No forward history available.');
		}
		return nextUrl;
	}

	peek() {
		return this.history?.[this.history.length - 1] ?? 'Home';
	}

	size() {
		return this.history.length + this.forwardStack.length;
	}

	print() {
		console.log(`Back History:\n ${this.history.join('\n ')}`);
		console.log('\n=========================================\n');
		console.log(`Forward History:\n ${this.forwardStack.join('\n ')}`);
	}
}

const history = new BrowserHistory();

browserSimulator();

function browserSimulator() {
	console.clear();
	// console.log(history.print());

	console.log(`Current Page: ${history.peek()}`);

	rl.question(
		'Browser Simulator\nEnter "forward" or "back" to navigate\nOr enter a new URL: ',
		(answer) => {
			switch (answer) {
				case '':
					browserSimulator();
					break;

				case 'size':
					historySize();
					break;

				case 'history':
					browsingHistory();
					break;

				case 'forward':
					navForward();
					break;

				case 'back':
					back();
					break;

				case 'exit':
					console.clear();
					process.exit();

				default:
					addUrl(answer);
			}
		}
	);
}

function load() {
	setTimeout(() => {
		browserSimulator();
	}, 1000);
}

function addUrl(url) {
	history.push(url);
	load();
}

function back() {
	history.pop();
	console.log(`... to ${history.peek()}`);
	load();
}

function navForward() {
	history.forward();
	load();
}

function browsingHistory() {
	history.print();
	load();
}

function historySize() {
	console.log(`History Size: ${history.size()}`);
	load();
}

/* Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 * impresora compartida que recibe documentos y los imprime cuando así se le indica.
 * La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 * interpretan como nombres de documentos.
 */
// Solucion con entorno NodeJS
import { createInterface } from 'readline';

const rlPrinter = createInterface({
	input: process.stdin,
	output: process.stdout,
});

class printerQueue {
	constructor() {
		this.queue = ['Lorem Ipsum'];
	}

	enqueue(document) {
		this.queue.push(document);
		return this.queue;
	}

	dequeue() {
		return this.queue.shift();
	}

	peek() {
		return this.queue[0];
	}

	size() {
		return this.queue.length;
	}

	print() {
		console.log(this.queue.join('\n'));
	}

	isEmpty() {
		return this.queue.length === 0;
	}
}

const printer = new printerQueue();

printerSimulator();

function printerSimulator() {
	console.clear();

	if (printer.isEmpty()) {
		console.log('Queue is empty');
	} else {
		console.log(`Next in queue: ${printer.peek()}`);
	}

	rlPrinter.question(
		'Printer Simulator\nEnter "print" to print next document in queue\nOr enter a document name to enqueue:',
		(answer) => {
			switch (answer) {
				case '':
					printerSimulator();
					break;

				case 'print':
					printStart();
					break;

				case 'check':
					checkAllQueue();
					break;

				case 'delete':
					deleteDoc();
					break;

				case 'exit':
					console.clear();
					process.exit();

				default:
					addDocument(answer);
			}
		}
	);
}

function loadPrinter() {
	setTimeout(() => {
		printerSimulator();
	}, 1000);
}

function printStart() {
	if (printer.isEmpty()) {
		console.log('Queue is empty');
	} else {
		console.log(`Printing ${printer.dequeue()} ...`);
	}
	loadPrinter();
}

function addDocument(document) {
	console.log(`adding document "${document}" to the queue...`);
	printer.enqueue(document);
	loadPrinter();
}

function checkAllQueue() {
	if (printer.isEmpty()) {
		console.log('Queue is empty');
	} else {
		console.log(`Next in queue: ${printer.print()}`);
	}
	loadPrinter();
}

function deleteDoc() {
	if (printer.isEmpty()) {
		console.log('Queue is empty');
	} else {
		console.log(`Deleting ${printer.dequeue()}...`);
	}
	loadPrinter();
}
