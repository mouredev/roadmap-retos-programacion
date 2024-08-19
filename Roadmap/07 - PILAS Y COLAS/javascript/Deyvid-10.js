// pilas (stacks - LIFO)

let pila = [1, 2, 3]

pila.push(4) // push - Agrega un elemento al tope de la pila
console.log(pila);
pila.pop() // pop - Elimina el elemento en el tope de la pila
console.log(pila);
console.log(pila[pila.length-1]); // peek - Devuelve el elemento en el tope de la pila sin eliminarlo
console.log(pila.length === 0); // isEmpty - Comprueba si la pila está vacía

// colas (queue - FIFO)

let cola = [1, 2, 3]

cola.push(4) // enqueue - Agrega un elemento al final de la cola
console.log(cola);
cola.shift() // dequeue - Elimina el primer elemento de la cola
console.log(cola);
console.log(cola[0]); // front - Devuelve el primer elemento de la cola sin eliminarlo
console.log(cola.length === 0); // isEmpty - Comprueba si la cola está vacía