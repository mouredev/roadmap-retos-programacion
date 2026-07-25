import 'dart:io';

void main() {
  stdout.write(
    '\n************************** Funciones básicas ***********************\n\n',
  );

  String greetingsFromDart() {
    return 'Hola a todos programando con Dart';
  }

  print(greetingsFromDart());

  void greetingsArrowSyntax() =>
      print('Hola a todos programando con Dart (función abreviada)\n');
  greetingsArrowSyntax();

  print('');

  stdout.write(
    '********************** Paremetros nombrados ***********************\n\n',
  );

  // Los parametros nombrados son opcionales por defecto pero no pueden ser nulos salvo que se añada la palabra clave required
  // lo que obliga a que se deban utilizar los argumentos requeridos.
  String namedParamsGreetings({required String name, required String greet}) {
    return ('$greet $name');
  }

  print(namedParamsGreetings(name: 'Ajecs', greet: 'Hola mi nombre es:'));
  print(
    namedParamsGreetings(
      greet: '¡Como andas che!, mi nombre es:',
      name: 'Pepito',
    ),
  );

  stdout.write(
    '\n********************** Devolver más de un valor *********************************\n\n',
  );
  // Con el fin de retornar varios valores a la vez se usa la estructura Record, equivalente a la tupla en python
  // En Dart los records son estrictamente tipados y mantienen su orden a diferencia de python .
  (String, String) multipleGreetings() => ('Primer valor', 'Segundo valor');
  // Se desestructuran los valores de la función.
  String greet1,
      greet2; // ! Las variables tienen que ser declaradas previamente ):
  (greet1, greet2) = multipleGreetings();

  print(greet1);
  print(greet2);

  stdout.write(
    '\n**************************** Funciones variádicas **************************************\n\n',
  );

  // Debido a la filosofía de Dart no existe una forma directa de añadir un numero variable de parámetros a una función.
  // Esto se soluciona pasando una lista como argumento.

  void printLangList(List<String> languageList) {
    print('Lenguajes de programación: ${languageList.join(', ')}');
    for (String language in languageList) {
      print('Programo en $language');
    }
  }

  printLangList(['Dart', 'Python', 'JavaScript', 'PHP', 'Go', 'C#']);

  stdout.write(
    '\n**************************** Funciones variádicas nombradas **************************************\n\n',
  );
  // Con el fin de obtener el mismo resultado que en python, es posible enviar un Map como parametro.
  // e imprimir la clave y el valor pasados como argumentos.

  void printPlayer(Map<String, String> playerMap) {
    playerMap.forEach((key, value) => print('$key: $value'));
  }

  printPlayer({
    'Delantero': 'Messi',
    'Mediocampista': 'McAllister',
    'Arquero': 'Martinez',
    'Defensor': 'Romero',
  });

  stdout.write(
    '********************** Función dentro de función ***********************\n\n',
  );

  void outerFunction() {
    void innerFunction() {
      print('Hola, ¿como andas?');
    }

    innerFunction();
  }

  outerFunction();

  // Se añaden parametros, uno de ellos opcional
  Function(num, [num]) basicOperation = (num value1, [num? value2]) {
    num result = value1;
    if (value2 != null) result = value1 + value2;
    return result;
  };
  String showOperations() {
    return ('El valor de la operación es: ${basicOperation(10)}' +
        '\n' +
        'El valor de la operación es: ${basicOperation(2, 3)}');
  }

  print(showOperations());

  stdout.write(
    '\n************************* Built-in functions ***********************\n\n',
  );

  // La principal función del lenguaje es main(). Que cumple la función de más alto nivel.
  // Es del tipo void, no retorna nada y recibe un parámetro de tipo List<String>.

  print('ajecs'.toUpperCase());

  stdout.write(
    '\n********************** Variables locales y globales ****************************\n\n',
  );

  String globalVar = 'variable global';

  void callingVar() {
    String localVar = 'variable local';
    print('Hola soy una $globalVar');
  }

  callingVar();

  stdout.write(
    '\n************************************ Extra *************************\n\n',
  );

  // Ejercicio "Fizz Buzz"

  int countNumbers({
    String multiple3 = 'multiplo de 3',
    String multiple5 = 'multiplo de 5',
  }) {
    Iterable<int> range = Iterable.generate(100, (i) => i + 1); // Se quita el 0 del rango
    int numberNonMultiple = 0;
    for (int value in range) {
      if (value % 3 == 0 && value % 5 == 0)
        print('$value es $multiple3 y $multiple5');
      else if (value % 3 == 0)
        print('$value es $multiple3');
      else if (value % 5 == 0)
        print('$value es $multiple5');
      else {
        print(value);
        numberNonMultiple++;
      }
    }
    print('');
    return numberNonMultiple;
  }

  print('Hay ${countNumbers()} números no multiplos de 3 y 5');
  print('');
  
}
