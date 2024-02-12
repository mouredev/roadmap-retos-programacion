//#02 --- FUNCIONES Y ALCANCE//

/*
*recordatorio , el lenguaje arduino esta hecho para usarlo con las placas del
*mismo nombre y para probar este codigo se requiere utilizar un arduino para el
*ensendido y apagado de la led del pin 13 recomendado probar los codigos
*en el IDE propio de arduino , para ver los resultados se utiliza el ,
*monitor seria
*/

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


// Declaración de una variable global 'led' que representa el pin 13.
int led = 13;

void setup() {
  // Inicialización de la comunicación serial a 9600 bps.
  Serial.begin(9600);

  // Llamada a la función 'holaMundo' y muestra un divisor antes y después de la llamada.
  printDivider("Hola Mundo");
  holaMundo();

  // Llamada a la función 'Saludo', muestra un divisor y luego imprime el resultado.
  printDivider("Saludo");
  String saludo = Saludo();
  Serial.println(saludo);

  // Llamada a la función 'suma', muestra un divisor y luego imprime el resultado.
  printDivider("Suma");
  suma(5, 3);

  // Llamada a la función 'resta', muestra un divisor y luego imprime el resultado.
  printDivider("Resta");
  int resultadoResta = resta(8, 3);
  Serial.println(resultadoResta);

  // Llamada a la función 'funcionesDelLenguaje', muestra un divisor y realiza operaciones con el lenguaje Arduino.
  printDivider("Funciones del Lenguaje");
  funcionesDelLenguaje();

  // Llamada a la función 'ensendidoApagado', muestra un divisor y realiza un ejemplo de encendido y apagado.
  printDivider("Encendido y Apagado");
  ensendidoApagado();

  // Llamada a la función 'printNumbers', muestra un divisor y realiza la lógica descrita en los comentarios.
  printDivider("Print Numbers");
  printNumbers("Fizz", "Buzz");
}

void loop(){
  // El bucle principal. Puede estar vacío ya que la lógica principal se realiza en el 'setup'.
}

// Función para imprimir un divisor con el nombre de la función.
void printDivider(String functionName) {
  Serial.println("----------" + functionName + "----------");
}

// Función 'holaMundo' que imprime "Hola Mundo".
void holaMundo() {
  Serial.println("Hola Mundo");
}

// Función 'Saludo' que retorna una cadena de texto.
String Saludo() {
  return "Hola Mundo";
}

// Función 'suma' que recibe dos parámetros, los suma e imprime el resultado.
void suma(int num1, int num2) {
  Serial.println("Suma: " + String(num1 + num2));
}

// Función 'resta' que recibe dos parámetros, realiza la resta y retorna el resultado.
int resta(int num1, int num2) {
  return num1 - num2;
}

// Función 'funcionesDelLenguaje' que realiza operaciones comunes del lenguaje Arduino.
void funcionesDelLenguaje() {
  // Configuración del pin 'led' como salida.
  pinMode(led, OUTPUT);
  // Enciende el pin 'led' durante 1 segundo.
  digitalWrite(led, HIGH);
  delay(1000);
  // Apaga el pin 'led' durante 1 segundo.
  digitalWrite(led, LOW);
}

// Función 'ensendidoApagado' que realiza el ejemplo de parpadeo (blink).
void ensendidoApagado() {
  int espera = 250;

  // Ciclo que enciende y apaga el pin 'led' en un patrón.
  for (int i = 0; i < 30; i++) {
    digitalWrite(led, HIGH);
    delay(espera);
    digitalWrite(led, LOW);
    delay(espera);
  }
}

// Función 'printNumbers' que imprime números según ciertas condiciones y cuenta el número de impresiones.
void printNumbers(String text_1, String text_2) {
  int count = 0;
  // Ciclo que itera sobre los números del 1 al 100.
  for (int number = 1; number <= 100; ++number) {
    // Verifica si el número es múltiplo de 3 y/o 5 y realiza la impresión correspondiente.
    if (number % 3 == 0 && number % 5 == 0) {
      Serial.println(text_1 + text_2);
    } else if (number % 3 == 0) {
      Serial.println(text_1);
    } else if (number % 5 == 0) {
      Serial.println(text_2);
    } else {
      Serial.println(number);
      count++;
    }
  }
  // Imprime el número total de veces que se ha impreso un número.
  Serial.print("Count: ");
  Serial.println(count);
}

