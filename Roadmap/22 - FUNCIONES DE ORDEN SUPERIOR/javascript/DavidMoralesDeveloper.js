
//  * EJERCICIO:
//  * Explora el concepto de funciones de orden superior en tu lenguaje 
//  * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
// map filter reduce....

function procesar(array, callback) {
  return array.map(callback);
}

const numeros = [1, 2, 3];
const cuadrados = procesar(numeros, x => x * 2);
console.log(cuadrados); // [2, 4, 6]

// ---------
function crearMultiplicador(factor) {
  return function(numero) {
    return numero * factor;
  };
}

const multiplicarPor3 = crearMultiplicador(3);
console.log(multiplicarPor3(5)); // 15

//  * DIFICULTAD EXTRA (opcional):
//  * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
//  * lista de calificaciones), utiliza funciones de orden superior para 
//  * realizar las siguientes operaciones de procesamiento y análisis:
//  * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
//  *   y promedio de sus calificaciones.
//  * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
//  *   que tienen calificaciones con un 9 o más de promedio.
//  * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
//  * - Mayor calificación: Obtiene la calificación más alta de entre todas las
//  *   de los alumnos.
//  * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
const estudiantes =[
    {
    nombre: "Ana García",
    fechaNacimiento: "2000-03-15",
    calificaciones: [85, 92, 78, 88, 95]
  },
  {
    nombre: "Carlos López",
    fechaNacimiento: "1999-07-22",
    calificaciones: [76, 82, 90, 85, 79]
  },
  {
    nombre: "María Rodríguez",
    fechaNacimiento: "2001-01-10",
    calificaciones: [95, 98, 92, 97, 94]
  }
]

   
// function escuela (estudiantes)  {
    
//     const nomyPro = estudiantes.map(estudiante => ({
//         "name": estudiante.nombre,
//          "promedio": estudiante.calificaciones.reduce((total, suma)=> total + suma)/estudiante.calificaciones.length
//         }) 
//     )
    
// return nomyPro
// }
// console.log(escuela(estudiantes))

const promedio = (calificaciones) => {
    return calificaciones.reduce((total, sum)=> total + sum) / calificaciones.length
}

console.log("nombre y promedio")
//nombre y promedio
const nomyprom = estudiantes.map(estudiantes => ({
    "nombre": estudiantes.nombre,
    "promedio": promedio(estudiantes.calificaciones)
}))

console.log(nomyprom)

//Mejores
// const mejores = estudiantes.map(estudiante => (
//     ( promedio(estudiante.calificaciones) > 90 ? estudiante.nombre : "" )
// ))

// console.log(mejores)
console.log("estudiantes con promedio superior a 9")

const mejores = estudiantes
    .filter(estudiante => promedio(estudiante.calificaciones) > 90)
    .map(estudiante => estudiante.nombre)

    console.log(mejores)

  //  * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
  console.log("estudiantes ordenados desde el mas joven")
  function dateDeNacimiento (fechaString) {
    const [año, mes, dia]= fechaString.split("-")
    return new Date(año,mes-1,dia)
  }

  
//   const masJoven = estudiantes.map(estudiante => dateDeNacimiento(estudiante.fechaNacimiento)).sort()
const masJoven = [...estudiantes]. sort((a,b) => {
    const fechaA = dateDeNacimiento(a.fechaNacimiento)
    const fechaB = dateDeNacimiento(b.fechaNacimiento)
    return fechaA - fechaB

})
  

  console.log(masJoven)

  console.log("mayor calificacion de cada alumno")

//   Falta el operador spread (...) para expandir el array---------

  const calidicacionMayor = Math.max(...estudiantes.map(calificanciones => Math.max(...calificanciones.calificaciones)))

  console.log(calidicacionMayor)
  