// OPERADORES ARITMÉTICOS
console.log('OPERADORES ARITMÉTICOS');
const firstNumber: number = 7;
const secondNumber: number = 2;
let result: number;

// Operador suma (+)
result = firstNumber + secondNumber;
console.log(`La suma de ${firstNumber} + ${secondNumber} es ${result}`);

// Operador resta (-)
result = firstNumber - secondNumber;
console.log(`La resta de ${firstNumber} - ${secondNumber} es ${result}`);

// Operador multiplicación (*)
result = firstNumber * secondNumber;
console.log(`La multiplicación de ${firstNumber} * ${secondNumber} es ${result}`);

// Operador división (/)
result = firstNumber / secondNumber;
console.log(`La división de ${firstNumber} / ${secondNumber} es ${result}`);

// Operador módulo (%)
result = firstNumber % secondNumber;
console.log(`El resto de la división de ${firstNumber} / ${secondNumber} es ${result}`);

// OPERADORES LÓGICOS
console.log('\nOPERADORES LÓGICOS');
const firstBool: boolean = true;
const secondBool: boolean = false;

// Operador lógico AND (&&)
const logicAnd: boolean = (firstBool && secondBool);
console.log(`AND lógico: ${logicAnd}`);

// Operador lógico OR (||)
const logicOr: boolean = (firstBool || secondBool);
console.log(`OR lógico: ${logicOr}`);

// Operador lógico NOT (!)
const logicNot: boolean = !firstBool;
console.log(`NOT lógico: ${logicNot}`);

// OPERADORES DE COMPARACIÓN
console.log('\nOPERADORES DE COMPARACIÓN');
// Operador mayor que (>)
const greatThan: boolean = (5 > 10);
console.log(`¿Es 5 mayor que 10? -> ${greatThan}`);

// Operador menor que (>)
const lessThan: boolean = (5 < 10);
console.log(`¿Es 5 menor que 10? -> ${lessThan}`);

// Operador mayor o igual que (>=)
const greatOrEqual: boolean = (5 >= 10);
console.log(`¿Es 5 mayor o igual que 10? -> ${greatOrEqual}`);

// Operador menor o igual que (<=)
const lessOrEqual: boolean = (5 <= 10);
console.log(`¿Es 5 menor o igual que 10? -> ${lessOrEqual}`);

// OPERADORES DE ASIGNACIÓN
console.log('\nOPERADORES DE ASIGNACIÓN');
// Operador de asignación simple (=)
let number:number = 10;
console.log(`Valor asignado: ${number}`);

// Operador de suma y asignación (+=)
number += 5; // 10 + 5 = 15
console.log(`Valor del resultado de suma y asignación: ${number}`);

// Operador de resta y asignación (-=)
number -= 5; // 15 - 5 = 10
console.log(`Valor del resultado de resta y asignación: ${number}`);

// Operador de multiplicación y asignación (+=)
number *= 5; // 10 * 5 = 50
console.log(`Valor del resultado de multiplicación y asignación: ${number}`);

// Operador de división y asignación (/=)
number /= 5; // 50 / 5 = 10
console.log(`Valor del resultado de división y asignación: ${number}`);

// Operador de módulo y asignación (%=)
number %= 5; // 10 % 5 = 0
console.log(`Valor del resultado de módulo y asignación: ${number}`);

// OPERADORES DE IDENTIDAD
console.log('\nOPERADORES IDENTIDAD');
// Operador de igualdad estricta
const strictEqualComp: boolean = (5 === 5);
console.log(`¿Es 5 estrictamente igual a 5? -> ${strictEqualComp}`);

// Operador de desigualdad estricta (!==)
const strictDiffComp: boolean = ('5' !== '5');
console.log(`¿Es '5' estrictamente diferente a '5'? -> ${strictDiffComp}`);

// OPERADORES DE PERTENENCIA
console.log('\nOPERADORES DE PERTENENCIA')
const intArray: number[] = [1, 12, 5, 643, 3];
const firstCheck: boolean = 3 in intArray; // Devolverá true
const secondCheck: boolean = 65 in intArray; // Devolverá false

console.log(`¿Está el número 3 en el array de números? -> ${firstCheck}`);
console.log(`¿Está el número 65 en el array de números? -> ${secondCheck}`);

// OPERADORES DE BITS
console.log('\nOPERADORES DE BITS')
const firstBit: number = 5; // Representación binaria: 0000 0101
const secondBit: number = 3 // Representación binaria: 0000 0011

