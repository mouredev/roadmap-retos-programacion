/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */
class Persona {
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    imprimirDatos() {
        console.log(`Nombre: ${this.nombre}, Edad: ${this.edad}`);
    }
}


let persona1 = new Persona('Juan', 30);
persona1.imprimirDatos();

persona1.nombre = 'Ana';
persona1.edad = 25;
persona1.imprimirDatos();


//DIFICULTAD EXTRA 

//DIFICULTAD EXTRA 
class Pila{
    constructor(){
        this.elementos=[]
    }
    agregar(elemento){
        this.elementos.push(elemento)
    }
    eliminar(elemento){
        return this.elementos.pop()
    }
    longitud() {
        return this.elementos.length;
    }
    imprimir() {
        console.log(this.elementos);
    }
}


class Cola {
    constructor() {
        this.elementos = [];
    }

    agregar(elemento) {
        this.elementos.push(elemento);
    }

    eliminar() {
        return this.elementos.shift();
    }

    longitud() {
        return this.elementos.length;
    }

    imprimir() {
        console.log(this.elementos);
    }
}

let miPila = new Pila();
miPila.agregar(1);
miPila.agregar(2);
miPila.agregar(3);
miPila.imprimir();
console.log('Elemento eliminado:', miPila.eliminar());
miPila.imprimir();


let miCola = new Cola();
miCola.agregar(1);
miCola.agregar(2);
miCola.agregar(3);
miCola.imprimir();
console.log('Elemento eliminado:', miCola.eliminar());
miCola.imprimir();