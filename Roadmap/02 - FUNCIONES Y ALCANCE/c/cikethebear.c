// CikeTheBear - https://github.com/CikeTheBear/

#include <stdio.h>

// === Funciones ===

// Funcion simple ---
void simple()
{
    printf("Hola, C\n");
}

// Funcion con argumento ---
void conArgumento(char *texto)
{
    printf("%s\n", texto);
}

// Funcion con mas de un argumento ---
void conArgumentos(char *texto, int numero)
{
    printf("El primer argumento es %s y el segundo es %d\n", texto, numero);
}

// Funcion con argumento por defecto (En C no existe esta posibilidad, pero se puede "simular" de la siguiente manera) ---
void conArgumentoPorDefecto(char *texto)
{
    if (texto == NULL)
    {
        texto = "Valor por defecto";
    }
    printf("%s\n", texto);
}

// Funcion con retorno ---
int conRetorno(int n, int m)
{
    int suma = n + m;
    return suma;
}

// Funcion dentro de una funcion (Tecnicamente, C no lo permite, por lo menos no de manera estandar, pero compilar con GCC se salta esa restriccion) ---
void funcion_externa(char *texto_1, int n)
{

    int funcion_interna(int n)
    {

        int resultado = n * 5;

        return resultado;
    }

    printf("Funcion Externa dice: %s\n", texto_1);
    printf("Funcion Interna calcula: %d\n", funcion_interna(n));
}

// Dificultad Extra ---

int dificultad_extra(char *cadena_1, char *cadena_2)
{
    for (int i = 1; i >= 1 && i <= 100; i++)
    {
        if (i % 3 == 0 && i % 5 == 0)
        {
            printf("%s%s\n", cadena_1, cadena_2);
        }
        if (i % 3 == 0)
        {
            printf("%s\n", cadena_1);
        }
        else if (i % 5 == 0)
        {
            printf("%s\n", cadena_2);
        }
        else
        {
            printf("%d\n", i);
        }
    }
}

// ====== Funcion prinicipal ======
int main()
{
    simple();

    conArgumento("Argumento");

    conArgumentos("Palabra", 34);

    conArgumentoPorDefecto(NULL);

    printf("Funcion con retorno: %d\n", conRetorno(50, 25));

    funcion_externa("Por dentro, tengo una calculadora que multiplica por 5", 5);

    dificultad_extra("Fizz", "Buzz");

    return 1;
}
