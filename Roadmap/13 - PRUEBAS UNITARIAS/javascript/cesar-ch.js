/*
    * #13 PRUEBAS UNITARIAS
*/

const sum = (num1, num2) => num1 + num2

// test
const result1 = sum(2, 3)
if (result1 === 5) {
    console.log('Test passed')
} else {
    console.error('Error: The sum of 2 and 3 is 5')
}

/*
    * DIFICULTAD EXTRA
*/

const person = {
    name: 'cesar-ch',
    age: 3,
    birthDate: '2021-02-03',
    programmingLanguages: ["Javascript", "Python", "Java"]
}

// test for existence of fields
const expectedKeys = ["name", "age", "birthDate", "programmingLanguages"]
const allKeysExist = expectedKeys.every(key => key in person)
if (allKeysExist) {
    console.log('Test passed')
} else {
    console.error('Error: The person object has the expected keys')
}

// test to verify field data
if (typeof person.name !== "string") {
    console.error('Error: The name field is not string')
}

if (isNaN(person.age) || person.age < 0) {
    console.error('Error: Age must be a positive number')
}

const regexDate = /^\d{4}-\d{2}-\d{2}$/

if (!regexDate.test(person.birthDate)) {
    console.error('Error: Birth date is not in the expected format')
}

if (!Array.isArray(person.programmingLanguages)) {
    console.error('Error: Programming languages is not an array')
}
