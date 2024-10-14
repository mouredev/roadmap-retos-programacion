//Ejercicio
try {
  connect.mongodb()
} catch(error) {
  console.log(error)
} finally {
  console.log('saliendo..')
}
console.log('hola fuera del error')

class MiErrorPersonalizado extends Error {
  constructor(mensaje) {
    super(mensaje);
    this.name = this.constructor.name;
  }
}

//Ejercicio extra
function procesarParametros(parametro) {
  try {
    // Verificar si el parámetro es un número
    if (typeof parametro !== 'number') {
      throw new TypeError('El parámetro debe ser un número');
    }

    // Verificar si el parámetro es negativo
    if (parametro < 0) {
      throw new RangeError('El parámetro no puede ser negativo');
    }

    // Lanzar una excepción personalizada manualmente
    if (parametro === 42) {
      throw new MiErrorPersonalizado('El parámetro no puede ser 42');
    }

    // Si no hay errores, imprimir el parámetro
    console.log('El parámetro es:', parametro);
    console.log('No se ha producido ningún error');

  } catch (error) {
    // Capturar y manejar todas las excepciones
    console.error('Tipo de error:', error.constructor.name);
    console.error('Mensaje de error:', error.message);
  } finally {
    // Imprimir que la ejecución ha finalizado
    console.log('La ejecución ha finalizado');
  }
}

// Ejemplo de llamada a la función con diferentes parámetros
console.log('--- Ejemplo 1 ---');
procesarParametros(10); // Sin errores
console.log('--- Ejemplo 2 ---');
procesarParametros(-5); // Lanza un RangeError
console.log('--- Ejemplo 3 ---');
procesarParametros('texto'); // Lanza un TypeError
console.log('--- Ejemplo 4 ---');
procesarParametros(42); // Lanza un MiErrorPersonalizado
