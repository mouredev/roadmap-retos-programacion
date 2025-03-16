/*
  EJERCICIO:
  Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
  y crea un ejemplo simple donde se muestre su funcionamiento
  de forma correcta e incorrecta.
*/

console.log("+++++++++ FORMA INCORRECTA +++++++++");

class AnimalProof {
  eat() {
    console.log('El animal está comiendo');
  }
}

class BirdProof extends AnimalProof {
  fly() {
    console.log('El ave está volando');
  }
}

class OstrichProof extends BirdProof {
  fly() {
    throw new Error('Las avestruces no pueden volar');
  }
}

const birdProof = new OstrichProof();
birdProof.eat();
// birdProof.fly();

console.log("\n+++++++++ FORMA CORRECTA +++++++++");

class Animal {
  eat() {
    console.log('El animal está comiendo');
  }
}

class Bird extends Animal {
  fly() {
    console.log('El ave está volando');
  }
}

class Ostrich extends Animal {}

const bird = new Bird();
bird.eat();
bird.fly();

const ostrich = new Ostrich();
ostrich.eat();

/*
  DIFICULTAD EXTRA (opcional):
  Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
  cumplir el LSP.
  Instrucciones:
  1. Crea la clase Vehículo.
  2. Añade tres subclases de Vehículo.
  3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
  4. Desarrolla un código que compruebe que se cumple el LSP.
*/

console.log("\n+++++++++ JERARQUÍA DE VEHÍCULOS +++++++++");

class Vehiculo {
  constructor() {
    this.speed = 0;
  }

  speedUp(acceleration) {
    this.speed += acceleration;

    console.log(`Acelerando. Velocidad a ${this.speed} km/h`);
  }

  curb(deceleration) {
    this.speed -= deceleration;

    console.log(`Frenando. Velocidad a ${this.speed} km/h`);
  }
}

class Carro extends Vehiculo {
  constructor(acceleration, deceleration) {
    super(acceleration, deceleration);
  }
}

class Bicicleta extends Vehiculo {
  constructor(acceleration, deceleration) {
    super(acceleration, deceleration);
  }
}

class Patineta extends Vehiculo {
  constructor(acceleration, deceleration) {
    super(acceleration, deceleration);
  }
}

const car = new Carro();
const skateboard = new Patineta();
const bicycle =  new Bicicleta();

function testingVehicle(vehicle) {
  console.log(`\n- ${vehicle.constructor.name}:`);

  vehicle.speedUp(10);
  vehicle.curb(5);
}

testingVehicle(bicycle);
testingVehicle(skateboard);
testingVehicle(car);
