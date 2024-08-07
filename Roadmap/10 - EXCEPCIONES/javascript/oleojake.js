/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 */

try {
	console.log(myvar);
} catch (error) {
	console.error(error);
} finally {
	console.log("La ejecución ha finalizado.");
}

/*
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

class CustomError extends Error {
  constructor(mensaje) {
    super(mensaje);
    this.name = this.constructor.name;
  }
}

function proccessNumberParam(param) {
	try {
		if (typeof param !== 'number') {
			throw new TypeError("El parámetro no puede ser undefined");
		}

		if (param < 0) {
			throw new RangeError("El parámetro no puede ser negativo");
		}

		if (param % 2 !== 0) {
			throw new CustomError("El parámetro no es un número par");
		}

		console.log("El parámetro es correcto y no se ha producido ningún error.");
	} catch (error) {
		console.error(error.constructor.name + ": " + error.message);
	} finally {
		console.log("La ejecución ha finalizado.");
	}
}

proccessNumberParam(10);
proccessNumberParam("10");
proccessNumberParam(-10);
proccessNumberParam(3);
