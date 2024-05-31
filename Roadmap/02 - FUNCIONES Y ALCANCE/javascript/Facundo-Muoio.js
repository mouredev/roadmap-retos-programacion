// funcionsin parametros
function noParams() {
	return console.log("funcion sin parametros");
}
noParams();

// funcion con un parametro y sin retorno
function sayHello(nombre) {
	console.log(`Hola ${nombre}`);
}
sayHello("Facundo");

// funcion con varios parametros y con parametros predeterminados
function sum(a = 5, b = 5) {
	return a + b;
}
console.log(sum(), sum(20, 50));

// funcion con rest params
function sumAllNumbers(a, b, ...c) {
	let sum = a + b;
	c.map(number => (sum += number));
	return sum;
}
console.log(sumAllNumbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));

// funcion dentro de otra funcion
function outer() {
	console.log("esta es una funcion que a su vez crea una funcion interna");
	function inner() {
		console.log("esta es la funcion interna creada dentro de la funcion outer");
	}
	inner();
}
outer();

// callback funcion
function hello(name) {
	return console.log("Hola " + name);
}

function processInputUser(callback) {
	var name = prompt("Por favor ingresa tu nombre.");
	callback(name);
}

processInputUser(hello);

// Declaracion de funciones
function unaFuncion() {
	return console.log("Esto es una declaracion de una funcion");
}
unaFuncion();

// Expresion de una funcion
const otraFuncion = function () {
	return console.log("Esto es una expresion dee una funcion ");
};
otraFuncion();

// Funcion anonima
const anonima = function () {
	console.log("Esto es una funcion anonima");
};
anonima();

// Funcion flecha
const arrowFunction = () =>
	"Soy una funcin flecha y no posee this entre otras diferencias con las funciones tradicionales";
console.log(arrowFunction());

// Expresion de funcion incovada inmediatamente IIFE
(function () {
	return console.log("Soy una Expresión de función invocada inmediatamente");
})();

let globalLet = "soy una variable global";
function printVariables() {
	let localLet = "soy una varable local";
	return console.log(globalLet, localLet);
}

//imprime ambas variables tanto la global como la local
printVariables();
console.log(globalLet);
// el siguiente console.log tendra un reference error, ya que la localLet variable no existe en su scope, esto es así porque carece de acceso al ambito de la variable de la funcion printVariables, esta funcion tiene un estado privado con respecto al entorno que engloba. Por lo cual no existe esta variable en el ambito global.
console.log(localLet);

//funciones ya creadas en el lenguaje
const arr = [1, 2, 3, 4, 5];

//itera sobere todos los elemntos del arreglo y devuelve un nuevo arreglo con sus elementos multiplicados x 2
console.log(arr.map(number => number * 2));
//Devuelve un nuevo arreglo con todos los elementos mayores a 2
console.log(arr.filter(number => number > 2));
//Devuelve el primer elemento del arreglo que satisfaga la callback function que pasamos como argumento
console.log(arr.find(number => number === 3));
//Devuelve la suma de todos los elemntos del arreglo
console.log(arr.reduce((cv, acc) => (acc += cv)));

//funcion extra
function extraPoint(str1, str2) {
	let acumulador = 0;
	for (let i = 1; i <= 100; i++) {
		i % 3 === 0 && i % 5 === 0
			? console.log(str1 + str2)
			: i % 3 === 0
			? console.log(str1)
			: i % 5 === 0
			? console.log(str2)
			: (console.log(i), acumulador++);
	}
	return acumulador;
}

console.log(extraPoint("uno", "dos"));
