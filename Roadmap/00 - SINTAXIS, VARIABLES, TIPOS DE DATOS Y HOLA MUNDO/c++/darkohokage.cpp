//https://cplusplus.com

//Con dos barras se crea un comentario de linea

/* Con barra y asterisco
se crea un comentario de 
varias lineas cerrando con asterisco y barra
*/

#include <iostream> //Se necesita incluir esta librería para las entradas y salidas en c++

using namespace std; //se utilizapara poder utilizar los identificadores de la biblioteca estandar sin tener que usar std:: aunque no es la mejor de las prácticas

main()
{
const constante = 100; //con la palabra reservada const podemos declarar una constante seguidamente del nombre y del valor que va a tener
int entero = 10; /*para decarar una variable que almacenará valores de tipo enteros de utiliza la parabra reservada int seguido del nombre 
de la variable, una buena practica es inicializar la variable es decir darle un valor en el momento de la declaración*/
float decimal = 10.10; //se utiliza para declarar numeros decimales usando mismo esquema que la anterior pero con la palabra float
doble decimales = 10.000020020203030203004040404; //se utiliza cuando se necesita trabajar con decimales muy grandes
bool logica = True; //esta es la forma de declarar una variable booleana de tipo logica, es decir, que sus valores son "true" o "false"
char texto = "Cadena de Texto"; //char se utiliza para declarar una variable de tipo cadena de texto

cout <<"¡Hola, C++!" <<endl; //con cout se imprime en pantalla y el comando endl permite devolver el cursor en la siguiente linea
  
}
