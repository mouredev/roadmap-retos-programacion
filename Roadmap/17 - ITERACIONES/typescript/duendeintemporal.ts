// #17 { retosparaprogramadores } - ITERACIONES    
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */

// short for console.log
let log = console.log;

// Conditional check for browser environment
if (typeof window !== 'undefined') {
    window.addEventListener('load', () => {
        const body: HTMLBodyElement | null = document.querySelector('body');
        const title = document.createElement('h1');

        body?.style.setProperty('background', '#000');
        body?.style.setProperty('text-align', 'center');

        title.textContent = 'Retosparaprogramadores #17.';
        title.style.setProperty('font-size', '3.5vmax');
        title.style.setProperty('color', '#fff');
        title.style.setProperty('line-height', '100vh');

        body?.appendChild(title);

        setTimeout(() => {
            alert('Retosparaprogramadores #17. Please open the Browser Developer Tools.');
        }, 2000);
        log('Retosparaprogramadores #17');
});
} else {
    log('This code is designed to run in a browser environment. Skipping window-related code.');
    log('Retosparaprogramadores #17');
}
for(let i = 1; i <= 10; i++){
    log(i);
}

let count: number = 0;
while(count < 10){
    count ++;
    log(count); // log numbers from 1 to 10
}

// forEach method
let nums: number[] = [1,2,3,4,5,6,7,8,9,10];
nums.forEach(n=>log(n)); // log numbers from 1 to 10

//Extra Dificulty Exercise

// do while
let i: number = 0;
do {
    console.log(i);
    i++;
} while (i < 5); // log numbers fronm 0 to 4


// Note: in the tsconfig.json
 // Enable 'downlevelIteration' to support iterating over iterators (e.g., Array.prototype.entries(),
        // Array.prototype.keys(), Array.prototype.values()) in environments that do not natively support them
        // (e.g., ES5 or older). This flag generates additional helper code to make iteration work correctly.
        // Without this flag, TypeScript throws errors when using modern iteration features with older targets.
       // "downlevelIteration": true,


//map method
const arr: number[] = [1, 2, 3, 4, 5];
const doubled = arr.map((value) => value * 2);
log(doubled); // [2, 4, 6, 8, 10]

// filter method
const arr1: number[] = [1, 2, 3, 4, 5];
const evenNumbers = arr1.filter((value) => value % 2 === 0);
log(evenNumbers); // [2, 4]

// reduce method
const arr2: number[] = [1, 2, 3, 4, 5];
const sum = arr2.reduce((total, current) => total + current, 0);
log(sum); // 15

// some method
const arr3: number[] = [1, 2, 3, 4, 5];
const hasEven = arr3.some((value) => value % 2 === 0);
log(hasEven); // true

// every method
const arr4: number[] = [1, 2, 3, 4, 5];
const allEven = arr4.every((value) => value % 2 === 0);
log(allEven); // false

// For of...
const arr5: number[] = [1, 2, 3, 4, 5];
for (const value of arr5) {
    log(value); // Logs: 1 2 3 4 5
}

// Iteración con entries
const arr6: string[] = ['a', 'b', 'c'];
for (const [index, value] of arr6.entries()) {
    log(index, value); // 0 'a' 1 'b' 2 'c'
}

const obj1: { [key: string]: number } = { a: 1, b: 2, c: 3 };
for (const [key, value] of Object.entries(obj1)) {
    log(key, value); // a 1 b 2 c 3
}

// Iteración con keys
const arr7: string[] = ['a', 'b', 'c'];
for (const index of arr7.keys()) {
    log(index); // 0 1 2
}

const obj2: { [key: string]: number } = { a: 1, b: 2, c: 3 };
for (const key of Object.keys(obj2)) {
    log(key); // a b c
}

// Iteración con values
const arr8: string[] = ['a', 'b', 'c'];
for (const value of arr8.values()) {
    log(value); // a b c
}

const obj3: { [key: string]: number } = { a: 1, b: 2, c: 3 };
for (const value of Object.values(obj3)) {
    log(value); // 1 2 3
}

const obj: { [key: string]: number } = { a: 1, b: 2, c: 3 };
for (const key in obj) {
    log(`${key}: ${obj[key]}`); // a: 1 b: 2 c: 3
}

// Note2: I share my tsconfig.json
/*
{
    "compilerOptions": {
        // Set the target JavaScript version to ES6 (ECMAScript 2015).
        // This ensures that TypeScript generates modern JavaScript code.
        "target": "es6",

        // Enable 'downlevelIteration' to support iterating over iterators (e.g., Array.prototype.entries(),
        // Array.prototype.keys(), Array.prototype.values()) in environments that do not natively support them
        // (e.g., ES5 or older). This flag generates additional helper code to make iteration work correctly.
        // Without this flag, TypeScript throws errors when using modern iteration features with older targets.
        "downlevelIteration": true,

        // Use CommonJS as the module system. This is the default module system for Node.js.
        "module": "commonjs",

        // Enable all strict type-checking options to enforce stricter type safety in the codebase.
        "strict": true,

        // Enable ES module interoperability. This allows using ES modules with CommonJS modules seamlessly.
        "esModuleInterop": true,

        // Skip type checking of declaration files (e.g., .d.ts files). This can improve compilation speed.
        "skipLibCheck": true,

        // Ensure consistent casing in file names. This helps avoid issues on case-sensitive file systems.
        "forceConsistentCasingInFileNames": true
    },

    // Include all files in the current directory and its subdirectories for compilation.
    */ 
   // "include": ["./**/*"],

    // Exclude files in the '../Javascript' and '../Python' directories from compilation.
    // This prevents TypeScript from processing unrelated files in those directories.
   // "exclude": ["../Javascript/**/*", "../Python/**/*"]
//}


