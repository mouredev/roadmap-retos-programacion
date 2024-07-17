//EJERCICIO
//Stack - LIFO
console.log('STACK')

const stack: number[] = [1, 2, 3]

console.log('Array original:', stack)

stack.push(4)
console.log('Después de agregar un elemento:', stack)

stack.pop()
console.log('Después de eliminar un elemento:', stack)

//Queue - FIFO
console.log('\nQUEUE')

const queue: number[] = [1, 2, 3]

console.log('Array original:', queue)

queue.push(4)
console.log('Después de agregar un elemento:', queue)

queue.shift()
console.log('Después de eliminar un elemento:', queue)

//EXTRA
import * as readline from 'readline'

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
})

//Sistema de navegacion
function browser(): void {
	const stack = []
}

//Impresora compartida
function printer(): void {
	const queue = []
}
