/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
___________________________________________________
#28 SOLID: PRINCIPIO DE SUSTITUCIÓN DE LISKOV (LSP)
---------------------------------------------------
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
// ________________________________________________________
// Base
class Animal {
    constructor(name) {
        if (new.target === Animal) {
            throw new Error("No se puede instanciar una clase abstracta.");
        }
        this.name = name;
    }

    makeSound() {
        throw new Error("El método 'makeSound' debe ser implementado.");
    }
}

// Clases derivadas
class Dog extends Animal {
    makeSound() {
        return `${this.name} hace Woof`;
    }
}

class Cat extends Animal {
    makeSound() {
        return `${this.name} hace Meow`;
    }
}

// _____________________
// Pruebas
const dog = new Dog("Max");
console.log(dog.makeSound()); // Max hace Woof

const cat = new Cat("Milo");
console.log(cat.makeSound()); // Milo hace Meow

// ________________________________________________________
// DIFICULTAD EXTRA
// ----------------
// Clase base
class Vehicle {
    constructor(brand, model) {
        if (this.constructor === Vehicle) {
            throw new Error("No se puede instanciar la clase abstracta 'Vehicle'");
        }
        this._brand = brand;
        this._model = model;
    }

    get brand() {
        return this._brand;
    }

    get model() {
        return this._model;
    }

    accelerate() {
        throw new Error("Método 'accelerate' no implementado");
    }

    brake() {
        throw new Error("Método 'brake' no implementado");
    }
}

// Clases derivadas
class Car extends Vehicle {
    accelerate() {
        return `Acelerando auto: ${this.brand} - ${this.model}`;
    }

    brake() {
        return `Frenando auto: ${this.brand} - ${this.model}`;
    }
}

class Motorcycle extends Vehicle {
    accelerate() {
        return `Acelerando Motocicleta: ${this.brand} - ${this.model}`;
    }

    brake() {
        return `Frenando Motocicleta: ${this.brand} - ${this.model}`;
    }
}

class Truck extends Vehicle {
    accelerate() {
        return `Acelerando Camión: ${this.brand} - ${this.model}`;
    }

    brake() {
        return `Frenando Camión: ${this.brand} - ${this.model}`;
    }
}

// Verificar cumplimiento de LSP
function testSubClass(subClass) {
    console.log("\nPropiedades:");
    console.log(`${subClass.brand} - ${subClass.model}`);

    console.log("\nMétodos:");
    console.log(subClass.accelerate());
    console.log(subClass.brake());
}

// Instanciando
const car = new Car("Honda", "Civic");
testSubClass(car);

const motorcycle = new Motorcycle("Kawasaki", "Ninja");
testSubClass(motorcycle);

const truck = new Truck("Ford", "Raptor");
testSubClass(truck);
