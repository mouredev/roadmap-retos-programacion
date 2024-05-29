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

class Student {
	constructor(name, grades, date, month, year) {
		this.name = name;
		this.grades = grades;
		let birthDateNoFormat = new Date(year, month - 1, date);
		this.birthDate = birthDateNoFormat.toLocaleString();
		myStudents.push(this);
	}

	getAverage() {
		let result = 0;
		this.grades.forEach((element) => {
			result = result + element;
		});
		return result / this.grades.length;
	}
}

new Student('Sophie', [8, 8, 7, 9], 12, 11, 2004);
new Student('David', [7, 6, 9, 8], 23, 1, 2005);
new Student('Eliezer', [4, 6, 7, 5], 21, 2, 2005);
new Student('Rebeca', [8, 9, 10, 9], 16, 5, 2005);

myStudents.forEach((element) => {
	console.log(`\nEl promedio de ${element.name} es de ${element.getAverage()}`);
});
