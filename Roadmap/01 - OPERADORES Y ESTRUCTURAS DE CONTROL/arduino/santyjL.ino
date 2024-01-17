//#01 OPERADORES Y ESTRUCTURAS DE CONTROL

/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

//variables - operadores del lenguaje

//aritmetica
int suma = 3 + 4;
int resta = 3 - 4;
int multiplicacion = 3 * 5;
float division = 3 / 5;
int potencia =pow(3 , 5);
float modulo = 5 % 3;

//logicos -- los true y false en la terminal se presentan como 1 para true y 0 para false
bool AND0 = true && true;
bool AND1 = true && false ;
bool AND2= false && true;
bool AND3 = false && false;

bool OR0 = true || true;
bool OR1 = true || false;
bool OR2 = false || true;
bool OR3 = false || false;

bool NOT0 = !true;
bool NOT1 = !false;

//comparacion
bool mayorQue= 3 > 5;
bool menorQue= 3 < 5;
bool igualQue= 3 == 5;  //se puede considerar de identidad
bool mayorOIgualQue = 3 >= 5;
bool menorOIgualQue = 3 <= 5 ;
bool diferenteQUE = 3 != 5; //se puede considerar de identidad

//asignacion
int num = 12;
int num1 = num += 5;
int num2 = num -= 3;
int num3 = num *= 3;
float num4 = num /=5;
int num5 = num %= 3;

//pertenencia

//en arduino no existen por el hecho de que se prioriza el rendimiento y el almacenamiento por lo cual no se suele utilizar listas o datos compuestos

//bits
int byte1 = 0b11011010;
int byte2 = 0b10101011;

byte resultadoAND = byte1 & byte2;
byte resultadoOR = byte1 | byte2;
byte resultadoXOR = byte1 ^ byte2;
byte resultadoNOT = ~byte1;
byte resultadoShiftLeft = byte1 << 2;
byte resultadoShiftRight = byte1 >> 1;


void setup(){
  Serial.begin(9600);

  Serial.println("Operaciones Aritméticas:");
  Serial.println("Suma: " + String(suma));
  Serial.println("Resta: " + String(resta));
  Serial.println("Multiplicación: " + String(multiplicacion));
  Serial.println("División: " + String(division));
  Serial.println("Potencia: " + String(potencia));
  Serial.println("Módulo: " + String(modulo));

  delay(900);

  Serial.println("\nOperadores Lógicos:");
  Serial.println("AND0: " + String(AND0));
  Serial.println("AND1: " + String(AND1));
  Serial.println("OR0: " + String(OR0));
  Serial.println("OR1: " + String(OR1));

  delay(900);

  Serial.println("\nOperadores de Comparación:");
  Serial.println("Mayor que: " + String(mayorQue));
  Serial.println("Menor que: " + String(menorQue));
  Serial.println("Igual que: " + String(igualQue));

 delay(900);

  Serial.println("\nOperadores de Asignación:");
  Serial.println("Num1: " + String(num1));
  Serial.println("Num2: " + String(num2));
  Serial.println("Num3: " + String(num3));
  Serial.println("Num4: " + String(num4));
  Serial.println("Num5: " + String(num5));

 delay(900);

  Serial.println("\nOperadores de Bits:");
  Serial.println("Resultado AND: " + String(resultadoAND, BIN));
  Serial.println("Resultado OR: " + String(resultadoOR, BIN));
  Serial.println("Resultado XOR: " + String(resultadoXOR, BIN));
  Serial.println("Resultado NOT: " + String(resultadoNOT, BIN));
  Serial.println("Resultado Shift Left: " + String(resultadoShiftLeft, BIN));
  Serial.println("Resultado Shift Right: " + String(resultadoShiftRight, BIN));

 delay(900);

  //CONTROL DE FLUJO
  //CONDICIONALES

  int num = 1 ;
  Serial.println("\nCondicionales");

  if (num == 1){
    Serial.println("el numero es 1");
     delay(900);
  }

  else if (num == 2){
    Serial.println("cambiaron el codigo");
     delay(900);
  }

  else {
    Serial.println("cambiastes el codigo a algo que no es 2 ni 1");
     delay(900);
  }


  //BUCLES
  Serial.println("\nBucle For:");

  for (int i = 0; i <=10; i++ ){  //el i ++ es para sumarle un 1 a la       variable i la razon es porque este consume menos espacio
    Serial.println("valor de i : " + String(i));
     delay(250);
  }

    // Bucle While con Condiciones
    Serial.println("\nBucle While con Condiciones:");

    int contador = 0;
    while (contador <= 10) {

      if (contador % 2 == 0) {
        Serial.println("Número par: " + String(contador));
        delay(250);

    }
      contador++;
  }

  // Estructura switch

  Serial.println("\nSwitch");
  switch (num) {
    case 1:
      Serial.println("num es 1");
      break;
    case 2:
      Serial.println("num es 2");
      break;
    default:
      Serial.println("num no es ni 1 ni 2");
  }
  delay(900);

  //Extra
  Serial.println("\nEjercicio Extra : ");
  for (int i = 10 ; i <=55 ; i++ ){
    if(i % 2 == 0 && i % 3 != 0 || i == 55 && i != 16 ){
      Serial.println("valor es : " + String(i));
    }
  }
}



void loop(){ //el bucle loop es un bucle que nunca se deja de repetir este si es 100% infinito

}