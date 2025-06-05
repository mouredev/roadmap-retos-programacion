let number = 10 // Global variable

// Functions
function add() {
    console.log('This function could add values if I had parameters')
}

function addParameters(a, b) {
    return `${a} + ${b} is ${a + b}`
}
console.log(addParameters(2, 1))

function calculator(a, b) {
    function subtract(a, b) {
        return `${a} - ${b} is ${a-b}`
    }
    console.log(subtract(a,b))
}

calculator(1,4)

function roundNumber() {
    let numberToRound = 3.4     // Local variable
    return `${numberToRound} rounded is ${Math.round(numberToRound)}`
}

console.log(roundNumber())

function multiple(string1, string2) {
    if (typeof string1 == 'string' && typeof string2 == 'string') {
        console.log(`${string1} is a string`)

        for(let i = 1; i <= 100; i ++) {

            if(i % 3 == 0 && i % 5 == 0) {
                console.log(string1 + string2)
            } else if (i % 3 == 0) {
                console.log(string1)
            } else if (i % 5 == 0) {
                console.log(string2)
            } else {
                console.log(i)
            }
        }

    } else {
        console.log('The values are not strings')
    }
}

multiple('hello', 'bye')