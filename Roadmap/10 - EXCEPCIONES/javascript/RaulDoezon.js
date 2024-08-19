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

console.log("+++++++++ EJERCICIO +++++++++");

try {
  const arreglo = [1, 2, 3];
  const division = 10 / 0;
  variable;

  console.log("En JavaScript, al acceder a un índice inexistente no se le considera como un error:");
  console.log(arreglo[3]);
  console.log("Tampoco al realizar la división de un número entre cero:");
  console.log(division);
  console.log(variable);
} catch (error) {
  console.log(`Se presentó el error: ${error}`);
}

console.log("+++++++++ DIFICULTAD EXTRA +++++++++");

function personalInformation(name, age) {
  try {
    if (isNaN(name)) {
      console.log(`Mi nombre es ${name}.`);
    } else {
      nameMessage;
    }

    if (isNaN(age)) {
      throw new Error("El valor ingresado para la edad no es un número.");
    } else {
      if (age > 17) {
        console.log(`Tengo ${age} años y soy mayor de edad`);
      } else {
        age.toUppercase();
      }
    }

    console.log(`¡No se produjo ningún error durante la ejecución!`);
  } catch (error) {
    console.log(`Se presentó el siguiente problema: ${error}`);
  } finally {
    console.log("--------- La ejecución ha finalizado ---------");
  }
}

personalInformation();
