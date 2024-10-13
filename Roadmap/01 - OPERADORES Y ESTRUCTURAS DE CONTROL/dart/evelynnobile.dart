/*

 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */



 import '../../00 - SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO/dart/kodenook.dart';

void main(){
/*- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...*/

//aritméticos:
var suma = 2+2;
print(suma);

var resta = 10 - 5;
print(resta);

int multiplicacion = 5 * 8;
print(multiplicacion);

double division = 5 / 2;
print(division);

var intDivision = 5 ~/ 2;
print(intDivision);

var modulo = 20 % 4;
print(modulo);

// Lógicos

//OR
var verdadero = true && true;
var verdaderoEjemplo2 = false || true;
//var verdaderoEjemplo3 = true || false;
var falso = false || false; 

print(verdadero);
print(verdaderoEjemplo2);
print(falso);

//AND
var verdaderoAnd = true && true;
//var falseAnd1= false && true;
var falseAnd2= true && false;
//var falseAnd3= false && false;

print(verdaderoAnd);
print(falseAnd2);

//negación

var ejemploNegacion = !false;
print(ejemploNegacion);


// De comparación
var ejemplo1= 2 == 2;
var ejemplo2= 2 != 4;
var ejemplo3= 5 > 10;
var ejemplo4= 5 < 2;
var ejemplo5= 5 >= 5;
var ejemplo6= 10 <= 20;

print(ejemplo1);
print(ejemplo2);
print(ejemplo3);
print(ejemplo4);
print(ejemplo5);
print(ejemplo6);

// De asignación
 var a = 2;
 var b;

 var c = b ??= 5;

var d = 4;
var e = a += d;

print(a);
print(c);
print(e);


 // De identidad
int num1 = 4;
int num2 = 4;
bool resultadoIdentical = identical(num1, num2);

  // De pertenencia
  var lista = [1, 2, 3, 4, 5];
  bool resultadoContains = lista.contains(3);

print(resultadoContains);
print(resultadoIdentical);

// Bits
//And
var bit1= 5;
var bit2= 10;

var resultado = bit1 & bit2;
var resultado2 = bit1 | bit2;

print(resultado);
 print(resultado2);


 /* * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 */

for (var i =0; i<5; i++){
  print(i);
}

var i = 0;
while( i < 5){
  print(i);
  i++;
};

var num = 10;

if (num > 20){
  print("es mayor");
  }
else {
  print("es menor");
}


var command = 'OPEN';
switch (command) {
  case 'CLOSED':
    print("CLOSED");
    break;
  case 'PENDING':
    print("PENDING");
    break;
  case 'APPROVED':
 print("APPROVED");
    break;
  case 'DENIED':
   print("DENIED");
    break;
  case 'OPEN':
   print("OPEN");
    break;
  default:
    print("PENDING");
}

 for (int i = 10; i <= 55; i++){
  if (i % 2 == 0 && i != 16 && i % 3 != 0){
    print(i);
  }
 }


}
 