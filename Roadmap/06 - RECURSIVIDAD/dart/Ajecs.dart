import 'dart:io';

void main() {
  stdout.write('********************* Recursividad ********************\n\n');

  void countingNumbers({int count = 100}) {
    if (count >= 0) {
      stdout.write('$count ');
      countingNumbers(count: count - 1);
    }
  }

  countingNumbers();

  stdout.write('\n\n********************* Extra ********************\n\n');

  stdout.write('¿Qué número del 1 al 20 quieres factorizar? ');

  /* 
    * El valaor int(entero) maneja 64 bits de forma local
    * 2,432,902,008,176,640,000 Es lo maximo que puede manejar un int. :O
    * Hasta 20!
    * De lo contrario al excederse devuelve un valor negativo incorrecto (cerca del 20) o cero (ej: !100).
  */

  String? input = stdin.readLineSync();
  int numberInput;
  ;
  try {
    numberInput = int.parse(input ?? '');
  } catch (error) {
    print('Por favor ingresa un número del 1 al 20');
    return;
  }

  int factorizeNum(int number) {
    if (number == 1 || number == 0) {
      return 1;
    } else if (number < 0) {
      throw ArgumentError('Los números negativos no tienen factoriales');
    }
    stdout.write('$number x ');
    return number * factorizeNum(number - 1);
  }

  print('1 -> El factorial de $numberInput es ${factorizeNum(numberInput)}');

  stdout.write('Ingrese la posición en la cadena de Fibonacci: ');

  String? fibonacciInput = stdin.readLineSync();
  int positionInput;
  ;
  try {
    positionInput = int.parse(fibonacciInput ?? '');
  } catch (error) {
    print('Por favor ingresa un valor válido');
    return;
  }

  int fibonacci(int position) {
    if (position <= 0) {
      throw ArgumentError('Los números negativos y el 0 no son válidos');
    }
    if (position == 1) return 0;
    if (position == 2) return 1;
    if (position > 18) {
      throw ArgumentError('Esta cadena de fibonacci muestra hasta la posición 18');
    }
    return fibonacci(position - 1) + fibonacci(position - 2);
    // Calcula el resultado de la función de la penúltima y suma el resultado de la antepenúltima.
     
    /* 
       Ej: 
       fibonacci(3) -> 1 + fibonacci(2) -> 1 = fibonacci(4) -> 2 
    */ 

    // Es por esto el motivo de la recursividad, y no solo declarar el valor position.
  }
  
  // 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597 ...

  print(
    'La $positionInput° posición de la cadena es el número ${fibonacci(positionInput)}',
  );

}
