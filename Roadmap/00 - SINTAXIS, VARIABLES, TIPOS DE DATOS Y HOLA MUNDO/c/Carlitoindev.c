// comentario en una sola linea

/*
comentario en varias lineas
*/

// Este lenguaje no tiene un sitio oficial, sino que funciona a travez de Manuales 
// Una referancia puede muy buena puede ser https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf  

#include <stdio.h>

int variable = 32;  // variable definida
#define cantidad = 100; // constante(es mucho mas rapida a la hora de ejecutarse que otras como <const>) 

// tipos de variables

int numero = 12; //  numero entero
long numero2; // numero entero pero mas largo que el admitido por <int>
char letra = 'r'; // un caracter independirnte o parte de una cadena
float dinero = 3.05; // numeros reales hasta 6 decimales.
double cuenta_bancaria = 123131312312312312312.312312312312312; // reales hasta 14 decimales.   

int main(void){
    printf("Hola C\n");
}
