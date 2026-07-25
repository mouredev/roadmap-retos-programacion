/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
__________________________________________
#27 SOLID: PRINCIPIO ABIERTO-CERRADO (OCP)
------------------------------------------
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
*/

// ________________________________________________________
// SIN APLICAR OCP
// ---------------
class Product_ {
    constructor(name, price, type) {
        this.name = name;
        this.price = price;
        this.type = type;
    }

    finalPrice() {
        let discount = 0;

        if (this.type === "electronics") {
            discount = this.price * 0.05;
        } else if (this.type === "clothing") {
            discount = this.price > 50 ? 10 : 0;
        }
        // Si se necesita un nuevo tipo, habría que añadir más condicionales aquí

        return this.price - discount;
    }
}

function processProduct_(product) {
    console.log(`Producto: ${product.name}, Precio final: ${product.finalPrice()}`);
}


// ________________________________________________________
// APLICANDO OCP
// ---------------
class Product {
    constructor(name, price) {
        if (new.target === Product) {
            throw new Error("Cannot instantiate an abstract class.");
        }
        this.name = name;
        this.price = price;
    }

    applyDiscount() {
        throw new Error("Method 'applyDiscount()' must be implemented.");
    }

    finalPrice() {
        return this.price - this.applyDiscount();
    }
}

// Clase concreta
class ElectronicsProduct extends Product {
    applyDiscount() {
        return this.price * 0.05; // Descuento del 5%
    }
}

// Clase concreta
class ClothingProduct extends Product {
    applyDiscount() {
        return this.price > 50 ? 10 : 0; // Descuento basado en la condición
    }
}

function processProduct(product) {
    console.log(`Producto: ${product.name}, Precio final: ${product.finalPrice()}`);
}

// Pruebas
const laptop = new ElectronicsProduct("Laptop", 700);
const pants = new ClothingProduct("Pants", 55);

processProduct(laptop); // Producto: Laptop, Precio final: 665
processProduct(pants);  // Producto: Pants, Precio final: 45

// ________________________________________________________
// DIFICULTAD EXTRA
// ---------------

// Clase base
class Calculator {
    constructor(a, b) {
        if (typeof a === "number" && typeof b === "number") {
            this.a = a;
            this.b = b;
        } else {
            this.a = null;
            this.b = null;
            console.error("Operación inválida.");
        }
    }

    // Método abstracto simulado
    mathOperation() {
        throw new Error("El método 'mathOperation()' debe ser implementado.");
    }

    printResult() {
        if (this.a !== null && this.b !== null) {
            console.log(`Es: ${this.mathOperation()}`);
        } else {
            console.error("Campos incorrectos.");
        }
    }
}

// Clases concretas
class Sum extends Calculator {
    mathOperation() {
        console.log(`\nSuma de ${this.a} + ${this.b}:`);
        return this.a + this.b;
    }
}

class Subtraction extends Calculator {
    mathOperation() {
        console.log(`\nResta de ${this.a} - ${this.b}:`);
        return this.a - this.b;
    }
}

class Multiplication extends Calculator {
    mathOperation() {
        console.log(`\nMultiplicación de ${this.a} * ${this.b}:`);
        return this.a * this.b;
    }
}

class Division extends Calculator {
    mathOperation() {
        console.log(`\nDivisión de ${this.a} / ${this.b}:`);
        return this.a / this.b;
    }
}

class Pow extends Calculator {
    mathOperation() {
        console.log(`\nPotencia de ${this.a} ^ ${this.b}:`);
        return this.a ** this.b;
    }
}

// Pruebas
const sum = new Sum(2, 2);
sum.printResult();

const subtraction = new Subtraction(2, 2);
subtraction.printResult();

const multiplication = new Multiplication(2, 2);
multiplication.printResult();

const division = new Division(2, 2);
division.printResult();

const power = new Pow(2, 2);
power.printResult();

