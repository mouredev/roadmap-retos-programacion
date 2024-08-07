/*
    Stack methods for insert and recover items...
*/

console.log('Stack methods for insert and recover items...')

const stack: number[] = [6, 4, 2, 0, 5]

console.log('\nconst stack: number[] = [6, 4, 2, 0, 5]')

console.log('\nInsert an element at the end of the stack...')

stack.push(3)

console.log(`\nstack.push(3) --> stack = [${stack}]`)

console.log('\nRecover an element of the stack...')

const stackElement = stack.pop()

console.log(`\nstack.pop() --> stackElement = ${stackElement}`)

console.log('\n# ---------------------------------------------------------------------------------- #\n')

/*
    Queue methods for insert and recover items...
*/

console.log('Queue methods for insert and recover items...')

const queue: string[] = ['Hello', 'World']

console.log("\nconst queue: string[] = ['Hello', 'World']")

console.log('\nInsert an element at the end of the queue...')

queue.push('TypeScript')

console.log(`\nqueue.push("TypeScript") --> queue = [${queue}]`)

console.log('\nRecover an element of the queue...')

const queueElement = queue.shift()

console.log(`\nqueue.shift() --> queueElement = ${queueElement}`)

console.log('\n# ---------------------------------------------------------------------------------- #\n')

/*
    Additional challenge...
*/

// Stack exercise...
console.log('Stack exercise...')

type Operation = Uppercase<'forward' | 'back'>

const operationActions: Record<Operation, (stack: string[]) => string[]> = {
	BACK: (stack) => [...stack.slice(0, stack.length - 1)],
	FORWARD: (stack) => {
		const lastPageNumber: number = parseInt(stack.at(-1)?.slice(-2) ?? '0')
		return [...stack, `Page ${lastPageNumber + 1}`]
	},
}

let browserHistory: string[] = []

while (true) {
	console.table(browserHistory)

	const operation = prompt('Select an operation ("Back", "Forward", or "Exit"):')
	if (!operation || operation.match(/exit/i)) break

	const operationFormatted = operation.toUpperCase()
	const operationAction = operationActions[operationFormatted]
	browserHistory = operationAction ? operationAction(browserHistory) : browserHistory
}

// Queue exercise...
console.log('Queue exercise...')

const documents: string[] = []

while (true) {
	console.table(documents)

	const userInput = prompt('Add a document to print, or write "print" to print the document in the queue:')
	if (!userInput) break

	const userInputFormatted = userInput.toUpperCase()

	if (userInputFormatted === 'PRINT') {
		const printedDocument = documents.shift()
		console.log(`Printed document --> ${printedDocument}`)
	} else documents.push(userInput)
}
