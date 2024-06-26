// ** EJERCICIO

function ordenSuperior(comprobar, funcion) {
    if (comprobar){
        funcion()
    } else {
        console.log('No hay nada que decir')
    }
}

function decirHola(){
    console.log('Hola')
}

ordenSuperior('Sí que hay algo', decirHola)

// ** DIFICULTAD EXTRA ** -------------------------------------------------------------------------------------------------------------------------------

// const estudiantes = [
//     { nombre: 'Estudiante1', fechaNacimiento: '2000-04-22', notas: [7, 8, 9, 8, 7, 9, 8] },
//     { nombre: 'Estudiante2', fechaNacimiento: '1999-08-15', notas: [6, 7, 8, 7, 8, 9, 7] },
//     { nombre: 'Estudiante3', fechaNacimiento: '2001-12-03', notas: [8, 9, 9, 8, 9, 8, 9] },
//     { nombre: 'Estudiante4', fechaNacimiento: '2002-02-27', notas: [7, 8, 7, 8, 7, 8, 7] },
//     { nombre: 'Estudiante5', fechaNacimiento: '2000-11-10', notas: [9, 8, 8, 9, 8, 8, 9] },
//     { nombre: 'Estudiante6', fechaNacimiento: '1998-05-30', notas: [6, 7, 7, 6, 7, 7, 6] }
// ];


// // Promedio calificaciones: Obtiene una lista de estudiantes por nombre y promedio de sus calificaciones.
// const obtenerPromedio = notas => notas.reduce((a, b) => a + b, 0) / notas.length;

// const promedios = estudiantes.map(estudiante => ({
//     nombre: estudiante.nombre,
//     promedio: obtenerPromedio(estudiante.notas)
// }));

// console.log("Promedios:", promedios);

// // Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes que tienen calificaciones con un 9 o más de promedio.
// const mejoresEstudiantes = promedios
//     .filter(estudiante => estudiante.promedio >= 9)
//     .map(estudiante => estudiante.nombre);

// console.log("Mejores estudiantes:", mejoresEstudiantes);

// // Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
// const estudiantesOrdenadosPorNacimiento = estudiantes
//     .slice()
//     .sort((a, b) => new Date(b.fechaNacimiento) - new Date(a.fechaNacimiento));

// console.log("Estudiantes ordenados por nacimiento (de más joven a más viejo):", estudiantesOrdenadosPorNacimiento.map(est => est.nombre));

// // Mayor calificación: Obtiene la calificación más alta de entre todas las de los alumnos.
// const mayorCalificacion = Math.max(...estudiantes.flatMap(estudiante => estudiante.notas));

// console.log("Mayor calificación:", mayorCalificacion);