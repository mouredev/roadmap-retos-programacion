/*
    Assignment By Value
*/

let var1 = 3;
let var2 = var1;

var1 = 4;

console.log(var1)
console.log(var2)

/*
    Assignment By Reference
*/

let var3 = [10, 20]
let var4 = var3

var3.push(30)

console.log(var3)
console.log(var4)

/*
    Exercise
*/

function ByValue(a, b) {
    let c = b
    let d = a

    return [c, d]
}

let original1 = 20
let original2 = 30
let values = ByValue(original1, original2)

console.log('By Values')
console.log('Original Values')
console.log(original1)
console.log(original2)
console.log('After Function Values')
console.log(values[0])
console.log(values[1])

function ByReference(a, b) {
    let c = b
    let d = a

    return [c, d]
}

let original3 = 20
let original4 = 30
let values2 = ByReference(original3, original4)

console.log('By Reference')
console.log('Original Values')
console.log(original3)
console.log(original4)
console.log('After Function Values')
console.log(values2[0])
console.log(values2[1])