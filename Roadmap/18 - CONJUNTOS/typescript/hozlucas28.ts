/*
    Data methods...
*/

console.log('Data methods...')

class Data<T extends string> {
	private savedData: T[]

	constructor(initialData: T[]) {
		this.savedData = this.sanitizeData(initialData)
	}

	public getData(): T[] {
		return this.savedData
	}

	public setData(newInitialData: T[]): this {
		this.savedData = this.sanitizeData(newInitialData)
		return this
	}

	private sanitizeData(data: T[]): T[] {
		const uniqueData: Set<T> = new Set(data)
		const uniqueDataValues: IterableIterator<T> = uniqueData.values()

		const sanitizedData: T[] = []
		for (let i = 0; i < uniqueData.size; i++) {
			sanitizedData.push(uniqueDataValues.next().value)
		}

		return sanitizedData
	}

	public appendEnd(newData: T[]): this {
		this.savedData.push(...newData)
		return this
	}

	public appendStart(newData: T[]): this {
		this.savedData.unshift(...newData)
		return this
	}

	public appendAt(index: number, newData: T | T[]): this {
		const head: T[] = this.savedData.slice(0, index)
		const tail: T[] = this.savedData.slice(index)

		const newSavedData: T[] = [...head]

		typeof newData === 'string'
			? newSavedData.push(newData)
			: newSavedData.push(...newData)

		newSavedData.push(...tail)

		this.setData(newSavedData)
		return this
	}

	public clear(): this {
		this.setData([])
		return this
	}

	public deleteAt(index: number): this {
		const head: T[] = this.savedData.slice(0, index)
		const tail: T[] = this.savedData.slice(index + 1)

		const newSavedData: T[] = [...head, ...tail]

		this.setData(newSavedData)
		return this
	}

	public has(data: T): boolean {
		return this.savedData.some((value) => value === data)
	}

	public updateAt(index: number, newValue: T): this {
		this.savedData[index] = newValue
		return this
	}
}

const data: Data<string> = new Data([
	'Buenos Aires',
	'Texas',
	'Madrid',
	'Houston',
	'Buenos Aires',
	'California',
	'Texas',
])

console.log(
	`\nconst data: Data<string> = new Data(['Buenos Aires', 'Texas', 'Madrid', 'Houston', 'Buenos Aires', 'California', 'Texas'])`
)

console.table(data.getData())

console.log('\nAppend data at the end...')
console.log(`\ndata.appendEnd(['Berlin'])`)

data.appendEnd(['Berlin'])
console.table(data.getData())

console.log('\nAppend data at the start...')
console.log(`\ndata.appendStart(['Chaco'])`)

data.appendStart(['Chaco'])
console.table(data.getData())

console.log('\nAppend several data at the end...')
console.log(`\ndata.appendEnd(['Paris', 'Montana'])`)

data.appendEnd(['Paris', 'Montana'])
console.table(data.getData())

console.log('\nAppend several data at index 4...')
console.log(`\ndata.appendAt(4, ['Jujuy', 'Formosa'])`)

data.appendAt(4, ['Jujuy', 'Formosa'])
console.table(data.getData())

console.log('\nDelete data at index 3...')
console.log(`\ndata.deleteAt(3)`)

data.deleteAt(3)
console.table(data.getData())

console.log('\nUpdate data at index 6...')
console.log(`\ndata.updateAt(6, 'Miami')`)

data.updateAt(6, 'Miami')
console.table(data.getData())

console.log('\nCheck if a data is present...')
console.log(`\ndata.has('Buenos Aires') => ${data.has('Buenos Aires')}`)

console.table(data.getData())

console.log('\nClear saved data...')
console.log(`\ndata.clear()`)

data.clear()
console.table(data.getData())

console.log(
	'\n# ---------------------------------------------------------------------------------- #\n'
)

/*
    Additional challenge...
*/

console.log('Additional challenge...')

function differenceSets<T>(firstSet: Set<T>, secondSet: Set<T>): Set<T> {
	const differenceSets: Set<T> = new Set()

	const firstSetValues: IterableIterator<T> = firstSet.values()

	for (let i = 0; i < firstSet.size; i++) {
		const firstSetValue = firstSetValues.next().value
		if (!secondSet.has(firstSetValue)) differenceSets.add(firstSetValue)
	}
	return differenceSets
}

function intersectionSets<T>(firstSet: Set<T>, secondSet: Set<T>): Set<T> {
	const intersectedSets: Set<T> = new Set()

	const [shortestSet, longestSet]: [Set<T>, Set<T>] =
		firstSet.size < secondSet.size
			? [firstSet, secondSet]
			: [secondSet, firstSet]

	const shortestSetValues: IterableIterator<T> = shortestSet.values()

	for (let i = 0; i < shortestSet.size; i++) {
		const shortestSetValue = shortestSetValues.next().value
		if (longestSet.has(shortestSetValue)) intersectedSets.add(shortestSetValue)
	}

	return intersectedSets
}

function joinSets<T>(firstSet: Set<T>, secondSet: Set<T>): Set<T> {
	const joinedSets: Set<T> = new Set()

	const [shortestSet, longestSet]: [Set<T>, Set<T>] =
		firstSet.size < secondSet.size
			? [firstSet, secondSet]
			: [secondSet, firstSet]

	const shortestSetValues: IterableIterator<T> = shortestSet.values()
	const longestSetValues: IterableIterator<T> = longestSet.values()

	for (let i = 0; i < longestSet.size; i++) {
		if (i < shortestSet.size) joinedSets.add(shortestSetValues.next().value)
		joinedSets.add(longestSetValues.next().value)
	}

	return joinedSets
}

function symmetricDifferenceSets<T>(
	firstSet: Set<T>,
	secondSet: Set<T>
): Set<T> {
	const symmetricDifferenceSets: Set<T> = new Set()

	const headDifference = differenceSets(firstSet, secondSet)
	const tailDifference = differenceSets(secondSet, firstSet)

	const headDifferenceValues = headDifference.values()
	const tailDifferenceValues = tailDifference.values()

	for (let i = 0; i < headDifference.size + tailDifference.size; i++) {
		const headDifferenceValuesObj = headDifferenceValues.next()
		const tailDifferenceValuesObj = tailDifferenceValues.next()

		if (!headDifferenceValuesObj.done)
			symmetricDifferenceSets.add(headDifferenceValuesObj.value)

		if (!tailDifferenceValuesObj.done)
			symmetricDifferenceSets.add(tailDifferenceValuesObj.value)
	}

	return symmetricDifferenceSets
}

const firstSet: Set<string> = new Set(['Hello', 'TypeScript', 'World!'])
const secondSet: Set<string> = new Set(['By', 'TypeScript'])

console.log('\nfirstSet =', firstSet)
console.log('\nsecondSet =', secondSet)

const intersectedSets: Set<string> = intersectionSets(firstSet, secondSet)

console.log('\nIntersection (firstSet, and secondSet) =>', intersectedSets)

const joinedSets: Set<string> = joinSets(firstSet, secondSet)

console.log('\nJoin (firstSet, and secondSet) =>', joinedSets)

const differenceSetsRtn: Set<string> = differenceSets(firstSet, secondSet)

console.log('\nDifference (firstSet, and secondSet) =>', differenceSetsRtn)

const symmetricDifferenceSetsRtn: Set<string> = symmetricDifferenceSets(
	firstSet,
	secondSet
)

console.log(
	'\nSymmetric difference (firstSet, and secondSet) =>',
	symmetricDifferenceSetsRtn
)
