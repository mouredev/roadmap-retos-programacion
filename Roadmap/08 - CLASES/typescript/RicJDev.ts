//EJERCICIO
interface Person {
  name: string
  age: number
}

interface Programer {
  languages: string[]
}

class Programer implements Person, Programer {
  name: string
  age: number

  constructor(name: string, age: number, languages: string[]) {
    this.name = name
    this.age = age
    this.languages = languages
  }

  sayHi(): void {
    console.log(`Hi, my name is ${this.name}`)
  }

  sayYourAge(): void {
    console.log(`I'm ${this.age} years older`)
  }

  sayLangs(): void {
    console.log(`I learned this languanges: ${this.languages.join(', ')}`)
  }

  learnLang(lang: string): void {
    this.languages.push(lang)

    console.log(`Learning ${lang}...`)
  }
}

let Sebas = new Programer('Sebastian', 23, ['Java', 'Python', 'C++'])

Sebas.sayHi()
Sebas.sayYourAge()
Sebas.sayLangs()

Sebas.learnLang('Golang')
Sebas.sayLangs()

//EXTRA
console.log('\nSTACK')
class Stack {
  stack: number[] = []

  add(item: number): void {
    this.stack.push(item)
  }

  remove(): void {
    this.stack.pop()
  }

  count(): number | string {
    if (this.stack.length > 0) {
      return this.stack.length
    } else {
      return 'Void stack'
    }
  }

  display(): void {
    this.stack.forEach((elem) => {
      console.log(elem)
    })
  }
}

const myStack = new Stack()

console.log('Stack elements:', myStack.count())

myStack.add(1)
myStack.add(2)
myStack.add(3)
myStack.add(4)

console.log('\nBefore remove: ')
myStack.display()

console.log('After remove: ')
myStack.remove()
myStack.display()

console.log('Stack elements:', myStack.count())

console.log('\nQUEUE')
class Queue {
  queue: any[] = []

  add(item: any): void {
    this.queue.push(item)
  }

  remove(): void {
    this.queue.shift()
  }

  count(): number | string {
    if (this.queue.length > 0) {
      return this.queue.length
    } else {
      return 'Void queue'
    }
  }

  display(): void {
    this.queue.forEach((elem) => {
      console.log(elem)
    })
  }
}

const myQueue = new Queue()

console.log('Queue elements:', myQueue.count())

myQueue.add(1)
myQueue.add(2)
myQueue.add(3)
myQueue.add(4)

console.log('\nBefore remove: ')
myQueue.display()

console.log('After remove: ')
myQueue.remove()
myQueue.display()

console.log('Queue elements:', myQueue.count())
