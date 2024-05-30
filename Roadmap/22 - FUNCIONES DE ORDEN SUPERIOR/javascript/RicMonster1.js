//EJERCICIO
let arr = [1, 2, 3];

console.log(arr.map((n) => n * 2));

Array.prototype.customMap = function (callback) {
	let result = [];
	for (let i = 0; i < this.length; i++) {
		let element = callback(this[i]);
		result.push(element);
	}
	return result;
};

console.log(arr.customMap((n) => n * 2));

//EXTRA
let myStudents = [];
let bestStudents = [];

class Student {
	constructor(name, grades, birthDate) {
		this.name = name;
		this.birthDate = birthDate;
		this.grades = grades;
		this.age = this.getAge();
		this.average = this.getAverage();

		myStudents.push(this);

		if (this.average >= 9) {
			bestStudents.push(this);
		}
	}

	getAverage() {
		let result = 0;
		this.grades.forEach((element) => {
			result = result + element;
		});
		let average = result / this.grades.length;
		return average;
	}

	getAge() {
		let now = new Date();
		let age =
			(now.getTime() - this.birthDate.getTime()) / (365 * 24 * 60 * 60 * 1000);
		return age;
	}
}

new Student('Sophie', [8, 8, 7, 9], new Date(2002, 8, 21));
new Student('Rebeca', [8, 9, 10, 9], new Date(2001, 4, 16));
new Student('David', [7, 6, 9, 8], new Date(2003, 0, 15));
new Student('Eliezer', [4, 6, 7, 5], new Date(2005, 1, 21));
new Student('Robert', [10, 10, 10, 9], new Date(2002, 0, 16));

function getHighestAverage() {
	let result;
	let average = 0;
	bestStudents.forEach((element) => {
		if (element.average > average) {
			result = element;
		}
	});
	return result;
}
let highestAverage = getHighestAverage();

//Pendiente por revisar
function sortByAge() {
	for (let i = 0; i < myStudents.length; i++) {
		for (let j = i + 1; j < myStudents.length; j++) {
			if (myStudents[i].age > myStudents[j].age) {
				let change = myStudents[i];
				myStudents[i] = myStudents[j];
				myStudents[j] = change;
			}
		}
	}

	return myStudents;
}

let sortedByAge = sortByAge();

let sortedByAverage = myStudents.sort(function (a, b) {
	return a.average - b.average;
});

console.log('\nLISTA DE PROMEDIOS');

sortedByAverage.customMap((element) => {
	console.log(`\n${element.name}: ${element.average}`);
});

console.log('\nMEJORES ESTUDIANTES');

bestStudents.customMap((element) => {
	console.log(`\n${element.name}: ${element.average}`);
});

console.log('\nLISTA DE NACIMIENTOS');

sortedByAge.customMap((element) => {
	console.log(`\n${element.name}: ${element.birthDate.toLocaleString()}`);
	console.log(`${Math.floor(element.age)} años`);
});

console.log('\nMEJOR PROMEDIO DE LA CLASE');

console.log(
	`\nFelicidades a ${highestAverage.name}. Con un ${highestAverage.average} se ha coronado como el mejor promedio de la clase`
);
