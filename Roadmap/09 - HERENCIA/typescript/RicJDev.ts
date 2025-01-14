//EJERCICIO
class Animal {
  name: string
  constructor(name: string) {
    this.name = name

    if (new.target === Animal) {
      throw new TypeError('unable to instantiate class "Animal"')
    }
  }

  speak(): void {
    throw new Error('the method "speak()" must be implemented')
  }
}

class Dog extends Animal {
  constructor(name: string) {
    super(name)
  }

  speak(): void {
    console.log(`${this.name}: woof, woof!`)
  }
}

class Cat extends Animal {
  constructor(name: string) {
    super(name)
  }

  speak(): void {
    console.log(`${this.name}: meow, meow!`)
  }
}

const charlie = new Dog('Charlie')
charlie.speak()

const mike = new Cat('Mike')
mike.speak()

//EXTRA
class Employee {
  name: string
  workerID: number
  title: string

  constructor(name: string, workerID: number, title: string) {
    this.name = name
    this.workerID = workerID
    this.title = title
  }

  work(): void {
    console.log(`${this.name} is working...`)
  }
}

interface hasWorkers {
  workers: Employee[]
  addWorker: (worker: Employee) => void
  displayWorkersList: () => void
}

class Manager extends Employee implements hasWorkers {
  workers: Employee[] = []

  constructor(name: string, workerID: number) {
    super(name, workerID, 'manager')
  }

  addWorker(worker: Employee): void {
    this.workers.push(worker)

    console.log(`${worker.name} is now working for ${this.name}.`)
  }

  displayWorkersList(): void {
    console.log(`${this.name}'s workers:`)

    this.workers.forEach((worker) => {
      console.log(`- ${worker.name}: ${worker.workerID}. ${worker.title}`)
    })
  }
}

class ProjectManager extends Employee implements hasWorkers {
  workers: Employee[]

  constructor(name: string, workerID: number) {
    super(name, workerID, 'Project Manager')
  }

  addWorker(worker: Employee) {
    this.workers.push(worker)
  }

  displayWorkersList(): void {
    console.log(`${this.name}'s workers:`)

    this.workers.forEach((worker) => {
      console.log(`- ${worker.name}: ${worker.workerID}. ${worker.title}`)
    })
  }
}

class Programer extends Employee {}
