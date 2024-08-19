/*
* EJERCICIO:
* Explora el concepto de funciones de orden superior en tu lenguaje 
* creando ejemplos simples (a tu elección) que muestren su funcionamiento.
*
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


//Map 

const languages = ["Java", "Python", "JavaScript", "Go", "Bash"];

const languagesLower = languages.map((lan) => lan.toLowerCase());
console.log(languagesLower)

// Filter

const is_name_long = languages.filter((lan) => lan.length > 6);
console.log(is_name_long)

const numbers = [1, 2, 3, 4, 5];

const is_odd = numbers.filter((num) => num % 2!= 0 );
console.log(is_odd)

// Reduce

const sum = numbers.reduce((acc, cur) => acc + cur, 0);

console.log(sum)

// every

const areAllint = numbers.every((nume) => typeof nume === "number");

console.log(areAllint)

// find

const name_long = languages.find((lan) => lan.length > 3);
console.log(name_long)


const scores = [
  {name: "Juan", score: 90},
  {name: "Raul", score: 78},
  {name: "Pedro", score: 69},
  {name: "Matias", score: 98},
];

const user_score = scores.find((user) => user.score > 91 );
console.log(user_score)

// findIndex

const ages = [34, 15, 26, 87, 47]

const age = ages.findIndex((age) => age < 20);
console.log(age)

// some

const list_age = [34, 15, "26", 87, 47]

const someTrue = list_age.some((x) => x==="26");
console.log(someTrue)



//////////////-----------------------------  EXTRA ----------------------------------/////////////////////////

students = [
  {"name": "Carlos", "date_birth": "15-05-2001", "grades": [8.5, 9, 9.5]},
  {"name": "Juan", "date_birth": "08-11-2000", "grades": [10, 9, 9.5]},
  {"name": "Pedro", "date_birth": "17-01-2002", "grades": [7, 8, 7.6]},
  {"name": "Jose", "date_birth": "22-10-2000", "grades": [9.5, 7.5, 8.5]},
  {"name": "Mau","date_birth": "30-09-2000", "grades": [6.5, 9, 10]},
  {"name": "Chris", "date_birth": "10-04-2001","grades": [8.5, 10, 9.5]},
  {"name": "Marcelo", "date_birth": "15-12-2000", "grades": [7.5, 10, 5]},
  {"name": "Edward", "date_birth": "04-01-2001", "grades": [5.5, 8.8, 9.6]},
  {"name": "Rodrigo", "date_birth": "01-06-2002", "grades": [9.4, 5.6, 9.3]}
]

function calculateAverage(grades) {
  const validGrades = grades.filter(grade => grade >= 0 && grade <= 10);
  return validGrades.length ? validGrades.reduce((sum, grade) => sum + grade, 0) / validGrades.length : 0;
}

function getAverageStudent(student) {
  return {
      name: student.name,
      average_grade: calculateAverage(student.grades).toFixed(2)
  };
}

function best_student(student) {
  return student.average_grade>= 9
}

function parseDate(dob) {
  const [day, month, year] = dob.split("-");
  return new Date(year, month - 1, day); // Note: month is 0-based in JavaScript Date
}

function getDateOfBirth(student) {
  return parseDate(student.date_birth);
}

const averageStudents = students.map(getAverageStudent);

const best_students = averageStudents.filter(best_student)

const studentsByAge = students.slice().sort((a, b) => getDateOfBirth(a) - getDateOfBirth(b));

let highestGrade = 0;
let studentWithHighestGrade = null;

for (const student of students){
  for (const grade of student.grades){
    if (grade > highestGrade){
      highestGrade = grade
      studentWithHighestGrade = student.name
    }
  }
}

console.log("Estudiantes con sus promedios de calificaciones:")
for (const student of averageStudents){
 console.log(`${student['name']}: ${student['average_grade']}`)
}

console.log("\nMejores Estudiantes (promedio >= 9):");
for (const student of best_students) {
  console.log(student.name);
}

console.log("\nEstudiantes ordenados desde el más joven:");
for (const student of studentsByAge) {
  console.log(`${student.name}: ${student.date_birth}`);
}

console.log(`\nLa calificacion mas alta es ${highestGrade} de ${studentWithHighestGrade}`)