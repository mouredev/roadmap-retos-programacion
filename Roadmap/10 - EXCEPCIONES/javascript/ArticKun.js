

// ⚡ EXCEPCIONES =====================

/*

En JavaScript, puedes manejar errores o excepciones 
utilizando bloques try, catch, y finally.
El Throw permite personalizar un error 
si se lanza como un tipo error se usa:  throw new Error(')

*/

try {
  // Intenta ejecutar el código que podría lanzar un error
    let resultado = 10 / 0; // Intenta dividir por cero
    console.log(resultado); // Esto no se ejecutará si se lanza un error
  } catch (error) {
  // Captura cualquier error que ocurra en el bloque try
    console.error('Se ha producido un error:', error);
  } finally {
  // Este bloque se ejecutará siempre, ya sea que haya ocurrido un error o no
    console.log('El bloque try-catch ha terminado de ejecutarse.');
  }
  
//Salida : infinity 
//El bloque try-catch ha terminado de ejecutarse.

/*
  
  ⚡ En este ejemplo, si intentas dividir 10 por 0, se lanzará un 
  error de división por cero. Este error será capturado por el bloque 
  catch, donde puedes manejarlo adecuadamente. Además, el bloque finally 
  se ejecutará independientemente de si se produce un error o no, lo que 
  te permite realizar tareas de limpieza o finalización de manera consistente.

*/

/*
⚡ Si ves "Infinity" en la consola cuando divides 10 por 0 en JavaScript, 
eso significa que el resultado de la operación es infinito. En JavaScript, 
dividir un número finito por cero resulta en un valor especial llamado 
"Infinity". No se produce un error en este caso, sino que JavaScript maneja 
la situación devolviendo este valor especial.

Por lo tanto, si estás intentando capturar un error cuando divides por cero,
debes tener en cuenta que JavaScript no lanzará una excepción en este caso. 
Si deseas manejar explícitamente la división por cero como un error, puedes 
hacerlo mediante una condición antes de realizar la operación de división

 */

try {
    let divisor = 0;
    if (divisor === 0) {
      throw new Error('División por cero no permitida');
    }
    let resultado = 10 / divisor;
    console.log(resultado);
  } catch (error) {
    console.error('Se ha producido un error:', error);
  } finally {
    console.log('El bloque try-catch ha terminado de ejecutarse.');
  }

  //Con esta modificación, si el divisor es 0, se lanzará una excepción 
  //que puede ser capturada por el bloque catch.


  /*

  ⚡ DIFICULTAD EXTRA (opcional) =========================================

     Crea una función que sea capaz de procesar parámetros, pero que también
     pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
     corresponderse con un tipo de excepción creada por nosotros de manera
     personalizada, y debe ser lanzada de manera manual) en caso de error.
     - Captura todas las excepciones desde el lugar donde llamas a la función.
     - Imprime el tipo de error.
     - Imprime si no se ha producido ningún error.
     - Imprime que la ejecución ha finalizado.

  */


     function procesarParametros(param1, param2) {
        try {
          // Verificamos que se pasen al menos dos parámetros
          if (arguments.length < 2) {
            throw 'Error: Se requieren al menos dos parámetros';
          }
      
          // Procesamos los parámetros
          if (typeof param1 !== 'number' || typeof param2 !== 'number') {
            throw 'TypeError: Ambos parámetros deben ser números';
          }
      
          if (param1 < 0 || param2 < 0) {
            throw 'RangeError: Los parámetros no pueden ser números negativos';
          }
      
          // Si no se ha producido ningún error
          console.log('Los parámetros se han procesado correctamente.');
        } catch (error) {
          // Capturamos y manejamos las excepciones
          console.error('Se ha producido un error:', error);
        } finally {
          // Indicamos que la ejecución ha finalizado
          console.log('La ejecución ha finalizado.');
        }
      }
      
      // Llamada a la funcion
      console.log('Intento 1:');
      procesarParametros(10, 5);
      
      console.log('\nIntento 2:');
      procesarParametros(-5, 10);
      
      console.log('\nIntento 3:');
      procesarParametros('Hola', 10);
      
      console.log('\nIntento 4:');
      procesarParametros(42, 10);
      
      console.log('\nIntento 5:');
      procesarParametros(2);
      