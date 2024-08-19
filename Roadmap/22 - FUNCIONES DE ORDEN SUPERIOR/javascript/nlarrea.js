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

// Funciones de orden superior -> funciones que toman una función como argumento
// o que devuelven una función como resultado

// map


function cube(x) {
    return x**3;
}


let numbers = [1, 2, 3, 4, 5];
const cubeNumbers = numbers.map(number => cube(number));
console.log(cubeNumbers);  // [1, 8, 27, 64, 125]


// filter


function even(x) {
    return x % 2 == 0;
}


const evenNumbers = numbers.filter(number => even(number));
console.log(evenNumbers);  // [2, 4]


// sorted

numbers = [1, 4, 2, 6, 9];
console.log(numbers.slice().sort());  // [1, 2, 4, 6, 9]
console.log(numbers.slice().sort((a, b) => b - a));  // [9, 6, 4, 2, 1]

const fruits = ['banana', 'apple', 'melon', 'pineapple'];
console.log(fruits.slice().sort((a, b) => a.length - b.length));  // sorts fruits based on the length of strings
// ['apple', 'melon', 'banana', 'pineapple']
console.log(fruits.slice().sort((a, b) => b.length - a.length));
// ['pineapple', 'banana', 'apple', 'melon']


// reduce

numbers = [1, 2, 3, 4, 5];
const sumOfValues = numbers.reduce((total, current) => total + current);
console.log(sumOfValues);  // 15


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

const studentsData = [
    {
        firstName: 'Brennan',
        lastName: 'Wiza',
        birthDate: '11-02-2004',
        marks: [5, 6.7, 8, 9.2, 3],
    },
    {
        firstName: 'Hilton',
        lastName: 'Schimmel',
        birthDate: '07-07-1998',
        marks: [8, 7.6, 7.8, 5.5, 9],
    },
    {
        firstName: 'Aditya',
        lastName: 'Rowe',
        birthDate: '02-05-1999',
        marks: [7.6, 8.9, 9.3, 10, 7.8],
    },
    {
        firstName: 'Estella',
        lastName: 'King',
        birthDate: '29-06-1997',
        marks: [9.6, 8.9, 9.3, 10, 7.8],
    },
];


// Average


function average(grades) {
    return Math.round(
        (
            grades.reduce((total, current) => total + current)
            / grades.length
        ) * 100
    ) / 100;
}


console.log(
    studentsData.map(student => {
        return {name: student.firstName, average: average(student.marks)}
    })
);
/*
  [{ name: 'Brennan', average: 6.38 },
  { name: 'Hilton', average: 7.58 },
  { name: 'Aditya', average: 8.72 },
  { name: 'Estella', average: 9.12 }]
 */


// Best students

console.log(
    studentsData
    .filter(student => average(student.marks) >= 9)
    .map(student => student.firstName)
)
// [ 'Estella' ]


// Birth Day

console.log(
    studentsData.slice().sort((a, b) => {
        const dateA = new Date(a.birthDate);
        const dateB = new Date(b.birthDate);
        return dateB - dateA;
    })
);


// Highest score

console.log(Math.max(...studentsData.flatMap(student => student.marks)));
// 10
