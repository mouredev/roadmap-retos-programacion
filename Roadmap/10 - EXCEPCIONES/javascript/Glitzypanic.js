/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
 */

// Función para dividir dos números
function dividir() {
  try {
    let divisor = 0;
    if (divisor === 0) {
      throw new Error("No se puede dividir por cero");
    }
    let resultado = 10 / divisor;
    console.log(`El resultado es: ${resultado}`);
  } catch (Error) {
    console.log("Se produjo un error:", Error.message);
  }
}

class ExcepcionPersonalizada extends Error {
  constructor(message) {
    super(message);
    this.name = "Custom Error: ";
  }
}

// Función para registrar un usuario con excepciones
function user(name, age) {
  if (name === "") {
    throw new Error("El nombre no puede estar vacío");
  } else if (age < 18) {
    throw new TypeError("Debe ser mayor de edad");
  } else if (age > 100) {
    throw new ExcepcionPersonalizada("Debe ser menor de 100");
  } else {
    console.log("Usuario registrado correctamente");
  }
}

try {
  user("Jose", 25);
} catch (e) {
  console.log(`${e.name} ${e.message}`);
} finally {
  console.log("La ejecucion ha finalizado.");
}
