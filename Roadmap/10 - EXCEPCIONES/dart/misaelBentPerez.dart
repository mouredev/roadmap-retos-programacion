void main(List<String> arguments) {
  List<String> heroes = ['Superman'];
  try {
    printerHerores(heroes, 1);
  } catch (e) {}

  //EXTRA!!

  printer(10, '0');
  //lanza error al pasar como valor del parametro b -> '0' o algun caracter diferente a numero
}

//Ejercicio basico
void printerHerores(List<String> heroes, int index) {
  if (heroes.isEmpty || index > (heroes.length - 1)) {
    throw Exception('Index no valido');
  } else {
    print(heroes[1]);
  }
}


//EXTRA!!

///El parametro [b] es un string que se parcea para completar la operacion matematica
void printer(int a, String b) {
  try {
    posibleError(a, b);
  } on FormatException catch (e) {
    print(e);
  } on NoSuchMethodError catch (e) {
    print('Error en el uso del metodo: $e');
  } on Exception catch (e) {
    print(e);
  } finally {
    print('Se ha finalizado el proceso');
  }
}


//Funcion muy suceptible a generar errores 
void posibleError(int a, String b) {
  if (int.tryParse(b) == null) {
    throw FormatException(
        'Al parcear en la variable -b-, el valor no coincide con un int');
  } else if (b == '0') {
    throw CustomException('No es posible hacer la division por cero (0)');
  }
  int newB = int.parse(b);
  double result = a / newB;
  print(result);
}

//Excepcion personalizada
class CustomException implements Exception {
  String message;
  CustomException(this.message);

  @override
  String toString() {
    return "CustomException: $message";
  }
}
