let a = 5;
let b = 0;

try {
  // Intenta ejecutar el código que podría generar un error
  let resultado = a / b; // Intentando dividir por cero
  console.log(`La división fue exitosa: ${resultado}`);
} catch (error) {
  // Captura la excepción específica y maneja el error
  console.error(`Error: ${error}`);
} finally {
  // Este bloque se ejecuta siempre, independientemente de si hubo una excepción o no
  console.log("Fin del manejo de excepciones");
}

let lista = [1, 2, 3];

try {
  // Intenta acceder a un índice no existente de una lista
  let elemento = lista[4]; // Intentando acceder a un índice no existente
  console.log(`Elemento obtenido: ${elemento}`);
} catch (error) {
  // Captura la excepción específica y maneja el error
  console.error(`Error: ${error}`);
} finally {
  // Este bloque se ejecuta siempre, independientemente de si hubo una excepción o no
  console.log("Fin del manejo de excepciones");
}

// Ejercicio extra

class MiErrorPersonalizado extends Error {
  constructor(message) {
    super(message);
    this.name = "MiErrorPersonalizado";
  }
}

function procesarParametros(parametro) {
  try {
    if (typeof parametro !== "number") {
      throw new TypeError("El parámetro debe ser un número");
    }

    if (parametro === 0) {
      throw new Error("El parámetro no puede ser cero");
    }

    if (parametro < 0) {
      throw new MiErrorPersonalizado("El parámetro no puede ser negativo");
    }

    console.log("El parámetro es válido:", parametro);
  } catch (error) {
    console.error("Tipo de error:", error.name);
    console.error("Mensaje de error:", error.message);
  } finally {
    console.log("La ejecución ha finalizado");
  }
}

try {
  procesarParametros("cadena");
  procesarParametros(0);
  procesarParametros(-5);
  procesarParametros(10);
} catch (error) {
  console.error(`Se ha producido un error fuera de la función: ${error}`);
}
