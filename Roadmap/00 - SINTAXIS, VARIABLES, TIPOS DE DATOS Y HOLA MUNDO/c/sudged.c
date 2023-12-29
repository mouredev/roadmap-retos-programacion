#include <stdio.h> // son directivas del preprocesador que proporcionan la funcionalidad necesaria de los programas en c.
#include <stdbool.h> 

int main() //inicio del programa en C
{ 
	/* Sintaxis de comentarios en C:

	Existen dos tipos:
	- Comentario de una linea o simple // y se extiende hasta el final de la linea.
	- Comentario de varias lineas o multilineas /*  y termina con esto --> */
	*/


// Declaracion de una variable

int numero = 0; // (Declaro y inicializo) siempre hay que acabar con un ; porque se ha terminado la declaracion. Es una como si acabas de decir una frase y pones un .


// Declaracion de una constante 
const float PI = 3.14; // Cuando defines una constante en C, estás diciendo al compilador que este valor no debe ser modificado.



// Variables representando diferentes tipos de datos

char caracter = 'A'; // caracter
bool esdivertidoPorgramar = true; // Boleano
double precision = 2.7293; // Numero flotante de doble precision
*char saludo = "Hola"; // cadena de texto (opcion 1)
char saludo [] = "Adios"; // cadena de texto (opcion 2)


Imprimir en terminal

printf("Hola a todos!, Bienvenidos a C\n"); // cuando son cadenas de textos, es decir mas de una letra hay que añadir "".


return (0);
}