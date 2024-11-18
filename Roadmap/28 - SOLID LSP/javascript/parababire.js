// Ejercicio

/* Incorrecto */

/* class Ball {
  bounce() {
    console.log(`The ball bounce!!!`);
  }
}

class BowlingBall extends Ball {
  bounce() {
    throw new Error(`Bowling ball can't bounce!!!`)
  }
} */

/* const ball = new Ball()
const bowlingBall = new BowlingBall()
ball.bounce()
bowlingBall.bounce() */

/* Correcto */

class Ball {
  throw() {
    console.log(`Throw the ball`);
  }
}

class BowlingBall extends Ball {
  throw() {
    console.log(`Throw the ball toward pins`);
  }
}

let ball = new Ball()
let bowlingBall = new BowlingBall()
ball.throw()
bowlingBall.throw()

/* Comprobación del principio de sustitución de Likov */

ball = new BowlingBall()
bowlingBall = new Ball()
ball.throw()
bowlingBall.throw()

// Extra

class Vehicle {
  constructor(speed = 0) {
    this.speed = speed
  }

  accelerate(increment) {
    this.speed += increment
    console.log(this.speed);
    
  }
  break(decrement) {
    this.speed -= decrement
    if (this.speed <= 0) {
      console.log(this.speed = 0)
    }
    console.log(this.speed)
  }
}

class Car extends Vehicle {
  accelerate(increment) {
    console.log(`El carro está acelerando`)
    super.accelerate(increment)
  }
  break(decrement) {
    console.log(`El carro está frenando`)
    super.break(decrement)
  }
}
class Bike extends Vehicle {
  accelerate(increment) {
    console.log(`La bicicleta está acelerando`)
    super.accelerate(increment)
  }
  break(decrement) {
    console.log(`La bicicleta está frenando`)
    super.break(decrement)
  }
}
class Motocycle extends Vehicle {
  accelerate(increment) {
    console.log(`La moto está acelerando`)
    super.accelerate(increment)
  }
  break(decrement) {
    console.log(`La moto está frenando`)
    super.break(decrement)
  }
}

function testVehicle(vehicle) {
  vehicle.accelerate(2)
  vehicle.break(1)
}

const car = new Car()
const bike = new Bike()
const motocycle = new Motocycle()

testVehicle(car)
testVehicle(bike)
testVehicle(motocycle)