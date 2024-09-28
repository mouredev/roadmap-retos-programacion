// https://www.typescriptlang.org/

// Single line comment.

/*
    Multi line comment...
*/

let number01: number = 1
const number02: number = 2

number01 = 3
// number02 = 4 // Throw an error because It's a constant.

// Primitive data types
const numberVar: number = 12345
const bigIntVar: bigint = BigInt(1000)

const booleanVar: boolean = true

const stringVar: string = '¡Hello World!'

const symbolVar: symbol = Symbol('fibonacci')

const nullVar: null = null
const undefinedVar: undefined = undefined

// Outputs
console.log(`number01: ${number01}\nnumber02: ${number02}\n`)

console.log(`> numberVar: ${numberVar} --> ${typeof numberVar}`)
console.log(`> bigIntVar: ${bigIntVar} --> ${typeof bigIntVar}\n`)

console.log(`> booleanVar: ${booleanVar} --> ${typeof booleanVar}\n`)

console.log(`> stringVar: ${stringVar} --> ${typeof stringVar}\n`)

console.log(`> symbolVar: ${String(symbolVar)} --> ${typeof symbolVar}\n`)

console.log(`> nullVar: ${nullVar} --> ${typeof nullVar}\n`)
console.log(`> nullVar: ${undefinedVar} --> ${typeof undefinedVar}\n`)

console.log('¡Hello, TypeScript!')
