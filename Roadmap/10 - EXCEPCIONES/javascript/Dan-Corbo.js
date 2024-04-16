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


/* Soluciones */


function dividir(numero1, numero2) {
  // Valida los tipos de datos
  if (typeof numero1 !== "number" || typeof numero2 !== "number") {
    throw new TypeError("Los números deben ser enteros.");
  }

  // Valida la división por cero
  if (numero2 === 0) {
    throw new Error("No se puede dividir por cero.");
  }

  // Valida si el divisor es NaN
  if (isNaN(numero2)) {
    throw new Error("El divisor no puede ser NaN.");
  }

  return numero1 / numero2;
}


try {
  // const resultado = dividir(10, "0"); // "Error de tipo de dato: Los números deben ser enteros."
  // const resultado = dividir(10, NaN); // "Error: El divisor no puede ser NaN."
  const resultado = dividir(10, 0); // "Error: No se puede dividir por cero."
  console.log("El resultado de la división es:", resultado);
} catch (error) {
  if (error instanceof TypeError) {
    console.error("Error de tipo de dato:", error.message);
  } else if (error instanceof Error) { // Captura un error genérico
    console.error("Error:", error.message);
  } else {
    console.error("Error inesperado:", error);
  }
} finally {
  console.log("Fin del programa.\n"); // "Fin del programa."
}


/* Extra - Opcional */


function discoteca(nombre, edad) {
  // Valida los tipos de datos
  if (typeof nombre !== "string" && typeof edad !== "number" || isNaN(edad)) {
    throw new Error("El nombre debe ser un string y la edad un número.");
  }
  if (typeof nombre !== "string") {
    throw new Error("El nombre debe ser un string.");
  }
  if (typeof edad !== "number" || isNaN(edad)) {
    throw new Error("La edad debe ser un número.");
  }

  // Valida los campos vacíos
  if (!nombre || !edad) {
    throw new Error("Debes completar ambos campos.");
  }

  // Valida la edad del usuario
  if (edad >= 18) {
    console.log(`${nombre} puedes ingresar. ¡Bienvenida/o!`); // "Ana puedes ingresar. ¡Bienvenida/o!"
  } else {
    throw new Error("No puedes ingresar por ser menor de edad.");
  }
}

const nombres = [23, "Ana", "Pedro", "", 0];
const edades = [15, 20, 17, 25, ""];

for (let i = 0; i < nombres.length; i++) {
  try {
    discoteca(nombres[i], edades[i]);
  } catch (error) {
    switch (error.message) {
      case "El nombre debe ser un string y la edad un número.":
        console.log("El nombre y la edad no son válidos."); // "El nombre y la edad no son válidos."
        break;
      case "El nombre debe ser un string.":
        console.log("El nombre no es válido."); // "El nombre no es válido."
        break;
      case "La edad debe ser un número.":
        console.log("La edad no es válida.");
        break;
      case "Debes completar ambos campos.":
        console.log("Debes completar los dos campos."); // "Debes completar los dos campos."
        break;
      case "No puedes ingresar por ser menor de edad.":
        console.log(nombres[i],"lo siento, no puedes ingresar por ser menor de edad."); // "Pedro lo siento, no puedes ingresar por ser menor de edad."
        break;
    }
  } finally {
    console.log("Sigan pasando por favor, las mujeres entran gratis!!!\n");
  }
}
