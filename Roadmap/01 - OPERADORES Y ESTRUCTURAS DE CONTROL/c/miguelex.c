#include <stdio.h>

int main(){
    // operadores aritmeticos

    int a = 10;
    int b = 20;

    printf("Suma: %d\n", a + b);
    printf("Resta: %d\n", a - b);
    printf("Multiplicacion: %d\n", a * b);
    printf("Division: %d\n", a / b);
    printf("Modulo: %d\n", a % b);

    // operadores de asignacion

    a = 10;

    printf("Asignacion: %d\n", a);
    printf("Asignacion con suma: %d\n", a += 10);
    printf("Asignacion con resta: %d\n", a -= 10);
    printf("Asignacion con multiplicacion: %d\n", a *= 10);
    printf("Asignacion con division: %d\n", a /= 10);
    printf("Asignacion con modulo: %d\n", a %= 10);

    // operadores de incremento y decremento
    ++a; // a = a
    printf("Incremento: %d\n", a);
    --a; // a = a
    printf("Decremento: %d\n", a);

    // operadores de relacion
    a = 10;

    printf("Igualdad: %d\n", a == b);
    printf("Desigualdad: %d\n", a != b);
    printf("Mayor que: %d\n", a > b);
    printf("Menor que: %d\n", a < b);
    printf("Mayor o igual que: %d\n", a >= b);
    printf("Menor o igual que: %d\n", a <= b);

    // operadores logicos
    a = 10;

    printf("AND: %d\n", a > 5 && a < 15);
    printf("OR: %d\n", a > 5 || a < 15);
    printf("NOT: %d\n", !(a > 5 && a < 15));

    // operadores de desplazamiento

    a = 10;

    printf("Desplazamiento a la izquierda: %d\n", a << 2);
    printf("Desplazamiento a la derecha: %d\n", a >> 2);

    // operadores de bits

    a = 10;
    b = 7;
    printf("Bitwise AND: %d \n", a & b);
    printf("Bitwise OR: %d \n", a | b);
    printf("Bitwise XOR: %d \n", a ^ b);
    printf("Bitwise NOT: %d \n", ~a);

    // if else

    if (a > b)
    {
        printf("a es mayor que b\n");
    }
    else
    {
        printf("a es menor que b\n");
    }

    // switch case

    int option = 1;
    switch (option)
    {
        case 1:
        {
            printf("Realizar el registro de n usuarios\n");
            break;
        }
        case 2:
        {
            printf("Buscar usuario mediante su ID\n");
            break;
        }
        default:
        {
            printf("Este caso no existe!\n");
            break;
        }
    }

    // for

    for (int i = 1; i <= 10; i++)
    {
        printf("%d, ", i);
    }
    printf("\n");

    // do while

    option = 0;
    do {
        printf("Ingrese 1 para salir del ciclo\n");
        scanf("%d", &option);
    } while (option != 1);
    

    // while

    int i = 1;

    while (i <= 10)
    {
        printf("%d, ", i);
        i++;
    }
    printf("\n");

    // Extra

    for (int i = 10; i <= 55; i++)
    {
        if (i != 16 && i % 2 == 0 && i % 3 != 0)
        {
            printf("%d, ", i);
        }
    }
    printf("\n");
    
}