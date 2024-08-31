#include <stdint.h>
#include <stdio.h>

const uint8_t UPPER_BOUND = 55;
const uint8_t LOWER_BOUND = 10;

int main() {
    int32_t foo = 5;
    int32_t bar = 15;
    // Operadores aritméticos
    foo + bar; // 20
    foo - bar; // -15
    foo * bar; // 75
    bar / foo; // 3
    foo % foo; // 0
    ++foo;     // 6

    // Operadores a nivel de bit
    printf("%i\n", 2 & 1);
    printf("%i\n", 2 << 1);
    printf("%i\n", 2 >> 1);
    printf("%i\n", 2 | 1);

    // Operadores de asignación
    int32_t baz = 0;
    baz += 6; // 6
    baz -= 2; // 4
    baz /= 2; // 2
    baz *= 4; // 8
    baz %= 2; // 0

    // Operadores de comparación
    printf("%i\n", 1 > 2);  // 0
    printf("%i\n", 1 < 2);  // 1
    printf("%i\n", 1 >= 2); // 0
    printf("%i\n", 1 <= 2);  // 1
    printf("%i\n", 1 == 2);  // 0

    // Operadores lógicos
    1 && 0; // 0
    1 || 0; // 1

    // Estructuras de control
    // if
    if (5 == 2 + 2) {
        puts("Tenemos un problema");
    }

    // if-else
    if (5 == 2 + 2) {
        puts("Tenemos un problema");
    } else {
        puts("Las mates siguen funcionando");
    }

    // if-else if
    if (0) {
        puts("Cero");
    } else if (0 == 0) {
        puts("Cero ;)");
    } else {
        puts("No cero :(");
    }

    // for
    int32_t running_sum = 0;
    for (int32_t i = 0; i < 10; i++) {
        running_sum += i;
    }
    printf("Resultado de la suma: %i\n", running_sum);

    // while
    int32_t countdown = 10;
    while (countdown > 0) {
        printf("%i!\n", countdown);
        countdown--;
    }

    // do while
    int32_t c = 0;
    do {
        printf("%i\n", c);
        c--;
    } while (c > 0);

    // continue
    for (int32_t i = 0; i < 5; i++) {
        if (i == 3) {
            continue;
        }
        printf("%i\n", i);
    }

    // break
    for (int32_t i = 0; i < 5; i++) {
        if (i == 3) {
            break;
        }
        printf("%i\n", i);
    }

    // goto
    for (int32_t i = 0; i < 5; i++) {
        if (i == 3) {
            goto nos_fuimos;
        }
        printf("%i\n", i);
    }

nos_volvimos: {}
    // switch
    char command = 'q';
    switch(command) {
        case 'y':
            puts("Sí");
            break;
        case 'n':
            puts("No");
            break;
        case 'w':
        case 'a':
        case 's':
        case 'd':
            puts("Movimiento");
            break;
        case 'q':
            puts("Saliendo");
            break;
        default:
            printf("Comando '%c' no reconocido\n", command);
    }

    // Opcional: imprimir por consola los números pares entre 10 y 55
    // excluyendo el 16 y los múltiplos de 3
    for (uint8_t i = LOWER_BOUND; i <= UPPER_BOUND; i++) {
        if (i % 2 || (i % 3) == 0 || i == 16) {
            continue;
        }

        printf("%i\n", i);
    }
    return 0;

nos_fuimos:
    puts("Efectivamente nos fuimos");
    goto nos_volvimos;
}
