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


// Incorrect

class BadGeometricForm {
    drawSquare() {
        console.log('Drawing a square');
    }

    drawCircle() {
        console.log('Drawing a circle');
    }
}


// Correct

class GeometricForm {
    constructor() {
        if (this.constructor === GeometricForm) {
            throw new Error('You can\'t create an instance from GeometricForm class!')
        }
    }

    draw() {
        throw new Error('The method "draw" must be implemented!')
    }
}


class Square extends GeometricForm {
    draw() {
        console.log('Drawing a square!');
    }
}


class Circle extends GeometricForm {
    draw() {
        console.log('Drawing a circle!');
    }
}


const circle = new Circle();
circle.draw();  // Drawing a circle!


/*
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


/* Create an abstract class -> avoid creating instances of this class, but
still allows inherit from it */
class Operation {
    constructor() {
        if (this.constructor === Operation) {
            throw new Error('The class Operation can not be instantiated!');
        }
    }

    calculate(numOne, numTwo) {
        throw new Error('The method calculate() must be implemented!');
    }
}


// Create the different operations


class Sum extends Operation {
    calculate(numOne, numTwo) {
        return numOne + numTwo;
    }
}


class Subtraction extends Operation {
    calculate(numOne, numTwo) {
        return numOne - numTwo;
    }
}


class Multiplication extends Operation {
    calculate(numOne, numTwo) {
        return numOne * numTwo;
    }
}


class Division extends Operation {
    calculate(numOne, numTwo) {
        return numOne / numTwo;
    }
}


// Create the Calculator class


class Calculator {
    constructor() {
        this.operations = {};
    }

    /**
     * Allows setting a new operation to the Calculator.
     * @param {String} name The name of the operation to set
     * @param {Operation} operation The operation that must be implemented
     */
    setOperation(name, operation) {
        this.operations[name] = operation;
    }

    /**
     * @param {String} name The name of the operation to use
     * @param {Number} numOne The first number to use by the operation
     * @param {Number} numTwo The second number to use by the operation
     * @returns {Number} The result of the implemented operation
     */
    calculate(name, numOne, numTwo) {
        if (!Object.keys(this.operations).includes(name)) {
            throw new Error(`The operation "${name}" does not exist!`)
        }
        return this.operations[name].calculate(numOne, numTwo);
    }
}


// Create the calculator instance and add the different operations
const calculator = new Calculator();
calculator.setOperation('sum', new Sum());
calculator.setOperation('subtract', new Subtraction());
calculator.setOperation('multiply', new Multiplication());
calculator.setOperation('divide', new Division());

// Check if the current operations work
console.log(calculator.calculate('sum', 10, 2));  // 12
console.log(calculator.calculate('subtract', 10, 2));  // 8
console.log(calculator.calculate('multiply', 10, 2));  // 20
console.log(calculator.calculate('divide', 10, 2));  // 5
// console.log(calculator.calculate('pow', 10, 2));  // Error -> The operation "pow" does not exist!


// Create the Pow operation


class Pow extends Operation {
    calculate(numOne, numTwo) {
        return numOne ** numTwo;
    }
}


// Add the Pow operation to the calculator and check if it works
calculator.setOperation('pow', new Pow());
console.log(calculator.calculate('pow', 10, 2));  // 100