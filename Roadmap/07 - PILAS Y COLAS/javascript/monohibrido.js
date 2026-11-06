/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 */

/* PILA -> estructura para almacenar datos de forma lineal y unidireccional - LIFO = Last In First Out */
/* push() -> agrega un nuevo elemento en la última posición del array */


let stack = new Array;
stack.push("A");
stack.push("B");
stack.push("C");

console.log(stack); // [ 'A', 'B', 'C' ]

/* pop() -> Retorna el último valor ingresado a la pila, sacándolo de ésta. */

let ultimo = stack.pop();
console.log(`último = ${ultimo}`); // 'C'
console.log(stack); //[ 'A', 'B' ]


/*  COLAS -> FIFO First In First Out */

let fifito = new Array;
fifito.push("uno", "dos", "tres");
console.log(fifito); // [ 'uno', 'dos', 'tres' ]

/* shift() -> Retorna el primer valor ingresado a la cola, sacándolo de ésta*/
let primero = fifito.shift();

console.log(`primero: ${primero}`); // primero: uno
console.log(fifito); // [ 'dos', 'tres' ]


/******DIFICULTAD EXTRA ******/
/*
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
*/


const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

/*NAVEGADOR WEB*/
/*NAVEGADOR WEB*/

const pilaAtras = [];
const pilaActual = [];
const pilaAdelante = [];

function historial() {
    console.log(`
- Página anterior: ${pilaAtras.join(", ")}
- Página actual: ${pilaActual.join(", ")}
- Página siguiente: ${pilaAdelante.join(", ")}
`);
}

function mostrarPregunta() {
    console.log('¿Qué quieres hacer? Escribe una web nueva, "atras", "adelante" o "salir".');
}

mostrarPregunta();

rl.on("line", (linea) => {
    const sitioweb = linea.trim();
    const comando = sitioweb.toLowerCase();

    if (sitioweb === "") {
        console.log("Debes escribir un sitio web");
    } else if (comando === "atras" || comando === "atrás") {
        if (pilaAtras.length === 0) {
            console.log("No hay historial para atrás");
        } else {
            pilaAdelante.push(pilaActual.pop());
            pilaActual.push(pilaAtras.pop());
        }
    } else if (comando === "adelante") {
        if (pilaAdelante.length === 0) {
            console.log("No hay historial para adelante");
        } else {
            pilaAtras.push(pilaActual.pop());
            pilaActual.push(pilaAdelante.pop());
        }
    } else if (comando === "salir") {
        console.log("Saliendo...");
        rl.close();
        return;
    } else {
        if (pilaActual.length > 0) {
            pilaAtras.push(pilaActual.pop());
        }
        pilaActual.push(sitioweb);
        pilaAdelante.length = 0;
    }

    historial();
    mostrarPregunta();
});

/*************IMPRESORA*********************/
/*
const colaDocumentos = [];
let estado = "menu";

function mostrarMenu() {
    console.log(`
Elige una opción:
1. Agregar documento a la cola.
2. Imprimir.
3. Salir.
`);
}

function mostrarCola() {
    if (colaDocumentos.length === 0) {
        console.log("La cola de impresión está vacía.");
    } else {
        console.log(`La cola de impresión es: ${colaDocumentos.join(", ")}`);
    }
}

mostrarMenu();

rl.on("line", (linea) => {
    const texto = linea.trim();

    if (estado === "esperandoDocumento") {
        if (texto === "") {
            console.log("El nombre no puede estar vacío. Escríbelo de nuevo:");
            return;
        }

        colaDocumentos.push(texto);
        console.log(`Documento "${texto}" agregado.`);
        mostrarCola();

        estado = "menu";
        mostrarMenu();
        return;
    }

    switch (texto) {
        case "1":
            estado = "esperandoDocumento";
            console.log("Escribe el nombre del documento:");
            break;

        case "2":
            if (colaDocumentos.length === 0) {
                console.log("No hay documentos para imprimir.");
            } else {
                const documentoAImprimir = colaDocumentos.shift();
                console.log(`Imprimiendo: ${documentoAImprimir}`);
            }
            mostrarCola();
            mostrarMenu();
            break;

        case "3":
            console.log("Saliendo...");
            rl.close();
            break;

        default:
            console.log("La respuesta no está dentro de las opciones.");
            mostrarMenu();
            break;
    }
});

*/