void main(List<String> arguments) {
  //Funcion dificultad extra!!!
  printNumbers(10, 55);

  //OPERACIONES ESTRUCTURAS DE CONTROL

  //Condicionales:

  //Establezco un valor para realizar las operaciones
  int control = 10;

  if (3 < control) {
    print('El numero 3 es inferior a $control');
  } // condicional if

  if (20 < control) {
    print('El numero 20 es inferior a $control');
  } else {
    print('El numero 20 es superior a $control');
  } // condicional if/else

  if (20 < control) {
    print('El numero 20 es inferior a $control');
  } else if (20 == control) {
    print('El numero 20 es igual a $control');
  } else {
    print('El numero 20 no es inferior, ni igual a $control es superior');
  } // condicional else if

  Dias festivo = Dias.lunes;
  switch (festivo) {
    case Dias.lunes:
      print('El festivo es el lunes');
    case Dias.miercoles:
      print('El festivo es el miercoles');
    case Dias.viernes:
      print('El festivo es el viernes');
  } //condicional Switch

  //Bucles

  for (var i = 1; i <= control; i++) {
    print('Contando ... $i');
  } // Bucle for

  for (var kid in kids) {
    print(kid);
  } // Bucle for in

  while (counter < control) {
    print('La cuenta va en: $counter');
    counter++;
  } //Bucle while

  counter = 0;//Limpio el counter para no tener otra var

  do {
    print('Nueva cuenta en : $counter');
    counter++;
  } while (counter <= 0);// Bucle do while
} // Fin del Main

//Contador para el while
int counter = 0;

// List para que funcione el For in
List<String> kids = ['Andres', 'Julian', 'Federico'];

//Enum para que funcione el switch
enum Dias { lunes, miercoles, viernes }

//Operadores aritmeticos
int sumResult = 1 + 1; //Suma
int restResult = 1 - 1; //Resta
int multiResult = 1 * 1; //Multiplicacion
double divResult = 4 / 2; //Division
double moduloResult = 4 % 2; // Modulo
double expo = 4 * 2; //Revisar

//Operadoores de comparacion
//Utilizo funciones tipo flecha para retornar un bool haciendo comparaciones
bool isEqual(int a, int b) => a == b; //Igualdad ==
bool isNotSame(int a, int b) => a != b; //Desigualdad !=
bool isGreaterThan(int a, int b) => a > b; //Mayor que >
bool isLessThan(int a, int b) => a < b; //Menor que <
bool isGreaterEqualThan(int a, int b) => a >= b; //Menor o igual que >=
bool isLessEqualThan(int a, int b) => a <= b; //Menor o igual que <=

//Operadores logicos
bool isJustPrice(int value) => value > 0 && value < 2.50; // y logico &&
bool isInjustPrice(int value) => value < 2.50 || value > 5.50; // o logico ||

//Operadores asignacion
//Coloco ejemplo con funciones tipo flecha
int x = 1; // Asignacion
assignPlus(int a) => a += 3; // Suma y asignacion +=
assignRest(int a) => a -= 3; // Resta y asignacion -=
assignMulti(int a) => a *= 3; // Multiplicacion y asignacion *=
assignDiv(double a) => a /= 3; //Division y asigancion /=
assignIntDiv(int a) => a ~/= 3; //Division entera y asignacion ~/=
assignModulo(int a) => a %= 3; //Modulo y asignacion %=

//Operadores desplazamiento
//Aun no entiendo a cabalidad estos operadores.
displaceRight(int a) => a >> 3;
displaceLeft(int a) => a << 3;

//Operadores de Cadenas de texto
String getFullName(String name, String lastName) =>
    name + lastName; // Concatenar +
String getEco(String word) => word * 5; //Repetir *

//opedarores de incremento/drecremento
int increment(int a) => a++; // Incrementa de 1 en 1
int decrease(int a) => a--; // Decrementa de 1 en 1

// Funcion que hace que se impriman los numeros solicitados en el Extra!!
void printNumbers(int min, int max) {
  //Esta funcion evalua si un numero es multiplo de otro
  bool isMultipleOf(int a, int multiple) => a % multiple == 0;
  List<int> list = [];
  for (var i = min; i < max; i++) {
    if (isMultipleOf(i, 2) && !isMultipleOf(i, 3) && i != 16) {
      list.add(i);
    }
  }
  list.add(max);

  print(list);
}
