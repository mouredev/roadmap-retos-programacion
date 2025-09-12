//EJERCICIO
console.log('\n-BUCLE FOR-');

for (let i = 1; i <= 10; i++) {
	console.log(i);
}

console.log('\n-BUCLE WHILE-');

let counter = 1;

while (counter <= 10) {
	console.log(counter);
	counter++;
}

console.log('\n-BUCLE DO/WHILE-');

let counter2 = 1;

do {
	console.log(counter2);
	counter2++;
} while (counter2 <= 10);

//EXTRA
console.log('\n-RECURSIVIDAD-');

function countTen(i = 1) {
	if (i <= 10) {
		console.log(i);
		countTen(i + 1);
	}
}

countTen();

console.log('\n-BUCLE FOR EACH-');

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

numbers.forEach((n) => {
	console.log(n);
});

console.log('\n-BUCLE FOR IN-');

const numbersObj = {
	1: 'A',
	2: 'B',
	3: 'C',
	4: 'D',
	5: 'E',
	6: 'F',
	7: 'G',
	8: 'H',
	9: 'I',
	10: 'J',
};

for (let i in numbersObj) {
	console.log(i);
}

console.log('\n-BUCLE FOR OF-');

const numbersSet = new Set(numbers);

for (let i of numbersSet) {
	console.log(i);
}

console.log('\n-ITERANDO UNA STRING CONVERTIDA EN ARRAY-');
let numbersString = '1234567890';
numbersString.split('').forEach((n) => {
	console.log(n);
});
