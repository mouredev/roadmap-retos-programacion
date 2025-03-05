/* 🔥 EJERCICIO:
Explora el concepto de funciones de orden superior en tu lenguaje 
creando ejemplos simples (a tu elección) que muestren su funcionamiento.
*/

// Función de orden superior: map (transforma cada elemento de un array)
const numeros = [1, 2, 3, 4, 5]
const cuadrados = numeros.map(numero => numero * numero)
console.log("Cuadrados:", cuadrados) 
// Cuadrados: (5) [1, 4, 9, 16, 25]

// Función de orden superior: filter (filtra elementos de un array)
const pares = numeros.filter(numero => numero % 2 === 0)
console.log("Números pares:", pares) 
// Números pares: (2) [2, 4]

// Función de orden superior: reduce (reduce un array a un solo valor)
const suma = numeros.reduce((acumulador, numero) => acumulador + numero, 0)
console.log("Suma total:", suma) 
// Suma total: 15

// Función de orden superior personalizada
function operarNumeros(numeros, operacion) {
    return numeros.map(operacion)
}
const dobles = operarNumeros(numeros, numero => numero * 2)
console.log("Dobles:", dobles) 
// Dobles: (5) [2, 4, 6, 8, 10]

/* 🔥 DIFICULTAD EXTRA (opcional): ------------------------------------------------------------------------------
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

const estudiantes = [
    { nombre: "Ana", fechaNacimiento: "2005-03-15", calificaciones: [8.5, 9.0, 7.5] },
    { nombre: "Luis", fechaNacimiento: "2004-07-22", calificaciones: [9.5, 8.0, 9.0] },
    { nombre: "Carlos", fechaNacimiento: "2006-01-10", calificaciones: [7.0, 6.5, 8.0] },
    { nombre: "María", fechaNacimiento: "2003-11-30", calificaciones: [10.0, 9.5, 9.0] }
]
const promedios = estudiantes.map(estudiante => ({
    nombre: estudiante.nombre,
    promedio: estudiante.calificaciones.reduce((suma, nota) => suma + nota, 0) / estudiante.calificaciones.length
}))
console.log("Promedios:", promedios)
// Promedios: (4) [{…}, {…}, {…}, {…}]
// 0 : {nombre: 'Ana', promedio: 8.333333333333334}
// 1 : {nombre: 'Luis', promedio: 8.833333333333334}
// 2 : {nombre: 'Carlos', promedio: 7.166666666666667}
// 3 : {nombre: 'María', promedio: 9.5}
// length : 4
// [[Prototype]] : Array(0)

const mejoresEstudiantes = estudiantes
    .map(estudiante => ({
        nombre: estudiante.nombre,
        promedio: estudiante.calificaciones.reduce((suma, nota) => suma + nota, 0) / estudiante.calificaciones.length
    }))
    .filter(estudiante => estudiante.promedio >= 9)
    .map(estudiante => estudiante.nombre)
console.log("Mejores estudiantes:", mejoresEstudiantes)
// ['María']

const ordenadosPorEdad = estudiantes.sort((a, b) => new Date(a.fechaNacimiento) - new Date(b.fechaNacimiento))
console.log("Ordenados por edad:", ordenadosPorEdad.map(e => e.nombre))
// (4) ['María', 'Luis', 'Ana', 'Carlos']

const mayorCalificacion = Math.max(...estudiantes.flatMap(estudiante => estudiante.calificaciones))
console.log("Mayor calificación:", mayorCalificacion)
// Mayor calificación: 10