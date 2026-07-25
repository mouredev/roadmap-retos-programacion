/*
  * EJERCICIO:
  * Explora el concepto de funciones de orden superior en tu lenguaje
  * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
*/

const numberslist = [1,2,3,4,5]
numberslist.forEach((item) => {
  console.log(item)
})

function principal(a) {
  function add(b) {
    return a + b
  }
  return add
}

let c = principal(3)
console.log(c(3))

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

const studentsList = [
  {
    name: 'Victor',
    birthday: new Date(2002, 11, 17),
    notesList: [9.0, 8.7, 10, 9.5]
  },
  {
    name: 'Juan',
    birthday: new Date(2003, 10, 7),
    notesList: [9.0, 9.1, 9.0, 9.3]
  },
  {
    name: 'John',
    birthday: new Date(2000, 11, 21),
    notesList: [6.0, 7.0, 9.0, 9.0]
  }
]

//Promedio
const studentsWithAverage = studentsList.map(student => {
  const totalNotes = student.notesList.reduce((acc, note) => acc + note, 0)
  const average = totalNotes / student.notesList.length

  return {
    name: student.name,
    average: average.toFixed(1)
  }
})
console.log('Promedio: \n\n', studentsWithAverage)

//Mejores estudiantes
const bestStudents = studentsWithAverage.filter((item) => item.average >= 9)
console.log('\n Mejores estudiantes: \n\n',bestStudents)

//Nacimiento
const sortedStudents = studentsList.sort((a, b) => b.birthday - a.birthday)
console.log('\n Estudiantes mas jovenes: \n\n',sortedStudents)

//Calificación mas alta
const highestRating = studentsList.map(item => item.notesList).reduce((acc, val) => acc.concat(val), []).sort((a,b) => a - b)
console.log('\n Calificación mas alta: \n\n',highestRating[highestRating.length - 1])