/*
    Recursive function...
*/

console.log('\nRecursive function...')

function recursiveFn(from: number, to: number, rtn: number[]) {
	if (from < to) return rtn
	rtn.push(from)
	recursiveFn(from - 1, to, rtn)
}

console.log(`\nfunction recursiveFn(from: number, to: number, rtn: number[]) {
    if (from < to) return rtn
    rtn.push(from)
    recursiveFn(from - 1, to, rtn)
}`)

const recursiveRtn: number[] = []
recursiveFn(100, 0, recursiveRtn)

console.log(`\nrecursiveFn(100, 0, recursiveRtn)`)
console.log(`\nrecursiveRtn --> [${recursiveRtn}]`)

console.log('\n# ---------------------------------------------------------------------------------- #\n')

/*
    Additional challenge...
*/

console.log('Get factorial...')

function getFactorial(n: number): number {
	if (n === 1) return 1
	return n * getFactorial(n - 1)
}

console.log(`\nfunction getFactorial(n: number): number {
    if (n === 1) return 1
    return n * getFactorial(n - 1)
}`)

console.log(`\ngetFactorial(5) --> ${getFactorial(5)}`)

console.log('\n# ---------------------------------------------------------------------------------- #\n')

console.log('Get Fibonacci value by position...')

function getFibonacciValueByPos(posicion: number): number {
	if (posicion === 1 || posicion === 2) {
		return 1
	}

	return getFibonacciValueByPos(posicion - 1) + getFibonacciValueByPos(posicion - 2)
}

console.log(`\nfunction getFibonacciValueByPos(posicion: number): number {
    if (posicion === 1 || posicion === 2) {
        return 1
    }

    return getFibonacciValueByPos(posicion - 1) + getFibonacciValueByPos(posicion - 2)
}`)

console.log(`\ngetFibonacciValueByPos(8) --> ${getFibonacciValueByPos(8)}`)
