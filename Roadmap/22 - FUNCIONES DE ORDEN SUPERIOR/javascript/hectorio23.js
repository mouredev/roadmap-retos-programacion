// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

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

// Definimos una clase para representar a un estudiante
class Student {
    constructor(name, birthdate, grades) {
        this.name = name;
        this.birthdate = birthdate;
        this.grades = grades;
    }
}

// Función para calcular el promedio de una lista de calificaciones
function average(grades) {
    if (grades.length === 0) return 0.0;
    const sum = grades.reduce((acc, grade) => acc + grade, 0);
    return sum / grades.length;
}

// Lista de estudiantes
const students = [
    new Student("Adán", "2004-06-28", [9.7, 10.0, 9.9]),
    new Student("Andy", "2006-07-17", [9.5, 9.0, 9.0]),
    new Student("Mauricer", "2004-03-15", [6.0, 7.5, 8.0]),
    new Student("David", "2005-06-30", [10.0, 9.5, 9.5])
];

// Promedio de calificaciones
console.log("Promedio de calificaciones:");
students.forEach(student => {
    const avg = average(student.grades);
    console.log(`${student.name}: ${avg.toFixed(2)}`);
});

// Mejores estudiantes
console.log("\nMejores estudiantes (promedio >= 9):");
students.forEach(student => {
    if (average(student.grades) >= 9.0) {
        console.log(student.name);
    }
});

// Ordenar estudiantes por fecha de nacimiento, de más joven a más viejo
const studentsSortedByAge = students.sort((a, b) => new Date(b.birthdate) - new Date(a.birthdate));

console.log("\nEstudiantes ordenados por nacimiento (de más joven a más viejo):");
studentsSortedByAge.forEach(student => {
    console.log(`${student.name}: ${student.birthdate}`);
});

// Mayor calificación entre todos los estudiantes
const allGrades = students.flatMap(student => student.grades);
const highestGrade = Math.max(...allGrades);

console.log(`\nMayor calificación entre todos los estudiantes: ${highestGrade}`);
