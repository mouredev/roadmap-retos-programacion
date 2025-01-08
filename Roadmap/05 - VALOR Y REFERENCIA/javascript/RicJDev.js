//EJERCICIO
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
let miNumC = 5;

function suma40(num) {
	return num + 40;
}

console.log(miNumC);

suma40(miNumC);
console.log(miNumC);

//-Funciones con datos por referencia-
const arr3 = [12, 34, 53];

const agrega40ALaLista = (arr) => {
	return arr.push(40);
};

console.log(arr3);

agrega40ALaLista(arr3);
console.log(arr3);

//EXTRA
//-Por valor-
function intercambiaLosValores(a, b) {
	let temp = a;
	a = b;
	b = temp;
	return [a, b];
}

let miNumD = 45;
let miNumF = 63;

let [nuevoNumD, nuevoNumF] = intercambiaLosValores(miNumD, miNumF);

console.log(`\nValores originales: ${miNumD}, ${miNumF}`);
console.log(`\nValores luego de cambiarlos con la función: ${nuevoNumD}, ${nuevoNumF}`);

//-Por referencia-
//Funciona de la misma manera con los arrays
let miArr1 = [10, 45, 20, 78];
let miArr2 = [100, 200, 432, 590];

let [nuevoArr1, nuevoArr2] = intercambiaLosValores(miArr1, miArr2);

console.log('\nArrays originales:');
console.log(miArr1, miArr2);

console.log('\nArrays luego de pasarlos por la función:');
console.log(nuevoArr1, nuevoArr2);

let miObj1 = {
	a: 12,
	b: 24,
};

let miObj2 = {
	c: 45,
	d: 68,
};

console.log('\nFunciona igual para los objetos:');

console.log(miObj1, miObj2);
let [nuevoObj1, nuevoObj2] = intercambiaLosValores(miObj1, miObj2);
console.log(nuevoObj1, nuevoObj2);
