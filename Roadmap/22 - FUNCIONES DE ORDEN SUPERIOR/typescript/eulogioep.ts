// Interfaces para definir la estructura de datos
interface EstudianteInfo {
  nombre: string;
  fechaNacimiento: Date;
  calificaciones: number[];
}

interface PromedioEstudiante {
  nombre: string;
  promedio: number;
}

interface EstudianteEdad {
  nombre: string;
  fechaNacimiento: string;
}

// Clase Estudiante para manejar la información de cada alumno
class Estudiante implements EstudianteInfo {
  readonly nombre: string;
  readonly fechaNacimiento: Date;
  readonly calificaciones: number[];

  constructor(
    nombre: string,
    fechaNacimiento: string,
    calificaciones: number[]
  ) {
    this.nombre = nombre;
    this.fechaNacimiento = new Date(fechaNacimiento);
    // Validamos que las calificaciones estén entre 0 y 10
    this.calificaciones = calificaciones.filter(
      (calif) => calif >= 0 && calif <= 10
    );
  }
}

// Datos de ejemplo
const estudiantes: Estudiante[] = [
  new Estudiante("Ana García", "2000-05-15", [9.5, 8.7, 9.2, 9.8]),
  new Estudiante("Carlos Pérez", "1999-03-20", [7.5, 8.0, 6.5, 7.8]),
  new Estudiante("María López", "2001-08-10", [9.0, 9.5, 9.3, 9.7]),
];

// Funciones auxiliares
const calcularPromedio = (calificaciones: number[]): number => {
  return (
    calificaciones.reduce((acc, curr) => acc + curr, 0) / calificaciones.length
  );
};

// 1. Obtener lista de estudiantes con sus promedios
const obtenerPromedios = (estudiantes: Estudiante[]): PromedioEstudiante[] => {
  return estudiantes.map((estudiante) => ({
    nombre: estudiante.nombre,
    promedio: calcularPromedio(estudiante.calificaciones),
  }));
};

// 2. Obtener mejores estudiantes (promedio >= 9)
const obtenerMejoresEstudiantes = (estudiantes: Estudiante[]): string[] => {
  return estudiantes
    .filter((estudiante) => calcularPromedio(estudiante.calificaciones) >= 9)
    .map((estudiante) => estudiante.nombre);
};

// 3. Obtener lista ordenada por fecha de nacimiento (más joven primero)
const ordenarPorEdad = (estudiantes: Estudiante[]): EstudianteEdad[] => {
  return [...estudiantes]
    .sort((a, b) => b.fechaNacimiento.getTime() - a.fechaNacimiento.getTime())
    .map((estudiante) => ({
      nombre: estudiante.nombre,
      fechaNacimiento: estudiante.fechaNacimiento.toISOString().split("T")[0],
    }));
};

// 4. Obtener la calificación más alta de todos los estudiantes
const obtenerMayorCalificacion = (estudiantes: Estudiante[]): number => {
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

// Ejemplos adicionales de funciones de orden superior en TypeScript
console.log("\nEjemplos adicionales de funciones de orden superior:");

// Ejemplo 1: función que retorna otra función (closure) con tipos
const multiplicadorPor = (factor: number): ((numero: number) => number) => {
  return (numero: number): number => numero * factor;
};
const multiplicarPor2 = multiplicadorPor(2);
console.log("Multiplicar 4 por 2:", multiplicarPor2(4)); // Output: 8

// Ejemplo 2: función que recibe otra función como parámetro
const aplicarOperacion = <T, U>(
  valores: T[],
  operacion: (valor: T) => U
): U[] => valores.map(operacion);

const duplicar = (numero: number): number => numero * 2;
console.log("Duplicar números [1,2,3]:", aplicarOperacion([1, 2, 3], duplicar)); // Output: [2,4,6]

// Ejemplo 3: composición de funciones con tipos genéricos
const componerFunciones = <T, U, V>(
  f: (x: U) => V,
  g: (x: T) => U
): ((x: T) => V) => {
  return (x: T): V => f(g(x));
};

const sumar1 = (x: number): number => x + 1;
const duplicarYSumar1 = componerFunciones(sumar1, duplicar);
console.log("Duplicar 5 y sumar 1:", duplicarYSumar1(5)); // Output: 11

// Ejemplo 4: Función de orden superior con tipos union
type Operacion = "suma" | "resta" | "multiplicacion" | "division";

const crearCalculadora = (
  operacion: Operacion
): ((a: number, b: number) => number) => {
  switch (operacion) {
    case "suma":
      return (a, b) => a + b;
    case "resta":
      return (a, b) => a - b;
    case "multiplicacion":
      return (a, b) => a * b;
    case "division":
      return (a, b) => (b !== 0 ? a / b : NaN);
  }
};

const calculadoraSuma = crearCalculadora("suma");
console.log("Suma de 5 + 3:", calculadoraSuma(5, 3)); // Output: 8
