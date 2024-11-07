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

const devolverFuncion = () => {

    const sum = (num1, num2) => num1 + num2; 

    return sum;
}

const funcionDevuelta = devolverFuncion();

console.log(funcionDevuelta(1, 1));

console.log('----------DIFICULTAD EXTRA---------');

let estudiantes = [
    {
        nombre: 'Grace',
        fechaNacimiento: '27/07/1999',
        calificaciones: [10, 9, 8.5]
    },
    {
        nombre: 'Cate',
        fechaNacimiento: '12/08/1999',
        calificaciones: [9, 6]
    },
    {
        nombre: 'Valeria',
        fechaNacimiento: '24/04/2007',
        calificaciones: [9.9, 7]
    },
];

const getExpediente = (calcularPromedio, getMejoresEstudiantes, orderEstudiantesByBirth, getMayorNota) => {

    console.log('Promedios: ',calcularPromedio());
    console.log('Mejores estudiantes', getMejoresEstudiantes());
    console.log('Nacimientos', orderEstudiantesByBirth());
    console.log('Mayor nota', getMayorNota());
}

const calcularPromedio = () => {
    let promedios = {};

    estudiantes.forEach(estudiante => {
        let suma = 0;
        estudiante.calificaciones.forEach(cal => suma += cal); 
        let promedio = suma / estudiante.calificaciones.length; 

        let nombre = estudiante.nombre;
        promedios[nombre] = promedio;
    });
    
    return promedios; 
}

const getMejoresEstudiantes = () => {
    const promedios = calcularPromedio();
    
    const mejoresEstudiantes = Object.entries(promedios).filter(([nombre, promedio]) => promedio > 9);
    const resultado = Object.fromEntries(mejoresEstudiantes);
    
    return resultado;
}

const orderEstudiantesByBirth = () => {

    return estudiantes.sort((a, b) => new Date(a.fechaNacimiento) - new Date(b.fechaNacimiento));
}

const getMayorNota = () => {

    return Math.max(...estudiantes.flatMap(estudiante => estudiante.calificaciones))
}

getExpediente(calcularPromedio, getMejoresEstudiantes, orderEstudiantesByBirth, getMayorNota);