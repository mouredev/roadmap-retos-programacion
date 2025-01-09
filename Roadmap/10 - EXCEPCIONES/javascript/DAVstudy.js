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

// Try - Catch - Finally - Throw

try {
    // El bloque try intentara ejecutar al logica
    // En este caso llamo a una funcion que no existe,
    callFunction()
} catch (error) {
    // el bloque Catcht captura el error para que el codigo pueda seguir ejecutandose fuera de este bloque
    console.log(error.message);
    
} finally {
    console.log("Codigo que se ejecuta siempre");
    
}

// Con Throw podemos generar los tipos de error como tambien alguno de tipo personalizado

try {
    throw new Error("Error del tipo 'Error'")
} catch (error) {
    console.log(error.message);
}

// Crear un error personalizado
const gifts = {
    toys: ["playstation 5", "pelota", "mochila"],
    //books : ["Harry potter", "Percy Jackson", "Codigo Limpio"],
    sport: ["shorts", "pesas", "cuerda de saltar"],
  };
  
  class CategoryNotFound extends Error {
    constructor(message) {
      super(message);
    }
  }
  
  // 5. Lanza una excepción personalizada.
  if (!("books" in gifts)) {
    try {
      throw new CategoryNotFound(
        "Error: No existe la categoria libros en los regalos"
      );
    } catch (error) {
      console.log(error.message); 
    }
  }

/*
  * Crea una función que sea capaz de procesar parámetros, pero que también
  * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
  * corresponderse con un tipo de excepción creada por nosotros de manera
  * personalizada, y debe ser lanzada de manera manual) en caso de error.
  * - Captura todas las excepciones desde el lugar donde llamas a la función.
  * - Imprime el tipo de error.
  * - Imprime si no se ha producido ningún error.
  * - Imprime que la ejecución ha finalizado. 
*/

// Excepción personalizada
class CustomError extends Error {
  constructor(message) {
    super(message);
    this.name = "CustomError";
  }
}

// Función que procesa parámetros y lanza excepciones
function paramProcess(param) {
  if (param === null || param === undefined) {
    throw new TypeError("El parámetro no puede ser null o undefined");
  }

  if (typeof param !== "number") {
    throw new CustomError("El parámetro debe ser un número");
  }

  if (param < 0) {
    throw new RangeError("El parámetro no puede ser negativo");
  }

  // Proceso normal si no hay errores
  return `El parámetro procesado es: ${param}`;
}

// Llamada a la función y manejo de excepciones
try {
  console.log(paramProcess(-1)); // Cambia este valor para probar diferentes casos
  console.log("No se ha producido ningún error.");
} catch (error) {
  if (error instanceof CustomError) {
    console.error(`Error personalizado: ${error.message}`);
  } else if (error instanceof TypeError) {
    console.error(`Error de tipo: ${error.message}`);
  } else if (error instanceof RangeError) {
    console.error(`Error de rango: ${error.message}`);
  } else {
    console.error(`Error desconocido: ${error.message}`);
  }
} finally {
  console.log("La ejecución ha finalizado.");
}