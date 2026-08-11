#include <iostream>
#include <cstring>

// Las funciones siempre deben ser declaradas antes de ser utilizadas, ya sea mediante su prototipo o 
// mediante su definicion completa.
void primeraFuncion(); // Declaracion de la funcion primeraFuncion
void segundaFuncion(int numero); // Declaracion de la funcion segundaFuncion, la cual recibe un parametro de tipo entero
int tercerFuncion(int numero1, int numero2); // Declaracion de la funcion tercerFuncion, la cual recibe dos parametros de 
//tipo entero y retorna un valor de tipo entero

// No es posible declarar una funcion dentro de otra funcion, ya que esto generaria un error de compilacion.
// No es posible crear una funcion dentro de otra funcion, ya que esto generaria un error de compilacion. 
// Sin embargo, si es posible llamar a una funcion dentro de otra funcion, lo cual es una practica comun en la programacion.
int cuartaFuncion(int numero3, int numero4) {
    std::cout << "" << std::endl;
    std::cout << "Esta es la cuarta funcion." << std::endl;
    std::cout << "Esta funcion recibe dos parametros, los cuales son: " << numero3 << " y " << numero4 << std::endl;
    std::cout << "Esta funcion retorna un valor, el cual es la multiplicacion mas la suma de los dos parametros." << std::endl;
    return (numero3 * numero4) + tercerFuncion(numero3, numero4); // Llamada a la funcion tercerFuncion, pasando los valores 
    // de los parametros numero3 y numero4.
} // Otra forma de declarar una funcion es mediante su definicion completa, la cual incluye el tipo de retorno, el nombre de la 
// funcion, los parametros que recibe y el bloque de codigo que se ejecuta cuando la funcion es llamada.

int variableGlobal = 10; // Variable global, la cual puede ser utilizada en cualquier parte del programa, incluso dentro de 
// las funciones.
#define PI 3.14159 // Definicion de una constante, la cual se puede considerar como una variable global.
const int constanteGlobal = 20; // Definicion de una constante, la cual se puede considerar como una variable global.

int Multiplos(char cadena3[33], char cadena4[33]); // Declaracion de la funcion Multiplos, la cual recibe dos parametros de

int main() {

    int resultado1, resultado2; // Variables locales, las cuales solo pueden ser utilizadas dentro de la funcion main.
    char resultado3[20]= "Hola ";
    char cadena1[33] = "Este es un numero multiplo de 3";
    char cadena2[33] = "Este es un numero multiplo de 5";
    int resultado4;

    primeraFuncion(); // Llamada a la funcion primeraFuncion
    segundaFuncion(5); // Llamada a la funcion segundaFuncion, pasando el valor 5 como parametro
    resultado1 = tercerFuncion(10, 20); // Llamada a la funcion tercerFuncion, pasando los valores 10 y 20 como parametros y 
    //almacenando el resultado en la variable resultado
    std::cout << "" << std::endl;
    std::cout << "El resultado de la funcion tercerFuncion es: " << resultado1 << std::endl;     
    resultado2 = cuartaFuncion(3, 4); // Llamada a la funcion cuartaFuncion, pasando los valores 3 y 4 como parametros y
    //almacenando el resultado en la variable resultado2

    std::cout << "" << std::endl;
    std::cout << "El resultado de la funcion cuartaFuncion es: " << resultado2 << std::endl;

    // Funcion ya creada en c++, strcat, la cual concatena dos cadenas de caracteres
    std::strcat(resultado3, "Mundo"); // Llamada a la funcion strcat, la cual concatena dos cadenas de caracteres 
    //y retorna un puntero a la cadena resultante
    std::cout << "" << std::endl;
    std::cout << "El resultado de la funcion strcat es: " << resultado3 << std::endl;

    // Dificultad Extra
    std::cout << "" << std::endl;
    std::cout <<"******************" << std::endl;
    std::cout << "Dificultad Extra:" << std::endl;
    std::cout <<"******************" << std::endl;

    resultado4 = Multiplos(cadena1, cadena2);
    std::cout << "" << std::endl;
    std::cout << "El resultado de la funcion Multiplos es: " << resultado4 << std::endl;
    
}

void primeraFuncion() { // Esta funcion no recibe parametros y no retorna ningun valor.
    std::cout << "Hola, esta es la primera funcion." << std::endl;
    std::cout << "Esta funcion no recibe parametros y no retorna ningun valor." << std::endl;
}

void segundaFuncion(int numero) { // Esta funcion recibe un parametro de tipo entero y no retorna ningun valor.
    std::cout << "" << std::endl;
    std::cout << "Esta es la segunda funcion." << std::endl;
    std::cout << "Esta funcion recibe un parametro, el cual es el numero: " << numero << std::endl;
    std::cout << "Esta funcion tampoco retorna ningun valor." << std::endl;
}

int tercerFuncion(int numero1, int numero2) { // Esta funcion recibe dos parametros de tipo entero y retorna un valor de tipo entero.
    std::cout << "" << std::endl;
    std::cout << "Esta es la tercera funcion." << std::endl;
    std::cout << "Esta funcion recibe dos parametros, los cuales son: " << numero1 << " y " << numero2 << std::endl;
    std::cout << "Esta funcion retorna un valor, el cual es la suma de los dos parametros." << std::endl;
    return numero1 + numero2;
}

int Multiplos(char cadena3[33], char cadena4[33]) { // Esta funcion recibe dos parametros de tipo cadena y retorna un valor de tipo entero.

    int x=0;
    int i=0;
    do
    { 
        x++;
        if ((x % 3 == 0) && (x % 5 == 0)) {
            std::cout << "numero: " << x << " " << cadena3 << cadena4 << std::endl;
        }
        else if (x % 3 == 0) {
            std::cout << "numero: " << x << " " << cadena3 << std::endl;
        }
        else if (x % 5 == 0) {
            std::cout << "numero: " << x << " " << cadena4 << std::endl;
        }
        else {
            std::cout << "numero: " << x << std::endl;
            i++;
        }
    }
    while (x < 100);

    return i;     
}