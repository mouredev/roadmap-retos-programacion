// Wrong way
class Bird { 
    fly() {
        console.log('Flying!');
    }
}

class Penguin extends Bird {
    fly() {
        throw new Error('Penguins cannot fly!');
    }
}

function makeBirdFly(bird) {
    bird.fly();
}

const bird = new Bird();
const penguin = new Penguin();

makeBirdFly(bird);
// makeBirdFly(penguin); // Not working //

// Correct way
class Bird2 {
    eat() {
        console.log('Eating...');
    }
}

class FlyingBird extends Bird2 {
    fly() {
        console.log('Flying!');
    }
}

class Penguin2 extends Bird2 {
    swin() {
        console.log('Swimming!');
    }
}

function makeFlyingBirdFly(bird) {
    bird.fly();
}

const eagle = new FlyingBird();
const penguin2 = new Penguin2();

makeFlyingBirdFly(eagle);
// makeBirdFly(penguin); // Not working //

// Extra Exercise //
class Vehicle {
    accelerate() {
        throw new Error('accelerate() must be implemented');
    }

    brake() {
        throw new Error('brake() must be implemented'); 
    }
}

class Car extends Vehicle {
    accelerate() {
        console.log('Car is accelerating');
    }

    brake() {
        console.log('Car is braking');
    }
}

class Motorcycle extends Vehicle {
    accelerate() {
        console.log('Motorcycle is accelerating');
    }

    brake() {
        console.log('Motorcycle is braking');
    }
}

class Bicycle extends Vehicle {
    accelerate() {
        console.log('Bicycle is accelerating');
    }

    brake() {
        console.log('Bicycle is braking');
    }
}

function testVehicle(vehicle) {
    vehicle.accelerate();
    vehicle.brake();
}

const car = new Car();
const motorcycle = new Motorcycle();
const bicycle = new Bicycle();

testVehicle(car);
testVehicle(motorcycle);
testVehicle(bicycle);
