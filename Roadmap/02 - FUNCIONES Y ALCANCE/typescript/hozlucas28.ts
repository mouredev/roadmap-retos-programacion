/*
    Types of functions...
*/

// IIFE
;((): void => {
	console.log('IFE (Immediately-Invoked Function Expression): (() => {<INTRUCTIONS...>})()')
})()

// Arrow function
const arrowFunction = (): void => {
	console.log('Arrow function: const <FUNCTION NAME> = (<PARAMETERS...>) => {<INTRUCTIONS...>}')
}

// Common function
function commonFunction(): void {
	console.log('Common function: function <FUNCTION NAME>(<PARAMETERS...>) {<INTRUCTIONS...>}')
}

// With parameters
function fnWithParameters(name: string): void {
	console.log(`Common function (with parameters): function <FUNCTION NAME>(name) {<INTRUCTIONS...>} --> Hello ${name}!`)
}

// Without parameters
function fnWithoutParameters(): void {
	console.log(`Common function (without parameters): function <FUNCTION NAME>() {<INTRUCTIONS...>} --> Hello!`)
}

// With default parameters
function fnWithDefaultParameters(lastName: string = 'Hoz'): void {
	console.log(
		`Common function (with default parameters): function <FUNCTION NAME>(lastName = "Hoz") {<INTRUCTIONS...>} --> By ${lastName}!`
	)
}

// With rest parameter
function fnWithRestParameter(...rest: string[]): void {
	console.log(`Common function (with rest parameter): function <FUNCTION NAME>(...rest) {<INTRUCTIONS...>} --> ${rest}`)
}

// With return
function fnWithReturn(): string {
	return 'Lucas Hoz'
}

// Without return
function fnWithoutReturn(): void {
	console.log(
		`Common function (without return): function <FUNCTION NAME>() {<INTRUCTIONS (return not included)...>} --> return void`
	)
}

arrowFunction()
commonFunction()
fnWithParameters('Lucas')
fnWithoutParameters()
fnWithDefaultParameters()
fnWithRestParameter('JavaScript', 'TypeScript', 'ReactJS', 'NextJS')
console.log(
	`Common function (with return): function <FUNCTION NAME>() {<INTRUCTIONS (with return definition included)...>} --> return '${fnWithReturn()}'`
)
fnWithoutReturn()

/*
    Function definition inside another function...
*/

// Arrow function inside a common function definition
function wrapperFn(): void {
	const innerFn = (): void => {
		console.log('Inner function called')
	}

	console.log('\nWrapper function called')
	innerFn()
}

wrapperFn()

/*
    Native functions...
*/

const result: number = eval('1 + 7')
console.log(`\nNative functions: eval('1 + 7') --> ${result}`)

const casting: number = parseInt('12')
console.log(`Native functions: parseInt('12') --> ${casting} (${typeof casting})`)

/*
    Global and local variables...
*/

const country: string = 'Argentina'

function showCountry(): string {
	const state = 'Buenos Aires'
	return `function call with a global variable --> country = '${country}'`
}

console.log(`\nGlobal variable: ${showCountry()}`)
// console.log(`Local variable: variable defined inside a function but called outside it --> state = ${state}`) // Throw a reference error.
console.log(`Local variable: variable defined inside a function but called outside it --> state = ReferenceError`)

/*
    Additional challenge...
*/

function additionalChallenge(str01: string, str02: string): number {
	console.log('')

	let counter: number = 0
	for (let i = 1; i < 101; i++) {
		const multipleOfFive = i % 5 === 0
		const multipleOfThree = i % 3 === 0

		if (multipleOfFive && multipleOfThree) {
			console.log(str01 + str02)
			continue
		}

		if (multipleOfFive) {
			console.log(str02)
			continue
		}

		if (multipleOfThree) {
			console.log(str01)
			continue
		}

		console.log(i)
		counter++
	}

	return counter
}

console.log(`\n${additionalChallenge('fizz', 'buzz')} numbers was printed instead of 'fizz' or 'buzz' (function arguments)!`)
