// #05 VALOR Y REFERENCIA

/**
 * Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 * su tipo de dato.
 */

// por valor: la variable se copia, no la referencia (con valores primitivos)
let numberOne = 10;
let numberTwo = numberOne;

numberOne += 2;

console.log(numberOne, numberTwo); // -> 12, 10

let stringOne = 'Hello';
let stringTwo = stringOne;

stringOne += ' JavaScript!';

console.log(stringOne, stringTwo); // -> 'Hello JavaScript!', 'Hello'

let booleanOne = true;
let booleanTwo = booleanOne;

booleanOne = false;

console.log(booleanOne, booleanTwo); // -> false, true

// por referencia: el valor no se copia, lo que se asigna es la referencia (con objetos, arrays)
let personOne = {
	name: 'John',
	age: 37,
};
let personTwo = personOne;

personOne.age = 38;

console.log(personOne, personTwo); // -> { name: 'John', age: 38 }, { name: 'John', age: 38 }

let arrayOne = [10, 20, 30];
let arrayTwo = arrayOne;

arrayTwo.push(40);

console.log(arrayOne, arrayTwo); // -> [10, 20, 30, 40], [10, 20, 30, 40]

let func1 = () => console.log('1');
let func2 = func1;

func2 = () => console.log('2');

console.log(func1(), func2()); // -> 1, 2

/*
 *  Muestra ejemplos de funciones con variables que se les pasan "por valor" y
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 */

// pasando valores primitivos en una funcion...
// el valor que recibimos dentro de la función es siempre una “copia”,
// lo que implica que cualquier mutación o re-asignación de los parámetros
// dentro de una función no afecta al valor en el contexto de invocación.
// Primitivos
const returnNumber = (num) => {
	num = 0;
	return num;
};

const aNumber = 10;

console.log(returnNumber(aNumber)); // -> 0
console.log(aNumber); // -> 10

// No Primitivos
const addSix = (arr) => {
	const results = [];
	for (let num of arr) {
		let add6;
		add6 = num + 6;
		results.push(add6);
	}
	return results;
};
const arr = [1, 2, 3, 4];

console.log(double(arr)); // -> [2, 4, 6, 8]
console.log(arr); // -> [1, 2, 3, 4]

/** referencia circular:
 * En estos ejemplos, la propiedad self del objeto user hace referencia a sí mismo.
 * Esto crea un ciclo infinito en el que el objeto user apunta a sí mismo y viceversa.
 *
 * Y el array students El método push(students) intenta agregar el mismo array students
 * como un nuevo elemento al final de sí mismo.
 * Esto crea una situación en la que el último elemento del array students apunta de nuevo
 * al propio array, formando un bucle cerrado o referencia circular.
 * */
let user = {
	name: 'Juan',
	age: 25,
	self: 'user',
};

user.self = user;
console.log(user); // -> { name: 'Juan', age: 25, self: [Circular *1] }

let students = ['John', 'Mark', 'Jane'];
students.push(students);

console.log(students); // -> ['John', 'Mark', 'Jane', [Circular *1]]

/**
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

let valueOne = 'ONE';
let valueTwo = 'TWO';
let referenceOne = [1, 2, 3];
let referenceTwo = [4, 5, 6];

function byValue(pam1, pam2) {
	let pam1Temporal = pam1;
	pam1 = pam2;
	pam2 = pam1Temporal;
	return [pam1, pam2];
}

let changedValueOne = byValue(valueOne, valueTwo)[0];
let changedValueTwo = byValue(valueOne, valueTwo)[1];

console.log(
	`Value One: ${valueOne} 
  \nValue Two: ${valueTwo}
  \nChanged Value One: ${changedValueOne}
  \nChanged Value Two: ${changedValueTwo}`
);
// -> Value One: ONE
// -> Value Two: TWO
// -> Changed Value One: TWO
// -> Changed Value Two: ONE

function byReference(pam1, pam2) {
	let pam1Temporal = pam1;
	pam1 = pam2;
	pam2 = pam1Temporal;
	return [pam1, pam2];
}

let changedReferenceOne = byReference(referenceOne, referenceTwo)[0];
let changedReferenceTwo = byReference(referenceOne, referenceTwo)[1];

console.log(referenceOne); // -> [1, 2, 3]
console.log(referenceTwo); // -> [4, 5, 6]
console.log(changedReferenceOne); // -> [4, 5, 6]
console.log(changedReferenceTwo); // -> [1, 2, 3]
