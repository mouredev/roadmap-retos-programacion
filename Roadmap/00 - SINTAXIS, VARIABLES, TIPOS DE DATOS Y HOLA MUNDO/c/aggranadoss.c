/*
  Reto #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
  mouredev
  
  ANGEL GRANADOS ALIAS aggranadoss
 */


/*
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */

#include<stdio.h>
#include<stdbool.h>

int main(int argc, char argv[argc + 1]){

/********************************************/

/*Sitio oficial del lenguaje C  https://www.iso-9899.info/wiki/The_Standard*/


/********************************************/


// Comentario en una sóla línea


/********************************************/


/********************************************/

/*

  Comentario en varias líneas

*/


/********************************************/


/**
 * Comentario Doxygen se utiliza para generar documentacion
 * automaticamente a partir del codigo fuente. 

 */

/********************************************/

const int exit_success = 0;

float variable = 10.5; // variable
const int constante = 3.141592; // constante

/********************************************/

// Entero
int numero = 10;
short int numero_corto = 10;
long int numero_largo = 100000;
long long numero_muy_largo = 10000000000;


// Flotantes
float flotante = 3.141592;
double doble = 1.4142;
long double doble_largo = 3.423482349283479283;

// Flotantes con Complejos
float _Complex complejo_float = 1.0 + 2.0i;
double _Complex complejo_doble = 1.0 + 2.0i;
long double _Complex complejo_largo_doble = 1.0 + 2.0i;


// Caracteres

char caracteres = 'A';
unsigned char caracter_sin_signo = 'B';


// Booleano

bool boleano = true;
bool boleano_2 = false;

// Imprimir Hola y el nombre del lenguaje de programación

printf("\n Hola, Lenguaje C \n\n");

return exit_success;

}
