import 'dart:io';

// La implementación de una clase en otra solo copia su estructura no su lógica.
class BooleanParamException implements Exception {
  String message;
  BooleanParamException(this.message);
}

void main() {
  stdout.write('\n****************** Excepciones *******************\n\n');

  /*
    A diferencia de Java, todas las excepciones de Dart son excepciones no verificadas. 
    Los métodos no declaran qué excepciones pueden lanzar, y no es necesario capturar ninguna excepción.

    Dart proporciona tipos Exception y Error, así como numerosos subtipos predefinidos. 
    Por supuesto, puedes definir tus propias excepciones. Sin embargo, los programas Dart pueden lanzar 
    como excepción cualquier objeto que no sea nulo, no solo los objetos Exception y Error.
    https://dart.dev/language/error-handling

    ! La regla de oro es nunca tratar de capturar un Error en un bloque try-catch. Ya que se silencian. Siempre
    trabajar con Exceptions.
  */

  void divideNumbers(a, b) {
    // ! La división flotante (/) no da error devuelve Infinity.
    try {
      print(a ~/ b);
    } catch (error) {
      print(
        'No puedes dividir un número por cero. Su valor es infinito: $error\n',
      );
    }
  }

  divideNumbers(10, 0); // -> IntegerDivisionByZeroException

  throwErr() => throw UnimplementedError();
  // throwErr();

  // Capturar una excepción impide que se propague (a menos que la vuelvas a lanzar). Permite manejarla
  List<dynamic> items = [];
  void findItem() {
    try {
      print(items[2]);
      // Cualquier operación que supere el rango (quitar un elemento inexistente, etc.) de items de una lista
      // genera un Error del tipo RangeError con "on" se especifica que Error manejar.
    } on RangeError catch (error, stackTrace) {
      // No es lo recomendado.
      // Si no se especifica apropiadamente el tipo de error no se captura.
      print('No hay elementos en la lista: \n${error}');
      print('Stack Trace: \n$stackTrace');
    }
  }

  findItem();

  void greeting(dynamic name, dynamic place) {
    String greet = 'Hola soy $name, vivo en $place';

    if (name is bool || place is bool) {
      throw BooleanParamException('Los argumentos no pueden ser booleanos');
    }

    if (name.length > 50 || place.length > 50) {
      throw ArgumentError(
        'El argumento no debe ser mayor a 50 caracteres',
        name,
      ); // Se difine que error lanzar.
    }
    print(greet);
    // print(greet.substring(0, 50));
  }

  //  try / catch solo captura excepciones que ocurren durante la ejecución
  //  Ejemplos como greeting() o greeting(null, null) se detectan antes.

  try {
    // EL primer parametro es recibe un valor int que no acepta el getter length.
    greeting(true, '${'Ajecs' * 50}');
    // greeting(true, 'Ajecs');
    print('El programa se ejecutó sin errores');
  } on TypeError {
    print('Añade parametros válidos'); // No es lo recomendado.
  } on FormatException {
    // print(int.parse('hola')); -> FormatException
    print('Error de formato');
  } on NoSuchMethodError catch (error) {
    print(
      'Los enteros no tienen el getter "length".\n Tipo de error \x1B[1m${error.runtimeType}\x1B[0m.\n Detalles: $error',
    );
  } on BooleanParamException catch (error) {
    print(
      'Error personalizado.\nTipo de error: \x1B[1m${error.runtimeType}\x1B[0m.\nDetalles: ${error.message}',
    );
    rethrow; 
    // Con rethrow se lanza de nuevo el error en la pila y se ejecuta el catch correspondiente.
  } catch (error) {
    print('Detalles de la excepción: $error');
  } finally {
    print('La ejecución ha finalizado\n');
  }
}

/////////////////// STACK TRACE //////////////////////////////////////
/*  
  El objeto Stack Trace muestra en pantalla todos las llamadas que el programa realizo y se ejecuta por defecto al lanzar una excepción.
    * El nivel #0 indica el punto exacto donde se generó el error.
    * Los siguiente niveles forman una secuencia de "main.función" o "clase.método" que llama al anterior nivel (propagación)
    * "package:archivo" donde esta ubicado el archivo que contiene la función.
    * ":linea:columna" linea y columna en el archivo.

  Teniendo en cuenta el ejemplo el error se propaga en el nivel 3 / 4 al archivo isolate_patch
  Este gestiona la inicialización y el procesamiento de mensajes de los Isolates (hilos de ejecución del motor).
  Es decir es el encargado de iniciar el programa.
*/
