//EJERCICIO
class Animal {
  name: string
  constructor(name: string) {
    this.name = name
  }

  speak(): void {
    throw new Error('Must be implemented')
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
  id: number
  title: string
  employees: string[]

  constructor(name: string, id: number, title: string) {
    this.name = name
    this.id = id
    this.title = title
    this.employees = []
  }

  get Credential() {
    const credential = {
      title: this.title,
      name: this.name,
      id: this.id,
    }

    return credential
  }
}

const John = new Employee('John', 12, 'Manager')
console.log(John.Credential)