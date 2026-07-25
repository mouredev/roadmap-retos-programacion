class Animal {

    constructor(name, type) {
        this.name = name
        this.type = type
    }

    setName(newName) {
        this.name = newName
    }

    getName() {
        return this.name
    }
}

let dog = new Animal('Bartolo', 'Dog')
// console.log(dog)
dog.setName('Lucio')
// console.log(dog)



class Stack {

    constructor() {
        this.stackElements = []
    }

    addElement(element) {
        this.stackElements.push(element)
    }
    deleteElement() {
        this.stackElements.pop()
    }
    getElements() {
        return this.stackElements
    }
    getAmountOfElements() {
        return `Amount of elements: ${this.stackElements.length}`
    }
}

// let newStack = new Stack()
// newStack.addElement('hello')
// newStack.addElement('hell')
// newStack.addElement('hel')
// newStack.deleteElement('hello')
// console.log(newStack)
// console.log(newStack.getAmountOfElements())


class Queue {

    constructor() {
        this.queueElements = []
    }

    addElement(element) {
        this.queueElements.push(element)
    }
    deleteElement() {
        this.queueElements.shift()
    }
    getElements() {
        return this.queueElements
    }
    getAmountOfElements() {
        return `Amount of elements: ${this.queueElements.length}`
    }
}

let newQueue = new Queue()
newQueue.addElement('first')
newQueue.addElement('second')
newQueue.addElement('third')
newQueue.deleteElement()
console.log(newQueue)
console.log(newQueue.getAmountOfElements())
