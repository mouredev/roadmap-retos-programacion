import { setTimeout } from 'timers/promises'

/*
    Asynchrony...
*/

console.log('Asynchrony...')

console.log(
	'\n> Instructions executed before calling `asyncFn` (asynchrony function)'
)

async function asyncFn(time: number): Promise<void> {
	console.log('\nasyncFn start...')
	console.time('asyncFn')

	await setTimeout(time)

	console.timeEnd('asyncFn')
	console.log('asyncFn end!')

	additionalChallenge()
}

asyncFn(5 * 1000)

console.log(
	'\n> Instructions executed after called `asyncFn` (asynchrony function)\n'
)

/*
    Additional challenge...
*/

function additionalChallenge() {
	console.log(
		'\n# ---------------------------------------------------------------------------------- #\n'
	)

	console.log('Additional challenge...\n')

	const aFn = async () => {
		console.time('aFn')
		await setTimeout(1 * 1000)
		console.timeEnd('aFn')
	}

	const bFn = async () => {
		console.time('bFn')
		await setTimeout(2 * 1000)
		console.timeEnd('bFn')
	}

	const cFn = async () => {
		console.time('cFn')
		await setTimeout(3 * 1000)
		console.timeEnd('cFn')
	}

	const dFn = async () => {
		console.time('dFn')
		await setTimeout(1 * 1000)
		console.timeEnd('dFn')
	}

	Promise.all([aFn(), bFn(), cFn()]).then(async () => await dFn())
}
