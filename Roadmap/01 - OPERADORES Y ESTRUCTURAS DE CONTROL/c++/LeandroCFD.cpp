#include <iostream>
#include <string>


int main() {

    // Declaración de variables
    int a, b, i;
    float c, d;
    bool e, f;
    char g, h;

    // Operadores de asignación
    // C++ tiene los operadores de asignación: = (asignación simple), += (suma y asignación), -= (resta y asignación),
    // *= (multiplicación y asignación), /= (división y asignación) y %= (módulo y asignación).

    std::cout << "************************" << std::endl;
    std::cout << "OPERADORES DE ASIGNACIÓN" << std::endl;
    std::cout << "************************" << std::endl;

    std::cout << "" << std::endl;
    a = 12; // Asignación simple
    std::cout << "a = " << a << std::endl;
    a += 5; // Suma y asignación (a = a + 5)
    std::cout << "a += 5 -> a = " << a << std::endl;
    a -= 3; // Resta y asignación (a = a - 3)
    std::cout << "a -= 3 -> a = " << a << std::endl;
    a *= 2; // Multiplicación y asignación (a = a * 2)
    std::cout << "a *= 2 -> a = " << a << std::endl;
    a /= 4; // División y asignación (a = a / 4)
    std::cout << "a /= 4 -> a = " << a << std::endl;
    a %= 2; // Módulo y asignación (a = a % 2)
    std::cout << "a %= 2 -> a = " << a << std::endl;
    a++; // Incremento (a = a + 1)
    std::cout << "a++ -> a = " << a << std::endl;
    a--; // Decremento (a = a - 1)
    std::cout << "a-- -> a = " << a << std::endl;

    // Operaciones aritméticas
    // C++ tiene los operadores aritméticos básicos: + (suma), - (resta), * (multiplicación), / (división) y % (módulo).

    std::cout << "" << std::endl;
    std::cout << "**********************" << std::endl;
    std::cout << "OPERADORES ARITMÉTICOS" << std::endl;
    std::cout << "**********************" << std::endl;

    std::cout << "" << std::endl;
    std::cout << "1) Operaciones numeros enteros" << std::endl;
    a = 10, b = 5;
    std::cout << "a = " << a << " y b = " << b << std::endl;
    std::cout << "a + b = " << a + b << std::endl; // Suma
    std::cout << "a - b = " << a - b << std::endl; // Resta
    std::cout << "a * b = " << a * b << std::endl; // Multiplicación
    std::cout << "a / b = " << a / b << std::endl; // División
    std::cout << "a % b = " << a % b << std::endl; // Módulo
    
    std::cout << "" << std::endl;
    std::cout << "2) Operaciones numeros decimales" << std::endl;
    c = 10.5, d = 5.2;
    std::cout << "c = " << c << " y d = " << d << std::endl;
    std::cout << "c + d = " << c + d << std::endl; // Suma
    std::cout << "c - d = " << c - d << std::endl; // Resta
    std::cout << "c * d = " << c * d << std::endl; // Multiplicación
    std::cout << "c / d = " << c / d << std::endl; // División

    // Las operaciones aritméticas en c++ tienen un orden de precedencia, que es el siguiente:
    // 1. Paréntesis ()
    // 2. Exponentes (no existe un operador de potencia en C++, pero se puede usar la función pow() de la biblioteca <cmath>)
    // 3. Multiplicación *, División / y Módulo %
    // 4. Suma + y Resta -

    // Operadores de comparación
    // C++ tiene los operadores de comparación: == (igual a), != (diferente de), > (mayor que), < (menor que), 
    // >= (mayor o igual que) y <= (menor o igual que).
    
    std::cout << "" << std::endl;
    std::cout << "*************************" << std::endl;
    std::cout << "OPERADORES DE COMPARACIÓN" << std::endl;
    std::cout << "*************************" << std::endl;
    std::cout << "" << std::endl;

    e = (a > b); // ¿a es mayor que b?
    std::cout << "a es mayor que b: " << e << std::endl;
    e = (a < b); // ¿a es menor que b?
    std::cout << "a es menor que b: " << e << std::endl;
    e = (a == b); // ¿a es igual a b?
    std::cout << "a es igual a b: " << e << std::endl;
    e = (a != b); // ¿a es diferente de b?
    std::cout << "a es diferente de b: " << e << std::endl;
    e = (a >= b); // ¿a es mayor o igual que b?
    std::cout << "a es mayor o igual que b: " << e << std::endl;
    e = (a <= b); // ¿a es menor o igual que b?
    std::cout << "a es menor o igual que b: " << e << std::endl;

    // Operadores lógicos
    // C++ tiene los operadores lógicos: && (AND), || (OR) y ! (NOT).

    std::cout << "" << std::endl;
    std::cout << "******************" << std::endl;
    std::cout << "OPERADORES LÓGICOS" << std::endl;
    std::cout << "******************" << std::endl;
    std::cout << "" << std::endl;

    f = (a > b) && (c > d); // ¿a es mayor que b Y c es mayor que d? (operador AND)
    std::cout << "a es mayor que b Y c es mayor que d: " << f << std::endl;
    f = (a > b) || (c < d); // ¿a es mayor que b O c es menor que d? (operador OR)
    std::cout << "a es mayor que b O c es menor que d: " << f << std::endl;
    f = !(a > b); // NO a es mayor que b (operador NOT)
    std::cout << "NO a es mayor que b: " << f << std::endl;

    // Operadores de Bits
    /* C++ tiene los siguientes operadores de bits:
     * & (AND)
     * | (OR)
     * ^ (XOR)
     * ~ (NOT)
     * << (desplazamiento a la izquierda)
     * >> (desplazamiento a la derecha)
     */

    std::cout << "" << std::endl;
    std::cout << "******************" << std::endl;
    std::cout << "OPERADORES DE BITS" << std::endl;
    std::cout << "******************" << std::endl;
    std::cout << "" << std::endl;

    i = a & b; // AND bit a bit
    std::cout << "a AND b = " << i << std::endl;
    i = a | b; // OR bit a bit
    std::cout << "a OR b = " << i << std::endl;
    i = a ^ b; // XOR bit a bit
    std::cout << "a XOR b = " << i << std::endl;
    i = ~a; // NOT bit a bit
    std::cout << "NOT a = " << i << std::endl;
    i = a << 1; // Desplazamiento a la izquierda de a por 1 bit
    std::cout << "a desplazado a la izquierda por 1 bit = " << i << std::endl;
    i = a >> 1; // Desplazamiento a la derecha de a por 1 bit
    std::cout << "a desplazado a la derecha por 1 bit = " << i << std::endl;

    // En C++ NO existen operadores de pertenencia ni operadores de identidad como en Python, pero se pueden simular 
    // con operadores de comparación y lógicos.

    // Estructuras de control
    // C++ tiene las siguientes estructuras de control:
    // 1. Condicionales: if, if else, switch
    // 2. Bucles: for, while, do-while
    
    std::cout << "" << std::endl;
    std::cout << "**********************" << std::endl;
    std::cout << "ESTRUCTURAS DE CONTROL" << std::endl;
    std::cout << "**********************" << std::endl;
    std::cout << "" << std::endl;
    // Condicionales

    std::cout << "1) Condicionales" << std::endl;
    std::cout << "" << std::endl;
    std::cout << "1.1) if simple" << std::endl;
    std::cout << "" << std::endl;
    if (a > b) 
        std::cout << "a es mayor que b" << std::endl; // if simple sin llaves, solo para una línea de código
    
    std::cout << "" << std::endl;
    std::cout << "1.2) if simple con llaves" << std::endl;
    std::cout << "" << std::endl;
    if (a > b) {
        std::cout << "a es mayor que b" << std::endl; // if simple con llaves, para una o más líneas de código
    }

    std::cout << "" << std::endl;
    std::cout << "1.3) if else" << std::endl;
    std::cout << "" << std::endl;
    if (a > b) {
        std::cout << "a es mayor que b" << std::endl; // if else con llaves, para una o más líneas de código
    } else {
        std::cout << "a no es mayor que b" << std::endl;
    }

    std::cout << "" << std::endl;
    std::cout << "1.4) Switch" << std::endl;
    std::cout << "Ingrese un valor entero para a: ";
    std::cin >> a; // Leer un valor entero para a desde la entrada estándar

    switch (a) { // switch para múltiples condiciones basadas en el valor de a
        case 0:
            std::cout << "a es cero" << std::endl;
            break;
        case 1:
            std::cout << "a es uno" << std::endl;
            break;
        case 10:
            std::cout << "a es diez" << std::endl;
            break;
        default:
            std::cout << "a no es ni cero, ni uno, ni diez" << std::endl;
    }
    
    // Bucles
    std::cout << "" << std::endl;
    std::cout << "2) Bucles" << std::endl;
    std::cout << "" << std::endl;
    a=10; // Asignar a el valor 10 para los bucles
    std::cout << "2.1) Bucle while" << std::endl;
    while (a > 0) { // Bucle while, se ejecuta mientras a sea mayor que 0
        std::cout << "a = " << a << std::endl;
        a--; // Decrementar a en 1
    }

    std::cout << "" << std::endl;
    std::cout << "2.2) Bucle do-while" << std::endl;
    do { // Bucle do-while, se ejecuta al menos una vez y luego se repite mientras a sea mayor que 0
        std::cout << "a = " << a << std::endl;
        a++; // Incrementar a en 1
    } while (a < 5);

    std::cout << "" << std::endl;
    std::cout << "2.3) Bucle for" << std::endl;
    for (i = 0; i < 5; i++) { // Bucle for, se ejecuta desde i = 0 hasta i < 5, incrementando i en 1 en cada iteración
        std::cout << "i = " << i << std::endl;
    }

    std::cout << "" << std::endl;
    std::cout << "****************" << std::endl;
    std::cout << "DIFICULTAD EXTRA" << std::endl;
    std::cout << "****************" << std::endl;
    std::cout << "" << std::endl;

    for (i = 10; i <= 55; i++) {
        if (i % 2 == 0 && i != 16 && i % 3 != 0 || i == 55) { 
            // Imprimir los números pares entre 10 y 55, excepto el 16 y los múltiplos de 3
            std::cout << i << std::endl;
        }    
    }
}