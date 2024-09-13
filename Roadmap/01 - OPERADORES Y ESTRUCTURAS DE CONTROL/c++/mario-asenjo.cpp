#include <iostream>

// RETO #01 - EJERCICIOS

int main(){

// - 1. Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
//     (Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...)(Ten en cuenta que cada lenguaje puede poseer unos diferentes).

/*OPERADORES C++ : En C++, los operadores se dividen en varias categorías:
 operadores aritméticos, operadores de asignación, operadores de comparación, operadores lógicos,
 operadores bit a bit (bitwise), operadores de incremento/decremento, operadores de punteros, operadores ternarios y operadores de tipo.*/

    // Operadores Aritméticos: Realizan operaciones matemáticas.
    int a = 10, b = 3;
    int suma = a + b;  // Suma: 13
    int resta = a - b;  // Resta: 7
    int multiplicacion = a * b;  // Multiplicación: 30
    int division = a / b;  // División: 3
    int modulo = a % b;  // Módulo: 1 (resto de la división)

    // Operadores de Asignación: Asignan valores a variables.
    int c = 5;  // Asignación simple
    c += 3;  // Equivale a c = c + 3, ahora c es 8
    c -= 2;  // Equivale a c = c - 2, ahora c es 6
    c *= 4;  // Equivale a c = c * 4, ahora c es 24
    c /= 2;  // Equivale a c = c / 2, ahora c es 12
    c %= 5;  // Equivale a c = c % 5, ahora c es 2

    // Operadores de Comparación: Comparan dos valores.
    bool esIgual = (a == b);  // Igualdad: false
    bool esDiferente = (a != b);  // Desigualdad: true
    bool esMayor = (a > b);  // Mayor que: true
    bool esMenor = (a < b);  // Menor que: false
    bool esMayorOIgual = (a >= b);  // Mayor o igual: true
    bool esMenorOIgual = (a <= b);  // Menor o igual: false

    //Operadores Lógicos: Combinan expresiones lógicas.
    bool verdadero = true;
    bool falso = false;

    bool yLogico = (verdadero && falso);  // AND lógico: false
    bool oLogico = (verdadero || falso);  // OR lógico: true
    bool negacion = !verdadero;  // NOT lógico: false

    //Operadores Bit a Bit (BitWise): Realizan operaciones a nivel de bits.
    int x = 5;  // 5 en binario es 0101
    int y = 3;  // 3 en binario es 0011

    int andBitwise = x & y;  // AND bit a bit: 0101 & 0011 = 0001 (1)
    int orBitwise = x | y;  // OR bit a bit: 0101 | 0011 = 0111 (7)
    int xorBitwise = x ^ y;  // XOR bit a bit: 0101 ^ 0011 = 0110 (6)
    int notBitwise = ~x;  // NOT bit a bit: ~0101 = 1010 (depende del tamaño del tipo)
    int desplazamientoIzquierda = x << 1;  // Desplazamiento a la izquierda: 1010 (10)
    int desplazamientoDerecha = x >> 1;  // Desplazamiento a la derecha: 0010 (2)

    //Operadores de Incremento y Decremento: Para aumentar o disminuir el valor de una variable.
    int contador = 10;
    contador++;  // Incremento: contador ahora es 11
    contador--;  // Decremento: contador ahora es 10

    //Operadores de Punteros: Se usan para trabajar con direcciones de memoria.
    int numero = 42;
    int* puntero = &numero;  // Operador de dirección: obtiene la dirección de la variable
    int valor = *puntero;  // Operador de desreferencia: obtiene el valor de la variable apuntada

    //Operador Ternario: Actua como un condicional compacto.
    int edad = 18;
    std::string mensaje = (edad >= 18) ? "Mayor de edad" : "Menor de edad";  // Si edad >= 18, devuelve "Mayor de edad", sino "Menor de edad".

    //Operadores de Tipo: Convierten tipos de datos.
    int numeroEntero = 7;
    double numeroDecimal = static_cast<double>(numeroEntero);  // Convertir entero a double

// - 2. Crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje: Condicionales, iterativas, excepciones...
    
    /*ESTRUCTURAS DE CONTROL : Las estructuras de control permiten alterar el flujo normal del programa. Estas
    incluyen condicionales, bucles y estructuras de salto.*/

    //Estructura condicional if-else: Ejecuta bloques de código basados en una condicion.
    int numero = 10;
    if (numero > 0) {
        std::cout << "El número es positivo" << std::endl;
    } else if (numero < 0) {
        std::cout << "El número es negativo" << std::endl;
    } else {
        std::cout << "El número es cero" << std::endl;
    }

    //Estructura switch : Ejecuta bloques de código según el valor de una variable.
    char letra = 'A';
    switch (letra) {
        case 'A':
            std::cout << "Es la letra A" << std::endl;
            break;
        case 'B':
            std::cout << "Es la letra B" << std::endl;
            break;
        default:
            std::cout << "Es otra letra" << std::endl;
            break;
    }

    //Bucles while: Ejecutan bloque de código mientras una condición sea verdadera.
    int contador = 0;
    while (contador < 5) {
        std::cout << "Contador: " << contador << std::endl;
        contador++;
    }

    //Bucles do-while: Similar a while, pero garantiza que el bloque de código se ejecute al menos una vez.
    int contador = 0;
    do {
        std::cout << "Contador: " << contador << std::endl;
        contador++;
    } while (contador < 5);

    //Bucles for: Se usa cuando el número de iteraciones es conocido.
    for (int i = 0; i < 5; i++) {
        std::cout << "Iteración: " << i << std::endl;
    }

    // Estructura break y continue: break termina el bucle prematuramente, continue salta a la siguiente iteración.
    for (int i = 0; i < 10; i++) {
        if (i == 5) {
            break;  // Sale del bucle cuando i es 5
        }
        if (i % 2 == 0) {
            continue;  // Salta a la siguiente iteración si i es par
        }
        std::cout << "i: " << i << std::endl;
    }

return 0;
}