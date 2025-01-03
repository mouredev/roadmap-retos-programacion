// #00 Sintaxis, variables, tipos de datos y hola mundo
// Autor: Clotrack | Lenguaje: C | Publucacion: 26/12/2023 | Correccion: 21/07/2024

#include <stdio.h>
#include <stdbool.h>

/* Ejercicio 1: Crea un comentario en el código y coloca la URL del sitio web oficial del
    lenguaje de programación que has seleccionado. */

// No hay web oficial del lenguaje C pero aqui se puede encontrar mucha informacion
// sobre el lenguaje: |  https://www.w3schools.com/c/index.php  |  

/* Ejercicio 2: Representa las diferentes sintaxis que existen de crear comentarios
   en el lenguaje (en una línea, varias...) */

// Esto es un comentario de linea

/* Esta es otra forma de hacer comentario, todo lo que escribamos dentro de estos simbolos 
    es un comentaro sin importar las lineas utilizadas */

int main() {

    /* Ejecicio 3: Crea una variable (y una constante si el lenguaje lo soporta). */

    char caracter = 'C';
    const int diasEnero = 31;

    /* Ejercicio 4: Crea variables representando todos los tipos de datos primitivos
    del lenguaje (cadenas de texto, enteros, booleanos...). */

    int numEntero = 3;
    short numcorto = -58;
    float numFlotante = 3.5;
    double numDoble = 35.55;
    char unCaracter = 'L';
    const int diasMarzo = 31;
    bool clotrackEstado = true;

    /* Ejercicio 5: Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"  */

    printf("Maquina puedes escribir 0 si Clotrack esta cuerdo y 1 si esta loco: %d\n", clotrackEstado);
    printf("¡Hola C bienvenido al mundo!");
    
}
