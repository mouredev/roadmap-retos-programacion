/*
    Liskov Substitution Principle (LCP)...
*/

console.log('Liskov Substitution Principle (LCP)...')

console.log('\nBad implementation of Liskov Substitution Principle (LCP)...')

interface IBadAnimal {
    walk(): void
}

abstract class BadAnimal implements IBadAnimal {
    public abstract walk(): void
}

function walk(animal: BadAnimal) {
    animal.walk()
}

class BadDog extends BadAnimal {
    public walk(): void {
        console.log('Dog walking!')
    }
}

class BadFish extends BadAnimal {
    public walk(): void {
        throw new Error('Fish can not fly')
    }
}

console.log(`\n\`\`\`\ninterface IBadAnimal {
    walk(): void
}

abstract class BadAnimal implements IBadAnimal {
    public abstract walk(): void
}

function walk(animal: BadAnimal) {
    animal.walk()
}

class BadDog extends BadAnimal {
    public walk(): void {
        console.log('Dog walking!')
    }
}

class BadFish extends BadAnimal {
    public walk(): void {
        throw new Error('Fish can not fly')
    }
}\n\`\`\``)

console.log(
    '\nThis is a bad implementation of Liskov Substitution Principle (LCP),\n' +
        'because the "BadFish" class implements the "walk" method which produces a\n' +
        'different side effect than the "walk" method inside the "BadDog" class. So,\n' +
        'if we execute the "walk" function with both classes ("BadDog", and "BadFish") the\n' +
        'function will produce different side effects that could be break the function execution.'
)

console.log('\nGood implementation of Liskov Substitution Principle (LCP)...')

interface IGoodAnimal {
    move(): void
}

abstract class GoodAnimal implements IGoodAnimal {
    public abstract move(): void
}

function move(animal: GoodAnimal): void {
    animal.move()
}

class GoodDog extends GoodAnimal {
    public move(): void {
        console.log('Dog walking!')
    }
}

class GoodFish extends GoodAnimal {
    public move(): void {
        console.log('Fish swimming!')
    }
}

console.log(`\n\`\`\`\ninterface IGoodAnimal {
    move(): void
}

abstract class GoodAnimal implements IGoodAnimal {
    public abstract move(): void
}

function move(animal: GoodAnimal): void {
    animal.move()
}

class GoodDog extends GoodAnimal {
    public move(): void {
        console.log('Dog walking!')
    }
}

class GoodFish extends GoodAnimal {
    public move(): void {
        console.log('Fish swimming!')
    }
}\n\`\`\``)

console.log(
    '\nThis is a good implementation of Liskov Substitution Principle (LCP),\n' +
        'because all child classes of "GoodAnimal" class implements each method\n' +
        'with the same side effect. So, if we execute the "move" function with both\n' +
        'classes ("GoodDog", and "GoodFish"), we are not going to have side effects that\n' +
        'could break the function execution.'
)

console.log(
    '\n# ---------------------------------------------------------------------------------- #\n'
)

/*
    Additional challenge...
*/

console.log('Additional challenge...')

interface IVehicle {
    brake(): void
    speedUp(): void
}

abstract class Vehicle implements IVehicle {
    public abstract brake(): void
    public abstract speedUp(): void
}

function brake(vehicle: Vehicle) {
    vehicle.brake()
}

function speedUp(vehicle: Vehicle) {
    vehicle.speedUp()
}

class Car extends Vehicle {
    public brake(): void {
        console.log('Car braking!')
    }

    public speedUp(): void {
        console.log('Car speeding up!')
    }
}

class Truck extends Vehicle {
    public brake(): void {
        console.log('Truck braking!')
    }

    public speedUp(): void {
        console.log('Truck speeding up!')
    }
}

class Boat extends Vehicle {
    public brake(): void {
        console.log('Boat braking!')
    }

    public speedUp(): void {
        console.log('Boat speeding up!')
    }
}

const car: Car = new Car()
const truck: Truck = new Truck()
const boat: Boat = new Boat()

console.log()
speedUp(car)
speedUp(truck)
speedUp(boat)

console.log()
brake(car)
brake(truck)
brake(boat)
