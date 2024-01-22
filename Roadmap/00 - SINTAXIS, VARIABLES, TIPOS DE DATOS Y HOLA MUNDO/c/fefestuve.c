#include <stdio.h>
#include <stdlib.h>

//No existe pagina oficial para C
/*tambien se puede escribir un comentario de varias lineas
usando esta sintaxis*/

//se puede escribir una constante con un define
#define CONSTANTE 23

int main(void){
    //tambien se puede de esta forma
    const int entero = 23;
    int entero2 = 10;
    long largo = 47398344837493;

    float decimal = 0.5;
    double doble = 0.473892762783;

    char caracter = 'A';
    char string1[5] = "Hola";
    //tambien se puede generar un string de esta forma
    char *string2 = malloc(5);
    string2 = "Hola";

    printf("¡Hola C!");
}