// Pilas y Colas 

// Pilas - Stacks (LIFO "Last In First Out")

class Pila {
    constructor() {
        this.elementos = []; // Array para almacenar los elementos de la pila
    }

    // Añadir un elemento al tope de la pila
    push(elemento) {
        this.elementos.push(elemento);
    }

    // Eliminar y devolver el elemento en el tope de la pila
    pop() {
        if (this.isEmpty()) {
            return "La pila está vacía";
        }
        return this.elementos.pop();
    }

    // Ver el elemento en el tope sin eliminarlo
    peek() {
        if (this.isEmpty()) {
            return "La pila está vacía";
        }
        return this.elementos[this.elementos.length - 1];
    }

    // Verificar si la pila está vacía
    isEmpty() {
        return this.elementos.length === 0;
    }

    // Tamaño de la pila
    size() {
        return this.elementos.length;
    }
}

let pila = new Pila();
pila.push(10);
pila.push(20);
pila.push(30);

console.log(pila.peek()); // 30
console.log(pila.pop());  // 30
console.log(pila.pop());  // 20
console.log(pila.isEmpty()); // false
console.log(pila.size()); // 1




// Colas - Queues (FIFO "First In First Out")

class Cola {
    constructor() {
        this.elementos = []; // Array para almacenar los elementos de la cola
    }

    // Añadir un elemento al final de la cola
    enqueue(elemento) {
        this.elementos.push(elemento);
    }

    // Eliminar y devolver el elemento al frente de la cola
    dequeue() {
        if (this.isEmpty()) {
            return "La cola está vacía";
        }
        return this.elementos.shift();
    }

    // Ver el elemento al frente sin eliminarlo
    front() {
        if (this.isEmpty()) {
            return "La cola está vacía";
        }
        return this.elementos[0];
    }

    // Verificar si la cola está vacía
    isEmpty() {
        return this.elementos.length === 0;
    }

    // Tamaño de la cola
    size() {
        return this.elementos.length;
    }
}

// Ejemplo de uso
let cola = new Cola();
cola.enqueue(10);
cola.enqueue(20);
cola.enqueue(30);

console.log(cola.front()); // 10
console.log(cola.dequeue()); // 10
console.log(cola.dequeue()); // 20
console.log(cola.isEmpty()); // false
console.log(cola.size()); // 1