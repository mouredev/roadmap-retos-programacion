/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 */

class Car {
    constructor(initMarca, initModelo, initColor, initPrecio){
        this.marca = initMarca;
        this.modelo = initModelo;
        this.color = initColor;
        this.precio = initPrecio;
    }

    getSpecs(){
        return "| SPECS | Marca: " + this.marca + " | Modelo: " + this.modelo + " | Color: " + this.color + " | Precio: " + this.precio
    }
}

const coche1 = new Car('Ford', 'Fiesta', 'Rojo', 12000);
console.log(coche1.getSpecs())
coche1.modelo = 'Focus'
coche1.color = 'Blanco'
coche1.precio = '18000'
console.log(coche1.getSpecs())



/* DIFICULTAD EXTRA (opcional):
* Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
* en el ejercicio número 7 de la ruta de estudio)
* - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
*   retornar el número de elementos e imprimir todo su contenido.
*/


// PILA (Last In First Out)

class Pila {
    constructor(initElements){
        this.elements = [...initElements];
    }

    insert (element) {
        this.elements.push(element);
    }

    delete () {
        this.elements.pop();
    }

    peek () {
        return this.elements[this.elements.length-1];
    }

    size () {
        return this.elements.length;
    }

    print () {
        return this.elements;
    }
}


const pila1 = new Pila(['Fresa', 'Mango']);
console.log(pila1.print()); 
pila1.insert('Naranja');
pila1.insert('Manzana');
pila1.insert('Pera');
console.log(pila1.print()); 
console.log(pila1.peek()); 
console.log(pila1.size()); 
pila1.delete();
console.log(pila1.print()); 


// COLA First In First Out

class Cola {
    constructor(initElements){
        this.elements = [...initElements]
    }

    insert (element) {
        this.elements.push(element);
    }

    delete () {
        this.elements.shift();
    }

    peek () {
        return this.elements[0];
    }

    size () {
        return this.elements.length;
    }

    print () {
        return this.elements;
    }
}

const cola1 = new Cola(['Papaya', 'Plátano']);
console.log(cola1.print()); 
cola1.insert('Naranja');
cola1.insert('Manzana');
cola1.insert('Pera');
console.log(cola1.print());
console.log(cola1.peek());
console.log(cola1.size());
cola1.delete();
console.log(cola1.print());