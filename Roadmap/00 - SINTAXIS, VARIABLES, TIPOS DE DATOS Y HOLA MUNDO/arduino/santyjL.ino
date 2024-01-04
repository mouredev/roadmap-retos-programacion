//https://www.arduino.cc/

// 00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO / documentacion de una linea

/*
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!
 * esta es la documentacion en varias lineas
*/


String lenguaje = "Arduino!"; //variabe
const int hora = 60; //constante

//datos primitivos

String texto = "esto es un string";
int numeroEntero = 50;
float numeroFlotante = 50.5;
bool boleano = true;

void setup (){
    Serial.begin(9600);
}

void loop(){

    Serial.print("¡Hola, "); // Sigue en la misma línea el siguiente print
    Serial.print(lenguaje); // El siguiente print se mostrará en la misma línea
    Serial.println("!"); // El siguiente print se mostrará en otra línea

    return;
}
