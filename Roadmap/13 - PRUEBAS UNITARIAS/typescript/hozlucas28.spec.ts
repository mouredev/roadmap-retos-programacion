import type { Author } from './hozlucas28'
import { add, author } from './hozlucas28'

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
