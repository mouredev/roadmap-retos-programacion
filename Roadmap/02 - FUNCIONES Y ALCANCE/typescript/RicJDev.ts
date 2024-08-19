//EJERCICIO
function doSomething() {
	console.log('Hola, soy una función sin retorno ni parámetros');
}

doSomething();

function greeting(name: string) {
	console.log(
		`Hola, ${name}. Soy una función que admite un parámetro pero no retorno ningún valor`
	);
}

greeting('George');

function addTwoNumbers(a: number, b: number) {
	console.log(a + b);
}

addTwoNumbers(10, 20);

function returnAMessage(message: string) {
	return message;
}

let message = returnAMessage('Soy una función que retorna un valor');
console.log(message);

function getTotal(...arg: number[]) {
	let result: number = 0;

	for (let i = 0; i < arg.length; i++) {
		result = result + arg[i];
	}

	return result;
}

let total = getTotal(12, 23, 4, 10);
console.log(total);

function returnSomeValues() {
	return [12, 20, 40];
}

let [a, b, c] = returnSomeValues();
console.log(a);
console.log(b);
console.log(c);

function operate(a: number) {
	function divide() {
		return a / 2;
	}

	function multiply() {
		return a * 2;
	}

	const double = multiply();
	const half = divide();

	console.log(`El doble de ${a} es ${double}, mientras que la mitad es ${half}`);
}

operate(10);

const anonymus = function () {
	console.log('Soy una función anónima');
};

anonymus();

const arrowFun = () => {
	console.log('Soy una función flecha');
};

arrowFun();

let scopeVariable =
	'Soy una variable con alcance global. Cualquier parte de este código puede acceder a mí';
console.log(scopeVariable);

{
	let blockScopeVariable =
		'Soy una variable con alcance local. Solo soy accesible dentro de este bloque de código';

	console.log(blockScopeVariable);
}

//console.log(blockScopeVariable) daría error fuera del bloque de código

{
	var globalScope =
		'Soy una variable con alcance global. Cualquier parte de este código puede acceder a mí';
}

console.log(globalScope);

//EXTRA
function fizzBuzz(a: string = 'Fizz', b: string = 'Buzz') {
	for (let i = 1; i <= 100; i++) {
		if (i % 3 === 0 && i % 5 === 0) {
			console.log(a + ' ' + b);
		} else if (i % 3 === 0) {
			console.log(a);
		} else if (i % 5 == 0) {
			console.log(b);
		} else {
			console.log(i);
		}
	}
}

fizzBuzz('papa', 'frita');
