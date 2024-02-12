/*
    Variable assignment by value...
*/

console.log('Variable assignment by value...')

let a: number = 5
const b: number = a

console.log(`\nlet a: number = 5
const b: number = a`)
console.table({ a, b }) // { a: 5, b: 5 }

a = a * 2

console.log(`\na = a * 2`)
console.table({ a, b }) // { a: 10, b: 5 }

console.log('\n# ---------------------------------------------------------------------------------- #')

/*
    Variable assignment by reference...
*/

console.log('\nVariable assignment by reference...')

const c: Record<'First property', number> = {
	'First property': 6,
}
const d: Record<'First property', number> = c
console.log(`\nconst c: Record<string, number> = { 'First property': 6 }
const d: Record<'First property', number> = c`)

console.table({ c, d })

c['First property'] = 6 * 3
console.log(`\nc['First property'] = 6 * 3`)

console.table({ c, d })

console.log('\n# ---------------------------------------------------------------------------------- #')

/*
    Function with an argument passed by value...
*/

console.log('\nFunction with an argument passed by value...')

const value: number = 10
function fnWithParamenterByValue(x: number) {
	x += x
}

console.log('\nconst value: number = 10')
console.log(`function fnWithParamenterByValue(x: number) {
    x += x
}`)

fnWithParamenterByValue(value)
console.log('\nfnWithParamenterByValue(value)')

console.table({ value })

/*
    Function with an argument passed by reference...
*/

console.log('\nFunction with an argument passed by reference...')

const reference: { zipCode: number } = { zipCode: 127 }
function fnWithParamenterByReference(params: { zipCode: number }) {
	params.zipCode = params.zipCode * 2
}

console.log('\nconst reference: { zipCode: number } = { zipCode: 127 }')
console.log(`function fnWithParamenterByReference(params: { zipCode: number }) {
    params.zipCode = params.zipCode * 2
}`)

fnWithParamenterByReference(reference)
console.log('\nfnWithParamenterByReference(reference)')

console.table({ reference })

console.log('\n# ---------------------------------------------------------------------------------- #\n')

/*
    Additional challenge...
*/

function firstProgram(param01: number, param02: number): [number, number] {
	const aux: number = param01
	param01 = param02
	param02 = aux
	return [param01, param02]
}

function secondProgram(
	param01: Record<'firstName', string>,
	param02: Record<'firstName', string>
): [Record<'firstName', string>, Record<'firstName', string>] {
	const aux: string = param01.firstName
	param01.firstName = param02.firstName
	param02.firstName = aux
	return [param01, param02]
}

const arg01: number = 12
const arg02: number = 34
const arg03: Record<'firstName', string> = { firstName: 'Lucas' }
const arg04: Record<'firstName', string> = { firstName: 'Nahuel' }

const [newArg01, newArg02]: [number, number] = firstProgram(arg01, arg02)
const [newArg03, newArg04]: [Record<string, string>, Record<string, string>] = secondProgram(arg03, arg04)

console.table({
	original: [arg01, arg02],
	new: [newArg01, newArg02],
})

console.table({
	original: [arg03, arg04],
	new: [newArg03, newArg04],
})
