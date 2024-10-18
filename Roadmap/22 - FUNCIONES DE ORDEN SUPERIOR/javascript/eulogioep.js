// Clase Estudiante para manejar la información de cada alumno
class Estudiante {
  constructor(nombre, fechaNacimiento, calificaciones) {
    this.nombre = nombre;
    this.fechaNacimiento = new Date(fechaNacimiento);
    // Validamos que las calificaciones estén entre 0 y 10
    this.calificaciones = calificaciones.filter(
      (calif) => calif >= 0 && calif <= 10
    );
  }
}

// Creamos una lista de estudiantes de ejemplo
const estudiantes = [
  new Estudiante("Ana García", "2000-05-15", [9.5, 8.7, 9.2, 9.8]),
  new Estudiante("Carlos Pérez", "1999-03-20", [7.5, 8.0, 6.5, 7.8]),
  new Estudiante("María López", "2001-08-10", [9.0, 9.5, 9.3, 9.7]),
];

// Funciones auxiliares
const calcularPromedio = (calificaciones) => {
  return (
    calificaciones.reduce((acc, curr) => acc + curr, 0) / calificaciones.length
  );
};

// 1. Obtener lista de estudiantes con sus promedios
const obtenerPromedios = (estudiantes) => {
  return estudiantes.map((estudiante) => ({
    nombre: estudiante.nombre,
    promedio: calcularPromedio(estudiante.calificaciones),
  }));
};

// 2. Obtener mejores estudiantes (promedio >= 9)
const obtenerMejoresEstudiantes = (estudiantes) => {
  return estudiantes
    .filter((estudiante) => calcularPromedio(estudiante.calificaciones) >= 9)
    .map((estudiante) => estudiante.nombre);
};

// 3. Obtener lista ordenada por fecha de nacimiento (más joven primero)
const ordenarPorEdad = (estudiantes) => {
  return [...estudiantes]
    .sort((a, b) => b.fechaNacimiento - a.fechaNacimiento)
    .map((estudiante) => ({
      nombre: estudiante.nombre,
      fechaNacimiento: estudiante.fechaNacimiento.toISOString().split("T")[0],
    }));
};

// 4. Obtener la calificación más alta de todos los estudiantes
const obtenerMayorCalificacion = (estudiantes) => {
  return Math.max(
    ...estudiantes.flatMap((estudiante) => estudiante.calificaciones)
  );
};

// Mostrar resultados
console.log("1. Promedios de calificaciones:");
console.log(obtenerPromedios(estudiantes));

console.log("\n2. Mejores estudiantes (promedio >= 9):");
console.log(obtenerMejoresEstudiantes(estudiantes));

console.log("\n3. Estudiantes ordenados por edad (más joven primero):");
console.log(ordenarPorEdad(estudiantes));

console.log("\n4. Mayor calificación de todos los estudiantes:");
console.log(obtenerMayorCalificacion(estudiantes));

// Ejemplos adicionales de funciones de orden superior en JavaScript
console.log("\nEjemplos adicionales de funciones de orden superior:");

// Ejemplo 1: función que retorna otra función (closure)
const multiplicadorPor = (factor) => (numero) => numero * factor;
const multiplicarPor2 = multiplicadorPor(2);
console.log("Multiplicar 4 por 2:", multiplicarPor2(4)); // Output: 8

// Ejemplo 2: función que recibe otra función como parámetro
const aplicarOperacion = (numeros, operacion) => numeros.map(operacion);
const duplicar = (numero) => numero * 2;
console.log("Duplicar números [1,2,3]:", aplicarOperacion([1, 2, 3], duplicar)); // Output: [2,4,6]

// Ejemplo 3: composición de funciones
const componerFunciones = (f, g) => (x) => f(g(x));
const sumar1 = (x) => x + 1;
const duplicarYSumar1 = componerFunciones(sumar1, duplicar);
console.log("Duplicar 5 y sumar 1:", duplicarYSumar1(5)); // Output: 11
