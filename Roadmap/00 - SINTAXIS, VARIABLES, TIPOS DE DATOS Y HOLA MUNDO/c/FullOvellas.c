/*
 * Documentación y estándar de C
 * +-----------------------------------------------------------------------------------------------------------------------+
 * |https://devdocs.io/c/                                                                                                  |
 * |https://web.archive.org/web/20180118051003/http://www.open-std.org/jtc1/sc22/wg14/www/abq/c17_updated_proposed_fdis.pdf|
 * +-----------------------------------------------------------------------------------------------------------------------+
 */

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>

// Comentario monolínea

/*
 * Comentario
 * multilínea
 */

// Constante definida con una macro object-like
#define MEANING_OF_LIFE 42

int main() {
    // Constante definida con la palabra reservada `const`
    const double PI = 3.14159265;

    // Variable
    int one = 1;

    // Tipos primitivos
    // Los valores máximos y mínimos se define en el header `limits.h` y `float.h`
    char c = 'a';
    unsigned char uc = 255;
    signed char sc = 127;
    short s = 32767;
    unsigned short us = 65535;
    int i = 32767;
    unsigned int ui = 65535;
    long l = 2147483647l;
    unsigned long ul = 4294967295ul;
    long long ll = 9223372036854775807ll;
    unsigned long long ull = 18446744073709551615ull;
    float f = 1.1f;
    double d = 1.1;
    long double ld = 1.1l;
    // Necesario incluír el header `stdbool.h` para tener acceso a las macros `true` y `false`.
    // El tipo `_Bool` nos ayuda a prevenir errores de overflow
    _Bool b = true;
    // Entero sin signo definido en el header `stddef.h`, su tamaño depende de la plataforma
    size_t arch = 0;
    // Entero con signo definido en el header `stddef.h`, representa la diferencia entre punteros del mismo tipo
    ptrdiff_t pd = 0;


    // Enteros fixed-width
    // Longitud exacta:
    int8_t i8 = INT8_MAX;
    int16_t i16 = INT16_MAX;
    int32_t i32 = INT32_MAX;
    uint8_t u8 = UINT8_MAX;
    uint16_t u16 = UINT16_MAX;
    uint32_t u32 = UINT32_MAX;
    uint64_t u64 = UINT64_MAX;

    // Longitud mínima
    int_least8_t il8 = 0;
    uint_least8_t uil8 = 0;
    // etc...

    // Más rápido
    int_fast8_t if8 = 0;
    uint_fast8_t uif8 = 0;
    // etc...

    // Puntero
    intptr_t ip = INTPTR_MAX;

    // Longitud máxima
    intmax_t im = INTMAX_MAX;
    uintmax_t uim = UINTMAX_MAX;

    // C no tiene un tipo string básico
    const char msg[] = "¡Hola, C!";

    puts(msg);
}
