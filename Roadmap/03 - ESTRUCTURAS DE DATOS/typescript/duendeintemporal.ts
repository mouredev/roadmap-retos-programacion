/*
 * { Retos para programadores } #3 ESTRUCTURAS DE DATOS
 * 
 * Based on "Professional JavaScript for Web Developers" by Matt Frisbie (z-lib.org) for accurate information in some comments.
 * TypeScript - Official URL: https://www.typescriptlang.org/
 * 
 * In TypeScript, there are several built-in data structures that you can use to store and manipulate data. 
 * Here is a list of the most common ones, with additional TypeScript-specific insights.
 */

let log = console.log;

/* Primitive Data Types */

// Number: Represents both integer and floating-point numbers. In TypeScript, you can explicitly annotate the type.
let age: number = 35; // Integer
let total: number = 118.87; // Floating-point
log('age: ', age + ', total: ', total); // age: 35, total: 118.87
log(0.3); // 0.3

let octNum: number = 0o45;
log(octNum); // 37

let hexNum: number = 0x2f;
log(hexNum); // 47

// NaN (Not a Number) is a special value that indicates that an operation that should return a number has failed.
let greeting: string = 'Hi man how you doing?';
let someNumber: any = greeting + 4; // Using `any` is discouraged in TypeScript; prefer `unknown` for safer type handling.
log(someNumber); // Hi man how you doing?4

let someValue: any = "04";
log(isNaN(someValue)); // false  ( because it can be converted to a number )

// String: Represents a sequence of characters. In TypeScript, strings can be annotated with the `string` type.
let dreamyGirl = "Lucy";
let song = dreamyGirl + ' in the sky with diamonds';
let songInfo = `"${song}" is a song from The Beatles that alludes to LSD`;
log(songInfo); // "Lucy in the sky with diamonds" is a song from The Beatles that alludes to LSD

// Template literals and special characters
let num1: number = 40;
let num2: number = 80;
let sum: string = `${num1} + ${num2} = ${num1 + num2}`;
log(sum); // "40 + 80 = 120"

log(`\u57A8`); // 垨
log(String.raw`\u57A8`); // \u57A8

log(`first line\nsecond line`);
// first line
// second line
log(String.raw`first line\nsecond line`); // "first line\nsecond line"

// Boolean: Represents a logical entity with two values: `true` and `false`. In TypeScript, booleans are explicitly typed.
let isChecked: boolean = true;
log(!isChecked); // false

// Undefined: A variable that has been declared but not assigned. In TypeScript, you can use `undefined` as a type.
let somebody: unknown; // Using `unknown` is safer than `any` for uninitialized variables.
log(somebody); // undefined

// Null: Represents the intentional absence of any object value. In TypeScript, `null` is a subtype of all other types.
let animals: null = null;
log(animals); // null

// Symbol: A unique and immutable primitive value, often used as an object property key. In TypeScript, symbols are explicitly typed.
const Id: symbol = Symbol('xm');
const otherId: symbol = Symbol('xm');
log('equal symbols: ', Id == otherId); // false

const emailSymbol: symbol = Symbol('email');

class User {
    constructor(name: string, email: string) {
        this.name = name;
        this[emailSymbol] = email; // Using a symbol as a unique property key.
    }
    name: string;

    getName() {
        return this.name;
    }

    getEmail() {
        return this[emailSymbol];
    }
}

const user1 = new User('Barbarella', 'softbaby@something.com');
console.log(user1.name); // Barbarella
console.log(user1.getEmail()); // softbaby@something.com

// BigInt: Represents integers with arbitrary precision. In TypeScript, BigInt literals require the `n` suffix.
let bigNumber: bigint = BigInt(765466743212345679874653358945321);
log(bigNumber); // 765466743212345647593078160097280n

/* Reference Data Types */

// Object: A collection of key-value pairs. In TypeScript, you can define interfaces or types to describe the shape of objects.
interface Debian {
    name: string;
    description: string;
    location: string;
    speak: () => void;
}

let debian: Debian = {
    name: 'Debian',
    description: 'Ardilla parlante cuyo núcleo está basado en un Sistema Operativo del mismo nombre, lucha contra el Sistema establecido y habita más allá del Borde (el Universo conocido)',
    location: 'No Found',

    speak: () => {
        console.log(this.description);
    }
};

