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

function exception(n){
    try{
      let res=n/0
      console.log(res)
    }catch(error){
      console.error("Ha ocurrido un error:", error.message);
    }
     finally {
    // Este bloque siempre se ejecuta, haya ocurrido un error o no
    console.log("La ejecución ha finalizado.");
  }
  }
  exception(10)
  

  // Excepción personalizada
class MiErrorPersonalizado extends Error {
    constructor(mensaje) {
      super(mensaje);
      this.name = "MiErrorPersonalizado";
    }
  }
  
  // Función que puede lanzar diferentes tipos de excepciones
  function procesar(parametro) {
    if (typeof parametro !== 'number') {
      throw new TypeError("El parámetro debe ser un número.");
    }
    if (parametro < 0) {
      throw new RangeError("El parámetro no puede ser negativo.");
    }
    if (parametro === 42) {
      throw new MiErrorPersonalizado("¡Oh, no! El parámetro es 42.");
    }
    console.log("Parámetro procesado correctamente:", parametro);
  }
  
  // Llamada a la función dentro de un bloque try-catch
  try {
    procesar("texto");  // Provoca un TypeError
    procesar(-5);       // Provoca un RangeError
    procesar(42);       // Provoca un MiErrorPersonalizado
    procesar(10);       // Se ejecuta correctamente
  } catch (error) {
    console.error("Se ha producido un error:", error.name, error.message);
  } finally {
    console.log("La ejecución ha finalizado.");
  }
  
