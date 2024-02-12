/*
    Type of operators...
*/

// Arithmetic
let number01: number = 10

console.log(number01 + 1)
console.log(number01 - 1)

console.log(number01 * 2)
console.log(number01 ** 2)

console.log(number01 / 5)
console.log(number01 % 5)

number01++
console.log(number01)

number01--
console.log(number01)

// Comparison
const obj = { text: 'Hello' }

// @ts-expect-error
console.log(1 == '1')
console.log(1 === 1)

console.log(1 > 1)
console.log(2 < 2)
console.log(1 >= 1)
console.log(2 <= 2)

// @ts-expect-error
console.log(obj === { text: 'hello' })
console.log(Object.is(obj, { text: 'hello' }))

// Logical
console.log(!true)

console.log(true && false)
console.log(true || false)

console.log(undefined ?? 'Hi!')

/*
    Control structures...
*/

// < if >
if (!true) {
	console.log('¡Hello World!')
} else {
	console.log('¡By World!')
}

// < ternary >
const text: string = true ? 'Mouredev' : 'Midudev'
console.log(text)

// < switch >
const letter: string = 'A'

switch (letter) {
	case 'A':
		console.log('Case 1 --> Letter A')
		break
	case 'E':
		console.log('Case 2 --> Letter E')
		break
	case 'I':
		console.log('Case 3 --> Letter I')
		break
	case 'O':
		console.log('Case 4 --> Letter O')
		break
	case 'U':
		console.log('Case 5 --> Letter U')
		break

	default:
		console.log(`Default case --> Letter ${letter}`)
		break
}

// < while > and < do while >
let i: number = 0

while (i !== 2) {
	console.log('While!')
	i++
}

do {
	console.log('Do while!')
} while (false)

// < for >
for (let j = 0; j < 5; j++) {
	if (j === 3) break
	console.log(j)
}

// < for of > and < for in >
const animals: string[] = ['Dog', 'Cat', 'Crocodile', 'Shark']

for (const animal of animals) {
	if (animal === 'Crocodile') continue
	console.log(animal)
}

for (const index in animals) {
	console.log(index)
}

/*
    Additional challenge...
*/

console.log()
for (let i = 10; i < 56; i++) {
	const isEven = i % 2 === 0
	const isMultipleOfThree = i % 3 === 0
	if (isEven && i !== 16 && !isMultipleOfThree) console.log(i)
}
