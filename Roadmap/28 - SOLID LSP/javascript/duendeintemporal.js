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

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #28.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #28. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #28'); 
});


class Shape {
    area() {
        throw new Error("Method 'area' must be implemented");
    }
}

class Rectangle extends Shape {
    constructor(width, height) {
        super();
        this.width = width;
        this.height = height;
    }

    area() {
        return this.width * this.height;
    }
}

class Square extends Shape {
    constructor(side) {
        super();
        this.side = side;
    }

    area() {
        return this.side * this.side;
    }
}

const calculateArea = (shape)=> {
    return shape.area();
}

const rectangle = new Rectangle(83, 105);
const square = new Square(40);

log(calculateArea(rectangle)); // 8715
log(calculateArea(square)); // 1600   

//Extra Dificulty Exercise

class Car {
    constructor(brand, model, maxSpeed, acceleration, deceleration) {
        this.brand = brand;
        this.model = model;
        this.maxSpeed = maxSpeed; // Maximum speed in km/h
        this.acceleration = acceleration; // Acceleration in km/h per second
        this.deceleration = deceleration; // Deceleration in km/h per second
        this.currentSpeed = 0; // Current speed in km/h
    }

    accelerate(seconds) {
        const newSpeed = this.currentSpeed + (this.acceleration * seconds);
        this.currentSpeed = Math.min(newSpeed, this.maxSpeed);
        log(`${this.brand} ${this.model} accelerated to ${this.currentSpeed} km/h.`);
    }

    brake(seconds) {
        const newSpeed = this.currentSpeed - (this.deceleration * seconds);
        this.currentSpeed = Math.max(newSpeed, 0);
        log(`${this.brand} ${this.model} braked to ${this.currentSpeed} km/h.`);
    }
}

class SportsCar extends Car {
    constructor(brand, model) {
        super(brand, model, 300, 30, 20); 
    }
}

class FamilyCar extends Car {
    constructor(brand, model) {
        super(brand, model, 200, 15, 10); 
    }
}

function testCar(car) {
    car.accelerate(5); 
    car.brake(2);      
}



const sportsCars = [
    {
        brand: "Ferrari",
        model: "488",
        maxSpeed: 330,
        acceleration: 30, 
        deceleration: 20,            
    },
    {
        brand: "Porsche",
        model: "911 Turbo S",
        maxSpeed: 320, 
        acceleration: 28, 
        deceleration: 18,            
    },
    {
        brand: "Lamborghini",
        model: "Huracán",
        maxSpeed: 325,
        acceleration: 32, 
        deceleration: 22,            
    }
];

const familyCars = [
    {
        brand: "Toyota",
        model: "Sienna",
        maxSpeed: 180,
        acceleration: 10, 
        deceleration: 8,           
    },
    {
        brand: "Honda",
        model: "Odyssey",
        maxSpeed: 175,
        acceleration: 9,  
        deceleration: 7,              
    },
    {
        brand: "Chrysler",
        model: "Pacifica",
        maxSpeed: 180,
        acceleration: 9,  
        deceleration: 7,              
    }
];


const sportsCar = new SportsCar(...Object.values(sportsCars[0]));
const familyCar = new FamilyCar(...Object.values(familyCars[1]));

testCar(sportsCar); //Ferrari 488 accelerated to 150 km/h.
// Ferrari 488 braked to 110 km/h.
testCar(familyCar); // Honda Odyssey accelerated to 75 km/h.
// Honda Odyssey braked to 55 km/h.
