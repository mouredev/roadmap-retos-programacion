/*
  * EJERCICIO:
  * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
  * y crea un ejemplo simple donde se muestre su funcionamiento
  * de forma correcta e incorrecta.
*/

class Worker {
  work() {
    return 'Realizando tareas generales'
  }
}

class Developer extends Worker {
  work() {
    return 'Escribiendo código'
  }
}

class Designer extends Worker {
  work() {
    return 'Creando diseños'
  }
}

let worker = new Worker()
console.log(worker.work())

let developer = new Developer()
console.log(developer.work())

let designer = new Designer()
console.log(designer.work())


worker = new Developer()
console.log(worker.work())

worker = new Designer()
console.log(worker.work())


/*
  * DIFICULTAD EXTRA (opcional):
  * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
  * cumplir el LSP.
  * Instrucciones:
  * 1. Crea la clase Vehículo.
  * 2. Añade tres subclases de Vehículo.
  * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
  * 4. Desarrolla un código que compruebe que se cumple el LSP.
*/
console.log('--Extra--')

class Vehicle {
  speed = 0
  constructor(speed) {
    this.speed = speed
  }

  speedUp() {
    this.speed += 1
    return `Velocidad: ${this.speed}`
  }

  slowDown() {
    if (this.speed > 0) {
      this.speed -= 1
      return `Velocidad: ${this.speed}`
    } else {
      this.speed = 0
      return `Velocidad: ${this.speed}`
    }
  }
}

class Car extends Vehicle {
  speedUp() {
    this.speed += 4
    return `Velocidad: ${this.speed}`
  }
}

class Plane extends Vehicle {
  speedUp() {
    this.speed += 10
    return `Velocidad: ${this.speed}`
  }

  slowDown() {
    if (this.speed > 0) {
      this.speed -= 5
      return `Velocidad: ${this.speed}`
    } else {
      return `El avión ya está detenido`
    }
  }
}


class Bus extends Vehicle {
  speedUp() {
    this.speed += 3
    return `Velocidad: ${this.speed}`
  }
}

let vehicle = new Vehicle(0)

let car = new Car(10)
console.log(car.speedUp())
console.log(car.slowDown())

let plane = new Plane(50)
console.log(plane.speedUp())
console.log(plane.slowDown())

let bus = new Bus(20)
console.log(bus.speedUp())
console.log(bus.slowDown())

vehicle = new Car(0)
console.log(vehicle.speedUp())
console.log(vehicle.slowDown())

vehicle = new Plane(0)
console.log(vehicle.speedUp())
console.log(vehicle.slowDown())

vehicle = new Bus(0)
console.log(vehicle.speedUp())
console.log(vehicle.slowDown())