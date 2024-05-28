/** #08 - JavaScript ->Jesus Antonio Escamilla */
/**
 * Las cales son plantillas para crear objetos.
 *  Las clases son una forma de encapsular datos y funciones relacionadas en un solo objeto,
    proporcionando una estructura más organizada y orientada a objetos al código JavaScript. 
 */

//-----CLASE-----
class Persona{
    // Inicializar
    constructor(nombre, edad){
        this.nombre = nombre;
        this.edad = edad;
    }

    // Función
    saludar(){
        console.log(`Hola, soy ${this.nombre} y tengo ${this.edad} años.`);
    }
}

// Crear un objeto para usar la clase
const persona1 = new Persona("Jesus Antonio", 24);

// Imprime la información
persona1.saludar(); // Llama el saludo que esta dentro de la clase

// Modificación del objeto
persona1.nombre = "Fatima";
persona1.edad = 19;

// Imprimir información después de la modificación
persona1.saludar();



/**-----DIFICULTAD EXTRA-----*/

//-----PILAS-----
class Stack{
    constructor() {
        this.pila = [];
    }

    push(item) {
        return this.pila.push(item);
    }

    pop() {
        if(this.count() == 0){
            return "None";
        }else{
            return this.pila.pop();
        }
    }

    count() {
        return this.pila.length;
    }

    print(){
        return console.log(this.pila);
    }
}

//  Ejemplo de Pila
const myStack = new Stack();
myStack.push("A");
myStack.push("B");
myStack.push("C");
console.log(myStack.count()); // Imprime -> 3
myStack.print(); //[ 'A', 'B', 'C' ]
console.log(myStack.pop()); // Imprime -> 'C'
console.log(myStack.pop()); // Imprime -> 'B'
console.log(myStack.pop()); // Imprime -> 'A'
console.log(myStack.pop()); // Imprime -> None
console.log(myStack.print()); // Imprime -> undefined - Ya no hay elementos en la lista



//-----COLAS-----
class Queue{
    constructor() {
        this.cola = [];
    }

    enqueue(item) {
        return this.cola.push(item);
    }

    dequeue() {
        if (this.count() == 0) {
            return "None"
        }else{
            return this.cola.shift();
        }
    }

    count() {
        return this.cola.length;
    }

    print() {
        return console.log(this.cola);
    }
}

//  Ejemplo de Cola
const myQueue = new Queue();
myQueue.enqueue("A");
myQueue.enqueue("B");
myQueue.enqueue("C");
console.log(myQueue.count());
myQueue.print(); //[ 'A', 'B', 'C' ]
console.log(myQueue.dequeue()); // Imprime -> 'A'
console.log(myQueue.dequeue()); // Imprime -> 'B'
console.log(myQueue.dequeue()); // Imprime -> 'C'
console.log(myQueue.dequeue()); // Imprime -> None
console.log(myQueue.print()); // Imprime -> undefined - Ya no hay elementos en la lista

/**-----DIFICULTAD EXTRA-----*/