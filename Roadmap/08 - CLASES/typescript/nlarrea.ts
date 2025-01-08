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


class Student {
    name: string
    email: string
    subjects: string[]

    constructor(name: string, email: string, subjects: string[]) {
        this.name = name
        this.email = email
        this.subjects = subjects
    }

    printStudentData() {
        console.log(`Name: ${this.name}`)
        console.log(`Email: ${this.email}`)
        
        console.log('These are this student\'s subjects:')
        for (const subject of this.subjects) {
            console.log(` - ${subject}`)
        }
    }
}


const student1 = new Student(
    'Naia',
    'naia@email.com',
    ['Electronics', 'Informatics', 'Maths']
)
const student2: Student = new Student(
    'Cristina',
    'cristina@email.com',
    ['Anatomy', 'Pathologies']
)

student1.printStudentData()
/**
 * Name: Naia
 * Email: naia@email.com
 * These are this student's subjects:
 *  - Electronics
 *  - Informatics
 *  - Maths
 */
student2.printStudentData()
/**
 * Name: Cristina
 * Email: cristina@email.com
 * These are this student's subjects:
 *  - Anatomy
 *  - Pathologies
 */


/*
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */


// Stack - LIFO


class Stack {
    stack: any[]

    constructor(stack: any[] = []) {
        this.stack = stack
    }

    insert(item: any): void {
        this.stack.push(item)
    }

    remove() {
        this.stack.pop()
    }

    length(): number {
        return this.stack.length
    }

    getContent(): any[] {
        return this.stack
    }
}


const myStack: Stack = new Stack()
console.log(myStack.length())  // 0

// Add data
myStack.insert(1)
myStack.insert(2)
myStack.insert(3)
myStack.insert(4)

console.log(myStack.getContent())  // [1, 2, 3, 4]
console.log(myStack.length())  // 4

// Remove data
myStack.remove()
console.log(myStack.getContent())  // [1, 2, 3]
console.log(myStack.length())  // 3

myStack.remove()
console.log(myStack.getContent())  // [1, 2]
console.log(myStack.length())  // 2


// Queue - FIFO


class Queue {
    queue: any[]

    constructor(queue: any[] = []) {
        this.queue = queue
    }

    insert(item: any): void {
        this.queue.push(item)
    }

    remove() {
        this.queue.splice(0, 1)
    }

    length(): number {
        return this.queue.length
    }

    getContent(): any[] {
        return this.queue
    }
}


const myQueue: Queue = new Queue()
console.log(myQueue.length())  // 0

// Add data
myQueue.insert(1)
myQueue.insert(2)
myQueue.insert(3)
myQueue.insert(4)

console.log(myQueue.getContent())  // [1, 2, 3, 4]
console.log(myQueue.length())  // 4

// Remove data
myQueue.remove()
console.log(myQueue.getContent())  // [2, 3, 4]
console.log(myQueue.length())  // 3

myQueue.remove()
console.log(myQueue.getContent())  // [3, 4]
console.log(myQueue.length())  // 2