/*
  * EJERCICIO:
  * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
  * atributos y una función que los imprima (teniendo en cuenta las posibilidades
  * de tu lenguaje).
  * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
  * utilizando su función.
*/

class User {
  name: string
  age: number
  email: string
  constructor(name: string, age: number, email: string) {
    this.name = name
    this.age = age
    this.email = email
  }

  print():void {
    console.log(`Nombre: ${this.name}, Edad: ${this.age}, Email: ${this.email}`)
  }
}

const user1 = new User('Victor', 21, 'victor@gmail.com')
user1.print()

/*
  * DIFICULTAD EXTRA (opcional):
  * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
  * en el ejercicio número 7 de la ruta de estudio)
  * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
  *   retornar el número de elementos e imprimir todo su contenido.
*/

// Pilas - LIFO

class Stack<T> {
  private listStack: T[]

  constructor() {
    this.listStack = []
  }

  adding(input: T): void {
    this.listStack.push(input)
  }

  removing(): T | undefined {
    return this.listStack.pop()
  }

  numberOfElements(): number {
    return this.listStack.length
  }

  printStackContent(): void {
    console.table(this.listStack)
  }
}

const numberStack = new Stack<number>()
numberStack.adding(1)
numberStack.adding(2)
numberStack.adding(3)
numberStack.removing()
console.log(numberStack.numberOfElements())
numberStack.printStackContent()

// Colas - FIFO

class Queue<T> {
  private listQueue: T[]

  constructor() {
    this.listQueue = []
  }
  adding(input: T): void {
    this.listQueue.push(input)
  }

  removing(): T | undefined {
    return this.listQueue.shift()
  }

  numberOfElements(): number {
    return this.listQueue.length
  }

  printStackContent(): void {
    console.table(this.listQueue)
  }
}

const myQueue: Queue<number> = new Queue()
myQueue.adding(1)
myQueue.adding(2)
myQueue.adding(3)
myQueue.removing()
console.log(myQueue.numberOfElements())
myQueue.printStackContent()