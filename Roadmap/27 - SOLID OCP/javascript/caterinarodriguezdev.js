/*
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

// Violación del OCP
class AreaCalculator {
    calculateRectangleArea(width, height) {
        return width * height;
    }

    calculateCircleArea(radius) {
        return Math.PI ** radius;
    }
}

const calculator = new AreaCalculator();
console.log(calculator.calculateRectangleArea(5, 10)); 
console.log(calculator.calculateCircleArea(7));

// OCP
class Shape {
    area() {
        throw new Error("Método area debe ser implementado");
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

class Circle extends Shape {
    constructor(radius) {
        super();
        this.radius = radius;
    }

    area() {
        return Math.PI ** this.radius;
    }
}

class AreaCalculatorOCP {
    calculateArea(shape) {
        return shape.area();
    }
}

const calculatorOCP = new AreaCalculator();
const rectangle = new Rectangle(10, 10);
const circle = new Circle(10);

console.log(rectangle.area());
console.log(circle.area());


console.log('--------------DIFICULTAD EXTRA------------');

class Calculadora {

    sumar(n1, n2) {
        return n1 + n2
    }

    restar(n1, n2) {
        return n1 - n2
    }

    multiplicar(n1, n2) {
        return n1 * n2
    }

    dividir(n1, n2) {
       return n1 / n2
    }
}

const calculadora = new Calculadora();
console.log(calculadora.sumar(1, 1));
console.log(calculadora.restar(1, 1));
console.log(calculadora.multiplicar(1, 1));
console.log(calculadora.dividir(1, 1));

