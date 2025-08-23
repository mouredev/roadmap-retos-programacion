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

/// 1. [Manejo de excepciones]:
void exceptionExample1() {
  try {
    int tryThisDivision = 10 ~/ 0; // Error
    print('10 ~/ 0 = $tryThisDivision');
  } catch (e) {
    print('Exception details:\n $e');
  }
}

void exceptionExample2() {
  try {
    List<dynamic> myList = [0, 1, 2];
    print('${myList[3]}'); // Error
  } catch (e) {
    print('Exception details:\n $e');
  }
}

/// 2. [DIFICULTAD EXTRA]:
class StringTypeError implements Exception {
  final String message;

  StringTypeError([this.message = 'Must not be String']);
  
  @override
  String toString() => 'StringTypeError: $message';
}

void processParameters(List<dynamic> parameters) {
  if (parameters.first is String) {
    throw StringTypeError();  // Excepción personalizada
  }

  else if (parameters.last == null) {
    throw ArgumentError.notNull();
  }

  else if (parameters.length < 6) {
    throw RangeError.range(parameters.length, 6, null);
  }
}

void main() {
  /// 1. [Manejo de excepciones]:
  exceptionExample1();  // Captura: IntegerDivisionByZeroException
  exceptionExample2();  // Captura: RangeError (length) ...

  /// 2. [DIFICULTAD EXTRA]:
  bool noError = false;
  try {
    // processParameters(['1', 2, 3, 4, null]); // Lista con todos los errores
    processParameters([1, 2, 3, 4, null, 'hello']); // Lista sin errores
    noError = true;
  } on StringTypeError catch (e) {
    print('parameters.first no debe ser String:\n $e');
  } on RangeError catch (e) {
    print('parameters.length no es mayor o igual a 6:\n $e');
  } on Exception catch (e) {
    print('parameters.last no debe ser null:\n $e');
  } on ArgumentError catch (e) {
    print('Un error inesperado: $e');
  } finally {
    if (noError) print('¡No se ha producido ningún error!');
    print('¡Programa finalizado sin interrupciones!');
  }
}
