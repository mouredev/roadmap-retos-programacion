// Wrong way
class ShapeCalculator {
    calculateArea(shape) {
        if (shape.type === 'circle'){
            return Math.PI * Math.pow(shape.radius, 2);
        } else if (shape.type === 'square') {
            return Math.pow(shape.side, 2);
        } else {
            throw new Error('Shape not supported');
        }
    }
}

const calculator = new ShapeCalculator();
console.log(calculator.calculateArea({ type: 'circle', radius: 5 }));
console.log(calculator.calculateArea({ type: 'square', side: 4 }));

// Correct way
class Shape {
    calculateArea(shape) {
        throw new Error('calculateArea() must be implemented');
    }
}

class Circle extends Shape {
    constructor(radius) {
        super();
        this.radius = radius;
    }

    calculateArea() {
        return Math.PI * Math.pow(this.radius, 2);
    }
}

class Square extends Shape {
    constructor(side) {
        super();
        this.side = side;
    }

    calculateArea() {
        return Math.pow(this.side, 2);
    }
}

function printArea(shape) {
    console.log(`Area: ${shape.calculateArea()}`);
}

const circle = new Circle(5);
const square = new Square(4);
printArea(circle);
printArea(square);

// Extra Exercise //
class Operation {
    calculate(a, b) {
        throw new Error('calculateOperation() must be implemented');
    }
}

class Addition extends Operation {
    calculate(a, b) {
        return a + b;
    }
}

class Subtraction extends Operation {
    calculate(a, b) {
        return a - b;
    }
}

class Multiplication extends Operation {
    calculate(a, b) {
        return a * b;
    }
}

class Division extends Operation {
    calculate(a, b) {
        if (b === 0) throw new Error('Division by zero is not allowed');
        return a / b;
    }
}

class Pow extends Operation {
    calculate(a, b) {
        return Math.pow(a, b);
    }
}

class Calculator {
    constructor() {
        this.operations = {};
    }

    addOperation(name, operation) {
        this.operations[name] = operation;
    }

    calculate(name, a, b) {
        const operation = this.operations[name];
        if (!operation) throw new Error(`Operation "${name}" not supported`);
        return operation.calculate(a, b);
    }
}

const calculator2 = new Calculator();
calculator2.addOperation('addition', new Addition());
calculator2.addOperation('subtraction', new Subtraction());
calculator2.addOperation('multiplication', new Multiplication());
calculator2.addOperation('division', new Division());
calculator2.addOperation('pow', new Pow());

console.log(calculator2.calculate('addition', 2, 10));
console.log(calculator2.calculate('subtraction', 2, 10));
console.log(calculator2.calculate('multiplication', 2, 10));
console.log(calculator2.calculate('division', 10, 5));
console.log(calculator2.calculate('pow', 10, 2));


