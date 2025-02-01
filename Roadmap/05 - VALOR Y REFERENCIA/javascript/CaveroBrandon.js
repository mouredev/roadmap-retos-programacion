/*
 EJERCICIO:
- Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
su tipo de dato.
- Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
"por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
(Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
*/

// Assigning a value by value
let currentYear = 2025;
console.log('Assigned by value: ' + currentYear);

// Assigning a value by reference
let animals = ['lion', 'fish', 'dog'];
console.log('Assigned by value: ' + animals);
let animalsArrayCopy = animals;
console.log('Assigned by reference: ' + animalsArrayCopy);

// Changing the first array assigned by value
animals.push('cat');
console.log('Assigned by value after change: ' + animals);
// The array assigned by reference is also updated
console.log('Assigned by reference after change: ' + animalsArrayCopy);


/*
* DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
Comprueba también que se ha conservado el valor original en las primeras.
*/

// Receives two values and assign them by value
function firstProgram(first, second) {
    let aux = first;
    first = second;
    second = aux;
    return [first, second];
}
function secondProgram(first, second) {
    first = vegetables;
    second = fruits;
    return [first, second];
}

console.log('---------------------------------');
const a = 1;
const b = 2;
console.log('Variables before executing first method');
console.log('firstVariable = ' + a + ', secondVariable = ' + b);
console.log('Variables after executing first method');
let [firstValue, secondValue] = firstProgram(a, b);
console.log('firstVariable = ' + firstValue + ', secondVariable = ' + secondValue);

console.log('---------------------------------');
let fruits = ['apple', 'banana', 'grape'];
let vegetables = ['tomato', 'carrot', 'radish'];
console.log('Variables before executing second method');
console.log('firstVariable = ' + fruits + ', secondVariable = ' + vegetables);
console.log('Variables before executing second method');
let [firstArray, secondArray] = secondProgram(fruits, vegetables);
console.log('firstVariable = ' + firstArray + ', secondVariable = ' + secondArray);
