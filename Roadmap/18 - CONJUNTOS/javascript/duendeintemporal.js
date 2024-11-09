//#18 - CONJUNTOS
/* * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */

let log = console.log;

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #18.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #18. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #18'); 
});


let arr = [1,2,3,4,5];
log(arr)// [1,2,3,4,5]
// Adds an element to the end.
arr.push(6);
log(arr); // [1,2,3,4,5,6]

// Adds an element to the beginning.
arr.unshift(0);
log(arr); // [0, 1, 2, 3, 4, 5, 6]
// Adds multiple elements in bulk to the end.
arr2 = [7,8,9,10];
arr.push(...arr2);
log(arr); //  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// Adds multiple elements in bulk at a specific position.
arr3 = [3.1, 3.2, 3.4]
arr.splice(4,0, ...arr3);
log(arr); // [0, 1, 2, 3, 3.1, 3.2, 3.4, 4, 5, 6, 7, 8, 9, 10]

// Removes an element at a specific position.
arr.splice(6,1);
log(arr); // [0, 1, 2, 3, 3.1, 3.2, 4, 5, 6, 7, 8, 9, 10]

// Updates the value of an element at a specific position.
arr.splice(arr.length - 1, 1, 9.1);
log(arr); // [0, 1, 2, 3, 3.1, 3.2, 4, 5, 6, 7, 8, 9, 9.1]

// Checks if an element is in a set.
let nums = new Set();
arr.forEach(n=>nums.add(n));
log('Is 10 in nums: ', nums.has(10)) // false

// Removes all content from the set.
nums.clear();
log(nums); // {size: 0}

// EXTRA DIFFICULTY (optional):

// Union.
let arr4 = [10, 11, 12, 13, 14];
let union = new Set([...arr, ...arr4]);
log('union: ', union); // {0, 1, 2, 3, 3.1, …}

// Intersection.
let arr5 = [1,4,5,6,15,16,17,18,19];
let intersection = new Set();
arr5.forEach(n => {
    if (union.has(n)) {
        intersection.add(n);
    }});

log('Intersection:', [...intersection]); //  [1, 4, 5, 6]  

// Difference.
let difference = new Set(arr); 
arr5.forEach(n => {
    if (difference.has(n)) {
        difference.delete(n); 
    }});

log('Difference:', [...difference]); // [0, 2, 3, 3.1, 3.2, 7, 8, 9, 9.1]

// Symmetric difference.
let symmetricDiff = new Set([...arr, ...arr5]); 
arr5.forEach(n => {
    if (union.has(n)) {
        symmetricDiff.delete(n); 
    }
});
arr.forEach(n => {
    if (arr5.includes(n)) {
        symmetricDiff.delete(n); 
    }});

log('Symmetric Difference:', [...symmetricDiff]); // [0, 2, 3, 3.1, 3.2, 7, 8, 9, 9.1, 15, 16, 17, 18, 19]
