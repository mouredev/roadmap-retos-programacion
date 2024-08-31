#include <stdio.h>
#include <stdbool.h>

// No existe página oficial, por lo que adjunto la wikipedia
// https://es.wikipedia.org/wiki/C_(lenguaje_de_programaci%C3%B3n)

//Esto es un comentario de una sola línea

/*
Esto es un comentario multilínea.
*/

const char GLOBAL[] =  "Constante global";
int VARIABLE = 10;

int ENTERO = 10000;
short ENTERO_CORTO = 5;
long ENTERO_LARGO = 1010010101;
long long ENTERO_MUY_LARGO = 999999999999999;
float DECIMAL = 10.54;
double DECIMAL_PRECISO = 10.44553434234;
long double DECIMAL_MUY_PRECISO = 43.3421342342341234141234;
char CARACTER = 1;
signed char CARACTER_FIRMADO = 1;
unsigned char CARACTER_SIN_SIGNO = 1;
bool BOOLEANO = true;

int main() {
    
    const char LOCAL[] = "Constante local";

    printf("Esto es una constante global: %s\n", GLOBAL);
    printf("Esto es una constante local: %s\n", LOCAL);
    printf("Esto es una variable de tipo int: %d\n", VARIABLE);

    printf("Hola mundo!");

}
