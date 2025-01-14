/*
  EJERCICIO:
  Explora el concepto de funciones de orden superior en tu lenguaje 
  creando ejemplos simples (a tu elección) que muestren su funcionamiento.
*/

console.log("+++++++++ FUNCIÓN DE ORDEN SUPERIOR QUE TOMA UN CALLBACK COMO ARGUMENTO +++++++++");

const higherOrderFunction = (callback) => {
  const message = "¡Hola, soy una función de orden superior!";

  callback(message);
}

higherOrderFunction(console.log);

console.log("\n+++++++++ DEVOLVER UNA FUNCIÓN DESDE OTRA FUNCIÓN +++++++++");

const callMe = () => console.log;

callMe()("Hola, soy una función que devuelve otra función; en este caso, un console.log()");

/*
  DIFICULTAD EXTRA (opcional):
  Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
  lista de calificaciones), utiliza funciones de orden superior para 
  realizar las siguientes operaciones de procesamiento y análisis:
  - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
    y promedio de sus calificaciones.
  - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
    que tienen calificaciones con un 9 o más de promedio.
  - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
  - Mayor calificación: Obtiene la calificación más alta de entre todas las
    de los alumnos.
  - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
*/

console.log("\n+++++++++ LISTA DE ESTUDIANTES +++++++++");

const students = [
  {
    name: "Pedro",
    birthday: "01/01/1990",
    ratings: [9.1, 8.4, 9, 9.8, 9.9, 8.2],
  },
  {
    name: "Juan",
    birthday: "02/02/1993",
    ratings: [6, 5.6, 7.8, 9.2, 9.8, 9.7],
  },
  {
    name: "Santiago",
    birthday: "03/03/1992",
    ratings: [9, 8.1, 8.4, 6.8, 7.7, 7.5],
  },
  {
    name: "Mateo",
    birthday: "04/04/1991",
    ratings: [5.1, 5.7, 6, 9, 9.4, 8.5],
  },
  {
    name: "Pablo",
    birthday: "05/05/1994",
    ratings: [9, 9.2, 9.4, 9.8, 9.9, 10],
  },
];

function average(data) {
  const initialAverage = 0;
  const sumOfGrades = data.ratings.reduce((accumulator, currentValue) => accumulator + currentValue, initialAverage);
  return sumOfGrades / (data.ratings.length);
}

const allStudents = () => students.map((student) => console.log(`- Nombre: ${student.name}. Promedio: ${average(student)}.`));

const sortByBirthDay = () => {
  const sorting = students.slice().sort((a, b) => {
    const birthDayA = new Date(a.birthday);
    const birthDayB = new Date(b.birthday);

    return birthDayB - birthDayA;
  });

  sorting.map((student) => console.log(`- Nombre: ${student.name}. Fecha de nacimiento: ${student.birthday}`));
}

const bestAverages = () => {
  students.map((student) => {
    if (average(student) >= 9) {
      console.log(`- ${student.name}.`);
    }
  });
}

const bestGrade = () => {
  console.log(Math.max(...students.map((student) => Math.max(...student['ratings']))));
}

console.log("Listado:");
allStudents();

console.log("\nEstudiantes con un promedio de 9 o superior:");
bestAverages();

console.log("\nEstudiantes ordenados de menor a mayor edad:");
sortByBirthDay();

console.log("\nLa calificación más alta:");
bestGrade();
