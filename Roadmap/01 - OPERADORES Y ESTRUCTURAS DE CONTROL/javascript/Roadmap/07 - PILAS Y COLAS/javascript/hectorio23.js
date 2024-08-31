// Autor: Héctor Adán 
// GitHub: https://github.com/hectorio23 
const readline = require('readline');

/******************************************
************* CLASE WebPage ***************
******************************************/

class WebPage {
    constructor(title, index) {
        this.title = title;
        this.index = index;
    }

    getInfo() {
        console.log(`<Object WebPage - ${this.title} at ${this}>`);
    }
}

/******************************************
************* CLASE Stack *****************
******************************************/

class Stack {
    constructor() {
        this.items = [];
    }

    push(item) {
        this.items.push(item);
    }

    pop() {
        if (!this.isEmpty()) {
            return this.items.pop();
        }
    }

    isEmpty() {
        return this.items.length === 0;
    }

    get size() {
        return this.items.length;
    }
}

/******************************************
************* CLASE Queue *****************
******************************************/

class Queue {
    constructor() {
        this.items = [];
    }

    push(item) {
        this.items.push(item);
    }

    pop() {
        if (!this.isEmpty()) {
            return this.items.shift();
        }
    }

    isEmpty() {
        return this.items.length === 0;
    }

    get size() {
        return this.items.length;
    }
}

/******************************************
************* FUNCIONES *******************
******************************************/

function imprimirMenu(counter) {
    const stack = new Stack();
    const backStack = new Stack();
    let index = new WebPage("index", counter);
    stack.push(index);

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.setPrompt("\nOpción del usuario> ");

    rl.on('line', (choose) => {
        choose = choose.trim();

        if (choose.length > 1) {
            let temporal = new WebPage(choose, counter);
            stack.push(temporal);
        } else if (choose.toLowerCase() === 'a' && stack.size > 1) {
            let otroTemporal = stack.pop();
            otroTemporal.getInfo();
            stack.items[stack.size - 1].getInfo();
            backStack.push(otroTemporal);
            console.log("Mostrando página anterior...");
        } else if (choose.toLowerCase() === 's' && backStack.size > 0) {
            let atrasTemporal = backStack.pop();
            atrasTemporal.getInfo();
            stack.items[stack.size - 1].getInfo();
            stack.push(atrasTemporal);
            console.log("Mostrando siguiente página...");
        } else {
            console.log("Opción no disponible. Por favor, crea una página web.");
        }

        rl.prompt();
    });

    rl.prompt();
}

/******************************************
************* PROGRAMA PRINCIPAL **********
******************************************/

let q1 = new Queue();
let s1 = new Stack();
let counter = 1;

/******************************************
******** USO DE UN STACK DINÁMICO *********
******************************************/

console.log("\n************ USO DE UN STACK DINÁMICO ************");

let w1 = new WebPage("Index", 2);
let w2 = new WebPage("Account", 5);
let w3 = new WebPage("Login", 6);

console.log(`\nCantidad de elementos de Stack antes de agregarlos: ${s1.size} elementos`);
s1.push(w1);
s1.push(w2);
s1.push(w3);
console.log(`Cantidad de elementos de Stack después de agregarlos: ${s1.size} elementos`);

s1.pop();
s1.pop();
s1.pop();
console.log(`Cantidad de elementos de Stack después de eliminarlos: ${s1.size} elementos`);

/******************************************
******** USO DE UN QUEUE DINÁMICO *********
******************************************/

console.log("\n************ USO DE UN QUEUE DINÁMICO ************");

console.log(`\nCantidad de elementos de Queue antes de agregarlos: ${q1.size} elementos`);
q1.push(w1);
q1.push(w2);
q1.push(w3);
console.log(`Cantidad de elementos de Queue después de agregarlos: ${q1.size} elementos`);

q1.pop();
q1.pop();
q1.pop();
console.log(`Cantidad de elementos de Queue después de eliminarlos: ${q1.size} elementos`);

/******************************************
************* MENU PRINCIPAL **************
******************************************/

imprimirMenu(counter);
