#include <stdio.h> // printf
#include <stdbool.h> // bool 

// No existe pagina oficial de C 
// URL = https://www.learn-c.org

/*
    Para comentar varias lineas 
    Se puede hacer de esta manera
*/

#include <stdio.h> // printf

// Crea una variable 
int num = 1; 
int num2 = 2;

// Variable constante
const float PI = 3.1416; 

// Variables 
int entero = 1;                                 // Tipo entero 
int *punteroAEntero = &entero;                  // Puntero a una variable de tipo entero 
short int enteroCorto = 1;                      // Tipo entero corto 
long int enteroLargo = 100000;                  // Tipo entero largo 
long double dobleLargo = 3.1415926535897932;    // Tipo entero doble largo 
unsigned int enteroSinSigno = 20;               // Tipo entero sin signo 
unsigned long largoSinSigno = 30;               // Tipo entero largo sin signo 
unsigned short enteroCorto = 23;                // Tipo entero corto sin signo 
float flotante = 25.554;                        // Tipo flotante
double doble = 30.5;                            // Tipo doble 
char caracter = 'A';                            // Tipo caracter 
int array[5] = {1, 2, 3, 4, 5};                 // Array de enteros
bool boole = true;                              // Tipo booleano

// Programa 
int main()
{
    printf("Hola, C\n");
    return 0;
}
