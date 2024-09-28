/*
    Classes...
*/

type Brand = 'BMW' | 'Ford' | 'Toyota' | 'Fiat'
type Color = 'black' | 'grey' | 'red' | 'blue' | 'yellow'

type Constructor = {
	brand: Brand
	color: Color
	name: string
	price: number
}

class Car {
	private _brand: Brand
	private _color: Color
	private _name: string
	private _price: number

	constructor({ brand, color, name, price }: Constructor) {
		this._brand = brand
		this._color = color
		this._name = name
		this._price = price
	}

	public get brand(): Brand {
		return this._brand
	}

	public get color(): Color {
		return this._color
	}

	public get name(): string {
		return this._name
	}

	public get price(): number {
		return this._price
	}

	public set brand(brand: Brand) {
		this._brand = brand
	}

	public set color(color: Color) {
		this._color = color
	}

	public set name(name: string) {
		this._name = name
	}

	public set price(price: number) {
		this._price = price
	}

	public printAttributes(): void {
		console.log('\nCar attributes:')
		console.log(`Brand --> ${this._brand}`)
		console.log(`Color --> ${this._color}`)
		console.log(`Name --> ${this._name}`)
		console.log(`Price --> $${this._price}`)
	}
}

console.log('Classes in TypeScript...\n')

console.log(`type Brand = 'BMW' | 'Ford' | 'Toyota' | 'Fiat'
type Color = 'black' | 'grey' | 'red' | 'blue' | 'yellow'

type Constructor = {
    brand: Brand
    color: Color
    name: string
    price: number
}

class Car {
    private _brand: Brand
    private _color: Color
    private _name: string
    private _price: number

    constructor({ brand, color, name, price }: Constructor) {
        this._brand = brand
        this._color = color
        this._name = name
        this._price = price
    }

    public get brand(): Brand {
        return this._brand
    }

    public get color(): Color {
        return this._color
    }

    public get name(): string {
        return this._name
    }

    public get price(): number {
        return this._price
    }

    public set brand(brand: Brand) {
        this._brand = brand
    }

    public set color(color: Color) {
        this._color = color
    }

    public set name(name: string) {
        this._name = name
    }

    public set price(price: number) {
        this._price = price
    }

    public printAttributes(): void {
        console.log('\\nCar attributes:')
        console.log(\`Brand --> \${this._brand}\`)
        console.log(\`Color --> \${this._color}\`)
        console.log(\`Name --> \${this._name}\`)
        console.log(\`Price --> $\${this._price}\`)
    }
}`)

console.log(
	'\n' +
		`const car = new Car({ brand: 'Ford', color: 'grey', name: 'Focus', price: 21000 })
car.printAttributes()`
)

const car = new Car({ brand: 'Ford', color: 'grey', name: 'Focus', price: 21000 })
car.printAttributes()

console.log(
	'\n' +
		`car.brand = 'Fiat'
car.color = 'grey'
car.name = 'Cronos'
car.price = 18000
car.printAttributes()`
)

car.brand = 'Fiat'
car.color = 'grey'
car.name = 'Cronos'
car.price = 18000
car.printAttributes()

console.log('\n# ---------------------------------------------------------------------------------- #\n')

/*
    Additional challenge...
*/

console.log('Additional challenge...')

// Stack exercise...
class Stack<T extends number | string> {
	private _lastElement: T | undefined
	private _length: number
	private _stack: T[]

	constructor(stack: T[] = []) {
		this._lastElement = stack.at(-1)
		this._length = stack.length
		this._stack = stack
	}

	public get lastElement(): T | undefined {
		return this._lastElement
	}

	public get length(): number {
		return this._length
	}

	public get stack(): T[] {
		return this._stack
	}

	public appendElement(element: T): this {
		this._length = this._stack.push(element)
		this._lastElement = this._stack.at(-1)
		return this
	}

	public deleteLastElement(): this {
		this._stack.pop()
		this._lastElement = this._stack.at(-1)
		this._length--
		return this
	}

	public printAttributes(): this {
		console.table({
			lastElement: this._lastElement,
			length: this._length,
			stack: this._stack,
		})
		return this
	}
}

const myStack = new Stack<string>(['Lucas', 'Nahuel', 'Hoz'])

myStack.appendElement('21')

console.log('\nStack attributes...')
myStack.printAttributes()

myStack.deleteLastElement().deleteLastElement()

console.log('\nStack attributes...')
myStack.printAttributes()

const stackLength = myStack.length
console.log(`\nStack length --> ${stackLength}`)

// Queue exercise...

class Queue<T extends number | string> {
	private _length: number
	private _firstElement: T | undefined
	private _queue: T[]

	constructor(queue: T[]) {
		this._length = queue.length
		this._firstElement = queue.at(0)
		this._queue = queue
	}

	public get length(): number {
		return this._length
	}

	public get firstElement(): T | undefined {
		return this._firstElement
	}

	public get queue(): T[] {
		return this._queue
	}

	public appendElement(element: T): this {
		this._length = this._queue.push(element)
		return this
	}

	public deleteFirstElement(): this {
		this._queue.shift()
		this._length--
		this._firstElement = this._queue.at(0)
		return this
	}

	public printAttributes(): this {
		console.table({
			length: this._length,
			firstElement: this._firstElement,
			queue: this._queue,
		})
		return this
	}
}

const myQueue = new Queue<string>(['Buenos', 'Aires', 'Argentina'])

myQueue.appendElement('2024')

console.log('\nQueue attributes...')
myQueue.printAttributes()

myQueue.deleteFirstElement().deleteFirstElement()

console.log('\nQueue attributes...')
myQueue.printAttributes()

const queueLength = myQueue.length
console.log(`\nQueue length --> ${queueLength}`)
