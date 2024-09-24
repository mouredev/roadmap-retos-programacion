// Ejercicio

/* Incorrecto */

class Animal {
  constructor(sound) {
    this.sound = sound
  }

  makeSound () {
    switch (this.sound) {
      case 'meau':
        console.log(`The animal makes meau!!!`);
        break;
      case 'woof':
        console.log(`The animal makes woof!!!`);
        break;
      default:
        console.log('Please incert an animal sound!');
        break;
    }
  }
}
const animal = new Animal('meau')
animal.makeSound()

/* Correcto */

class Person {
  constructor(name, occupation) {
    this.name = name
    this.occupation = occupation
  }

  getOccupation() {
    return this.occupation.getOccupation()
  }
}

class PersonOccupation {
  getOccupation() {}
}

class IndustrialEngineer extends PersonOccupation {
  getOccupation() {
    return 'I am an industrial engineer.'
  }
}

const engineer = new Person('Yojan', new IndustrialEngineer())
console.log(`Hola mi nombre es ${engineer.name} soy ${engineer.getOccupation()}`)

// Extra

/* Clase abstracta. No puede ser instanciada directamente pero es capaz de ser heredada por la descendencia */

class Operation {
  constructor() {
    if (new.target === Operation) {
      throw new TypeError("No puedes instanciar la clase abstracta 'Operation' directamente")
    }
  }
  execute() {
    throw new Error("Método 'execute()' debe ser implementado en la clase hija")
  }
}

class Addition extends Operation{
  constructor(a, b) {
    super()
    this.a = a
    this.b = b
  }
  execute() {
    return this.a + this.b
  }
}

class Subtract extends Operation{
  constructor(a, b) {
    super()
    this.a = a
    this.b = b
  }
  execute() {
    return this.a - this.b
  }
}

class Multiply extends Operation{
  constructor(a, b) {
    super()
    this.a = a
    this.b = b
  }
  execute() {
    return this.a * this.b
  }
}

class Divide extends Operation{
  constructor(a, b) {
    super()
    this.a = a
    this.b = b
  }
  execute() {
    return this.a / this.b
  }
}

class Power extends Operation{
  constructor(a, b) {
    super()
    this.a = a
    this.b = b
  }
  execute() {
    return this.a ** this.b
  }
}

class Calculator {
  constructor() {
    this.operations = {}
  }
  
  addOperation(name, operation) {
    this.operations[name] = operation
  }

  calculate(name) {
    if (!this.operations[name]) {
      throw new Error(`Operación ${name} no es valida`)
    }
    return this.operations[name].execute()
  }
}

const calculadora = new Calculator()
calculadora.addOperation('addition', new Addition(10, 2))
calculadora.addOperation('subtraction', new Subtract(5, 2))
calculadora.addOperation('multiplication', new Multiply(9, 2))
calculadora.addOperation('division', new Divide(9, 2))
calculadora.addOperation('power', new Power(5, 4))

console.log(calculadora.calculate('subtraction'))
console.log(calculadora.calculate('addition'))
console.log(calculadora.calculate('multiplication'))
console.log(calculadora.calculate('division'))
console.log(calculadora.calculate('power'))