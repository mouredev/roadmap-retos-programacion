//Implementacionde una pila

class Stack<T> {
    private items: T[] = [];

    // Añade un elemento al final de la pila
    push(element: T): void {
        this.items.push(element);
    }

    // Retira el último elemento de la pila y lo devuelve
    pop(): T | undefined {
        return this.items.pop();
    }

    // Mira el último elemento de la pila sin retirarlo
    peek(): T | undefined {
        return this.items[this.items.length - 1];
    }

    // Verifica si la pila está vacía
    isEmpty(): boolean {
        return this.items.length === 0;
    }

    // Devuelve el tamaño de la pila
    size(): number {
        return this.items.length;
    }

    // Imprime todos los elementos de la pila
    print(): void {
        console.log(this.items);
    }
}

// Ejemplo de uso
let stack = new Stack<number>();
stack.push(1);
stack.push(2);
stack.push(3);
console.log(stack.pop()); // 3
console.log(stack.peek()); // 2
stack.print(); // [1, 2]

//Implementacion de una cola
class Queue<T> {
    private items: T[] = [];

    // Añade un elemento al final de la cola
    enqueue(element: T): void {
        this.items.push(element);
    }

    // Retira el primer elemento de la cola y lo devuelve
    dequeue(): T | undefined {
        return this.items.shift();
    }

    // Mira el primer elemento de la cola sin retirarlo
    peek(): T | undefined {
        return this.items[0];
    }

    // Verifica si la cola está vacía
    isEmpty(): boolean {
        return this.items.length === 0;
    }

    // Devuelve el tamaño de la cola
    size(): number {
        return this.items.length;
    }

    // Imprime todos los elementos de la cola
    print(): void {
        console.log(this.items);
    }
}

// Ejemplo de uso
let queue = new Queue<number>();
queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(3);
console.log(queue.dequeue()); // 1
console.log(queue.peek()); // 2
queue.print(); // [2, 3]
