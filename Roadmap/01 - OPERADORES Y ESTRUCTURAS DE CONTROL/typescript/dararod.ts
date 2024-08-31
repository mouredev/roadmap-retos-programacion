/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

// OPERADORES -->

let firstNumber: number = 10;
let secondNumber: number = 2;
let numericResult: number;
let booleanResult: boolean;

//Arithmetic Operators
//Adition (+)
numericResult = firstNumber + secondNumber;
console.log(`The sum of ${firstNumber} + ${secondNumber} returns ${numericResult}`);

//Subtraction (-)
numericResult = firstNumber - secondNumber;
console.log(`The differece of ${firstNumber} - ${secondNumber} returns ${numericResult}`);

//Multiplication (*)
numericResult = firstNumber * secondNumber;
console.log(`The product of ${firstNumber} * ${secondNumber} returns ${numericResult}`);

//Division (/)
numericResult = firstNumber / secondNumber;
console.log(`The quotient of ${firstNumber} / ${secondNumber} returns ${numericResult}`);

//Modulus (%)
numericResult = firstNumber % secondNumber;
console.log(`The remainder of ${firstNumber} % ${secondNumber} returns ${numericResult}`);

//Increment (++)
numericResult = firstNumber++;
console.log(`Increment ${firstNumber} returns ${numericResult}`);

//Decrement (--)
numericResult = firstNumber--;
console.log(`Decrement ${firstNumber} returns ${numericResult}`);


//Relational Operators
//Greater than (>)
booleanResult = firstNumber > secondNumber;
console.log(`${firstNumber} > ${secondNumber} returns ${booleanResult}`);

//Lesser than (<)
booleanResult = firstNumber < secondNumber;
console.log(`${firstNumber} < ${secondNumber} returns ${booleanResult}`);

//Greater than or equal to (>=)
booleanResult = firstNumber >= secondNumber;
console.log(`${firstNumber} >= ${secondNumber} returns ${booleanResult}`);

//Lesser than or equal to (<=)
booleanResult = firstNumber <= secondNumber;
console.log(`${firstNumber} <= ${secondNumber} returns ${booleanResult}`);

//Equality (==)
booleanResult = firstNumber == secondNumber;
console.log(`${firstNumber} == ${secondNumber} returns ${booleanResult}`);

//Not equal (!=)
booleanResult = firstNumber != secondNumber;
console.log(`${firstNumber} != ${secondNumber} returns ${booleanResult}`);


//Logical Operators
//And (&&)
booleanResult = firstNumber > secondNumber && secondNumber < 5;
console.log(`${firstNumber} > ${secondNumber} && ${secondNumber} < 5 returns ${booleanResult}`);

//Or (||)
booleanResult = firstNumber > secondNumber || secondNumber < 1;
console.log(`${firstNumber} > ${secondNumber} || ${secondNumber} < 1 returns ${booleanResult}`);

//Not (!)
booleanResult = !(firstNumber > secondNumber);
console.log(`!(${firstNumber} > ${secondNumber}) returns ${booleanResult}`);


//Assignment Operators
let newNumber: number;

//Simple Assignment (=)
newNumber = firstNumber;
console.log(`newNumber value is ${newNumber}`);

//Add and Assignment (+=)
newNumber += firstNumber;
console.log(`newNumber value is ${newNumber}`);

//Subtract and Assignment (-=)
newNumber -= firstNumber;
console.log(`newNumber value is ${newNumber}`);

//Multiply and Assignment (*=)
newNumber *= firstNumber;
console.log(`newNumber value is ${newNumber}`);

//Divide and Assignment (/=)
newNumber /= firstNumber;
console.log(`newNumber value is ${newNumber}`);


//Ternary/Conditional Operator
let stringResult: string;
stringResult = firstNumber > 0 ? 'Number is positive' : 'Number is negative';
console.log(`stringResult value is ${stringResult}`);


//Type Operators
//typeof operator
stringResult = typeof firstNumber;
console.log(`stringResult value is ${stringResult}`);
// OPERADORES <--


//ESTRUCTURAS DE CONTROL
//Conditional (If else)
if (firstNumber > 0) {
    console.log('Number is positive.');
} else if (firstNumber === 0) {
    console.log('Number is cero.');
} else {
    console.log('Number is negative.');
}

//For
for (let i = 0; i <= firstNumber; i++) {
    console.log(i)
}

//For in
const object: object = { a: 1, b: 2, c: 3 };
for (const property in object) {
    console.log(`${property}: ${object[property]}`);
}

//For of
const numberArray: number[] = [0, 1, 2, 3, 4, 5];
for (const number of numberArray) {
    console.log(`Number ${number}`);
}

//While
while (secondNumber < firstNumber) {
    secondNumber++
    console.log(`Now secondNumber value is ${secondNumber}`)
}

//Switch
const expr: string = 'Papayas';
switch (expr) {
    case 'Oranges':
        console.log('Oranges are $0.59 a pound.');
        break;
    case 'Mangoes':
    case 'Papayas':
        console.log('Mangoes and papayas are $2.79 a pound.');
        break;
    default:
        console.log(`Sorry, we are out of ${expr}.`);
}

//Try catch
try {
    nonExistentFunction();
} catch (err) {
    console.error(err);
}


// DIFICULTAD EXTRA
/*  Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y
 *  que no son ni el 16 ni múltiplos de 3.*/
for (let i = 10; i <= 55; i++) {
    if ((i % 2 === 0) && (i !== 16) && (i % 3 !== 0)) {
        console.log("Value: " + i);
    }
}
