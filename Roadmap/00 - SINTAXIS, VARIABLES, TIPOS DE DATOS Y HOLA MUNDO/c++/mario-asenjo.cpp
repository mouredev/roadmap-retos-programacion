//RETO #00 - EJERCICIO

// - 1. Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.

// - 2. Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

// - Comentario de una sola línea con sitio oficial de C++ : https://isocpp.org/.

/* <-- Comentario multilínea
   - Así comentamos varias líneas de código. - Finalizamos comentario así --> */ 

// - 3. Crea una variable (y una constante si el lenguaje lo soporta).

#include <iostream> //Incluimos librerías de input y output.

int main(){ //Declaramos la funcion main.

    int variable_entera = -1; //Declaramos la variable entera.
    const int CONSTANTE_ENTERA = -1; //Declaramos la constante entera.

// - 4. Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).

    //Tipos de datos Enteros
    int entero = 43; // Entero de 4 bytes (tamaño puede variar según el compilador).
    short entero_corto = 300; // Entero corto, generalmente de 2 bytes.
    long entero_largo = 123456789; // Entero largo, normalmente de 4 u 8 bytes.
    long long entero_mas_largo = 9876543210; // Entero aún más largo, generalmente de 8 bytes
    unsigned int enteroSinSigno = 100;  // Entero sin signo, solo valores positivos
    unsigned short cortoSinSigno = 50000;  // Entero corto sin signo
    unsigned long largoSinSigno = 123456789;  // Entero largo sin signo
    unsigned long long muyLargoSinSigno = 1234567890123456789ULL;  // Entero largo sin signo y mayor rango

    // Tipos de Punto Flotante:
    float flotante = 3.14f;  // Número en coma flotante de precisión simple, normalmente de 4 bytes
    double doble = 3.1415926535;  // Número en coma flotante de precisión doble, generalmente de 8 bytes
    long double muyPreciso = 3.14159265358979323846L;  // Número de precisión extendida (generalmente 8 o 16 bytes)

    // Tipo de Caracteres:
    char caracter = 'A';  // Carácter o entero pequeño, almacenado en 1 byte
    unsigned char caracterSinSigno = 255;  // Carácter sin signo, valores de 0 a 255
    wchar_t caracterAncho = L'Ñ';  // Carácter ancho, útil para Unicode, generalmente 2 o 4 bytes

    // Tipo Booleano:
    bool booleano = true;  // Booleano, puede ser true (1) o false (0), generalmente 1 byte

    // Tipo Vacío (void no tiene ejemplo directo, pero se usa en funciones):
    // void no puede tener variables, se usa para funciones que no devuelven un valor.

// - 4. - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

    std::string nombreLenguaje = "C++";
    std::cout<<"El lenguaje elegido : "<<nombreLenguaje<<std::endl;

    return 0;
}