// ********* Array *********
let array = [1, 2, 3, 4]

array.push(5) // Add
array.pop() // Delete
array = [5, 6, 2, 8] // Update
array.sort() // Sort


// ********* Set *********
let mySet = new Set([1, 2, 3, 4])

mySet.add('Hellooo') // Add
mySet.delete(1) // Delete
mySet = [2, 8, 7] // Update
mySet.sort() // Sort


// ********* Map *********
let myMap = new Map( [
    ['name', 'Lia'],
    ['color', 'blue']
])

myMap.set('alias', 'li') // Add
myMap.delete('alias') // Delete
myMap.set('name', 'Mirko') // Update


// ********* Object *********
let person = {
    name: 'Matias',
    age: 10,
    walk: function() {
        console.log('Walking')
    }
}

person.color = 'red' // Add
delete person.color // Delete
person.name = 'Brais' // Update
console.log(person)