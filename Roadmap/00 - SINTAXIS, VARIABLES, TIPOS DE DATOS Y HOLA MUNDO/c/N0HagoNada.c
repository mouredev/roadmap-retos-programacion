#include <stdio.h>
#include <stdbool.h>
#include <stdint.h> // Para tipos de tamaño fijo

// Una pagina oficial podria ser https://www.learn-c.org/
/*
Comentarios en varias lienas
https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html
*/

int main()
{
    // Creación de una variable
    int ejemploVariable = 10;

    // Creación de una constante
    const float PI = 3.1416;

    // Variables representando todos los tipos de datos primitivos
    char unCaracter = 'A'; // Carácter
    int unEntero = 123;    // Número entero
    unsigned int enteroSinSigno = 20;
    short corto = 10;                                         // Entero corto
    unsigned short cortoSinSigno = 20;                        // Entero corto sin signo
    long largo = 123456789;                                   // Entero largo
    unsigned long largoSinSigno = 987654321;                  // Entero largo sin signo
    long long largoLargo = 123456789101112;                   // Entero largo largo
    unsigned long long largoLargoSinSigno = 1098765432112345; //
    long long int entero64 = 1234567890123456789;
    float unFlotante = 123.456;                        // Número flotante
    double unDoble = 123.456789;                       // Número de doble precisión
    long double dobleLargo = 3.14159265358979323846L;  // Número de doble precisión largo
    uint64_t entero64SinSigno = 18446744073709551615U; // Entero sin signo de 64 bits
    bool unBooleano = true;                            // Booleano (requiere #include <stdbool.h>)
    char *unaCadena = "Esto es una cadena de texto";   // Cadena de texto

    // Imprime por terminal el texto solicitado
    printf("¡Hola, C!\n");

    // Imprime los valores de las variables (opcional, para demostración)
    printf("Variable int: %d\n", ejemploVariable);
    printf("Constante float: %f\n", PI);
    printf("Entero sin signo: %u\n", enteroSinSigno);
    printf("Corto: %hd\n", corto);
    printf("Corto sin signo: %hu\n", cortoSinSigno);
    printf("Largo: %ld\n", largo);
    printf("Largo sin signo: %lu\n", largoSinSigno);
    printf("Largo largo: %lld\n", largoLargo);
    printf("Largo largo sin signo: %llu\n", largoLargoSinSigno);
    printf("char: %c\n", unCaracter);
    printf("int: %d\n", unEntero);
    printf("float: %f\n", unFlotante);
    printf("double: %lf\n", unDoble);
    printf("Doble largo: %Lf\n", dobleLargo);
    printf("Entero 64 bits: %ld\n", entero64);
    printf("Entero 64 bits sin signo: %lu\n", entero64SinSigno);
    printf("bool: %d\n", unBooleano); // En C, los booleanos se imprimen como enteros (0 para false, 1 para true)
    printf("char*: %s\n", unaCadena);

    return 0;
}