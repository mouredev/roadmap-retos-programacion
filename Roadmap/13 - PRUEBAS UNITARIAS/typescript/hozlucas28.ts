/*
    Tests...
*/

console.log('Tests...')

function add(a: number, b: number): number {
	if (typeof a !== 'number' || typeof b !== 'number') {
		throw new Error('Invalid arguments! Both of them should be numbers')
	}
	return a + b
}

console.log(`\nfunction add(a: number, b: number): number {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new Error('Invalid arguments! Both of them should be numbers')
    }
    return a + b
}`)

console.log(
	'\n# ---------------------------------------------------------------------------------- #\n'
)

/*
    Additional challenge...
*/

console.log('Additional challenge...')

type Author = Readonly<{
	age: string
	birth_date: string
	name: string
	programming_languages: string[]
}>

const author: Author = {
	age: '22',
	birth_date: '2002-02-20',
	name: 'Lucas',
	programming_languages: ['TypeScript', 'Python', 'Go (Golang)'],
}

console.log(`\ntype Author = Readonly<{
    age: string
    birth_date: string
    name: string
    programming_languages: string[]
}>

const author: Author = {
    age: '22',
    birth_date: '2002-02-20',
    name: 'Lucas',
    programming_languages: ['TypeScript', 'Python', 'Go (Golang)'],
}`)

export type { Author }

export { add, author }
