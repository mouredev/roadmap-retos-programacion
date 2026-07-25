/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 */
class Person {
    constructor(name, age, country) {
        this.name = name
        this.age = age
        this.country = country
    }

    showInfo(){
        console.log(`Nombre: ${this.name} | Edad: ${this.age} años | País: ${this.country}`)
    }

}
let newPerson = new Person("Bryan", 30, "Perú")
newPerson.showInfo()
newPerson.country = "Colombia"
newPerson.showInfo()


/* DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */
class Stack {
    constructor() {
        this.element = []
    }

    addStackElement(value) {
        this.element.push(value)
        console.log(`${value} agregado a la pila`)

    }
    
    deleteStackElement() {
        if (this.element.length >= 1) {
            console.log(`${this.element.pop()} eliminado`)
        } else {
                console.log("No hay ningún elemento para eliminar")
        }
    }

    sizeStack() {
        if (this.element.length >= 1 ) {
            console.log(`El tamaño de la pila es de ${this.element.length}`)
        } else {
            console.log("El tamaño de la pila es de 0")
        }
    }

    showStack() {
        if (this.element.length >= 1) {
            console.log("Los elementos de la pila son: ")
            for (let i of this.element) {
                console.log(i)
            }
        } else {
            console.log("No hay ningún elemento en la pila")
        }
    }
}

let newStack = new Stack()
newStack.addStackElement("1")
newStack.addStackElement("2")
newStack.addStackElement("3")
newStack.deleteStackElement()
newStack.sizeStack()
newStack.showStack()

class Queue {
    constructor(){
        this.element = []
    }

    addQueueElement(value) {
        this.element.push(value)
        console.log(`${value} agregado a la cola`)
    }

    deleteQueueElement() {
        if (this.element.length >= 1) {
            console.log(`${this.element.shift()} eliminado`)
        } else {
            console.log("No hay ningún elemento para eliminar")
        }
    }

    sizeQueue() {
        if (this.element.length >= 1) {
            console.log(`El tamaño de la cola es ${this.element.length}`)
        } else {
            console.log("El tamaño de la cola es 0")
        }
    }

    showQueue() {
        if (this.element.length >= 1) {
            console.log("Los elementos de la cola son:")
            for (let i of this.element) {
                console.log(i)
            }
        } else {
            console.log("La cola no tienen ningún elemento")
        }
    }
}

let newQueue = new Queue()
newQueue.addQueueElement("1")
newQueue.addQueueElement("2")
newQueue.addQueueElement("3")
newQueue.deleteQueueElement()
newQueue.sizeQueue()
newQueue.showQueue()