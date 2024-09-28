
function name(): void {
    console.log('kodenook')
}

name()

function fullName({ fname = 'my', lname = 'name' }: { fname?: string, lname?: string }): void {
    console.log(`${fname} ${lname}`)
}

fullName({ lname: 'lname' })

function addition(...nums: number[]): number {
    let result: number = 0

    for (let x of nums) {
        result += x
    }

    return result
}

console.log(addition(1, 2, 2.4, 1.1, -2.2))

function first() {
    console.log('first')

    function second() {
        console.log('second')
    }

    second()
}

first()

let global = 'global'

function scope() {
    console.log(global)
    let local = 'local'
}

scope()

/*
    Exercise
*/

function exercise(word1: string, word2: string): number {
    let numberCount: number = 0

    for (let x of Array(101).keys()) {
        if (x % 3 == 0 && x % 5 == 0) {
            console.log(`${word1} ${word2}`)
        } else if (x % 3 == 0) {
            console.log(word1)
        } else if (x % 5 == 0) {
            console.log(word2)
        } else {
            numberCount++
        }
    }

    return numberCount
}

console.log(`number of times it was a number and not words: ${exercise('hello', 'typescript')}`)