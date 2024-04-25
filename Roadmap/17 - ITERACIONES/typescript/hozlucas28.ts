/*
    Iterations...
*/

console.log('Iterations...')

const FROM: number = 0
const TO: number = 10

function recursiveFn(from: number, to: number): void {
	console.log(`${from}`)
	from < to && recursiveFn(from + 1, to)
}

console.log('\nFirst method...\n')
recursiveFn(FROM, TO)

console.log('\nSecond method...\n')
for (let i: number = FROM; i <= TO; i++) console.log(`${i}`)

console.log('\nThird method...\n')
let nJ: number = FROM
while (nJ <= TO) {
	console.log(`${nJ}`)
	nJ++
}

console.log(
	'\n# ---------------------------------------------------------------------------------- #\n'
)

/*
    Additional challenge...
*/

console.log('Additional challenge...')

console.log('\nFirst method...\n')
recursiveFn(FROM, TO)

console.log('\nSecond method...\n')
for (let i: number = FROM; i <= TO; i++) console.log(`${i}`)

console.log('\nThird method...\n')
nJ = FROM
while (nJ <= TO) {
	console.log(`${nJ}`)
	nJ++
}

console.log('\nFourth method...\n')
nJ = FROM
do {
	console.log(`${nJ}`)
	nJ++
} while (nJ <= TO)

console.log('\nFifth method...\n')
Array.from({ length: TO }, (_, i) => i + 1).map((_, index) =>
	console.log(`${index + 1}`)
)

console.log('\nSixth method...\n')
Array.from({ length: TO }, (_, i) => i + 1).forEach((value, index) => {
	console.log(`${index + 1}`)
	return value
})

console.log('\nSeventh method...\n')
Array.from({ length: TO }, (_, i) => i + 1).reduce((_, current, currentI) => {
	console.log(`${currentI + 1}`)
	return current
}, 0)

console.log('\nEighth method...\n')
Array.from({ length: TO }, (_, i) => i + 1).every((_, index) => {
	console.log(`${index + 1}`)
	return true
})
