'uses strict'

/*
    Arrays
*/

let fruits = ['apple', 'orange', 'banana']

// insert

fruits[3] = 'pineapple'
fruits.push('lemon')
fruits.unshift('mango')

console.log(fruits)

// edit

fruits[1] = 'grapes'

console.log(fruits)

// delete

fruits.pop()
fruits.shift()
delete fruits[3]

console.log(fruits)

/*
    Sets
*/

letters = new Set(['a', 'b', 'c'])

// insert

letters.add('f')

console.log(letters)

// delete

letters.delete('b')

console.log(letters)
/*
    Maps
*/

person = new Map([
    ['name', 'kodenook'],
    ['country', 'chile']
])

// insert

person.set('continent', '')

console.log(person)

// insert

person.set('continent', 'america')

console.log(person)

// delete

person.delete('continent')

console.log(person)

/*
    Exercise
*/

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let option = 0
let data = new Map([])

function ask() {
    console.clear()

    console.log('1. search')
    console.log('2. add')
    console.log('3. edit')
    console.log('4. delete')
    console.log('5. exit')
    console.log('')

    rl.question('choose an option: ', (input) => {
        option = parseInt(input.trim());

        switch (option) {
            case 1:
                rl.question('name: ', (input) => {
                    let name = parseInt(input.trim());

                    console.log(data.get(name))
                    setTimeout(() => {
                        ask();
                    }, 2000);
                })
                break;
            case 2:
                rl.question('name: ', (input) => {
                    let name = parseInt(input.trim());

                    rl.question('number: ', (input) => {
                        let number = parseInt(input.trim());

                        data.set(name, number)
                        ask()
                    })
                })
                break;
            case 3:
                rl.question('name: ', (input) => {
                    let name = parseInt(input.trim());

                    rl.question('number: ', (input) => {
                        let number = parseInt(input.trim());

                        data.set(name, number)
                        ask()
                    })
                })
                break;
            case 4:
                rl.question('name: ', (input) => {
                    let name = parseInt(input.trim());

                    data.delete(name)

                    ask()
                })
                break;
            case 5:
                rl.close()
                break;
            default:
                break;
        }
    });

}

ask()