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
import * as readline from 'node:readline/promises'

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
})

//Sistema de navegación
function browser(): void {
	const pagesStack: string[] = []

	function menu(): void {
		if (pagesStack.length > 0) {
			console.log(`\nActualmente estas en ${pagesStack[pagesStack.length - 1]}`)
		} else {
			console.log('\nEstas en la pagina de inicio')
		}

		rl.question(
			'Elige una opcion\n1. Avanzar\n2. Retroceder\n3. Salir del navegador\nIr a otra pagina '
		).then((answer) => {
			if (answer === '1') {
				menu()
			} else if (answer === '2') {
				pagesStack.pop()
				menu()
			} else if (answer === '3') {
				console.log('\nSaliendo del navegador...')
				printer()
			} else {
				pagesStack.push(answer)
				menu()
			}
		})
	}

	menu()
}

browser()

//Impresora compartida
function printer(): void {
	const queue = []

	console.log('Hola')
	rl.close()

	function menu() {}
}
