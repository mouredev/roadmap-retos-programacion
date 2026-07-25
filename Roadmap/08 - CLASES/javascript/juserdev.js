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

class Producto {
    constructor(nombre, precio, stock) {
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stock;
    }

    print() {
        return `Producto: ${this.nombre}, Precio: ${this.precio}, Stock: ${this.stock}`
    }

}

const mesa = new Producto("Mesa", 1000, 10)

console.log(mesa.print())
mesa.precio = 100
console.log(mesa.print())


// Dificultad extra
//* Stack
console.log("--------------- Stack ---------------")

class Stack {
    constructor(stack = []) {
        this.stack = stack
    }

    addStack(number) { return this.stack.push(number) }
    removeStack() { return this.stack.pop() }
    print() { return this.stack }
    elements() { return this.stack.length }

}

const stack = new Stack()

console.log(stack.addStack(1))
console.log(stack.addStack(2))
console.log(stack.addStack(3))
console.log(stack.addStack(4))
console.log(stack.print())
console.log(stack.removeStack())
console.log(stack.addStack(5))
console.log(stack.print())
console.log(stack.elements())

console.log("--------------- Queue ---------------")

class Queue {
    constructor(stack = []) {
        this.stack = stack
    }

    addStack(number) { return this.stack.push(number) }
    removeStack() { return this.stack.shift() }
    print() { return this.stack }
    elements() { return this.stack.length }

}

const queue = new Queue()

console.log(queue.addStack(1))
console.log(queue.addStack(2))
console.log(queue.addStack(3))
console.log(queue.addStack(4))
console.log(queue.print())
console.log(queue.removeStack())
console.log(queue.addStack(5))
console.log(queue.print())
console.log(queue.elements())
console.log(queue.removeStack())
console.log(queue.print())