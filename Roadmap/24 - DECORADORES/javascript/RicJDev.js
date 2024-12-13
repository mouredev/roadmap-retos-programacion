//EJERCICIO
function steveDecorator(fun) {
	return function (...arg) {
		let result = fun(...arg);
		console.log('Soy Steve, el decorador');
		return result;
	};
}

function greeting(name) {
	console.log(`\nHola, ${name}`);
}

greeting('Jeff');

greeting = steveDecorator(greeting);

greeting('Gerard');

//EXTRA
function counterDecorator(fun) {
	let count = 0;

	return function (...arg) {
		count++;
		result = fun(...arg);
		console.log(`Conteo de llamadas de ${fun.name}(): ${count}`);
		return result;
	};
}

function addTwoNumbers(a, b) {
	console.log(`\nEl resultado de sumar ${a} y ${b} es ${a + b}`);
}

addTwoNumbers = counterDecorator(addTwoNumbers);

addTwoNumbers(10, 23);
addTwoNumbers(14, 3);

function square(a) {
	console.log(`\nEl cuadrado de ${a} es igual a ${a * a}`);
}

square = counterDecorator(square);

square(9);
square(5);
