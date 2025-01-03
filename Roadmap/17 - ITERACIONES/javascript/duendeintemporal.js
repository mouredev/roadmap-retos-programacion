// #17 - ITERACIONES    
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

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #17.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #17. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #17'); 
});

for(let i = 1; i <= 10; i++){
    log(i);
}

let count = 0;
while(count < 10){
    count ++;
    log(count);
}

// forEach method
let nums = [1,2,3,4,5,6,7,8,9,10];
nums.forEach(n=>log(n));

//Extra Dificulty Exercise

// do while
let i = 0;
do {
    console.log(i);
    i++;
} while (i < 5);

//map method
const arr = [1, 2, 3, 4, 5];
const doubled = arr.map((value) => value * 2);
log(doubled); // [2, 4, 6, 8, 10]

// filter method
const arr1 = [1, 2, 3, 4, 5];
const evenNumbers = arr1.filter((value) => value % 2 === 0);
log(evenNumbers); // [2, 4]

// reduce method
const arr2 = [1, 2, 3, 4, 5];
const sum = arr2.reduce((total, current) => total + current, 0);
log(sum); // 15

// some method
const arr3 = [1, 2, 3, 4, 5];
const hasEven = arr3.some((value) => value % 2 === 0);
log(hasEven); // true

// every method
const arr4 = [1, 2, 3, 4, 5];
const allEven = arr4.every((value) => value % 2 === 0);
log(allEven); // false

// For of...
const arr5 = [1, 2, 3, 4, 5];
for (const value of arr5) {
    log(value); // Logs: 1 2 3 4 5
}

// Iteración con entries
const arr6 = ['a', 'b', 'c'];
for (const [index, value] of arr6.entries()) {
    log(index, value); // 0 'a' 1 'b' 2 'c'
}

const obj1 = { a: 1, b: 2, c: 3 };
for (const [key, value] of Object.entries(obj1)) {
    log(key, value); // a 1 b 2 c 3
}

// Iteración con keys
const arr7 = ['a', 'b', 'c'];
for (const index of arr7.keys()) {
    log(index); // 0 1 2
}

const obj2 = { a: 1, b: 2, c: 3 };
for (const key of Object.keys(obj2)) {
    log(key); // a b c
}


// Iteración con values
const arr8 = ['a', 'b', 'c'];
for (const value of arr8.values()) {
    log(value); // a b c
}

const obj3 = { a: 1, b: 2, c: 3 };
for (const value of Object.values(obj3)) {
    log(value); // 1 2 3
}

// For in...
const obj = { a: 1, b: 2, c: 3 };
for (const key in obj) {
    log(`${key}: ${obj[key]}`); // a: 1 b: 2 c: 3
}




