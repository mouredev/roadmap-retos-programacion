/*
    Callbacks...
*/

console.log('Callbacks...')

function createArray<T extends number | string>(
    length: number,
    callback: (prevElement: undefined | T) => T
): T[] {
    const array: T[] = []

    for (let i = 0; i < length; i++) {
        const element: T = callback(array.at(i - 1))
        array.push(element)
    }

    return array
}

const arrayOfEvens: number[] = createArray<number>(10, (prevElement) => {
    if (typeof prevElement === 'undefined') return 0
    return prevElement + 2
})

console.log(`\nArray of evens: [${arrayOfEvens}]`)

const arrayOfOdds: string[] = createArray<string>(10, (prevElement) => {
    if (typeof prevElement === 'undefined') return 'I am the number 1'

    const prevElementValue = parseInt(
        prevElement.slice(prevElement.lastIndexOf(' '))
    )

    return `I am the number ${prevElementValue + 2}`
})

console.log(`\nArray of named odds: [${arrayOfOdds}]`)

console.log(
    '\n# ---------------------------------------------------------------------------------- #\n'
)

/*
    Additional challenge...
*/

console.log('Additional challenge...\n')

interface RestaurantParams<T extends string = string> {
    name: T
    onConfirm(dishName: T): Promise<void>
    onReady(dishName: T): void
    onDeliver(dishName: T): Promise<void>
}

async function prepareDish({
    name,
    onConfirm,
    onReady,
    onDeliver,
}: RestaurantParams): Promise<void> {
    await onConfirm(name)

    const randomTimeout: number =
        Math.max(Math.ceil(Math.random() * 10), 1) * 1000

    await new Promise((resolve) =>
        setTimeout(() => {
            onReady(name)
            resolve(null)
        }, randomTimeout)
    )

    await onDeliver(name)
}

Promise.all([
    prepareDish({
        name: 'Spaghetti',
        async onConfirm(dishName) {
            console.log(`${dishName} in preparation.`)
        },
        onReady(dishName) {
            console.log(`${dishName} is ready to deliver.`)
        },
        async onDeliver(dishName) {
            console.log(`${dishName} delivered.`)
        },
    }),
    prepareDish({
        name: 'Soup',
        async onConfirm(dishName) {
            console.log(`${dishName} in preparation.`)
        },
        onReady(dishName) {
            console.log(`${dishName} is ready to deliver.`)
        },
        async onDeliver(dishName) {
            console.log(`${dishName} delivered.`)
        },
    }),
])
