/*
  Author: Teren del Agua
  GitHub: https://github.com/Teren91

  Resources: https://dart.dev/language/error-handling

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

// Excepciones personalizadas
class DivisionPorCeroException implements Exception {}

class DivisionParesInvalidaException implements Exception {}

void main() {
  try {
    errorForzado();

    print(dividir(4, 2)); //No hay error devuelve 2.0
    print(dividir(2, 3)); //Salta error personalizado


    //Aserciones -> Se deben ejecutar con el flag --enable-asserts
    //  Detienen la ejecución si no se cumple la norma.
    numberFormat(10);
    numberFormat(0);
    numberFormat(-1);
  } catch (e) {
    print(e);
  } finally {
    print('Fin del programa.');
  }
}

void errorForzado() {
  try {
    dynamic foo = true;
    print(foo++); // Runtime error
    
  } on FormatException catch (e) {
    print('Controlando error de formato: $e');
  } on NoSuchMethodError catch (e) {
    print('Controlando error de método: $e');
  } on Exception catch (e) {
    print('Cualquier otro error: $e');
  } finally {
    print('Fin del método errorForzado.');
  }
}

void numberFormat(int x) {
  assert(x.isEven, 'El número debe ser par');
  assert(x != 0, 'El número no puede ser 0');
  assert(x > 0, 'El número debe ser positivo');
}

double dividir(int x, int y) {
  if (y == 0) {
    throw DivisionPorCeroException();
  }
  if (y.isOdd) {
    throw DivisionParesInvalidaException();
  }

  return x / y;
}
