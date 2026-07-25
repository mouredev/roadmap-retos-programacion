// Wrong way
// interface Shape {
//     type: string;
// }

// class ShapeCalculator {
//     calculateArea(shape: Shape): number {
//         if (shape.type === 'circle') {
//             return Math.PI * Math.pow((shape as Circle).radius, 2);
//         } else if (shape.type === 'square') {
//             return Math.pow((shape as Square).side, 2);
//         } else {
//             throw new Error('Shape not supported');
//         }
//     }
// }

// const calculator = new ShapeCalculator();
// console.log(calculator.calculateArea({ type: 'circle', radius: 5 } as Circle));
// console.log(calculator.calculateArea({ type: 'square', side: 4 } as Square));

// Correct way
abstract class ShapeBase {
    abstract calculateArea(): number;
}

class Circle extends ShapeBase {
    radius: number;

    constructor(radius: number) {
        super();
        this.radius = radius;
    }

    calculateArea(): number {
        return Math.PI * Math.pow(this.radius, 2);
    }
}

class Square extends ShapeBase {
    side: number;

    constructor(side: number) {
        super();
        this.side = side;
    }

    calculateArea(): number {
        return Math.pow(this.side, 2);
    }
}

function printArea(shape: ShapeBase): void {
    console.log(`Area: ${shape.calculateArea()}`);
}

const circle = new Circle(5);
const square = new Square(4);
printArea(circle);
printArea(square);

// ** Extra Exercise ** //
abstract class Operation {
    abstract calculate(a: number, b: number): number;
}

class Addition extends Operation {
    calculate(a: number, b: number): number {
        return a + b;
    }
}

class Subtraction extends Operation {
    calculate(a: number, b: number): number {
        return a - b;
    }
}

class Multiplication extends Operation {
    calculate(a: number, b: number): number {
        return a * b;
    }
}

class Division extends Operation {
    calculate(a: number, b: number): number {
        if (b === 0) throw new Error('Division by zero is not allowed');
        return a / b;
    }
}

class Pow extends Operation {
    calculate(a: number, b: number): number {
        return Math.pow(a, b);
    }
}

class Calculator {
    private operations: { [key: string]: Operation };

    constructor() {
        this.operations = {};
    }

    addOperation(name: string, operation: Operation): void {
        this.operations[name] = operation;
    }

    calculate(name: string, a: number, b: number): number {
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
