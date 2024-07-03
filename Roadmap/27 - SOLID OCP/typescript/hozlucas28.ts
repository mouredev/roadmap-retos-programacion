/*
    Open-Close Principle (OCP)...
*/

console.log('Open-Close Principle (OCP)...')

console.log('\nBad implementation of Open-Close Principle (OCP)...')

interface IBadCircle {
    radius: number
}

class BadCircle implements IBadCircle {
    public radius: number

    public constructor({radius}: {radius: number}) {
        this.radius = radius
    }
}

interface IBadRectangle {
    height: number
    width: number
}

class BadRectangle implements IBadRectangle {
    public height: number
    public width: number

    public constructor({height, width}: {height: number; width: number}) {
        this.height = height
        this.width = width
    }
}

interface IBadShapeCalculator {
    getArea(shape: BadCircle | BadRectangle): number
}

class BadShapeCalculator implements IBadShapeCalculator {
    public constructor() {}

    public getArea(shape: BadCircle | BadRectangle): number {
        if (shape instanceof BadCircle) {
            return Math.PI * Math.pow(shape.radius, 2)
        } else if (shape instanceof BadRectangle) {
            return shape.height * shape.width
        } else {
            return -1
        }
    }
}

console.log(`\n\`\`\`\ninterface IBadCircle {
    radius: number
}

class BadCircle implements IBadCircle {
    public radius: number

    public constructor({radius}: {radius: number}) {
        this.radius = radius
    }
}

interface IBadRectangle {
    height: number
    width: number
}

class BadRectangle implements IBadRectangle {
    public height: number
    public width: number

    public constructor({height, width}: {height: number; width: number}) {
        this.height = height
        this.width = width
    }
}

interface IBadShapeCalculator {
    getArea(shape: BadCircle | BadRectangle): number
}

class BadShapeCalculator implements IBadShapeCalculator {
    public constructor() {}

    public getArea(shape: BadCircle | BadRectangle): number {
        if (shape instanceof BadCircle) {
            return Math.PI * Math.pow(shape.radius, 2)
        } else if (shape instanceof BadRectangle) {
            return shape.height * shape.width
        } else {
            return -1
        }
    }
}\n\`\`\``)

console.log(
    '\nThis is a bad implementation of Open-Close Principle (OCP),\n' +
        'because the method "getArea" of class "BadShapeCalculator" will must change\n' +
        'if we have to add more shapes.'
)

console.log('\nGood implementation of Open-Close Principle (OCP)...')

interface Shape {
    getArea(): number
}

interface IGoodCircle extends Shape {
    radius: number
}

class GoodCircle implements IGoodCircle {
    public radius: number

    public constructor({radius}: {radius: number}) {
        this.radius = radius
    }

    public getArea(): number {
        return Math.PI * Math.pow(this.radius, 2)
    }
}

interface IGoodRectangle extends Shape {
    width: number
    height: number
}

class GoodRectangle implements IGoodRectangle {
    public height: number
    public width: number

    public constructor({height, width}: {height: number; width: number}) {
        this.height = height
        this.width = width
    }

    public getArea(): number {
        return this.height * this.width
    }
}

interface IGoodShapeCalculator {
    getArea(shape: Shape): number
}

class GoodShapeCalculator implements IGoodShapeCalculator {
    public constructor() {}

    public getArea(shape: Shape): number {
        return shape.getArea()
    }
}

console.log(`\n\`\`\`\ninterface Shape {
    getArea(): number
}

interface IGoodCircle extends Shape {
    radius: number
}

class GoodCircle implements IGoodCircle {
    public radius: number

    public constructor({radius}: {radius: number}) {
        this.radius = radius
    }

    public getArea(): number {
        return Math.PI * Math.pow(this.radius, 2)
    }
}

interface IGoodRectangle extends Shape {
    width: number
    height: number
}

class GoodRectangle implements IGoodRectangle {
    public height: number
    public width: number

    public constructor({height, width}: {height: number; width: number}) {
        this.height = height
        this.width = width
    }

    public getArea(): number {
        return this.height * this.width
    }
}

interface IGoodShapeCalculator {
    getArea(shape: Shape): number
}

class GoodShapeCalculator implements IGoodShapeCalculator {
    public constructor() {}

    public getArea(shape: Shape): number {
        return shape.getArea()
    }
}\n\`\`\``)

console.log(
    '\nThis is a good implementation of Open-Close Principle (OCP),\n' +
        'because the method "getArea" of class "GoodShapeCalculator" will must\n' +
        'not change if we have to add more shapes. So, "getArea" is closed to modification\n' +
        'but it is open to extension throw any shape which implements "Shape" interface.'
)

console.log(
    '\n# ---------------------------------------------------------------------------------- #\n'
)

/*
    Additional challenge...
*/

console.log('Additional challenge...')

interface MathOperation {
    execute(a: number, b: number): number
}

class AddOperation implements MathOperation {
    public constructor() {}

    public execute(a: number, b: number): number {
        return a + b
    }
}

class DivideOperation implements MathOperation {
    public constructor() {}

    public execute(a: number, b: number): number {
        if (b === 0) {
            throw new Error('The second parameter must not be zero')
        }

        return a / b
    }
}

class MultiplyOperation implements MathOperation {
    public constructor() {}

    public execute(a: number, b: number): number {
        return a * b
    }
}

class SubtractOperation implements MathOperation {
    public constructor() {}

    public execute(a: number, b: number): number {
        return a - b
    }
}

interface ICalculator {
    addOperation(name: string, operation: MathOperation): this
    executeOperation(name: string, a: number, b: number): number
}

class Calculator implements ICalculator {
    private operations: Record<string, MathOperation> = {}

    public addOperation(name: string, operation: MathOperation): this {
        const operationExist: boolean = !!this.operations[name]
        if (operationExist) {
            throw new Error(`The operation with '${name}' name already exist`)
        }

        this.operations[name] = operation
        return this
    }

    public executeOperation(name: string, a: number, b: number): number {
        const operation: undefined | MathOperation = this.operations[name]
        if (!operation) {
            throw new Error(`There is not operation with '${name}' name`)
        }

        return operation.execute(a, b)
    }
}

console.log('\nTesting the OCP system without a pow operation...')

const calculator: Calculator = new Calculator()
calculator.addOperation('add', new AddOperation())
calculator.addOperation('divide', new DivideOperation())
calculator.addOperation('multiply', new MultiplyOperation())
calculator.addOperation('subtract', new SubtractOperation())

let a: number = 10
let b: number = 5

console.log(
    `\nAdd operation result (${a} + ${b}): ${calculator.executeOperation(
        'add',
        a,
        b
    )}`
)

a = 10
b = 2

console.log(
    `Divide operation result (${a} / ${b}): ${calculator.executeOperation(
        'divide',
        a,
        b
    )}`
)

a = 5
b = 10

console.log(
    `Multiply operation result (${a} * ${b}): ${calculator.executeOperation(
        'multiply',
        a,
        b
    )}`
)

a = 6
b = 6

console.log(
    `Subtract operation result (${a} - ${b}): ${calculator.executeOperation(
        'subtract',
        a,
        b
    )}`
)

console.log('\nTesting the OCP system with a pow operation...')

class PowOperation implements MathOperation {
    public constructor() {}

    public execute(a: number, b: number): number {
        return Math.pow(a, b)
    }
}

calculator.addOperation('pow', new PowOperation())

a = 2
b = 10

console.log(
    `\nPow operation result (${a}^${b}): ${calculator.executeOperation(
        'pow',
        a,
        b
    )}`
)
