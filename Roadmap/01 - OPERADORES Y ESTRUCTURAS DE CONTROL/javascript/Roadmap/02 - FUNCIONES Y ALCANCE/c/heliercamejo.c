#include <stdio.h>
#include <math.h>

int global = 50;

void sin_retorno();
int con_retorno();
void sin_retorno_con_parametros(int);
float con_retorno_con_parametros(int);

int extra(char *, char *);

int main()
{
    int local = 10;
    printf("local=%d\n",local);
    sin_retorno();
    printf("%d\n", con_retorno());
    sin_retorno_con_parametros(local);
    printf("el area es: %0.2f\n", con_retorno_con_parametros(local));
    printf("%d numeros\n", extra("Hola", "Mundo"));
    return 0;
}

void sin_retorno()
{
    printf("Esto es una funcion sin retorno y sin parametros\n");
    printf("Global = %d\n", global);
}

int con_retorno()
{
    printf("Esto es una funcion con retorno = 50 y sin parametros\n");
    return 50;
}

void sin_retorno_con_parametros(int param)
{
    printf("Esto es una funcion sin retorno y con parametro=%d\n", param);
}

float con_retorno_con_parametros(int radio)
{
    printf("Esto es una funcion con retorno y con parametro\n");
    printf("Retorna el area del circulo\n");
    float area = 3.14 * pow(radio,2);
;    return  area;
}

int extra(char *cadena1, char *cadena2)
{
    int count = 0;
    for(int i = 0; i<=100; i++)
    {
        if (i%3==0 && i%5==0)
        {
            printf("%s%s",cadena1,cadena2);
        }
        else if (i%3==0)
        {
            printf("%s",cadena1);
        }
        else if (i%5==0)
        {
            printf("%s",cadena2);
        }
        else 
        {
            count++;
            printf("i=%d",i);
        }
        printf("\n");
    }
    return count;
}