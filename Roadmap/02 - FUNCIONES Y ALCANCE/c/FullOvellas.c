#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

/* Opcional: función que recibe dos cadenas de texto y
 *     - Imprime los números del 1 al 100 pero:
 *         - Si el número es múltiplo de 3 se imprime el primer parámetro
 *         - Si el número es múltiplo de 5 se imprime el segundo parámetro
 *         - Si el número es múltiplo de 3 y 5 se muestran ambas cadenas concatenadas
 *     - Devuelve el número de veces que se mostró el número en lugar de un texto
 */
int my_fun(const char *first_param, const char *second_param) {
    int count = 0;
    for (int32_t i = 1; i <= 100; i++) {
        _Bool div_by_3 = i % 3 == 0;
        _Bool div_by_5 = i % 5 == 0;
        if (div_by_3) {
            printf("%s", first_param);
        }
        if (div_by_5) {
            printf("%s", second_param);
        }
        
        if (div_by_3 || div_by_5) {
            printf("\n");
            continue;
        }
        
        printf("%i\n", i);
        count++;
    }

    return count;
}

char higher_val_char(char c1, const char c2) {
    return c1 > c2 ? c1 : c2;
}

void say_hi() {
    puts("Hola!");
}

void say_hi_to_user(char *user_name) {
    if (user_name[0] == 0) {
        puts("Hola, Usuario");
    } else {
        printf("Hola, %s\n", user_name);
    }
}

const double PI = 3.141593;

int main() {
    printf("Char de valor más alto ('a', 'b')? %c\n", higher_val_char('a', 'b'));
    say_hi();
    say_hi_to_user("");
    char user_name[] = "FullOvellas";
    say_hi_to_user(user_name);

    // Variable global
    printf("Variable global: %f\n", PI);

    // Función del lenguaje
    printf("%f elevado a 2 es: %f\n", 2.0, exp2(2.0));

    int32_t x = 10;
    printf("Variable `x` en scope local: %i\n", x);
    {
        int32_t x = 32;
        printf("Variable `x` en scope local anidado: %i\n", x);
    }
    printf("Variable `x` sigue teniendo el valor anterior (%i) fuera del scope anidado\n", x);

    printf("Resultado de la función opcional: %i\n", my_fun("Hola", ", C"));

    return 0;
}

