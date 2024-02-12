
/*
    Array
*/

let fruits: string[] = ['apple', 'orange', 'banana']

// insert

fruits.push('mango')
fruits[4] = 'grapes'
fruits.unshift('lemon')

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

let letters = new Set(['a', 'b', 'c'])

// insert

letters.add('f')

console.log(letters)

// delete

letters.delete('b')

console.log(letters)

/*
    Tuples
*/

let employee: [number, string] = [1, 'steve']

// insert

employee.push(2, 'bill')
employee.unshift(3, 'david')


console.log(employee)

// edit

employee[1] = 'jeff'

console.log(employee)

// delete

employee.shift()
employee.pop()

console.log(employee)

/*
    Maps
*/

let person = new Map<string, string>([
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