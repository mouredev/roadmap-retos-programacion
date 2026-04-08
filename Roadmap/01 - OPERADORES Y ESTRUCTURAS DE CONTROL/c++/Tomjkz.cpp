#include <iostream>

using namespace std;

int main()
{

/* Ejercicio #01 - Operadores y estructuras de control.

-Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
-Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje: Condicionales, iterativas, excepciones...
-Debes hacer print por consola del resultado de todos los ejemplos.

* DIFICULTAD EXTRA (opcional):
  Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3
*/

int a = 10;
int b = 5;

// OPERADORES ARITMÉTICOS: permiten realizar cálculos matemáticos entre variables o valores.

cout << "Suma: " << a << " + " << b << " = " << a + b << "\n";
cout << "Resta: " << a << " - " << b << " = " << a - b << "\n";
cout << "Multiplicación: " << a << " * " << b << " = " << a * b << "\n";
cout << "División: " << a << " / " << b << " = " << a / b << "\n";
cout << "Modulo: " << a << " % " << b << " = " << a % b << "\n";
a++;
cout << "Incremento: ahora 'a' vale " << a << "\n";
a--;
cout << "Decremento: ahora 'a' vuelve a valer " << a << "\n";

// OPERADORES DE ASIGNACIÓN: permiten guardar valores en variables.

// El '=' asigna un valor a una variable, en este caso la variable 'edad'.
int edad = 26;
cout << "Edad del paciente: " << edad << "\n";

// El '+=' suma y guarda una variable, en este caso 'puntos'.
int puntos = 0;
puntos += 500;
cout << "Tienes: "<< puntos << " puntos." << "\n";

// El '-=' resta y guarda una variable, en este caso 'puntos'.
puntos -= 500;
cout << "Tienes: " << puntos << " puntos." << "\n";

// El '*=' multiplica la variable por un valor y lo guarda, en este caso 'precios'.
int precios = 1000;
precios *= 2;
cout << "Estaba 1000 y aumento el doble, ahora cuesta: " << precios << "\n";

// El '/=' divide la variable por un valor y lo guarda, en este caso 'dinero'.
int dinero = 5000;
dinero /= 2;
cout << "Ganamos 5000 dividimos ganancias a la mitad y corresponde: " << dinero << " para cada uno." << "\n";

// El '%=' calcula el resto de una divison y lo guarda.
int numero = 10;
numero %= 3;
cout << "El resto es: " << numero << "\n";

// OPERADORES DE COMPARACIÓN: permiten comparar valores y devolver true o false.
int digito;
cout << "Ingrese un numero: ";
cin >> digito; 

// '==' es igual a.
if (digito == 10) {
    cout << "El numero es 10" << "\n";
}
// '!=' es diferente a.
if (digito != 10) {
    cout << "El numero no es 10" << "\n";
}
// '>' es mayor a.
if (digito > 10) {
    cout << "El numero es mayor a 10" << "\n";
}
// '<' es menor a.
if (digito < 10) {
    cout << "El numero es menor a 10" << "\n";
}
// '>=' es mayor o igual a.
if (digito >= 10) {
    cout << "El numero es mayor o igual a 10" << "\n";
}
// '<=' es menor o igual a.
if (digito <= 10) {
    cout << "El numero es menor o igual a 10" << "\n";
}

//OPERADORES LOGICOS: permiten combinar varias condiciones para construir reglas mas complejas.
int edad2;
bool tieneDni = true;
cout << "Cuantos años tenes?" << "\n"; 
    cin >> edad2; 
// && (Y logico): las dos condiciones deben ser true. 
if (edad2 > 18 && tieneDni) {
    cout << "Podes entrar al boliche." << "\n";
 }
// || (O logico): es suficiente que una de las dos condiciones sea true.
 if (edad2 < 18 || !tieneDni) {
    cout << "No podes entrar al boliche." << "\n";
 }

 /* ! (negación): invierte el valor de una condición.
    Si tieneDni es true, !tieneDni es false. */

// OPERADORES A NIVEL DE BITS: operan sobre la representación binaria de los números. Son mas utilizados para programación de bajo nivel.
int x = 5;  // En binario: 0101
int y = 3;  // En binario: 0011

// '&' (AND de bits): 0101 & 0011 = 0001 = 1
cout << "AND de bits (5 & 3): " << (x & y) << "\n";

// '|' (OR de bits): 0101 | 0011 = 0111 = 7
cout << "OR de bits (5 | 3): " << (x | y) << "\n";

// '^' (XOR): 0101 ^ 0011 = 0110 = 6
cout << "XOR (5 ^ 3): " << (x ^ y) << "\n";

// '~' (NOT de bits): invierte todos los bits de x
cout << "NOT de bits (~5): " << (~x) << "\n";

/*
'<<' desplazamiento a la izquierda: es como multiplicar por 2.
5 en binario es 0101, desplazado una posición queda 1010 = 10.
*/
cout << "Desplazamiento izquierda (5 << 1): " << (x << 1) << "\n";

/*
'>>' desplazamiento a la derecha: es como dividir por 2.
5 en binario es 0101, desplazado una posición queda 0010 = 2.
*/
cout << "Desplazamiento derecha (5 >> 1): " << (x >> 1) << "\n";

/* 
OPERADORES DE IDENTIDAD Y PERTENENCIA:
Estos operadores ('is', 'in') son propios de Python y no existen en C++.
En C++ la comparación de identidad se hace con '=='.
*/

// ESTRUCTURAS DE CONTROL.

/*
Condicionales: IF / ELSE IF / ELSE
El programa evalúa las condiciones en orden y ejecuta solo el primer bloque verdadero.
*/
int temperatura;
cout << "Ingresá la temperatura en grados: ";
cin >> temperatura;

if (temperatura < 10) {
    cout << "Hace mucho frío, abrigate bien." << "\n";
} else if (temperatura >= 10 && temperatura < 25) {
    cout << "Temperatura agradable." << "\n";
} else {
    cout << "Hace calor, tomá agua." << "\n";
}

/*
SWITCH
Es más limpio que varios 'else if' cuando comparás una variable contra valores fijos.
*/
int opcion;
cout << "Elegí una opción (1, 2 o 3): ";
cin >> opcion;

switch (opcion) {
    case 1:
        cout << "Elegiste la opción 1: Nueva partida." << "\n";
        break; // 'break' le dice al programa que salga del switch.
    case 2:
        cout << "Elegiste la opción 2: Cargar partida." << "\n";
        break;
    case 3:
        cout << "Elegiste la opción 3: Salir." << "\n";
        break;
    default: // es como si fuera un else, se ejecuta si el programa no entró a ningun case.
        cout << "Elegiste una opción invalida." << "\n";
        break;
}

/*
ITERATIVAS o BUCLES: FOR / WHILE / DO-WHILE
El programa se ejecuta hasta que se cumpla la condición.
*/

/*
FOR
Muy util cuando sabes cuantas repeticiones necesitas.
Se divide en tres partes: inicio, condicion y actualización.
*/

/*inicio*/ /*condición*/ /*actualización*/
for (int i = 1; i <= 5; i++) {
    // i comienza en 1, el bucle corre mientras i <= 5, y cada cuelva i aumenta en 1.
    cout << "Vuelta número: " << i << "\n";
}

/*
WHILE
Mas util cuando no sabes cuantas repeticiones necesitas con exactitud.
*/
int numero2 = 1;

while (numero2 <= 5) {
    cout << "Numero: " << numero2 << "\n";
    numero2++; // si no actualizo la variable el bucle no termina nunca.
}

/*
DO-WHILE
A diferencia del while, primero ejecuta las instrucciones y al final evalúa la condición.
si es verdadera repite el bloque, si es falsa termina.
Util para menus y validación de entrada del usuario.
*/
int intentos;

do {
    cout << "Ingrese un numero del 1 al 10: ";
    cin >> intentos;
}
while (intentos < 1 || intentos > 10); // si el numero esta fuera de rango vuelve a pedir.

cout <<"Número válido: " << intentos << "\n";

/*
EXCEPCIONES: TRY / CATCH / THROW.
Permiten manejar errores en tiempo de ejecución de forma controlada.
*/
int dividendo = 10;
int divisor;
bool huboError;

do {
    huboError = false;
    cout << "Ingresa un divisor: ";
    cin >> divisor;
    try {
    // dentro del 'try' va el codigo que podria dar error.
    if (divisor == 0) {
        throw "Error: no se puede dividir por cero."; // 'throw' lanza la excepción para que catch la atrape.
    }
    cout << "Resultado: " << dividendo / divisor << "\n";
    }
catch (const char* mensaje) {
    // 'catch' atrapa la excepción y ejecuta este bloque.
    cout << mensaje << "\n";
    huboError = true;
}
} while (huboError);

// DESAFIO EXTRA.

for (int i2 = 10; i2 <= 55; i2++) {
    if (i2 % 2 == 00 && i2 != 16 && i2 % 3 != 00){
    cout << i2 << "\n";
    }
}

return 0;
}
