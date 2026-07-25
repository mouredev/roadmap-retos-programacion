// Wrong way
class Bird {
    fly(): void {
        console.log('Flying!');
    }
}

class Penguin extends Bird {
    fly(): void {
        throw new Error('Penguins cannot fly!');
    }
}

function makeBirdFly(bird: Bird): void {
    bird.fly();
}

const bird = new Bird();
const penguin = new Penguin();

makeBirdFly(bird);
// makeBirdFly(penguin); // Not working //

// Correct way
class Bird2 {
    eat(): void {
        console.log('Eating...');
    }
}

class FlyingBird extends Bird2 {
    fly(): void {
        console.log('Flying!');
    }
}

class Penguin2 extends Bird2 {
    swim(): void {
        console.log('Swimming!');
    }
}

function makeFlyingBirdFly(bird: FlyingBird): void {
    bird.fly();
}

const eagle = new FlyingBird();
const penguin2 = new Penguin2();

makeFlyingBirdFly(eagle);
// makeFlyingBirdFly(penguin2); // Not working //

// ** Extra Exercise ** //
abstract class Vehicle {
    abstract accelerate(): void;
    abstract brake(): void; 
}

class Car extends Vehicle {
    accelerate(): void {
        console.log('Car is accelerating');
    }

    brake(): void {
        console.log('Car is braking');
    }
}

class Motorcycle extends Vehicle {
    accelerate(): void {
        console.log('Motorcycle is accelerating');
    }

    brake(): void {
        console.log('Motorcycle is braking');
    }
}

class Bicycle extends Vehicle {
    accelerate(): void {
        console.log('Bicycle is accelerating');
    }

    brake(): void {
        console.log('Bicycle is braking');
    }
}

function testVehicle(vehicle: Vehicle): void {
    vehicle.accelerate();
    vehicle.brake();
}

const car = new Car();
const motorcycle = new Motorcycle();
const bicycle = new Bicycle();

testVehicle(car);
testVehicle(motorcycle);
testVehicle(bicycle);
