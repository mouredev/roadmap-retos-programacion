/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

// Ejemplos de estructuras de datos

// Arrays
const arrayEjemplo: number[] = [1, 2, 3, 4, 5];
console.log("Array original:", arrayEjemplo);

// Inserción
arrayEjemplo.push(6);
console.log("Array después de la inserción:", arrayEjemplo);

// Borrado
arrayEjemplo.pop();
console.log("Array después del borrado:", arrayEjemplo);

// Actualización
arrayEjemplo[0] = 10;
console.log("Array después de la actualización:", arrayEjemplo);

// Ordenación
const arrayOrdenado: number[] = [...arrayEjemplo].sort();
console.log("Array ordenado:", arrayOrdenado);

// Objetos
interface ObjetoEjemplo {
  nombre: string;
  edad: number;
  ciudad: string;
}

const objetoEjemplo: ObjetoEjemplo = { nombre: "Juan", edad: 25, ciudad: "Barcelona" };
console.log("Objeto original:", objetoEjemplo);

// Inserción/Actualización
objetoEjemplo.profesion = "Ingeniero";
console.log("Objeto después de la inserción/actualización:", objetoEjemplo);

// Borrado
delete objetoEjemplo.edad;
console.log("Objeto después del borrado:", objetoEjemplo);

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
