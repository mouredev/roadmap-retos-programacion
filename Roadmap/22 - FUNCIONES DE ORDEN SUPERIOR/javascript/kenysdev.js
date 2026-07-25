/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#22 FUNCIONES DE ORDEN SUPERIOR
---------------------------------------
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y
 * lista de calificaciones), utiliza funciones de orden superior para
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
*/
// ________________________________________________________
function arithmeticOp(func) {
    return function (x, y) {
        return func(x, y);
    };
}

function add(x, y) {
    return x + y;
}

function subtract(x, y) {
    return x - y;
}

function multiply(x, y) {
    return x * y;
}

const addition = arithmeticOp(add);
const subtraction = arithmeticOp(subtract);
const multiplication = arithmeticOp(multiply);

const rAddition = addition(2, 3);
const rSubtraction = subtraction(10, 5);
const rMultiplication = multiplication(2, 5);

console.log(`\n` +
    `Resultado de la suma:    ${rAddition} \n` +
    `Resultado de la resta:   ${rSubtraction} \n` +
    `Resultado de la multip.: ${rMultiplication}`);

// ________________________________________________________
console.log("\n----\nDIFICULTAD EXTRA\n");

const studentsList = [
    { name: "Ken", dob: "2012-04-21", grades: [9.5, 9.4, 9.3, 9.2] },
    { name: "Ben", dob: "2012-03-20", grades: [8.5, 8.4, 8.3, 8.2] },
    { name: "Ada", dob: "2012-02-19", grades: [7.5, 7.4, 7.3, 7.2] },
    { name: "Zoe", dob: "2012-01-18", grades: [9.0, 9.1, 9.0, 9.1] },
];

// Función de orden superior
function higherOrderFun(msg, printFn) {
    return function (students) {
        console.log(`\n----\n${msg}`);
        students.forEach((student) => printFn(student));
    };
}

function printGPA(student) {
    const grades = student.grades;
    const averageGrade = grades.reduce((sum, grade) => sum + grade, 0) / grades.length;
    console.log(`${student.name}: ${averageGrade.toFixed(2)}`);
}

function printTop(student) {
    const grades = student.grades;
    const average = grades.reduce((sum, grade) => sum + grade, 0) / grades.length;
    if (average >= 9) console.log(student.name);
}

function printBirth(student) {
    console.log(`${student.name}: ${student.dob}`);
}

function printHighestGrade(student) {
    const maxGrade = Math.max(...student.grades);
    console.log(`${student.name}: ${maxGrade}`);
}

const gradePointAverage = higherOrderFun("Promedio de calificaciones:", printGPA);
const topStudents = higherOrderFun("Mejores estudiantes:", printTop);
const birthOrder = higherOrderFun("Orden de nacimiento:", printBirth);
const highestGrade = higherOrderFun("Mayor calificación:", printHighestGrade);

gradePointAverage(studentsList);
topStudents(studentsList);
birthOrder(
    [...studentsList].sort((a, b) => new Date(a.dob) - new Date(b.dob))
);

highestGrade(studentsList);
