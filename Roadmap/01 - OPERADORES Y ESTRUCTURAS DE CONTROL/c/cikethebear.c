// CikeTheBear - https://github.com/CikeTheBear/

// Operadores y Estructuras de Control en C

#include <stdio.h>

int main()
{
    printf("=== OPERADORES EN C ===\n");

    // Operadores Artiméticos
    printf("\n--- Operadores Artimeticos ---\n");
    printf("Suma: %d\n", 2 + 2);
    printf("Resta: %d\n", 10 - 4);
    printf("Multiplicacion: %d\n", 5 * 5);
    printf("Division: %d\n", 10 / 2);
    printf("Modulo: %d\n", 10 % 2);

    // Operadores Logicos
    printf("\n--- Operadores Logicos ---\n");
    printf("Operador Y / AND / &&: %d\n", 5 + 5 == 10 && 8 + 2 == 10);
    printf("Operador O / OR / ||: %d\n", 5 + 5 == 10 || 8 + 2 == 10);
    printf("Operador Negacion / NOT / !: %d\n", !5);

    // Operadores de Comparacion
    printf("\n--- Operadores de Comparacion ---\n");
    printf("Igual a: %d\n", 10 == 11);
    printf("Distinto a: %d\n", 10 != 11);
    printf("Mayor a: %d\n", 10 > 11);
    printf("Mayor o igual a: %d\n", 10 >= 11);
    printf("Menor a: %d\n", 10 < 11);
    printf("Menor o igual a: %d\n", 10 <= 11);

    // Operadores de Asignacion
    int oA;
    printf("\n--- Operadores de Asignacion ---\n");
    printf("Asignacion basica (=): %d\n", oA = 1);
    printf("Suma y asigna (+=): %d\n", oA += 1);
    printf("Resta y asigna (+=): %d\n", oA -= 1);
    printf("Multiplica y asigna (*=): %d\n", oA *= 2);
    printf("Divide y asigna (/=): %d\n", oA /= 1);
    printf("Modulo y asigna (%=): %d\n", oA %= 1);

    // Operadores de Identidad
    // En C no existen operadores de identidad, pero podemos lograr algo similar usando los punteros.

    int a = 0;
    int b = 1;
    
    int *pa = &a;
    int *pb = &b;

    printf("\n--- Operadores de Identidad ---\n");
    printf("a es *pa = %d\n", a == *pa);
    printf("*pb es b = %d\n",*pb == b);
    printf("a es *pb = %d\n", a == *pb);

    // Operadores de pertenencia
    // No existen en C

    // Operadores de Bits

    unsigned bitAND = 10 & 25;
    unsigned bitOR = 20 | 40;
    unsigned bitXOR = 55 ^ 44;
    unsigned bitNOT = ~5;
    unsigned bitShiftLeft = 3 << 1;
    unsigned bitShiftRight = 5 >> 2;

    printf("\n--- Operadores de Bits ---\n");
    printf("bit to bit AND (&): %d\n", bitAND);
    printf("bit to bit OR (|): %d\n", bitOR);
    printf("bit to bit XOR (^): %d\n", bitXOR);
    printf("bit to bit NOT (~): %d\n", bitNOT);
    printf("bit to bit Shift Left (<<): %d\n", bitShiftLeft);
    printf("bit to bit Shift Right >>): %d\n", bitShiftRight);

    // Estructuras de Control
    printf("\n=== ESTRUCTURAS DE CONTROL EN C ===\n");

    //  Estructuras Condicionales
    int condA = 3;
    int condB = 0;

    printf("\n--- Estructuras Condicionales ---\n");

    printf("\n--- if ---\n");
    if (condA == 0) {
        printf("condA es 0\n");
    }
    else if (condA == 1) {
        printf("condA es 1\n");
    }
    else {
        printf("condA no es ni 0 ni 1\n");
    }

    printf("\n--- switch ---\n");
    switch (condB) {
        case 0:
            printf("La opcion es 0\n");
            break;

        case 1:
            printf("La opcion es 1\n");
            break;

        case 2:
            printf("La opcion es 2\n");
            break;

        default:
            printf("La opcion se sale del rango\n");
            break;
    }

    //  Estructuras de Iteracion
    int iteA = 5;
    int iteB = 0;
    int iteC = 0;

    printf("\n--- Estructuras de Iteracion ---\n");

    printf("\n--- for ---\n");
    for (int i = 0; i < iteA; i++) {
        printf("Iteracion for: %d\n", i);
    }

    printf("\n--- while ---\n");
    while (iteB < 5) {
        printf("Iteracion while: %d\n", iteB);
        iteB++;
    }


    printf("\n--- do while ---\n");
    do {
        printf("Iteracion do-while: %d\n", iteC);
        iteC++;
    } while (iteC < 5);


    // Dificultad extra
    printf("\n=== DIFICULTAD EXTRA ===\n");

    printf("--- Programa que imprime numeros con ciertas condiciones ---\n"); 

    for (int i = 10; i <= 55; i += 2) {
        if (i == 16 || i % 3 == 0) continue;
        printf("Numero: %d\n", i);
    }

    return 0;
}