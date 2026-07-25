/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 */

class Stack{
    constructor (element) {
        this.element = element
    }

    push(value){
        this.element.push(value)
    }

    pop(){
        if (this.element.length === 0){
            console.log("No se puede borrar un array vacío")
        } else {
            this.element.pop()
        }
    }

    state() {
        console.log(this.element)
    }
}
let newStack = new Stack([])
newStack.state()

newStack.push("Manzana")
newStack.push("Pera")
newStack.push("Uva")
newStack.push("Fresa")
newStack.state()

newStack.pop()
newStack.state()

class Queue{
    constructor (element) {
        this.element = element
    }

    enqueue(value){
        this.element.push(value)
    }

    dequeue(){
        if (this.element.length === 0){
            console.log("No se puede borrar un array vacío")
        } else {
            this.element.shift()
        }
    }

    state() {
        console.log(this.element)
    }
}
let newQueue = new Queue([])
newQueue.state()

newQueue.enqueue("Cliente 1")
newQueue.enqueue("Cliente 2")
newQueue.enqueue("Cliente 3")
newQueue.enqueue("Cliente 4")
newQueue.state()

newQueue.dequeue()
newQueue.state()

/* DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 */ 

class StackNav {
    constructor(stack1, stack2){
        this.stack1 = stack1
        this.stack2 = stack2
    }

    newPage(word) {
        this.stack1.push(word)
        this.stack2 = []
        console.log(this.stack1[this.stack1.length-1])
    }
    
    atras(){
        if (this.stack1.length <= 0){
            console.log("No hay ninguna página atrás")
        } else {
            let element = this.stack1.pop()
            this.stack2.push(element)
            if (this.stack1.length === 0) {
                console.log("No hay ninguna página atrás")
            } else {
                console.log(this.stack1[this.stack1.length-1])
            }
        }
    }

    adelante() {
        if (this.stack2.length <= 0){
            console.log("No hay ninguna página adelante")
        } else {
        let element = this.stack2.pop()
        this.stack1.push(element)
        console.log(this.stack1[this.stack1.length-1])
        }
    }
}

let newStackNav = new StackNav([], [])

let comandos = ["Google", "Twitter", "adelante", "adelante", "adelante", "adelante"]

for (let comando of comandos) {
    if (comando !== "atrás" && comando !== "adelante") {
        newStackNav.newPage(comando)
    } else if (comando === "atrás") {
        newStackNav.atras()
    } else if (comando === "adelante") {
        newStackNav.adelante()
    }
}


/* - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

class QueuePrint {
    constructor(printer) {
        this.printer = printer
    }

    print() {
        if (this.printer.length === 0) {
            console.log("No hay documentos para imprimir")
        } else {
            console.log(`Imprimiendo: [${this.printer.shift()}]`)
            console.log(`Quedan pendientes: [${this.printer}]`)
        }
    }

    add(document) {
        this.printer.push(document)
        console.log(`Total de documentos: [${this.printer}]`)
    }
}
let newQueuePrint = new QueuePrint([])

let actions = ["Nuevo", "Documento", "imprimir"]

for (let action of actions){
    if (action === "imprimir") {
        newQueuePrint.print(action)
    } else {
        newQueuePrint.add(action)
    }
}