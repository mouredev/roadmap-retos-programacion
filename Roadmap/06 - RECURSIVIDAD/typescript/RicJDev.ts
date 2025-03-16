//EJERCICIO
console.log('\nNÚMEROS DEL 100 AL 0')
function countdown(n: number): void {
	if (n >= 0) {
		console.log(n)

		countdown(n - 1)
	}
}

countdown(100)

//EXTRA
console.log('\nFACTORIALES')
function getFactorial(num: number): number {
	if (num < 0) {
		console.log('Número no válido')

		return 0
	} else if (num === 0) {
		return 1
	} else {
		return num * getFactorial(num - 1)
	}
}

console.log(getFactorial(5))

console.log('\nSUCESIÓN DE FIBONACCI')
function fibonacciAt(position: number): number {
	if (position <= 0) {
		console.log('Número no válido')

		return 0
	} else if (position === 1) {
		return 0
	} else if (position === 2) {
		return 1
	} else {
		return getFactorial(position - 1) + fibonacciAt(position - 2)
	}
}

console.log(fibonacciAt(5))
