/*
    #08 CLASES 
*/
class Persona {

    // Inicializador (constructor)
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    // Función para imprimir los atributos
    imprimirInformacion() {
        console.log(`Nombre: ${this.nombre}`);
        console.log(`Edad: ${this.edad}`);
    }

    // Métodos adicionales (opcional)

    setNombre(nombre) {
        this.nombre = nombre;
    }

    getNombre() {
        return this.nombre;
    }

    setEdad(edad) {
        this.edad = edad;
    }

    getEdad() {
        return this.edad;
    }
}


const person1 = new Persona('Juan', 30);
person1.imprimirInformacion();
person1.setNombre('Pedro');
person1.setEdad(25);
person1.imprimirInformacion();
console.log(person1.getNombre());
console.log(person1.getEdad());
console.log(person1);

/* 
  DIFICULTAD EXTRA
*/

class Pila {
    constructor(pila) {
        this.pila = pila;
    }

    push(dato) {
        this.pila.push(dato);
    }

    pop() {
        return this.pila.pop();
    }

    imprimir() {
        console.log(this.pila);
    }
}

const pila1 = new Pila([]);
pila1.push(1);
pila1.push(2);
pila1.push(3);
pila1.imprimir();
console.log(pila1.pop());
pila1.imprimir();

class Cola {
    constructor(cola) {
        this.cola = cola;
    }

    enqueue(dato) {
        this.cola.push(dato);
    }

    dequeue() {
        return this.cola.shift();
    }


    imprimir() {
        console.log(this.cola);
    }
}

const cola1 = new Cola([]);
cola1.enqueue(1);
cola1.enqueue(2);
cola1.enqueue(3);
cola1.imprimir();
console.log(cola1.dequeue());
cola1.imprimir();
console.log(cola1);