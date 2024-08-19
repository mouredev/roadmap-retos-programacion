/*
    Enums...
*/

console.log('Enums...')

enum WeekDays {
	Monday,
	Tuesday,
	Wednesday,
	Thursday,
	Friday,
	Saturday,
	Sunday,
}

console.log(`\nName of the first week day: ${WeekDays[0]}`)
console.log(`Name of the second week day: ${WeekDays[1]}`)
console.log(`Name of the third week day: ${WeekDays[2]}`)
console.log(`Name of the fourth week day: ${WeekDays[3]}`)
console.log(`Name of the fifth week day: ${WeekDays[4]}`)
console.log(`Name of the sixth week day: ${WeekDays[5]}`)
console.log(`Name of the seventh week day: ${WeekDays[6]}`)

console.log(
	'\n# ---------------------------------------------------------------------------------- #\n'
)

/*
    Additional challenge...
*/

console.log('Additional challenge...')

enum State {
	Earring,
	Sent,
	Delivered,
	Cancelled,
}

class Order {
	protected id: number
	protected state: State

	constructor({ id, state }: { id: number; state: State }) {
		this.id = id
		this.state = state
	}

	public getId(): number {
		return this.id
	}

	public getState(): State {
		return this.state
	}

	public cancel(): void | never {
		if (this.state === State.Earring) {
			this.state = State.Cancelled
			return
		}

		throw new Error(`The order with ${this.id} id can't be cancelled`)
	}

	public delivered(): void | never {
		if (this.state === State.Sent) {
			this.state = State.Delivered
			return
		}

		throw new Error(`The order with ${this.id} id can't be delivered`)
	}

	public printState(): this {
		console.log(
			`The order with ${this.id} id was ${State[this.state].toLowerCase()}`
		)
		return this
	}

	public send(): void | never {
		if (this.state === State.Earring) {
			this.state = State.Sent
			return
		}

		throw new Error(`The order with ${this.id} id can't be sent`)
	}
}

const firstOrder: Order = new Order({ id: 1, state: State.Earring })
const secondOrder: Order = new Order({ id: 2, state: State.Sent })
const thirdOrder: Order = new Order({ id: 3, state: State.Delivered })
const fourthOrder: Order = new Order({ id: 4, state: State.Cancelled })

console.log()
firstOrder.printState()
secondOrder.printState()
thirdOrder.printState()
fourthOrder.printState()

firstOrder.send()
firstOrder.delivered()

console.log()
firstOrder.printState()

console.log()
try {
	secondOrder.send()
} catch (error) {
	if (error instanceof Error) console.error(error.message)
}

try {
	thirdOrder.delivered()
} catch (error) {
	if (error instanceof Error) console.error(error.message)
}

try {
	fourthOrder.send()
} catch (error) {
	if (error instanceof Error) console.error(error.message)
}
