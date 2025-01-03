//EJERCICIO
//LIFO. Last in first out: el ultimo en entrar es el primero en salir
let miStack = [1, 2, 3, 4];
console.log("\n---PILAS (STACKS - LIFO)---");
console.log("Antes de agregar elemento: \n", miStack);
miStack.push(5);
console.log("Agregando elemento: \n", miStack);
miStack.pop();
console.log("Después de quitar elemento: \n", miStack);

//FIFO. First in first out: el primero en entrar es el primero en salir
let miQueue = [1, 2, 3, 4];
console.log("\n---COLAS (QUEUE - FIFO)---");
console.log("Antes de agregar elemento: \n", miQueue);
miQueue.push(5);
console.log("Agregando elemento: \n", miQueue);
miQueue.shift();
console.log("Después de quitar elemento: \n", miQueue);

//EXTRA
const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

let navegador = () => {
	let pila = [];

	function muestraPagina() {
		if (pila.length > 0) {
			console.log(`\nAhora estás en ${pila[pila.length - 1]}`);
		} else {
			console.log("\nEstás en la HomePage");
		}

		muestraOpciones();
	}

	function muestraOpciones() {
		rl.question(
			"\nELige una opción o introduce una url: \n(1)Ir adelante \n(2)Ir atrás \n(3)Salir \n",
			(opcion) => {
				switch (opcion) {
					case "1":
						if (pila.length > 0) {
							console.log("\nHistorial borrado. Adquiera la suscripción para configurar");
						}
						muestraPagina();
						break;
					case "2":
						if (pila.length > 0) {
							pila.pop();
						}
						muestraPagina();
						break;
					case "3":
						console.log("\nSaliendo del navegador... abriendo impresora...");
						impresoraCompartida();
						break;
					default:
						pila.push(opcion);
						muestraPagina();
				}
			}
		);
	}

	muestraPagina();
};

let impresoraCompartida = () => {
	rl.resume();
	let cola = [];

	function muestraOpciones() {
		if (cola.length > 0) {
			console.log(
				`\nCola de impresión actual(${cola.length}): ${cola.join(", ")}`
			);
		} else {
			console.log("\nNo hay documentos en cola");
		}

		rl.question(
			"\nAgregue un documento o elija: \n(1)Imprimir \n(2)Salir \n",
			(opcion) => {
				switch (opcion) {
					case "1":
						if (cola.length > 0) {
							console.log(`\nImprimiendo ${cola[0]}`);
							cola.shift();
						}
						muestraOpciones();
						break;
					case "2":
						console.log("\nSaliendo de impresora...");
						rl.close();
						break;
					default:
						cola.push(opcion);
						muestraOpciones();
				}
			}
		);
	}

	muestraOpciones();
};

navegador();