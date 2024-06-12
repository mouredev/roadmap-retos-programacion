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
const myStudents = [];
const bestStudents = [];
const failedStudents = [];

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

		if (this.average < 5) {
			failedStudents.push(this);
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

new Student('Sophie', [8, 8, 7, 9], new Date(2003, 8, 21));
new Student('Rebeca', [8, 9, 10, 9], new Date(2001, 4, 16));
new Student('David', [7, 7, 9, 8], new Date(2003, 0, 15));
new Student('Eliezer', [4, 6, 7, 5], new Date(2005, 1, 21));
new Student('Robert', [10, 10, 10, 9], new Date(2002, 0, 16));
new Student('Erika', [10, 6, 6, 9], new Date(2003, 0, 20));
new Student('Tadeo', [4, 6, 3, 5], new Date(2004, 0, 2));

function getHighestAverage() {
	let result;
	let average = 0;
	myStudents.forEach((element) => {
		if (element.average > average) {
			average = element.average;
			result = element;
		}
	});
	return result;
}

let highestAverage = getHighestAverage();

let sortedByAverage = myStudents.toSorted((a, b) => {
	return b.average - a.average;
});

let sortedByAge = myStudents.toSorted((a, b) => {
	return a.age - b.age;
});

console.log(`\nCANTIDAD DE ESTUDIANTES: ${myStudents.length}`);

console.log('\nLISTA DE PROMEDIOS');

sortedByAverage.customMap((element) => {
	console.log(`\n${element.name}: ${element.average}`);
});

console.log(`\nMEJORES ESTUDIANTES: ${bestStudents.length}`);

bestStudents.customMap((element) => {
	console.log(`\n${element.name}: ${element.average}`);
});

console.log(`\nESTUDIANTES REPROBADOS: ${failedStudents.length}`);
failedStudents.customMap((element) => {
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