log(debian.description); // Ardilla parlante cuyo núcleo está basado en un Sistema Operativo del mismo nombre, lucha contra el Sistema establecido y habita más allá del Borde (el Universo conocido)

// Array: An ordered collection of values. In TypeScript, arrays are explicitly typed.
let friends: string[] = ['Susan', 'Maryatta', 'Denise', 'Luna', 'Kena', 'Maria'];
log(friends); // [ 'Susan', 'Maryatta', 'Denise', 'Luna', 'Kena', 'Maria' ]

// Function: A special type of object that can be called to perform a specific task. In TypeScript, functions can have explicit parameter and return types.
let from: number = 4, to: number = 12;
const randomValue = (from: number, to: number): number => {
    return Math.floor(Math.random() * (to - from + 1)) + from;
};

let count: number = from;
while (count < to) {
    log('random value: ', randomValue(from, to));
    count++;
}  /*  Possible Output: 
random value:  9
random value:  6
random value:  9
random value:  12
random value:  6
random value:  7
random value:  4
random value:  8
 */

/* Specialized Data Structures */

// Set: A collection of unique values. In TypeScript, sets are generic and can be explicitly typed.
let uniqueNumbers = new Set<number>([4, 4, 3, 5, 8, 1, 8, 1, 7]);
log(uniqueNumbers); // Set(6) { 4, 3, 5, 8, 1, 7 }

// Map: A collection of key-value pairs where keys can be of any type. In TypeScript, maps are generic and can be explicitly typed.
let map = new Map<string, any>();
map.set('gopi_name', 'Khamala');
map.set('age', 35);
log(map.get('gopi_name')); // Khamala

// WeakSet: Similar to Set, but holds "weak" references to its values. In TypeScript, WeakSets are generic.
let weakSet = new WeakSet<object>();
let obj = {};
weakSet.add(obj);
log(weakSet.has(obj)); // true

// WeakMap: Similar to Map, but holds "weak" references to its keys. In TypeScript, WeakMaps are generic.
let weakMap = new WeakMap<object, string>();
let keyObj = {};
weakMap.set(keyObj, "crazylady");
log(weakMap.get(keyObj)); // crazylady

/* Typed Arrays */

// Int8Array: Represents an array of 8-bit signed integers.
let int8Array = new Int8Array([-3, 5, -8, 99, 76]);
log(int8Array); // Int8Array(5) [ -3, 5, -8, 99, 76 ]

// Uint8Array: Represents an array of 8-bit unsigned integers.
let uint8Array = new Uint8Array([1, 2, 3]);
log(uint8Array); // Uint8Array(3) [ 1, 2, 3 ]

// Uint8ClampedArray: Represents an array of 8-bit unsigned integers, but with values "clamped" to the range [0, 255].
let uint8ClampedArray = new Uint8ClampedArray([-1, 256, 100]);
log(uint8ClampedArray); // Uint8ClampedArray(3) [ 0, 255, 100 ]

// Int16Array: Represents an array of 16-bit signed integers.
let int16Array = new Int16Array([1, -2, 3]);
log(int16Array); // Int16Array(3) [ 1, -2, 3 ]

// Uint16Array: Represents an array of 16-bit unsigned integers.
let uint16Array = new Uint16Array([1, 2, 3]);
log(uint16Array); // Uint16Array(3) [ 1, 2, 3 ]

// Int32Array: Represents an array of 32-bit signed integers.
let int32Array = new Int32Array([1, -2, 3]);
log(int32Array); // Int32Array(3) [ 1, -2, 3 ]

// Uint32Array: Represents an array of 32-bit unsigned integers.
let uint32Array = new Uint32Array([1, 2, 3]);
log(uint32Array); // Uint32Array(3) [ 1, 2, 3 ]

// Float32Array: Represents an array of 32-bit floating-point numbers.
let float32Array = new Float32Array([1.5, 2.5, 3.5]);
log(float32Array); // Float32Array(3) [ 1.5, 2.5, 3.5 ]

// Float64Array: Represents an array of 64-bit floating-point numbers.
let float64Array = new Float64Array([1.5, 2.5, 3.5]);
log(float64Array); // Float64Array(3) [ 1.5, 2.5, 3.5 ]

log('Retos para programadores #3'); // Retos para programadores #3