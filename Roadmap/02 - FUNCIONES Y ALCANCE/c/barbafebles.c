
// Funciondes definidas por el usuario 
#include <stdio.h>
#include <string.h>      // strlen

void simple()
{
    printf("Sin retorno\n");
}

void simple_personalizado(char *nombre)
{
    printf("Hola %s\n", nombre);
}

int simple_retorno()
{
    printf("Con retorno\n");
    return 30;
}
int suma(int a, int b)
{
    return a + b;
}
int simple_parametros(int param1, int param2)
{
    int resultado = suma(param1, param2);
    printf("La suma es: %d", resultado);
    return resultado;
}

// Funcion strlen 
void longitud_cadena(char *cadena)
{
    int longitud = strlen(cadena);
    printf("La longitud de la cadena es: %d\n", longitud);
}
// Variable global
double PI = 3.1416;

void imprimir_PI()
{
    printf("Imprimir el valor: %f\n", PI);
}
 /*DIFICULTAD EXTRA (opcional):*/
int imprimir(char *cadena1, char *cadena2) 
{
    int counter = 0;
    int i = 1;
    while(i <= 100) {
        if(i % 3 == 0 && i % 5 == 0) {
            printf("%s %s\n", cadena1, cadena2);
        } else if (i % 3 == 0) {
            printf("%s\n", cadena1);
        } else if(i % 5 == 0) {
            printf("%s\n", cadena2);
        } else {
            printf("%d\n", i);
            counter++;
        }
        i++;
    }
    return counter;
}

int main() 
{
    int variable_local = 5;
    printf("Variable local: %d, Variable global %f\n", variable_local, PI);
    simple();
    simple_personalizado("Pepe");
    simple_retorno();
    simple_parametros(5,3);
    longitud_cadena("Pruebas funciones");
    imprimir_PI();

    char* texto1 = "Hola";
    char* texto2 = "como estas?";
    int counter = imprimir(texto1, texto2);
    printf("Se imprimió el número en lugar de los textos %d veces.\n", counter);

    return 0;
}