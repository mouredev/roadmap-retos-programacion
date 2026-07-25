#include <iostream>


/*  Crea un comentario en el código y coloca la URL del sitio web oficial del
    lenguaje de programación que has seleccionado.*/

        // https://isocpp.org/

/*  Representa las diferentes sintaxis que existen de crear comentarios
    en el lenguaje (en una línea, varias...).*/
        
        /*Bloque para varios comentarios*/
        //Comentarios de una sola línea 
int main() {
/*  Crea una variable (y una constante si el lenguaje lo soporta).*/
        auto var = 0;
        const auto myConst= 0;

/*  Crea variables representando todos los tipos de datos primitivos
    del lenguaje (cadenas de texto, enteros, booleanos...).*/

        int numEntero = 0;
        long numEnteroLargo = 123456789;
        float numDecimal = 1.23;
        double numDecimalDoblePrecision = 2.33333;   
        char letra = 'M';
        bool mybool = true;
        void* myVoid = nullptr;

/*  Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"*/

    std::cout <<"¡Hola, C++!"<<std::endl;
    
    return 0;   //0 indica que el programa se ejecutó correctamente
}