/*
  * EJERCICIO:
  * Explora el concepto de manejo de excepciones según tu lenguaje.
  * Fuerza un error en tu código, captura el error, imprime dicho error
  * y evita que el programa se detenga de manera inesperada.
  * Prueba a dividir "10/0" o acceder a un índice no existente
  * de un listado para intentar provocar un error.
*/

try {
  console.log(number[3])
} catch (err) {
  console.error(err)
}

console.log(`Fuera de la exepción`)


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

class MyError extends Error {
  constructor(message: string) {
    super(message)
    this.name = this.constructor.name
  }
}

function process(param1: number): void {
  try {
    if (typeof param1 === 'string') {
      throw new TypeError('El tipo de dato no puede ser un string')
    }

    if (param1 > 10) {
      throw new RangeError('El numero no puede ser mayor que 10')
    }

    if (param1 === 7) {
      throw new MyError('El numero no ouede ser igual a 7')
    }

    console.log('No se han producido errores')
  } catch (error) {
    console.error('Tipo de error:', error.constructor.name)
    console.error('Mensaje de error:', error.message)
  } finally {
    console.log('la ejecución ha finalizado')
  }
}

process(7)