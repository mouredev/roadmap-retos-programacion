//https://learn.microsoft.com/en-us/cpp/c-language/?view=msvc-170

// Comentario

/*Esto tambien es
un comentario en
varias lineas*/

#include <stdio.h>
#include <string.h>

int main(){
    char myVariable[] = "Mi variable";
    strcpy(myVariable, "Nuevo valor");

    int myInt = 4; // un numero entero
    char myChar = 'h'; // un caracter
    float myFloat = 4.35; // numero flotante
    _Bool myBool = 1; // 1 es True

    const int y = 1;

    printf("!Hola Mundo!!!");

    return 0;
}
