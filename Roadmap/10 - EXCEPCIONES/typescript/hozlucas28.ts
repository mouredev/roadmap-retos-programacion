/*
    Exceptions...
*/

console.log('Exceptions...')

console.log(`\nlet array: number[][] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

try {
    array[3][0] += array[2][0]
    array[3][1] += array[2][1]
    array[3][2] += array[2][2]
} catch (error) {
    console.error(\`\\n\${error}\`)
}`)

let array: number[][] = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]

try {
	array[3][0] += array[2][0]
	array[3][1] += array[2][1]
	array[3][2] += array[2][2]
} catch (error) {
	console.error(`\n${error}`)
}

console.log(
	'\n# ---------------------------------------------------------------------------------- #\n'
)

/*
    Additional challenge...
*/

console.log('Additional challenge...')

function fn(param: number | string | string[] | Function): string | undefined {
	if (typeof param === 'number') throw new Error('My custom error')
	if (typeof param === 'function') param()
	// @ts-expect-error
	return param.toUpperCase()
}

// No error
try {
	const rtn = fn('Hello World!')
	console.log(`\n${rtn}`)
} catch (error) {
	console.error(`\n${error}`)
}

// Custom error
try {
	const rtn = fn(22)
	console.log(`\n${rtn}`)
} catch (error) {
	console.error(`\n${error}`)
}

// Range error
try {
	const recursiveFn = () => recursiveFn()
	const rtn = fn(recursiveFn)
	console.log(`\n${rtn}`)
} catch (error) {
	console.error(`\n${error}`)
}

// Type error
try {
	const rtn = fn(['Hello World!'])
	console.log(`\n${rtn}`)
} catch (error) {
	console.error(`\n${error}`)
}

console.log('\nAdditional challenge finished!')
