#include <iostream>
#include <random>

using namespace std;

int main() {
    // Declaración de variables
    int num1 = 57;
    int num2 = 23;
    cout << "Número 1: " << num1 << endl;
    cout << "Número 2: " << num2 << endl << endl;

    // Operadores aritméticos
    int suma = num1 + num2;
    int resta = num1 - num2;
    int producto = num1 * num2;
    int divicion = num1 / num2;
    int modulo = num1 % num2;
    cout << "Operadores aritméticos" << endl;
    cout << "Suma: " << suma << endl;
    cout << "Resta: " << resta << endl;
    cout << "Producto: " << producto << endl;
    cout << "División: " << divicion << endl;
    cout << "Módulo: " << modulo << endl;

    // Operadores lógicos
    bool orLogico = true || false;
    bool andLogico = false && true;
    bool esMayor = 38 > 17;
    bool esMenor = 1027 <= 243;
    bool negacion = !(5 <= 12);
    bool igual = suma == producto;
    bool noIgual = modulo != resta;

    cout << endl << "Operadores lógicos" << endl;
    cout << "Or: " << orLogico << endl;
    cout << "And: " << andLogico << endl;
    cout << "38 > 17: " << esMayor << endl;
    cout << "1027 <= 243: " << esMenor << endl;
    cout << "Negación de (5 <= 12): " << negacion << endl;
    cout << "La suma es igual a la multiplicación: " << igual << endl;
    cout << "El módulo no es igual a la resta: " << noIgual << endl;

    // Asignación
    cout << endl << "Asignación" << endl;
    int numero = num2 + 2;
    cout << "Número: " << numero << endl;
    numero += 5; // Suma y asignación
    numero -= 3; // Resta y asignación
    num2 *= 7; // Multiplicación y asignación
    num1 /= 3; // División y asignación
    cout << "Número 1: " << num1 << endl;
    cout << "Número 2: " << --num2 << endl;
    cout << "Número: " << numero++ << endl;

    // Generar un número aleatorio entre 1 y 7
    random_device rd;
    uniform_int_distribution<int> dist(0, 7);
    int numAleatorio = dist(rd);
    int numPar = numAleatorio % 2 == 0 ? numAleatorio : ++numAleatorio;
    cout << "Numero par: " << numPar << endl;

    // Manipulación de bits
    cout << endl << "Manipulación de bits" << endl;
    int a = 60;  // 60 = 0011 1100
    int b = 13;  // 13 = 0000 1101
    cout << "a = " << a << ", b = " << b << endl;
    int result;

    // AND bit a bit
    result = a & b;  // 12 = 0000 1100
    cout << "Resultado de a & b: " << result << endl;

    // OR bit a bit
    result = a | b;  // 61 = 0011 1101
    cout << "Resultado de a | b: " << result << endl;

    // XOR bit a bit
    result = a ^ b;  // 49 = 0011 0001
    cout << "Resultado de a ^ b: " << result << endl;

    // NOT bit a bit
    result = ~a;  // -61 = 1100 0011
    cout << "Resultado de ~a: " << result << endl;

    // Desplazamiento a la izquierda
    result = a << 2;  // 240 = 1111 0000
    cout << "Resultado de a << 2: " << result << endl;

    // Desplazamiento a la derecha
    result = a >> 2;  // 15 = 0000 1111
    cout << "Resultado de a >> 2: " << result << endl;

    // Condicionales
    cout << endl << "Condicionales" << endl;
    if (num1 > num2) {
        cout << "num1 es mayor que num2" << endl;
    } else if (num1 < num2) {
        cout << "num1 es menor que num2" << endl;
    } else {
        cout << "num1 es igual a num2" << endl;
    }

    int dia = dist(rd);
    cout << "Número aleatorio: " << dia << " -> ";
    switch (dia) {
        case 1:
            cout << "Lunes" << endl;
            break;
        case 2:
            cout << "Martes" << endl;
            break;
        case 3:
            cout << "Miércoles" << endl;
            break;
        case 4:
            cout << "Jueves" << endl;
            break;
        case 5:
            cout << "Viernes" << endl;
            break;
        case 6:
            cout << "Sábado" << endl;
            break;
        case 7:
            cout << "Domingo" << endl;
            break;
        default:
            cout << "Día no válido" << endl;
    }

    // Bucles e iteraciones
    cout << endl << "Bucles e iteraciones" << endl;
    cout << "Números impares menores a 39: ";
    for (int i = 1; i < 39; i += 2) {
        cout << i << ", ";
    }
    cout << endl;

    ++numero;
    bool esPrimo = true;
    int divisor = 2;
    while (divisor < numero) {
        if (numero % divisor == 0) {
            esPrimo = false;
            break;
        }
        divisor++;
    }
    string mensaje = esPrimo ? " es primo." : " no es primo.";
    cout << "El número " << numero << mensaje << endl;

    int entrada;
    do {
        cout << "Ingresa un número impar: ";
        cin >> entrada;
    } while (entrada % 2 == 0);
    cout << "Correcto " << entrada << " es impar." << endl;

    // Excepciones
    cout << endl << "Excepciones" << endl;
    cout << "Ingresa un número para dividir 17: ";
    cin >> divisor;
    try {
        if (divisor == 0) {
            throw invalid_argument("División por cero.");
        }
        cout << "Resultado: " << 17 / divisor << endl;
    } catch (const invalid_argument &e) {
        cout << "Error: " << e.what() << endl;
    }

    // Dificulta extra
    /* Crea un programa que imprima por consola todos los números comprendidos
       entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3 */
    cout << endl << "Dificulta extra" << endl;
    for (int i = 10; i < 56; i += 2) {
        // Saltar el 16
        if (i == 16) continue;

        // Filtrar los múltiplos de 3
        if (i % 3 == 0) continue;

        cout << i << ", ";
    }

    return 0;
}