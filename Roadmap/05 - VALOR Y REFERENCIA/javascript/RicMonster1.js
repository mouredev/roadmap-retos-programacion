/* EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 */

//-Tipos de datos por valor-
let miNumA = 20;
let miNumB = miNumA;
console.log(miNumB); //---> 20
miNumA = 40; //actualizar el valor de miNumbA no afecta al de miNumB
console.log(miNumA); //---> 40
console.log(miNumB); //---> 20

//-Tipos de datos por referencia-
let arr1 = [1, 2, 3];
let arr2 = arr1;
console.log(arr1); //---> [1, 2, 3]
console.log(arr2); //---> [1, 2, 3]
arr2.push(4); //operar arr2 si afecta a arr1
console.log(arr1); //---> [1, 2, 3, 4]
console.log(arr2); //---> [1, 2, 3, 4]

//-Funciones con datos por valor-
const cambiaEsteNumA40 = (n) => {
	console.log((n = 40));
};

let miNumC = 5;
cambiaEsteNumA40(miNumC);
console.log(miNumC);

//-Funciones con datos por referencia-
const arr3 = [12, 34, 53];

const cambiaEsteArr = (arr) => {
	arr.push(30);

	const arr4 = arr;
	arr4.push(24);

	console.log(arr);
	console.log(arr4);
};

cambiaEsteArr(arr3);
console.log(arr3);

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

//-Por valor-
const intercambiaPorValor = (a, b) => {
	let temp = a;
	a = b;
	b = temp;
	return [a, b];
};

let miNumD = 45;
let miNumF = 63;

let [nuevoNumD, nuevoNumF] = intercambiaPorValor(miNumD, miNumF);

console.log(miNumD + ' ' + miNumF);
console.log(nuevoNumD + ' ' + nuevoNumF);

//-Por referencia-
const intercambiaPorReferencia = (a, b) => {
	let temp = a;
	a = b;
	b = temp;
	return [a, b];
}

let miArr1 = [10, 45, 20, 78];
let miArr2 = [100, 200, 432, 590];

let [nuevoArr1, nuevoArr2] = intercambiaPorReferencia(miArr1, miArr2);

console.log(miArr1 + '\n' + miArr2);
console.log(nuevoArr1 + '\n' + nuevoArr2);