// Operador AND a nivel de bits (&)
const bitAnd: number = firstBit & secondBit; // Devuelve 1 (representación binaria: 0000 0001)
console.log(`Resultado AND bit a bit -> ${bitAnd}`);

// Operador OR a nivel de bits (|)
const bitOr: number = firstBit | secondBit; // Devuelve 7 (representación binaria: 0000 0111)
console.log(`Resultado OR bit a bit -> ${bitOr}`);

// Operador XOR a nivel de bits (^)
const bitXor: number = firstBit ^ secondBit; // Devuelve 6 (representación binaria: 0000 0110)
console.log(`Resultado OR bit a bit -> ${bitXor}`);

// Operador NOT a nivel de bits (~)
const bitNot: number = ~firstBit; // Devuelve -6 (representación binaria: 1111 1010)
console.log(`Resultado NOT bit a bit -> ${bitNot}`);

// Operador de desplazamiento hacia la derecha (>>)
const toRightBit: number = firstBit >> 1; // Devuelve 2 (representación binaria: 0000 0010)
console.log(`Desplazamiento hacia la derecha -> ${toRightBit}`);

// Operador de desplazamiento hacia la izquierda (>>)
const toLeftBit: number = firstBit << 1; // Devuelve 10 (representación binaria: 0000 1010)
console.log(`Desplazamiento hacia la derecha -> ${toLeftBit}`);

// ESTRUCTURAS DE CONTROL CONDICIONAL
console.log('\nESTRUCTURAS DE CONTROL CONDICIONAL')
// if-else
console.log('if-else')
const num: number = 10;

if (num > 0) {
    console.log('El número es positivo.');
} else if (num === 0) {
    console.log('El número es cero.');
} else {
    console.log('El número es negativo.');
}

// Operador ternario
console.log('\nOperador ternario');
console.log((num > 0) ? 'El número es positivo.' : 'El número es cero o negativo.');

// switch-case
console.log('\nSwitch-Case');
let option: number = 1;

switch (option) {
    case 1:
        console.log('Se ha seleccionado la opción 1.');
        break;
    case 2:
        console.log('Se ha seleccionado la opción 2.');
        break;
    default:
        console.log('Opción por defecto.');
}

// ESTRUCTURAS DE CONTROL ITERATIVAS
console.log('\nESTRUCTURAS DE CONTROL ITERATIVAS')
// while
console.log('Bucle While');
let counter: number = 0;
while (counter < 5) {
    console.log(`Iteración: ${counter}`);
    counter++;
}

// do-while
console.log('\nBucle do-while');
counter = 0;
do {
    console.log(`Iteración: ${counter}`);
    counter++;
} while (counter < 5);

// for
console.log('\nBucle for');
for (let counter: number = 0; counter < 5; counter++) {
    console.log(`Iteración: ${counter}`);
}

// for ... of
console.log('\nBucle for ... of');
const arrNumbers: number[] = [1, 2, 5, 2, 7, 9];
for (const number of arrNumbers) {
    console.log(`Número -> ${number}`);
}

// for ... in
console.log('\nBucle for ... in');
const persona: object = { name: 'Alberto', age: 33 };
for (const att in persona) {
    console.log(`${att} -> ${persona[att]}`);
}

// MANEJO DE EXCEPCIONES
console.log('\nMANEJO DE EXCEPCIONES');
console.log('Bloque try-catch');
const errNumber: number = 10;

try {
    if (errNumber === 10) {
        throw new Error('El número es igual a 10.');
    }
    console.log('El número es distinto de 10.');
} catch (error) {
    console.log(`Se ha producido un error debido a -> ${error.message}`);
}

console.log('\nBloque try-catch-finally');
try {
    if (errNumber === 10) {
        throw new Error('El número es igual a 10.');
    }
    console.log('El número es distinto de 10.');
} catch (error) {
    console.log(`Se ha producido un error debido a -> ${error.message}`);
} finally {
    console.log('Bloque finally. Esto siempre se ejecuta haya o no excepción.');
}

// DIFICULTAD EXTRA
console.log("\nEJERCICIO EXTRA");
/*  Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y
 *  que no son ni el 16 ni múltiplos de 3.*/
for (let i = 10; i <= 55; i++) {
    if ((i % 2 === 0) && (i !== 16) && (i % 3 !== 0)) {
        console.log("Iteración: " + i);
    }
}