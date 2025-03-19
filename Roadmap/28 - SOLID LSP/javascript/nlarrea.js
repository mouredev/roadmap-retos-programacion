/**
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
 */


// Incorrect


class BirdWrong {
    fly() {
        return 'Flying';
    }
};


class OstrichWrong extends BirdWrong {
    fly() {
        throw new Error('Ostriches can\'t fly');
    }
};


// let bird = new BirdWrong();
// console.log(bird.fly());  // Flying
// let ostrich = new OstrichWrong();
// console.log(ostrich.fly());  // Error


// Correct


class Bird {
    move() {
        return 'FLying';
    }
};


class Ostrich extends Bird {
    move() {
        return 'Walking';
    }
};


const bird = new Bird();
console.log(bird.move());  // Flying
const ostrich = new Ostrich();
console.log(ostrich.move());  // Walking


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


class Vehicle {
    constructor(speed=0) {
        this.speed = speed;
    }

    accelerate(increment) {
        this.speed += increment;
        console.log(`Speed: ${this.speed} km/h`);
    }

    brake(decrement) {
        this.speed -= decrement;
        console.log(`Speed: ${this.speed} km/h`);
    }
};


class Motorbike extends Vehicle {
    constructor(speed=0) {
        super(speed);
    }

    accelerate(increment) {
        console.log('Motorbike is accelerating...');
        super.accelerate(increment);
    }

    brake(decrement) {
        console.log('Motorbike is braking...');
        super.brake(decrement);
    }
};


class Car extends Vehicle {
    constructor(speed=0) {
        super(speed);
    }

    accelerate(increment) {
        console.log('Car is accelerating...');
        super.accelerate(increment);
    }

    brake(decrement) {
        console.log('Car is braking...');
        super.brake(decrement);
    }
};


class Bicycle extends Vehicle {
    constructor(speed=0) {
        super(speed);
    }

    accelerate(increment) {
        console.log('Bicycle is accelerating...');
        super.accelerate(increment);
    }

    brake(decrement) {
        console.log('Bicycle is braking...');
        super.brake(decrement);
    }
};


function testVehicle(vehicle) {
    vehicle.accelerate(10);
    vehicle.brake(2);
    console.log('');
};


const motorbike = new Motorbike();
const car = new Car();
const bicycle = new Bicycle();

testVehicle(motorbike);
testVehicle(car);
testVehicle(bicycle);