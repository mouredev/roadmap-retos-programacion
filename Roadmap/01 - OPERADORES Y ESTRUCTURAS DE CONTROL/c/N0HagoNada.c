#include <stdio.h>

int main()
{
    // Operadores aritméticos
    int suma = 5 + 3;
    int resta = 5 - 3;
    int multiplicacion = 5 * 3;
    double division = 5 / 3.0;
    int modulo = 5 % 3;

    printf("Suma: %d\n", suma);
    printf("Resta: %d\n", resta);
    printf("Multiplicacion: %d\n", multiplicacion);
    printf("Division: %.2f\n", division);
    printf("Modulo: %d\n", modulo);

    // Operadores lógicos y de comparación
    int a = 5, b = 3;
    int mayor = a > b;
    int menor_o_igual = a <= b;
    int igual = a == b;
    int diferente = a != b;
    int y_logico = (a > b) && (a != 0);
    int o_logico = (a < b) || (b < 5);

    printf("Mayor: %d\n", mayor);
    printf("Menor o igual: %d\n", menor_o_igual);
    printf("Igual: %d\n", igual);
    printf("Diferente: %d\n", diferente);
    printf("Y lógico: %d\n", y_logico);
    printf("O lógico: %d\n", o_logico);

    // Operadores de bits
    unsigned int and_bits = a & b;
    unsigned int or_bits = a | b;
    unsigned int xor_bits = a ^ b;
    unsigned int not_bits = ~a;
    unsigned int desplazamiento_izquierda = a << 1;
    unsigned int desplazamiento_derecha = a >> 1;

    printf("AND bits: %u\n", and_bits);
    printf("OR bits: %u\n", or_bits);
    printf("XOR bits: %u\n", xor_bits);
    printf("NOT bits: %u\n", not_bits);
    printf("Desplazamiento izquierda: %u\n", desplazamiento_izquierda);
    printf("Desplazamiento derecha: %u\n", desplazamiento_derecha);

    // Estructuras de control
    // Condicional: if-else
    if (a > b)
    {
        printf("a es mayor que b\n");
    }
    else
    {
        printf("a no es mayor que b\n");
    }

    // Iterativa: while
    int contador = 3;
    while (contador > 0)
    {
        printf("Contador: %d\n", contador);
        contador--;
    }

    // Iterativa: for
    for (int i = 0; i < 3; i++)
    {
        printf("For ciclo: %d\n", i);
    }

    // pcional
    for (int i = 10; i <= 55; i++)
    {
        if (i % 2 == 0 && i != 16 && i % 3 != 0)
        {
            printf("%d\n", i);
        }
    }

    return 0;
}
