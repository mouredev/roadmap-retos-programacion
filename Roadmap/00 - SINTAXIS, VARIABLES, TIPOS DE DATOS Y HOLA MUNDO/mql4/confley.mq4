// https://docs.mql4.com/

// Comentario de una sola línea 

/*  Está es la menra 
    de escribir un comentario
    de varias líneas 
*/ 



#define MY_CONSTANT "hola"; 

string miVariable = "Variable tipo tetxo"; // Variable global
// string miVariable = "Nuevo valor"; //! error 



void OnStart() {
    miVariable = "Cambiando el valor de la variable";
    
    int     my_int      = 0; 
    double  my_double   = 1.1; 
    bool    my_bool     = false; // true
    string  my_string   = "Cadena de texto"; 
    color   my_clr      = clrRed;           // Uso de colores predefinidos (web colors)
    color   my_customColor = C'255,0,0';    // Definición personalizada de un color (rojo)
    datetime my_datetime = D'2014.03.05 15:46:58'; 
    
    Print("¡Hola, mql4!");
}



//* OBSERVACIONES 
// - Para cambiar el valor de una variable global tiene que ser dentro de un método, fuera no es posible.
// - Print() no puede ser ejecutado fuera de un método 
// - Las constantes no se pueden imprimir ( Print(MY_CONSTANT) ) directamente. 
// - Hay muchas formas de especificar una fecha ( https://docs.mql4.com/basis/types/integer/datetime ). 
//?- Para programar MQL4 con VScode ( https://www.youtube.com/watch?v=WMe7ihFempE ). 