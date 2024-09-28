/// URL del sitio web oficial: https://dart.dev/

/// #01 - Operadores y estructruas de control

/// Ejemplos con los tipos de operadores

import 'dart:io';

void main() {

  int a = 20;
  int b = 4;
  int c = 3;

  /// Operadores aritméticos

  print(a + b); // Suma
  b = ++a; // Incrementa el valor de "a" antes de asignárselo a "b"
  print(b);

  c = a++; //Incremente el valor de "a" después de asigárselo a "b"
  print(c);

  print(a - b); // Resta

  print(a * b); // Multiplicación

  print(a / c); // División (devuelve con parte decimal)
  
  print(a ~/ c); // División (devuelve sin la parte decimal)
  
  print(a % c); // Develve el módulo de una división

  /// Operadores lógicos
  
  bool hola = true;
  bool adios = false;

  print(!hola); // Invierte el valor del booleano

  print(adios || hola); // Operador lógico OR

  print(hola && adios); // Operador lógico AND

  /// Operadores de comparación
  
  print(10 == 10); // Igual -  Devuelve booleano
  print(10 == 9); // Igual - Devuelve booleano

  print(10 != 10); // No igual - Devuelve booleano
  print(10 != 9); // No igual - Devuelve booleano

  print(10 > 9); // Mayor que
  print(9 < 10); // Menor que
  print(10 >= 8); // Mayor o igual que
  print(7 <= 29); // Menor o igual que

  /// Operadores "type test"
  

  if (adios is bool) {
    print(adios);
  } // Es verdadero si el objeto tiene ese tipo

  /// El código siguiente es una alternativa para ello.
  /// La diferencia es que si el anterior adios no es bool, no hace nada
  /// pero si en el siguiente no es, lanza una excepción.
  (adios as bool) = adios; 
  /// Ambos ejercicios anteriores no se utilizan con esos tipos, se suele hacer
  /// con tipos creados


  if (adios is! int) {
    print(hola);
  } // Es verdadero si el objeto no tiene ese tipo

  /// Operadores de asignación
  
  String edificio = "blanco"; // asigna el valor
  print(edificio);

  /// String n ??= "negro" //Esto asigna el valor a n si esta es null, sino, se queda como está (DA ERROR)
  
  /// Operadores de "bitwise" y desplazamiento
  /// En Dart se puede trabajar con bits
  
  int valor = 0x22;
  int hexadecimal = 0x0d;

  print(valor & hexadecimal); // Operador AND
  print(valor & ~hexadecimal); // Operador AND NOT
  print(valor | hexadecimal); // Operador OR
  print(valor ^ hexadecimal); // Operador XOR

  print(valor << 4); // Desplazamiento a la izquierda
  print(valor >> 4); // Desplazamiento a la derecha

  print(hexadecimal >>> 4); // Triple desplazamiento a la derecha
  /// El triple desplazamiento a la izquierda da error
  
  /// Expresiones condicionales
  
  /// Si la condición es verdadera, entonces se ejecuta la primera expresión
  /// si es falso, se ejecuta la segunda
  (3 == 2) ? print("Es verdad") : print("Es falso"); 

  a ?? b; // Si "a" no es null, devuelve el valor de "b", sino, devuelve el de "a"

  /// Estructuras de control

  /// For loops
  
  /// Este primer ejemplo es un for loop que concatena un String
  var reto = StringBuffer("Reto 01");
  for (int i = 0; i < 10; i++) {
    reto.write("!");
  }
  print(reto);
  /// StringBuffer se utiliza para poder concatenar Strings de forma más eficiente
  /// En vez de hacer ("String" + "Otro string"), se concatena con el método write

  /// UN EJEMPLO DE LA DOCMENTACIÓN:
  /// Otro for loop que añade valores a una lista
  var lista = [];
  for (var i = 0; i < 5; i++) {
    lista.add(() => print(i));
  }

  for (final c in lista) {
    c();
  }

  /// While loops: evalúa la condición (add !=10) antes del bucle
  
  var suma= 5;
  while(suma != 10) {
    suma++;
  }
  print("El valor ha llegado a 10");

  /// Do while loops: evalúa la condición antes del bucle
  
  var resta = 10;
  do {
    resta--;
  } while (resta != 5);
  print("El valor ha llegado a 5");

  /// Break
  /// ESTÁ COMENTADO PORQUE PARALIZA TODA LA EJECUCIÓN
  /** 
  var multiplicador = 2;

  while (true) {
    if (multiplicador == 4) {
      print(multiplicador);
      break;
    }
    multiplicador * 2;
  }
  */

  /// El continue se utiliza para pasar al siguiente bucle
  /// Ejemplo inspirado en la documentación
  
  var edades = [10, 11, 50, 23, 98, 7, 76];

  for (int i = 0; i < edades.length; i++) {
    var ed = edades[i];
    if (ed > 18) {
      continue;
    }
    print("$ed: Es mayor de edad"); // El $ se utiliza para poder concatenar elementos de distintos tipos
  }
  
  /// Branching
  
  /// if statements
  
  print("¿Cuántos años tienes? ");
  int? edad = int.parse(stdin.readLineSync()!);

  if (edad >= 18) { print("Eres mayor de edad"); }
  else { print("Eres menor de edad"); }

  /// switch
  
  print("Escribe un color: "); 
  var color = stdin.readLineSync();

  switch(color) {
    case "NEGRO": {
      print("Color negrp");
    }
    case "BLANCO": {
      print("Color blanco");
    }
    default: {
      print("No es ni blanco ni negro");
    }
  }

  ///Exceptions
  
 
    int x = 12;
    int y = 0;

  ///Try - on

  try {
    var res = x ~/ y;
    print(res);

  } on UnsupportedError {
    print("Cannot dive by zero");
  }

  ///Try - catch

    try {
      var res = x ~/ y;
      print(res);

    } catch(e) {
      print(e);
    }
  
  /// Ambos juntos + finally
  
  try {
      var res = x ~/ y;
      print(res);

    } on UnsupportedError {
      print("Cannot dive by zero");
    } catch(e) {
      print(e);
    } finally {
      print("Gracias :)");
    }

  /// DIFICULTAD EXTRA
  
  int limiteInferior = 10;
  int limiteSuperior  = 55;

  for (int i = limiteInferior; i <= limiteSuperior; i++) {
    if (((i == 16) || ((i % 2) != 0)) || ((i % 3) == 0) ){
      continue;
    }
    print(i);
  }
}

  
  
  
