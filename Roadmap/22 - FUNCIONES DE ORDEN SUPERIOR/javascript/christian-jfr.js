// #22 FUNCIONES DE ORDEN SUPERIOR
/**
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 */
// Callbacks
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

function arrayFilter(arr, callback) {
	const filteredArr = [];
	for (let i = 0; i < arr.length; i++) {
		callback(arr[i]) ? filteredArr.push(arr[i]) : null;
	}
	return filteredArr;
}

function isOdd(x) {
	return x % 2 != 0;
}

function isEven(x) {
	return x % 2 === 0;
}

console.log(arrayFilter(numbers, isOdd)); // -> [1, 3, 5, 7, 9]
console.log(arrayFilter(numbers, isEven)); // -> [2, 4, 6, 8, 10]

// Usando el filter que viene en javascript

console.log(numbers.filter(isOdd)); // -> [1, 3, 5, 7, 9]
console.log(numbers.filter(isEven)); // -> [2, 4, 6, 8, 10]

// return una funcion

function calculate(operator) {
	switch (operator) {
		case '*':
			return function (a, b) {
				console.log(`${a * b}`);
			};
		case '/':
			return function (a, b) {
				console.log(`${a / b}`);
			};
	}
}

calculate('*')(8, 4); // -> 32
calculate('/')(8, 4); // -> 2

/**
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

const students = [
	{ name: 'Christian', birthdate: '26-09-1987', grades: [7.2, 8.5, 8.8] },
	{ name: 'Nai', birthdate: '21-07-1985', grades: [9, 9.8, 10] },
	{ name: 'Johan', birthdate: '05-03-1986', grades: [9.2, 9.6, 10] },
	{ name: 'Nicholas', birthdate: '30-08-1988', grades: [5, 6, 8] },
	{ name: 'Dominique', birthdate: '12-04-1985', grades: [6.5, 7.2, 9] },
];

// Promedio calificaciones
function getAverage(studentGrades) {
	let sum = studentGrades.reduce(
		(accumulator, currentGrade) => accumulator + currentGrade,
		0
	);
	let average = parseFloat((sum / studentGrades.length).toFixed(1));
	return average;
}

const getStudentsAverage = students.map((student) => {
	return { name: student.name, average: getAverage(student.grades) };
});

// Mejores estudiantes
function isTopStudent(average) {
	return average >= 9;
}

const getTopStudents = getStudentsAverage.filter((student) => {
	return isTopStudent(student.average);
});

// Nacimiento
function parseDate(dateString) {
	const [day, month, year] = dateString.split('-');
	return new Date(year, month - 1, day);
}

const sortedStudents = students.sort((a, b) => {
	const dateA = parseDate(a.birthdate);
	const dateB = parseDate(b.birthdate);
	return dateB - dateA;
});

// Mayor calificación
const allGrades = students.flatMap((student) => student.grades);

const highestGrade = allGrades.reduce(
	(max, grade) => (grade > max ? grade : max),
	-Infinity
);

// Resultados
console.log(getStudentsAverage); // Muestra una lista con el nombre y promedio de calificaciones
console.log(getTopStudents); // Muestra los estudiantes que tuvieron una calificación de 9 o superior
console.log(sortedStudents); // Muestra la lista de estudiantes ordenados de menor a mayor edad
console.log(highestGrade); // Muestra la mayor calificación
