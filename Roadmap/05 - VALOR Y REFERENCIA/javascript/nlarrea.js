/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */


// Asignación por valor

let numberA = 11;
let numberB = numberA;
console.log('numberA:', numberA);  // numberA: 11
console.log('numberB:', numberB);  // numberB: 11
numberB = 7;
console.log('numberA:', numberA);  // numberA: 11
console.log('numberB:', numberB);  // numberB: 7

// Asignación por referencia

let arrayA = [1, 2, 3, 4];
let arrayB = arrayA;
console.log('arrayA:', arrayA);  // [1, 2, 3, 4]
console.log('arrayB:', arrayB);  // [1, 2, 3, 4]
arrayB.push(5);
console.log('arrayA:', arrayA);  // [1, 2, 3, 4, 5]
console.log('arrayB:', arrayB);  // [1, 2, 3, 4, 5]

// Funciones por valor

function printDouble(number) {
    number *= 2;
    console.log(number);
}

let myNumber = 2;
printDouble(myNumber);  // 4
console.log(myNumber);  // 2

// Funciones por referencia

function printAppendNumber(arr, num) {
    arr.push(num);
    console.log(arr);
}

let myArr = [1, 2, 3, 4]
printAppendNumber(myArr, 5);  // [1, 2, 3, 4, 5]
console.log(myArr);  // [1, 2, 3, 4, 5]


/*
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */


function exchangeByValue(valOne, valTwo) {
    [valOne, valTwo] = [valTwo, valOne]
    return [valOne, valTwo];
}

let firstValue = 11
let secondValue = 7
let [val1, val2] = exchangeByValue(firstValue, secondValue);
console.log(`1.1 Before function: ${firstValue}, After function: ${val1}`);
// 1.1 Before function: 11, After function: 7
console.log(`1.2 Before function: ${secondValue}, After function: ${val2}`);
// 1.2 Before function: 7, After function: 11


function exchangeByReference(arrOne, arrTwo) {
    [arrOne, arrTwo] = [[...arrTwo], [...arrOne]];
    return [arrOne, arrTwo]
}

let firstArray = [1, 2, 3, 4]
let secondArray = [9, 8, 7, 6]
let [arr1, arr2] = exchangeByReference(firstArray, secondArray);
console.log(`2.1 Before function: ${firstArray}, After function: ${arr1}`);
// 2.1 Before function: 1,2,3,4, After function: 9,8,7,6
console.log(`2.2 Before function: ${secondArray}, After function: ${arr2}`);
// 2.2 Before function: 9,8,7,6, After function: 1,2,3,4