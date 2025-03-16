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

/*
	Toda declaración, debajo del presente comentario, debe ser extraída a un archivo con el mismo nombre
	que el actual, pero finalizando con `*.spec.ts`, por ejemplo: `hozlucas28.spec.ts`. Caso contrario los
	tests no se ejecutaran correctamente.
*/

/*
    Tests...
*/

describe('Addition', () => {
	it('Numbers', () => {
		const result: number = add(1, 4)
		const expectedResult: number = 5
		expect(result).toBe<number>(expectedResult)
	})

	it('Floats', () => {
		const result: number = add(2.25, 6.75)
		const expectedResult: number = 9
		expect(result).toBe<number>(expectedResult)
	})

	it('Strings', () => {
		// @ts-expect-error
		expect(() => add('1', '4')).toThrow()
	})
})

/*
    Additional challenge...
*/

describe('Dictionary', () => {
	it('Schema', () => {
		const expectedResult: Author = {
			age: expect.any(String),
			birth_date: expect.any(String),
			name: expect.any(String),
			programming_languages: expect.any(Array),
		}

		expect(author).toMatchObject(expectedResult)
	})

	it('Data types', () => {
		const expectedResult: Author = {
			age: '22',
			birth_date: '2002-02-20',
			name: 'Lucas',
			programming_languages: ['TypeScript', 'Python', 'Go (Golang)'],
		}

		expect(author).toStrictEqual(expectedResult)
	})
})
