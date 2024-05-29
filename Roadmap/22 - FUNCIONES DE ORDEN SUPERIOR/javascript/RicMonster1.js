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

/*
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y
 * lista de calificaciones), utiliza funciones de orden superior para
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
 */

let myStudents = [];
let bestStudents = [];

class Student {
	constructor(name, grades, birthDate) {
		this.name = name;
		this.grades = grades;
		this.birthDate = birthDate;
		this.age = this.getAge();
		this.average = this.getAverage();
		myStudents.push(this);

		if (this.getAverage() >= 9) {
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
		let age = Math.floor(
			(now.getTime() - this.birthDate.getTime()) / (365 * 24 * 60 * 60 * 1000)
		);
		return age;
	}
}

new Student('Sophie', [8, 8, 7, 9], new Date(2002, 8, 21));
new Student('David', [7, 6, 9, 8], new Date(2003, 0, 15));
new Student('Eliezer', [4, 6, 7, 5], new Date(2005, 1, 21));
new Student('Rebeca', [8, 9, 10, 9], new Date(2001, 4, 16));
new Student('Robert', [10, 10, 10, 9], new Date(2002, 0, 16));

function getHighestAverage() {
	let result;
	let average = 0;
	bestStudents.forEach((element) => {
		if (element.getAverage() > average) {
			result = element;
		}
	});
	return result;
}

let highestAverage = getHighestAverage();

function sortByAge() {}

console.log(
	`\n${highestAverage.name} ha obtenido el mayor promedio de la clase: ${highestAverage.average}\n`
);

console.log(myStudents.find((element) => element.name === 'David'));

myStudents.customMap((element) => {
	console.log(`\nEl promedio de ${element.name} es de ${element.average}`);
});

myStudents.customMap((element) => {
	console.log(`\nEl nacimiento de ${element.name} fue el ${element.birthDate}`);
});
