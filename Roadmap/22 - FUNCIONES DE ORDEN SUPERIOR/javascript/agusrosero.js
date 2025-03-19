/*
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 */
const numbers = [1, 2, 3, 4, 5];

const double = (num) => num * 2;

const doubledNumbers = numbers.map(double);

console.log(doubledNumbers);

/* DIFICULTAD EXTRA (opcional):
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
const estudiantes = [
  {
    nombre: "Hernan",
    fechaNacimiento: "2000-03-08",
    notas: [7, 8, 9, 8, 7, 9, 8],
  },
  {
    nombre: "Agustin",
    fechaNacimiento: "2000-08-03",
    notas: [7, 8, 9, 8, 7, 9, 8],
  },
  {
    nombre: "Juan",
    fechaNacimiento: "1999-02-01",
    notas: [9, 9, 9, 9, 9, 9, 9],
  },
  {
    nombre: "María",
    fechaNacimiento: "2001-01-15",
    notas: [9.5, 10, 8.5, 10],
  },
];

// Promedio calificaciones
const calcularPromedio = (notas) => {
  const suma = notas.reduce((acc, nota) => acc + nota, 0);
  return suma / notas.length;
};

const promedios = estudiantes.map((estudiante) =>
  calcularPromedio(estudiante.notas)
);

const promedioGeneral =
  promedios.reduce((acc, promedio) => acc + promedio, 0) / promedios.length;

console.log(promedioGeneral);

// Filtrar estudiantes con promedio mayor o igual a 9
const mejoresEstudiantes = estudiantes
  .filter((estudiante) => calcularPromedio(estudiante.notas) >= 9)
  .map((estudiante) => estudiante.nombre);

console.log(mejoresEstudiantes);

// Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
const convertirFecha = (fecha) => new Date(fecha).getTime();

const estudiantesOrdenados = estudiantes.sort(
  (a, b) =>
    convertirFecha(b.fechaNacimiento) - convertirFecha(a.fechaNacimiento)
);

console.log(estudiantesOrdenados);

// Mayor calificación: Obtiene la calificación más alta de entre todas las de los alumnos.
const todasLasNotas = estudiantes.flatMap((estudiante) => estudiante.notas);

const mayorCalificacion = todasLasNotas.reduce(
  (max, nota) => Math.max(max, nota),
  -Infinity
);

console.log(mayorCalificacion);

// Una calificación debe estar comprendida entre 0 y 10 (admite decimales)
const lasNotas = estudiantes
  .flatMap((estudiante) => estudiante.notas)
  .filter((nota) => nota >= 0 && nota <= 10);

const calificacion = lasNotas.reduce(
  (max, nota) => Math.max(max, nota),
  -Infinity
);

console.log(calificacion);
