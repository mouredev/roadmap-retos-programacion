/*
Ejercicio
*/

// Pila/Stack (LIFO)

// push
let stack = [];
stack.push(1);
stack.push(2);
stack.push(3);
console.log(stack);

// pop
let stackItem = stack[stack.length - 1];
stack.pop();

console.log(stackItem);
console.log(stack);

stackItem = stack[stack.length - 1];
stack.pop();

console.log(stackItem);
console.log(stack);


// Cola/Queue (FIFO)

let queue = [];

// enqueue
queue.push(1);
queue.push(2);
queue.push(3);

// dequeue 
let queueItem = queue[0];
queue.shift();

console.log(queueItem);
console.log(queue);

queueItem = queue[0];
queue.shift();

console.log(queueItem);
console.log(queue);


/*
Extra
*/

// Web


const realine = require("node:readline/promises");

const rl = realine.createInterface({
    input: process.stdin,
    output: process.stdout
});


async function webNavigation() {
    let stack = [];
    let forwardStack = [];

    while(true){

        const action = await rl.question("Añade una url o interactua con palabras adelante/atras/salir: ");
    
        if (action === "salir") {
            console.log("Saliendo del navegador web");
            break;
        } else if (action === "adelante") {
            if(forwardStack.length > 0){
                const page = forwardStack.pop();
                stack.push(page);
            };
        } else if (action === "atras") {
            if(stack.length > 0){
                const page = stack.pop();
                forwardStack.push(page);
            }
        } else {
            forwardStack = [];
            stack.push(action);
        };

        if (stack.length > 0) {
            console.log(`Has navegado a la web: ${stack[stack.length - 1]}`);
        } else {
            console.log("Estas en la pagina de inicio");
        };
    };

};

webNavigation();


async function sharedPrinted() {
    let queue = [];

    while(true){

        const action = await rl.question("Añade un documento o selecciona imprimir/salir: ");

        if (action === "salir"){
            break;
        } else if (action === "imprimir"){
            if (stack.length > 0){
                console.log(`Imprimiendo: ${queue.shift()}`);
            }
        } else {
            queue.push(action);
        };

        console.log(`Cola de impresion: ${queue}`);
    };
};

sharedPrinted();