// Ejemplos de asignación por valor, todos los valores primitivos se pasan por valor
let number = 1;
let str = "Hola Mundo!";
let boolean = true;
let undf = undefined;
let nullish = null;
let bigInt = BigInt(13);
let symbol = Symbol("symbol");

// Ejemplos de asignación por referencia, todos los valores que no son primitivos se pasan por referencia
let arr = [1, 2, 3, 4];
let obj = { nombre: "Facundo", apellid: "Muoio" };
let sum = function (a, b) {
	return a + b;
};

// Ejemplo de una funcion con variables pasados por valor y referencia
// En el primer caso tomamos number que se pasa como valor por lo cual esta funcion es pura y no moficia ninguna variables del ambito externo u global. Como se visualiza en el console.log tendremos numXTwo = 2 y number continuara siendo 1 por mas que lo copiemos en la varable numXTWO

function multiply() {
	numXTwo = number;
	return (numXTwo *= 2);
}

console.log(multiply(), number);

// En este segundo caso modificaremos el arr que hemso declaro y notaremos que al pasarse por referencia cuando hagamos una copia del array
// dentro de la función y la modifiquemos los cambios seran visibles tanto en el array original como en la copia, ya que referencian al mismo
//objeto

function changeArray() {
	const arrayCopy = arr;
	arrayCopy.push("5");
	arrayCopy.shift();
	return arrayCopy;
}

console.log(arr, changeArray());

//Ejercicio extra
let variableUno = "uno";
let variableDos = "dos";

function forValue(par1, par2) {
	par1 = par2;
	par2 = variableUno;
	return [par1, par2];
}

let retornoVariableUno = forValue(variableUno, variableDos)[0];
let retornoVariableDos = forValue(variableUno, variableDos)[1];

console.log({
	variableUno,
	variableDos,
	retornoVariableUno,
	retornoVariableDos,
});

let array = [1, 2, 3];
let arrayDos = ["Uno", "Dos", "Tres"];

function forReference(arr1, arr2) {
	arr1 = arr2;
	arr2 = array;
	return [arr1, arr2];
}

console.log(array, arrayDos, arr1, arr2);
