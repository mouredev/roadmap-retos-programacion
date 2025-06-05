// Clases

class Persona {

    constructor(nombre, apellido, edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
    }

    saludar(){
        console.log(`Hola, soy ${this.nombre} ${this.apellido} y tengo ${this.edad} años`);
    }
}

let persona1 = new Persona('Fabian', 'Petit', 20);

persona1.saludar();

persona1.edad = 21;

persona1.saludar();

/*
* DIFICULTAD EXTRA (opcional):
* Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
* en el ejercicio número 7 de la ruta de estudio)
* - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
*   retornar el número de elementos e imprimir todo su contenido.
*/

class Pila {

    constructor() {
        this.elementos = [];
    }

    push(elemento){
        this.elementos.push(elemento);
    }

    pop(){

        if(this.isEmpty()){
            return "La pila está vacía";
        }

        return this.elementos.pop();
    }

    peek(){
        
        if(this.isEmpty()){
            return "La pila está vacía";
        }

        return this.elementos[this.elementos.length - 1];
    }

    isEmpty(){
        return this.elementos.length === 0;
    }

    size(){
        return this.elementos.length;
    }
}

let pila = new Pila();
pila.push(10);
pila.push(20);
pila.push(30);

console.log(pila.peek()); // 30
console.log(pila.pop());  // 30
console.log(pila.isEmpty()); // false
console.log(pila.size()); // 2
console.log(pila.elementos);




class Cola {

    constructor() {
        this.elementos = [];
    }

    enqueue(elemento) {
        this.elementos.push(elemento);
    }

    dequeue() {
        if (this.isEmpty()) {
            return "La cola está vacía";
        }
        return this.elementos.shift();
    }

    front() {
        if (this.isEmpty()) {
            return "La cola está vacía";
        }
        return this.elementos[0];
    }

    isEmpty() {
        return this.elementos.length === 0;
    }

    size() {
        return this.elementos.length;
    }
}


let cola = new Cola();
cola.enqueue(10);
cola.enqueue(20);
cola.enqueue(30);

console.log(cola.front()); // 10
console.log(cola.dequeue()); // 10
console.log(cola.isEmpty()); // false
console.log(cola.size()); // 2
console.log(cola.elementos);