// Esto es un comentario de una linea
/*Si deseas comentar varias lineas
puedes utilizar este formato*/
// No existe una pagina oficial de c++, sin embargo, esta es bastante buena: https://isocpp.org/

#include <iostream> // Libreria estandar de entrada y salida por terminal
#include <string> // Libreria estandar de cadenas de texto

int main() // Funcion principal, el programa inicia su ejecucion aqui
{
    //Para crear y utilizaruna variable en c++ se deben declarar primero, la sintaxis es la siguiente:
    int primero; // Declaracion de una variable de tipo entero llamada primero 
    float segundo; // Declaracion de una variable de tipo flotante llamada segundo (numeros reales con precision simple) 
    double tercero; // Declaracion de una variable de tipo doble llamada tercero (numeros reales con precision doble)
    long double cuarto; // Declaracion de una variable de tipo doble larga llamada cuarto (numeros reales con precision doble extendida)
    char quinto; // Declaracion de una variable de tipo caracter llamada quinto (un solo caracter)
    bool sexto; // Declaracion de una variable de tipo booleano llamada sexto (verdadero o falso)
    /*Las variables deben iniciar con una letra o con un guion bajo, no pueden iniciar con un numero ni con caracteres especiales
    , y no pueden contener espacios.*/
    // C++ distingue entre mayusculas y minusculas, por lo que "primero" y "Primero" son variables diferentes.
    
    // Para declarar diferentes variables del mismo tipo, se pueden separar por comas:
    int a, b, c; // Declaracion de tres variables de tipo entero llamadas a, b y c
    float x, y, z; // Declaracion de tres variables de tipo flotante llamadas x, y y z
    double p, q, r; // Declaracion de tres variables de tipo doble llamadas p, q y r
    char letra1, letra2, letra3; // Declaracion de tres variables de tipo caracter llamadas letra1, letra2 y letra3
    bool verdadero, falso; // Declaracion de dos variables de tipo booleano llamadas verdadero y falso

    // Importante resaltar que no existe un tipo de dato complejo en c++, sin embargo, se pueden utilizar librerias externas 
    // para trabajar con numeros complejos, como la libreria <complex>.

    // Para declarar una constante en c++, se utiliza la palabra reservada "const" antes del tipo de dato:
    const float PI = 3.14159; // Declaracion de una constante de tipo flotante llamada PI con el valor de 3.14159
    const double EULER = 2.71828; // Declaracion de una constante de tipo doble llamada EULER con el valor de 2.71828
    // Tambien es posible declarar constantes utilizando la palabra reservada "DEFINE" seguida del nombre de la constante y 
    // su valor, sin especificar el tipo de dato:
    #define GRAVEDAD 9.81 // Declaracion de una constante llamada GRAVEDAD con el valor de 9.81
    // Normalmente las constantes declaradas con #define se escriben antes de la función main y despues de las directivas
    // #include.
    // Las constantes declaradas con #define no llevan punto y coma al final.
    // Las Constantes se escriben en mayusculas para diferenciarlas de las variables.
    
    // Se puede asignar un valor a una variable en el momento de su declaración:
    int edad = 25; // Declaracion de una variable de tipo entero llamada edad con el valor de 25
    float altura = 1.75; // Declaracion de una variable de tipo flotante llamada altura con el valor de 1.75
    double peso = 70.5; // Declaracion de una variable de tipo doble llamada peso con el valor de 70.5
    char inicial = 'L'; // Declaracion de una variable de tipo caracter llamada inicial con el valor de 'L'
    bool esEstudiante = true; // Declaracion de una variable de tipo booleano llamada esEstudiante con el valor de true
    // Las variables bool pueden tomar los valores de true (verdadero) o false (falso), y se pueden asignar utilizando 
    // las palabras reservadas "true" y "false" o utilizando los valores enteros 1 (para true) y 0 (para false).

    // Tambien es posible asignar un valor a una variable despues de su declaracion:
    primero = 10; /* Asignacion del valor 10 a la variable primero (las variables de tipo int pueden contener numeros 
    enteros desde el -32767 hasta el 32767)*/
    segundo = 3.14; /* Asignacion del valor 3.14 a la variable segundo (las variables de tipo flotante pueden contener 
    numeros reales con precision simple desde aproximadamente 1.5 x 10^-45 hasta 3.4 x 10^38 con 7 digitos de precision)*/
    tercero = 2.71828; /* Asignacion del valor 2.71828 a la variable tercero (las variables de tipo doble pueden contener 
    numeros reales con precision doble desde aproximadamente 2.2 x 10^-308 hasta 1.8 x 10^308 con 15 digitos de precision)*/
    cuarto = 1.61803; /* Asignacion del valor 1.61803 a la variable cuarto (las variables de tipo long doble pueden contener 
    numeros reales con precision doble extendida desde aproximadamente 3.4 x 10^-4932 hasta 1.1 x 10^4932 con 18 digitos de 
    precision)*/
    quinto = 'A'; /* Asignacion del valor 'A' a la variable quinto (las variables de tipo char pueden contener un solo caracter 
    encerrado entre comillas simples)*/
    sexto = false; /* Asignacion del valor false a la variable sexto (las variables de tipo bool pueden contener los valores 
    true o false)*/

    /* Existe un tipo de dato llamado "string" que se utiliza para almacenar cadenas de texto, sin embargo, no es un tipo de dato 
    primitivo, sino que es una clase definida en la libreria <string>, por lo que se debe incluir esta libreria para utilizarlo:*/

    std::string lenguaje = "C++"; // Declaracion de una variable de tipo string llamada lenguaje con el valor de "C++"

    /* Para imprimir por terminal, se utiliza la funcion "cout" de la libreria <iostream>, seguida del operador de insercion "<<" 
    y el valor a imprimir:*/

    std::cout << "¡Hola, " << lenguaje << "!" << std::endl; // Imprime "¡Hola, C++!" seguido de un salto de linea
    // El operador "<<" se puede utilizar para imprimir multiples valores en una sola linea, separandolos por comas:
    std::getchar(); 

}