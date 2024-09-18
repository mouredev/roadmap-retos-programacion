#include <iso646.h>
#include <stdio.h>

int main() {
    //------------------Operadores
    // Aritméticos
    int suma = 3 + 3;
    int resta = 3 - 3;
    int multiplicacion = 3 * 3;
    int division = 3 / 3;
    int resto = 3 % 3;
    int incremento = ++suma;
    int decremento = --resta;
    printf("%d\n", suma);
    printf("%d\n", resta);
    printf("%d\n", multiplicacion);
    printf("%d\n", division);
    printf("%d\n", resto);
    printf("%d\n", incremento);
    printf("%d\n", decremento);

    // Asignación
    suma += 5;
    resta -= 5;
    multiplicacion *= 5;
    division /= 5;
    resto %= 5;
    int andOperator = 3 & 3;
    int orOperator = 3 | 3;
    int xorOperator = 3 ^ 3;
    int right = 3 >> 3; // desplaza los bits 3 posiciones a la derecha
    int left = 3 << 3; // desplaza los bits 3 posiciones  a la izquierda

    printf("%d\n", suma);
    printf("%d\n", resta);
    printf("%d\n", multiplicacion);
    printf("%d\n", division);
    printf("%d\n", resto);
    printf("%d\n", andOperator);
    printf("%d\n", orOperator);
    printf("%d\n", xorOperator);
    printf("%d\n", right);
    printf("%d\n", left);

    // Comparación
    printf("%d\n", 1 == 1);
    printf("%d\n", 1 != 1);
    printf("%d\n", 1 > 1);
    printf("%d\n", 1 < 1);
    printf("%d\n", 1 >= 1);
    printf("%d\n", 1 <= 1);

    // Operadores lógicos
    int x = 5;
    printf("%d\n", x < 5 &&  x < 10); //AND
    printf("%d\n", x < 5 || x < 4); //OR
    printf("%d\n", !(x < 5 && x < 10)); //NOT

    //--------------------------- Estructuras de control
    //  If - else

    if (x == 5) {
        printf("X es 5\n");
    } else if (x > 5) {
        printf("X es mayor que 5\n");
    } else {
        printf("X es menor que 5\n");
    }

    // Switch
    switch (x) {
        case 5:
            printf("X es 5\n");
            break;
        case 4:
            printf("X es 4\n");
            break;
        case 3:
            printf("X es 3\n");
            break;
        default:
            printf("No es nada\n");
    }

    // While
    while(x < 7) {
        printf("X vale %d\n", x);
        x++;
    }

    do {
        printf("X vale %d\n", x);
        x++;
    } while(x < 10);

    // For
    for(int i = 0; i <= 5; i++) {
        if (i == 3){
            continue;
        } else if (i == 5) {
            break;
        }
        printf("i vale %d\n", i);
    }

    //-------------- Ejercicio
    printf("** Ejercicio **\n");
    for (int i = 10; i <= 55; i++) {
        if (i % 2 == 0) {
            if (i != 16 && i % 3 != 0) {
                printf("%d\n", i);
            }
        }
    }

    return 0;
}
