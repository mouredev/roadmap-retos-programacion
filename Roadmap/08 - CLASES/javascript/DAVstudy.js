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

class Developer {
    constructor(name, code, level, alias = 'Sin alias') {
        this.name = name
        this.code = code
        this.level = level
        this.alias = alias
    }

    infoDev = () =>  `${this.name} tiene un nivel de ${this.level}, programando en ${this.exp}` 

    setAlias = function (alias) {
        this.alias = alias        
    }

}

let developer1 = new Developer('Diego', 'JavaScript', 'principiante')

console.log(developer1.infoDev());

console.log(developer1.alias);

developer1.setAlias('DevsDav')

console.log(developer1.alias)


/*
*
* DIFICULTAD EXTRA (opcional):
* Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
* en el ejercicio número 7 de la ruta de estudio)
* - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
*   retornar el número de elementos e imprimir todo su contenido.
*
*/

class Stack {

    constructor(initialElements = []) {
        this.stack = [...initialElements]
        this.lengthStack = this.stack.length
    }

    addElement(element) {
        this.stack.push(element)
        this.lengthStack = this.stack.length
    }

    getElement() {
        let element = this.stack.pop()
        this.lengthStack = this.stack.length
        return element
    }

    show() {
        console.log('Top')
        console.log('---')
        for (let i = this.stack.length - 1; i >= 0; i--) {
            if (i === this.stack.length - 1) {
                console.log(this.stack[i] + '  <-  ultimo en entrar, primero en salir.')
            }
            console.log(this.stack[i])
        }
        console.log('---')
        console.log('Bot')
    }


}

let myStack = new Stack()
console.log(myStack);

myStack.addElement('elemento 1')
myStack.addElement('elemento 2')
myStack.addElement('elemento 3')
myStack.addElement('elemento 4')
myStack.addElement('elemento 5')
myStack.show()
console.log(myStack.lengthStack);
console.log(myStack.getElement());
console.log(myStack.lengthStack);
console.log('');





class Queue {

    constructor(initialElements = []) {
        this.queue = [...initialElements]
        this.lengthQueue= this.queue.length
    }

    addElement(element) {
        this.queue.push(element)
        this.lengthStack = this.queue.length
    }

    getElement() {
        let element = this.queue.shift()
        this.lengthStack = this.queue.length
        return element
    }

    show() {
        console.log('Top')
        console.log('---')
        for (let i = this.queue.length - 1; i >= 0; i--) {
            if (i === 0) {
                console.log(this.queue[i] + '  <-  Primero en entrar, primero en salir.')
                continue
            }
            console.log(this.queue[i])
        }
        console.log('---')
        console.log('Bot')
    }


}

let myQueue= new Queue()
console.log(myQueue);

myQueue.addElement('elemento 1')
myQueue.addElement('elemento 2')
myQueue.addElement('elemento 3')
myQueue.addElement('elemento 4')
myQueue.addElement('elemento 5')
myQueue.show()
console.log(myQueue.lengthStack);
console.log(myQueue.getElement());
console.log(myQueue.lengthStack);

