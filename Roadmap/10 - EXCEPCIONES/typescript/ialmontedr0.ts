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

// Ejercicio: Manejo de excepciones en Typescript
try {
  // Código que podría generar una excepción
  let arreglo: number[] = [1, 2, 3, 4]; // Aquí podría haber un error de tipo de dato o índice fuera del rango
  let i: number = 3; // Aquí podría haber un error de índice fuera del rango

  if (!arreglo[i] || arreglo[i] < 0) {
    // Generará un error de índice fuera del rango
    throw new Error("Indice no existe o menor que cero"); // Lanza una excepción personalizada
  } else {
    // Si no hay error, muestra el valor del elemento
    console.log(arreglo[i]); // Imprime el valor del elemento
  }

  let resultado: number = 10 / 1; // Generará un error de división por cero
  if (resultado === Infinity || resultado === -Infinity) {
    // Generará un error de división por cero
    throw new Error("Division por cero"); // Lanza una excepción personalizada
  }
  console.log(resultado); // Imprime el resultado
} catch (error) {
  // Captura y muestra el error
  console.error("Se produjo un error:", error); // Imprime el error
}

// Ejercicio: Manejo de excepciones en Typescript (difícultad extra)

// Definimos las excepciones personalizadas
class ErrorIndice extends Error {
  constructor(message?: string) {
    super(message);
    this.name = "IndiceError";
    this.message =
      "La longitud de los parametros debe ser al menos de 3 indices";
  }
}

// Definimos la excepcion personalizada
class ErrorDivisionPorCero extends Error {
  constructor(message?: string) {
    super(message);
    this.name = "DivisionPorCeroError";
    this.message = "El segundo elemento de la lista no puede ser un cero";
  }
}

// Funcion que procesa los parametros
const procesarParametros = (parametros: number[]): void => {
  // Validaciones y procesos...
  if (parametros.length < 3) {
    throw new ErrorIndice(); // Lanza una excepcion personalizada
  } else if (parametros[1] === 0) {
    throw new ErrorDivisionPorCero();
  } else {
    console.log("No se produjeron errores");
  }

  // Imprimimos los valores de los parámetros
  console.log(parametros[2]);
  console.log(parametros[0] / parametros[1]); // Suma los dos primeros parámetros y muestra el resultado
  console.log(parametros[2] + 5);
};

// LLamar a la funcion
try {
  procesarParametros([1, 2, 3, 4]);
} catch (error) {
  if (error instanceof ErrorIndice) {
    console.log("Se ha producido un error", error.message);
  } else if (error instanceof ErrorDivisionPorCero) {
    console.log("Se produjo un error", error.message);
  } else if (error instanceof TypeError) {
    console.log("Se ha producido un error inesperado", error.message);
  } else if (error instanceof Error) {
    console.error("Se ha producido un error de tipo: " + error.message);
  }
} finally {
  console.log("El programa finaliza sin detenerse");
}
