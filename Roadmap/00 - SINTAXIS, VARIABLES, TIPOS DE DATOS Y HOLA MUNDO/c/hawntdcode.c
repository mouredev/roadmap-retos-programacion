// Para comentarios de una linea, basta con usar la doble diagonal, mientras que para un comentario con salto de linea, es importante utilizar un asterisco despues de la diagonal, esto para ambos extremos.


/*Hola, este es el leguaje C, dicho lenguaje fue creado entre 1969 y 1972

https://www.c-language.org/

*/

// Para inicializar cualquier programa hecho en C, es necesario que se utilice #include <stdio.h>, con esto identificamos al archivo e indicamos como hay que darle el tratamiento

#include <stdio.h>
#include <stdbool.h>

// Usamos el #define cuando se quiere definir una constante, seguido del nombre de la constante, y el valor de esta.

#define PI 3.1416

int main(){
    // Si nos referimos a variables, estas se representan colocando primero el tipo de dato que va a almacenar, seguido del nombre de la variable, de esta manera se consigue inicializar

    char language = 'C';

    int age = 20;

    // Con float, podemos representar decimales, pero solo hasta un maximo de 4 Bytes (32 Bits)

    float height = 6.11;

    // Double permite reservar hasta 64 bits, permitiendo ser mas precisos en calculos complejos

    double random_number = 3.141590239;

    /*

    Si requerimos de la representacion de booleanos, el propio lenguaje como tal no lo incluye, fue en C99 que crearon la libreria stdbool, con esta libreria se podia ahora si, hacer el uso de booleanos

    */

    bool adult = true;

    printf("Hello, %c!\n", language);

    return 0;
}

