/*
    Assignment By Value
*/

let var1: number = 3;
let var2: number = var1;

var1 = 4;

console.log(var1)
console.log(var2)

/*
    Assignment By Reference
*/

let var3: number[] = [10, 20]
let var4: number[] = var3

var3.push(30)

console.log(var3)
console.log(var4)

/*
    Exercise
*/

function ByValue(a: number, b: number): number[] {
    let c = b
    let d = a

    return [c, d]
}

let original1: number = 20
let original2: number = 30
let values: number[] = ByValue(original1, original2)

console.log('By Values')
console.log('Original Values')
console.log(original1)
console.log(original2)
console.log('After Function Values')
console.log(values[0])
console.log(values[1])

function ByReference(a: number, b: number): number[] {
    let c = b
    let d = a

    return [c, d]
}

let original3: number = 20
let original4: number = 30
let values2: number[] = ByReference(original3, original4)

console.log('By Reference')
console.log('Original Values')
console.log(original3)
console.log(original4)
console.log('After Function Values')
console.log(values2[0])
console.log(values2[1])