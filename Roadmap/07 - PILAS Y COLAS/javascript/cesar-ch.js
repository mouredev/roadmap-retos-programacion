/*
    #07 PILAS Y COLAS
*/


// pila
let pila = []

// push
pila.push(1)
pila.push(2)
pila.push(3)

// pop
pila.pop()
console.log(pila)

// cola
let cola = []

// enqueue
cola.push(1)
cola.push(2)
cola.push(3)

// dequeue
cola.shift()
console.log(cola)

/*
    DIFICULTAD EXTRA
*/

function webNavigation() {
    let stack = [];

    while (true) {
        let action = prompt("Añade una url o interactúa con palabras adelante/atras/salir: ");

        if (action === "salir") {
            console.log("Saliendo del navegador web.");
            break;
        } else if (action === "adelante") {
            continue
        } else if (action === "atras") {
            if (stack.length > 0) {
                stack.pop();
            }
        } else {
            stack.push(action);
        }

        if (stack.length > 0) {
            console.log(`Has navegado a la web: ${stack[stack.length - 1]}.`);
        } else {
            console.log("Estás en la página de inicio.");
        }
    }
}

// webNavigation();

function printed() {
    let queue = [];

    while (true) {
        let action = prompt("Añade un documento o selecciona imprimir/salir: ");

        if (action === "salir") {
            break;
        } else if (action === "imprimir") {
            if (queue.length > 0) {
                console.log(`Imprimiendo: ${queue.shift()}`);
            }
        } else {
            queue.push(action);
        }
        console.log(`Cola de impresión: ${queue}`);
    }
}

printed();