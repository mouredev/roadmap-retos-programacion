/*
    String operations...
*/

// Get length of a string
const strLength = 'Hello World!'.length
console.log('Get length of a string: const <VARIABLE NAME> = <STRING NAME>.length')
console.log(`'Hello World!'.length --> ${strLength}`)

// Get char of a string
const char = 'Hello World!'[1]
console.log('\nGet char of a string: const <VARIABLE NAME> = <STRING NAME>[<INDEX OF THE CHAR>]')
console.log(`'Hello World!'[1] --> '${char}'`)

// Get substring of a string
const substring = 'Hello World!'.substring(2, 9)
console.log('\nGet substring of a string: const <VARIABLE NAME> = <STRING NAME>.substring(<START - 1>, <END>)')
console.log(`'Hello World!'.substring(2, 9) --> '${substring}'`)

// String to uppercase
const uppercaseStr = 'Buenos Aires'.toUpperCase()
console.log('\nString to uppercase: const <VARIABLE NAME> = <STRING NAME>.toUpperCase()')
console.log(`"Buenos Aires".toUpperCase() --> '${uppercaseStr}'`)

// String to lowercase
const lowercaseStr = 'USA'.toLowerCase()
console.log('\nString to lowercase: const <VARIABLE NAME> = <STRING NAME>.toLowerCase()')
console.log(`"USA".toLowerCase() --> '${lowercaseStr}'`)

// Repeat a string
const repeatedStr = 'Juana'.repeat(2)
console.log('\nRepeat a string: const <VARIABLE NAME> = <STRING NAME>.repeat(<NUMBER OF REPEATS>)')
console.log(`"Juana".repeat(2) --> '${repeatedStr}'`)

// Concat two strings (first option)
const concatedStrOpt01 = 'Lucas ' + 'Hoz'
console.log(
	"\nConcat two strings (first option): const <VARIABLE NAME> = <FIRST STRING NAME> + <SECOND STRING NAME> + <'N' STRING NAME...>"
)
console.log(`"Lucas " + "Hoz" --> '${concatedStrOpt01}'`)

// Concat two strings (second option)
const concatedStrOpt02 = 'Lucas'.concat(' ', 'Hoz', ' - ', 'Argentina')
console.log("\nConcat two strings (second option): const <VARIABLE NAME> = <FIRST STRING NAME>.concat(<'N' STRING NAME...>)")
console.log(`'Lucas'.concat(' ', 'Hoz', ' - ', 'Argentina') --> '${concatedStrOpt02}'`)

// Replace substring of a string
const replacedStr = 'Hello Python!'.replace('Python', 'TypeScript')
console.log(
	'\nReplace substring of a string: const <VARIABLE NAME> = <STRING NAME>.replace(<SUBSTRING TO SEARCH>, <NEW SUBSTRING>)'
)
console.log(`'Hello Python!'.replace('Python', 'TypeScript') --> '${replacedStr}'`)

// Compare start of a string
const compareStart = 'Lucas'.startsWith('ho')
console.log('\nCompare start of a string: <STRING NAME>.startsWith(<SUBSTRING TO FIND>)')
console.log(`'Lucas'.startsWith('ho') --> ${compareStart}`)

// Compare end of a string
const compareEnd = 'Lucas'.endsWith('as')
console.log('\nCompare end of a string: <STRING NAME>.endsWith(<SUBSTRING TO FIND>)')
console.log(`'Lucas'.endsWith('as') --> ${compareEnd}`)

// Check if a string includes a substring
const includes = 'Lucas'.includes('c')
console.log('\nCheck if a string includes a substring: <STRING NAME>.includes(<SUBSTRING TO FIND>)')
console.log(`'Lucas'.includes('c') --> ${includes}`)

// Check if a string matches a regex
const regexStr = 'Lucas'.match(/[uca]/g)
console.log('\nCheck if a string matches a regex: <STRING NAME>.match(<REGEX>)')
console.log(`'Lucas'.match(/[uca]/g) --> [${regexStr}]`)

// Check if a string is equal to another string
// @ts-expect-error
const commonComparison = 'Lucas' === 'LuCaS'
console.log('\nCheck if a string is equal to another string: <FIRST STRING NAME> === <SECOND STRING NAME>')
console.log(`'Lucas' === 'LuCaS' --> ${commonComparison}`)

console.log('\n# ---------------------------------------------------------------------------------- #')

/*
    Additional challenge...
*/

function getPalindromeWords(words: string[]): string[] {
	const palindromes: string[] = []

	for (const word of words) {
		const reversedWord = [...word].toReversed().join('')
		if (word === reversedWord) palindromes.push(word)
	}

	return palindromes
}

function getAnagramWords(pairOfWords: string[][]): string[][] {
	const anagrams: string[][] = []

	for (const words of pairOfWords) {
		const [word01, word02] = words
		const longestWord = word01.length > word02.length ? word01 : word02

		let areAnagrams = true
		const uniqueChars = new Set([...longestWord])

		for (const char of longestWord) {
			if (uniqueChars.has(char)) continue
			areAnagrams = false
			break
		}

		if (areAnagrams) anagrams.push(words)
	}

	return anagrams
}

function getIsogramWords(words: string[]): string[] {
	const isograms: string[] = []

	for (const word of words) {
		const wordFmt = word.replace(' ', '')
		const uniqueChars = new Set([...wordFmt])
		if (uniqueChars.size === wordFmt.length) isograms.push(word)
	}

	return isograms
}

const arr01 = ['level', 'hello', 'racecar', 'world', 'madam', 'programming', 'deed', 'javascript']
const palindromeWords = getPalindromeWords(arr01)
console.log(`\nPalindrome words of [${arr01}] --> [${palindromeWords}]`)

const arr02 = [
	['listen', 'silent'],
	['hello', 'world'],
	['good', 'dog'],
]
const anagramWords = getAnagramWords(arr02)
console.log(`\nAnagram words of [${arr02}] --> [${anagramWords}]`)

const arr03 = ['hello', 'world', 'isogram', 'javascript', 'python', 'algorithm']
const isogramWords = getIsogramWords(arr03)
console.log(`\nIsogram words of [${arr03}] --> [${isogramWords}]`)
