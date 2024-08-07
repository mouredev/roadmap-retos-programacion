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
 */


class Person {

    languages = []
    
    constructor(name, username, age) {
        this.name = name;
        this.username = username;
        this.age = age;
    }
    
    printPerson() {
        console.log(`\nPrinting ${this.username}'s data:`);
        console.log('name:', this.name);
        console.log('age:', this.age);
        
        if (this.languages) {
            console.log('This person uses the following languages to code:');
            for (let language of this.languages) {
                console.log(` - ${language}`);
            }
        }
    }
}
        

me = new Person(name='Naia', username='nlarrea', age=25);
me.printPerson();
me.languages = ['Python', 'JavaScript', 'Kotlin'];
me.printPerson();
me.age = 26;
me.printPerson();


/*
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */


console.log('\nLIFO:\n')


/**
 * Stack is a LIFO (Last In First Out).
 */
class Stack{
    constructor() {
        this.stack = [];
    }
    
    add(...items) {
        this.stack = this.stack.concat([...items]);
    }
        
    remove() {
        if (this.length() === 0) {
            return null;
        }
        return this.stack.pop();
    }
        
    length() {
        return this.stack.length;
    }
        
    print() {
        for (let item of this.stack.slice().reverse()) {
            console.log(item);
        }
    }
}
        

lifo = new Stack();
lifo.add(1, 2, 3);
lifo.print();
/*
3
2
1
*/
console.log('LIFO length:', lifo.length());
// LIFO length: 3

lifo.remove();  // This would print the number 3 because it's the removed one
lifo.print();
/*
2
1
*/
console.log('LIFO length:', lifo.length());
// LIFO length: 2


console.log('\nFIFO:\n');


/**
 * A Queue is a FIFO (First In, First Out).
 */
class Queue {
    constructor() {
        this.queue = [];
    }

    add(...items) {
        this.queue = this.queue.concat([...items]);
    }
    
    remove() {
        if (this.length() === 0) {
            return null;
        }
        return this.queue.shift();
    }

    length() {
        return this.queue.length;
    }
    
    print() {
        for (let item of this.queue) {
            console.log(item);
        }
    }
}
        

fifo = new Queue();
fifo.add(1, 2, 3);
fifo.print();
/*
1
2
3
*/
console.log('FIFO length:', fifo.length());
// FIFO length: 3

fifo.remove();
fifo.print();
/*
2
3
*/
console.log('FIFO length:', fifo.length());
// FIFO length: 2