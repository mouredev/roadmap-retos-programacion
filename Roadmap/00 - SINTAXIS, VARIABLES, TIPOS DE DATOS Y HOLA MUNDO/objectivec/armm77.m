// armm77 ver. 0.1

// - Crea un comentario en el código y coloca la URL del sitio web oficial del
//   lenguaje de programación que has seleccionado.

// Documentacion oficial Apple
// https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Introduction/introObjectiveC.html

// Documentacion Alternativa GNUStep
// https://gnustep.github.io/developers/documentation.html

// - Representa las diferentes sintaxis que existen de crear comentarios
//   en el lenguaje (en una línea, varias...).
 
// 1. Comentario de una sola linea, se utiliza.
/*
   2. Comentario de varias lineas,
      seccion de codigo o documentacion.
 */

// - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {

// - Crea una variable (y una constante si el lenguaje lo soporta).
    int weight = 0; // Variable
    const int  LENGTH = 10; // Constante
    const char NEWLINE = '\n'; // Constante
    const float PI = 3.1415926535; // Constante
    const double WIDTH = 47.120577; // Constante

/*
   - Crea variables representando todos los tipos de datos primitivos
     del lenguaje (cadenas de texto, enteros, booleanos...).
 
     Al ser Objective-C una variantes del lenguaje C con clases al estilo de
     Smalltalk, hereda los tipos de datos del mismo C.
*/
    int i = 1; // valor entero
    char c = 'c'; // valor caracter
    float f = 1.11111111; // valor decimal
    double d = 12.2222222; // valor decimal
    BOOL Y = YES; // valor boleano
    BOOL N = NO; // valor boleano

    @autoreleasepool {
        NSLog(@"Hola, Mundo!");
        NSLog(@"Variable: %d", weight);
        NSLog(@"Valores costantes: %d, %f, %f",LENGTH,PI,WIDTH);
        NSLog(@"Salto de linea %c",NEWLINE);
        printf("Valor entero: %d \n", i);
        printf("Valor caracter: %c \n", c);
        printf("Valor decimal: %f \n", f);
        printf("Valor decimal: %f \n", d);
        NSLog(@"Valor boleano: %d", Y);
        NSLog(@"Valor boleano: %d", N);
    }
    return 0;
}
