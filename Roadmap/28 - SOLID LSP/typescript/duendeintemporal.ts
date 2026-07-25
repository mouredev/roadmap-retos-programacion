//#28 - Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)
/*
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

/* The Liskov Substitution Principle (LSP) is one of the five SOLID principles of object-oriented programming. This principle states that objects of a derived class should be able to replace objects of the base class without altering the correctness of the program. */

let log = console.log;

// Check if running in a browser environment
const isBrowser = typeof window !== 'undefined';

// Conditional check for browser environment
if (isBrowser) {
    window.addEventListener('load', () => {
        const body: HTMLBodyElement | null = document.querySelector('body');
        const title = document.createElement('h1');

        body?.style.setProperty('background', '#000');
        body?.style.setProperty('text-align', 'center');

        title.textContent = 'Retosparaprogramadores #28.';
        title.style.setProperty('font-size', '3.5vmax');
        title.style.setProperty('color', '#fff');
        title.style.setProperty('line-height', '100vh');

        body?.appendChild(title);

        setTimeout(() => {
            alert('Retosparaprogramadores #28. Please open the Browser Developer Tools.');
        }, 2000);
        log('Retosparaprogramadores #28');
    });
} else {
    log('This code is designed to run in a browser environment. Skipping window-related code.');
    log('Retosparaprogramadores #28');
}


// Liskov Substitution Principle (LSP) Example

class Shape {
    area(): number {
        return 0; // Default implementation
    }
}

class Rectangle extends Shape {
    constructor(private width: number, private height: number) {
        super();
    }

    area(): number {
        return this.width * this.height;
    }
}

class Square extends Shape {
    constructor(private side: number) {
        super();
    }

    area(): number {
        return this.side * this.side;
    }
}

const calculateArea = (shape: Shape): number => {
    return shape.area();
};

const rectangle = new Rectangle(83, 105);
const square = new Square(40);

log(calculateArea(rectangle)); // 8715
log(calculateArea(square)); // 1600

// Extra Difficulty Exercise

// Define the ICar interface
interface ICar {
    brand: string;
    model: string;
    maxSpeed: number;
    acceleration: number;
    deceleration: number;
}

// Define the Car class
class Car {
    constructor(
        public brand: string,
        public model: string,
        public maxSpeed: number,
        public acceleration: number,
        public deceleration: number,
        public currentSpeed: number = 0
    ) {}

    accelerate(seconds: number): void {
        const newSpeed = this.currentSpeed + this.acceleration * seconds;
        this.currentSpeed = Math.min(newSpeed, this.maxSpeed);
        log(`${this.brand} ${this.model} accelerated to ${this.currentSpeed} km/h.`);
    }

    brake(seconds: number): void {
        const newSpeed = this.currentSpeed - this.deceleration * seconds;
        this.currentSpeed = Math.max(newSpeed, 0);
        log(`${this.brand} ${this.model} braked to ${this.currentSpeed} km/h.`);
    }
}

// Define the SportsCar class
class SportsCar extends Car {
    constructor(brand: string, model: string, maxSpeed: number, acceleration: number, deceleration: number) {
        super(brand, model, maxSpeed, acceleration, deceleration);
    }
}

// Define the FamilyCar class
class FamilyCar extends Car {
    constructor(brand: string, model: string, maxSpeed: number, acceleration: number, deceleration: number) {
        super(brand, model, maxSpeed, acceleration, deceleration);
    }
}

/* Note: Originally, the code used the spread operator (...) with Object.values to pass properties to 
the constructor, like this:

const sportsCar = new SportsCar(...Object.values(sportsCars[0]) 
as [string, string, number, number, number]);

While this approach works in some cases, it has a critical flaw: Object.values does not guarantee the
 order of properties. This can lead to runtime errors if the order of properties in the object does
  not match the order of parameters in the constructor.*/
// That's why switched to using a factory function:

// Factory function for SportsCar
function createSportsCar(carProps: ICar): SportsCar {
    const { brand, model, maxSpeed, acceleration, deceleration } = carProps;
    return new SportsCar(brand, model, maxSpeed, acceleration, deceleration);
}

// Factory function for FamilyCar
function createFamilyCar(carProps: ICar): FamilyCar {
    const { brand, model, maxSpeed, acceleration, deceleration } = carProps;
    return new FamilyCar(brand, model, maxSpeed, acceleration, deceleration);
}

// Example data
const sportsCars: ICar[] = [
    { brand: "Ferrari", model: "488", maxSpeed: 330, acceleration: 30, deceleration: 20 },
    { brand: "Porsche", model: "911 Turbo S", maxSpeed: 320, acceleration: 28, deceleration: 18 },
    { brand: "Lamborghini", model: "Huracán", maxSpeed: 325, acceleration: 32, deceleration: 22 }
];

const familyCars: ICar[] = [
    { brand: "Toyota", model: "Sienna", maxSpeed: 180, acceleration: 10, deceleration: 8 },
    { brand: "Honda", model: "Odyssey", maxSpeed: 175, acceleration: 9, deceleration: 7 },
    { brand: "Chrysler", model: "Pacifica", maxSpeed: 180, acceleration: 9, deceleration: 7 }
];

// Create instances using the factory function
const sportsCar = createSportsCar(sportsCars[0]);
const familyCar = createFamilyCar(familyCars[1]);

// Test the cars
function testCar(car: Car, accelerateSeconds: number, brakeSeconds: number): void {
    car.accelerate(accelerateSeconds);
    car.brake(brakeSeconds);
}

testCar(sportsCar, 5, 2); // Ferrari 488 accelerated to 150 km/h. Ferrari 488 braked to 110 km/h.
testCar(familyCar, 5, 2); // Honda Odyssey accelerated to 45 km/h. Honda Odyssey braked to 31 km/h.