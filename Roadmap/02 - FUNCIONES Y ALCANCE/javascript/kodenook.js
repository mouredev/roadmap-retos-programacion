
function name() {
    console.log('kodenook')
}

name()

function fullName({ fname = 'my', lname = 'name' }) {
    console.log(`${fname} ${lname}`)
}

fullName({ lname: 'lname' })

function addition(...nums) {
    let result = 0

    nums.forEach(num => {
        result += num
    });

    return result
}

console.log(addition(1, 1, 3.2, -2.5))

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

function exercise(word1, word2) {
    let result = 0

    for (x of Array(101).keys()) {
        if (x % 3 == 0 && x % 5 == 0) {
            console.log(`${word1} ${word2}`)
        } else if (x % 3 == 0) {
            console.log(word1)
        } else if (x % 5 == 0) {
            console.log(word2)
        } else {
            result++
        }
    }

    return result
}

console.log(`number of times it was a number and not words: ${exercise('hello', 'javascript')}`)