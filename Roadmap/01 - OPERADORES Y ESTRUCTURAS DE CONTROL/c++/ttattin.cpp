#include <iostream>
#include <string>

int main() {
    // Operadores aritméticos
    std::cout << "Operadores aritméticos" << std::endl;
    int a = 10;
    int b = 20;
    std::cout << "a: " << a << std::endl;
    std::cout << "b: " << b << std::endl;
    std::cout << "a + b: " << a + b << std::endl;
    std::cout << "a - b: " << a - b << std::endl;
    std::cout << "a * b: " << a * b << std::endl;
    std::cout << "a / b: " << a / b << std::endl;
    std::cout << "a % b: " << a % b << std::endl;

    // Operadores relacionales
    std::cout << "Operadores relacionales" << std::endl;
    std::cout << std::boolalpha;
    std::cout << "a == b: " << (a == b) << std::endl;
    std::cout << "a != b: " << (a != b) << std::endl;
    std::cout << "a > b: " << (a > b) << std::endl;
    std::cout << "a < b: " << (a < b) << std::endl;
    std::cout << "a >= b: " << (a >= b) << std::endl;
    std::cout << "a <= b: " << (a <= b) << std::endl;

    // Operadores lógicos
    std::cout << "Operadores lógicos" << std::endl;
    bool c = true;
    bool d = false;
    std::cout << "c: " << c << std::endl;
    std::cout << "d: " << d << std::endl;
    std::cout << "c && d: " << (c && d) << std::endl;
    std::cout << "c || d: " << (c || d) << std::endl;
    std::cout << "!c: " << !c << std::endl;
    std::cout << "!d: " << !d << std::endl;

    // Operadores de asignación
    std::cout << "Operadores de asignacion" << std::endl;
    std::cout << "a: " << a << std::endl;
    a = 5;
    std::cout << "Después de asignar a = 5" << std::endl;
    std::cout << "a: " << a << std::endl;

    std::cout << "Incrementamos a en 7 unidades" << std::endl;
    a += 7;
    std::cout << "a: " << a << std::endl;

    std::cout << "Disminuimos a en 7 unidades" << std::endl;
    a -= 7;
    std::cout << "a: " << a << std::endl;

    std::cout << "Multiplicamos a por 2" << std::endl;
    a *= 2;
    std::cout << "a: " << a << std::endl;

    std::cout << "Dividimos a por 2" << std::endl;
    a /= 2;
    std::cout << "a: " << a << std::endl;

    std::cout << "Modulamos a por 2" << std::endl;
    a %= 2;
    std::cout << "a: " << a << std::endl;

    // Operadores de Bits
    std::cout << "Operadores de Bits" << std::endl;
    int e = 10;
    int f = 20;
    std::cout << "e: " << e << std::endl;
    std::cout << "f: " << f << std::endl;
    std::cout << "e & f: " << (e & f) << std::endl;
    std::cout << "e | f: " << (e | f) << std::endl;
    std::cout << "e ^ f: " << (e ^ f) << std::endl;
    std::cout << "~e: " << ~e << std::endl;
    std::cout << "e << 1: " << (e << 1) << std::endl;
    std::cout << "f >> 1: " << (f >> 1) << std::endl;
    std::cout << "e &= f" << std::endl; 
    e &= f;
    std::cout << "e: " << e << std::endl;

    std::cout << "e |= f" << std::endl;
    e |= f;
    std::cout << "e: " << e << std::endl;

    std::cout << "e ^= f" << std::endl;
    e ^= f;
    std::cout << "e: " << e << std::endl;
    
    // Condicional ternario
    std::cout << "Condicional ternario" << std::endl;
    int g = 10;
    int h = 20;
    std::cout << "relacion = g > h ?" << std::endl;
    std::string relacion = g > h ? "g es mayor que h" : "g es menor que h";
    std::cout << relacion << std::endl;

    // Estructuras de control if, else, else if
    std::cout << "Estructuras de control if, else, else if" << std::endl;
    if (g > h) {
        std::cout << "g es mayor que h" << std::endl;
    } else {
        std::cout << "g es menor que h" << std::endl;
    }

    if (g > h) {
        std::cout << "g es mayor que h" << std::endl;
    } else if (g < h) {
        std::cout << "g es menor que h" << std::endl;
    } else {
        std::cout << "g es igual a h" << std::endl;
    }

    // Estructuras de control switch
    std::cout << "Estructuras de control switch" << std::endl;
    switch (g) {
        case 10:
            std::cout << "g es 10" << std::endl;
            break;
        case 20:
            std::cout << "g es 20" << std::endl;
            break;
        case 30:
            std::cout << "g es 30" << std::endl;
            break;
        default:
            std::cout << "g es distinto de 10, 20 y 30" << std::endl;
            break;
    }

    // Estructuras de control for
    std::cout << "Estructuras de control for" << std::endl;
    for (int i = 0; i < 10; i++) {
        std::cout << i << std::endl;
    }

    // Estructuras de control while
    std::cout << "Estructuras de control while" << std::endl;
    int j = 0;
    while (j < 10) {
        std::cout << j << std::endl;
        j++;
    }

    // Estructuras de control do-while
    std::cout << "Estructuras de control do-while" << std::endl;
    int k = 0;
    do {
        std::cout << k << std::endl;
        k++;
    } while (k < 10);

    // Excepciones try, throw, catch
    std::cout << "Excepciones try, throw, catch" << std::endl;
    try {
        throw "Hola, código de prueba";
    } catch (const char* e) {
        std::cout << e << std::endl;
    }



    // DIFICULTAD EXTRA
    std::cout << "DIFICULTAD EXTRA" << std::endl;
    for (int i = 10; i <= 55; i++) {
        if (i % 2 == 0 && i % 3 != 0 && i != 16) {
            std::cout << i << std::endl;
        }
    }
}


