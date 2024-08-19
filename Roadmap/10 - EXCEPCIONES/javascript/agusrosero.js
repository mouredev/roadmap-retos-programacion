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

// EJERCICIO:
function miError() {
  try {
    console.log(10 / 0);
  } catch (err) {
    console.log(err);
  } finally {
    console.log("Fin de la ejecucion...");
  }
}

miError();

// DIFICULTAD EXTRA:
class ErrorPersonalizado extends Error {
  constructor(message) {
    super(message);
    this.name = "MiError";
  }
}

function procesarParametros(param1) {
  try {
    if (typeof param1 !== "number") {
      throw new TypeError("El dato debe ser un número");
    } else if (param1 < 0) {
      throw new RangeError("El dato debe ser mayor a 0");
    } else if (param1 === 0) {
      throw new ErrorPersonalizado("El dato no puede ser 0");
    }
  } catch (error) {
    console.log(error);
  } finally {
    console.log("Fin de la ejecucion..");
  }
}

console.log(procesarParametros(-1));
