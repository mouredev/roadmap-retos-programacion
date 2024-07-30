/*
 EJERCICIO:
 * -1º Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * -2º Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * -3º Crea una variable (y una constante si el lenguaje lo soporta).
 * -4º Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * -5º Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */
#include <stdio.h>
int main(void){
    //------1º----------//

      //C no tiene sitio oficial 

    //-------2º---------//

      //comentario en una linea 
      /*comentario en varias
      lineas*/

    //-------3º----------//

    //variable
    int num = 1;

    //const
    const int num2 = 2;

    //-------4º--------//
    int integer = 1; // Variable de tipo entero
    char caracter = 'a'; // Variable de tipo carácter
    float my_float = 5.5; // Variable de tipo float (precisión simple)
    double numberDouble = 2.4555; // Variable de tipo double (mayor precisión que float)
    long num_long = 1222222222; // Variable de tipo long (tamaño puede variar según la plataforma)
    unsigned char valor = 160; // Variable de tipo unsigned char (rango de 0 a 255)
    short int num_short = 123; // Variable de tipo short int (tamaño suele ser 2 bytes)
    unsigned short int unsigned_short_int = 64000; // Variable de tipo unsigned short int (rango de 0 a 65535)
    signed int signed_int = -400; // Variable de tipo signed int (puede ser negativo)
    unsigned int unsigned_int = 2; // Variable de tipo unsigned int (solo valores positivos)
    signed long int signed_long_int = -44444444; // Variable de tipo signed long int (puede ser negativo)
    unsigned long int unsigned_long_int = 44444444; // Variable de tipo unsigned long int (solo valores positivos)

    //------5º----------//

    char nombre_lenguaje = 'C';

    printf("¡Hola , %c\n " , nombre_lenguaje);
   
return 0;
}
   
   

/*El lenguaje C dedica nueve palabras para la identificación de los
 tipos de dato primitivos: void, char, int, float,
 double, short, long, signed e unsigned.Void: No es un tipo de dato en
 el sentido de que no se puede usar para declarar variables que contienen valores.
  Más bien, void se utiliza en el contexto de las funciones y punteros */