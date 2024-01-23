/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */


// Ejemplo 1: Funciones básicas

// Función sin párametros ni retorno
void funcionSinParametrosNiRetorno() {
  print("Esta función no tiene parámetros ni retorno");
}

//Función con parametros y sin retorno
int funcionConParametrosYRetorno(int a, int b) {
  return a + b;
}

void funcionConParametros(String nombre, int edad) {
  print("Nombre: $nombre, Edad: $edad");
}

 //Función con un parámetro nominal y sin retorno
void funcionParametroNominal({required String nombre}) {
  print('¡Hola, $nombre!');
}

// Ejemplo 2: Funciones dentro de funciones
void funcionExterna() {
  void funcionInterna() {
    print("Esta es una función interna");
  }

  funcionInterna();
  print('Función externa');
}

// Ejemplo 3: Uso de funciones ya creadas en Dart
void ejemploFuncionDart() {
  print("El cuadrado de 5 es: ${square(5)}");
}

int square(int num) {
  return num * num;
}

// Ejemplo 4: Variable LOCAL y GLOBAL
int variableGlobal = 10;

void funcionConVariableLocal() {
  int variableLocal = 5;
  print("Variable Local: $variableLocal, Variable Global: $variableGlobal");
}

// Ejemplo 5: Prueba de conceptos
void main() {
  print("Ejemplo 1:");
  funcionSinParametrosNiRetorno();
  
  print("Resultado de la función con parámetros y retorno: ${funcionConParametrosYRetorno(3, 7)}");
  
  funcionConParametros("Juan", 25);

  //Función con un parámetro nominal y sin retorno
  funcionParametroNominal(nombre: 'Angel');

  print("\nEjemplo 2:");
  funcionExterna();

  print("\nEjemplo 3:");
  ejemploFuncionDart();

  print("\nEjemplo 4:");
  funcionConVariableLocal();
  // Variable local no accesible fuera de la función
  // print("Variable Local fuera de la función: $variableLocal");

  print("\nEjemplo 6 (Dificultad Extra):");
  int resultado = funcionDificultadExtra("Fizz", "Buzz");
  print("La función se ejecutó $resultado veces.");
}

// Ejemplo 6 (Dificultad Extra): Función con parámetros de texto y retorno de número
int funcionDificultadExtra(String texto1, String texto2) {
  int conteo = 0;

  for (int i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      print("$i $texto1 $texto2");
    } else if (i % 3 == 0) {
      print("$i $texto1");
    } else if (i % 5 == 0) {
      print("$i $texto2");
    } else {
      print("$i");
    }
    conteo++;
  }

  return conteo;
}
