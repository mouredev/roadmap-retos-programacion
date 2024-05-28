//EJERCICIO
let arr = [1, 2, 3];

//console.log(arr.map((n) => n * 2));

Array.prototype.customMap = function (callback) {
	let result = [];
	for (let i = 0; i < this.length; i++) {
		let element = callback(this[i]);
		result.push(element);
	}

	return result;
};

//console.log(arr.customMap((n) => n * 2));

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

let myStudents = [
  {
    name: 'Ric',
    birthDate : new Date(2002, 8, 22),
    grades: [6, 7, 9, 7, 8, 9]
  },
  {
    name: 'Eric',
    birthDate: new Date(2002, 5, 5),
    grades: [9, 8, 9, 7, 9, 8],
  },
  {
    name: 'Rebeca',
    birthDate: new Date(2003, 0, 2),
    grades: [8, 7, 9, 6, 9, 8],
  }
];
*/

let myStudents = [];

class Student {
	constructor(name) {
		this.name = name;
		this.grades = [];
	}

	setBirthdate(date, month, year) {
		let birthDateNoFormat = new Date(year, month - 1, date);
		this.birthDate = birthDateNoFormat.toLocaleString();
	}
}

function createStudent(name, date, month, year) {
	let student = new Student(name);
	student.setBirthdate(date, month, year);
	myStudents.push(student);
}

Array.prototype.getAverage = function () {
	let result = 0;
	this.forEach((element) => {
		result = result + element;
	});
	return result / this.length;
};

createStudent('Sophie', 12, 3, 2004);

createStudent('David', 23, 5, 2005);

let randomArr = [5, 4, 5, 6, 7];

console.log(randomArr.getAverage());