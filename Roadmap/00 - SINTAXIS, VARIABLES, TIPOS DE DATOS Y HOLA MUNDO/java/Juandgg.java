// https://www.java.com/es/

/*
 * comentario de varias lineas
 * 
 */

// comentario en una sola linea




public class Juandgg{

    public static void main(String[] args) {
        //////  paso(1) tipos de variable en java

        /*
         * exiten 3 tipo de variable que podemos usar en java
         * (1) variable con tipo o variable que contiene su tipo de dato
         * (2) variable que puede tomas cualquier tipo de datos 
         * (3) variables constantes que pueden ser de tipo o tomar cualquier valo
         * 
         * Ejemplos a continuacion :
         */

         
        /* (1 tipo) : este ejemplo vemos una variable declarada e inicializada solo para poder ver este ejemplo  y comparacion con los siguientes tipos
        */ 
        int varTipo1Ejemplo =2 ;

        /* (2 tipo) : variable que usan la palabra reservada var la cual toma como tipo cualquier dato que se le intrusca
        */

        var varTipo2Ejemplo ="hola";

        /* (3 tipo) : variables constantes las cuales se declaran e se inicializan siempre las cuales puede tener cualquiera de los dos tipos anteriores
        */

        final var varTipo3Ejemplo ="hola";
        final int varTipo3_1Ejemplo =2000;

        


        /////  paso(2) todos los tipos de datos primitivos


        ///Tipos enteros

        byte edad = 25; //: 8 bits, rango de -128 a 127.
        short distancia = 10000; //16 bits, rango de -32,768 a 32,767.
        int numero = 123456; //32 bits, rango de -2^31 a 2^31 - 1.
        long poblacion = 1234567890L; //64 bits, rango de -2^63 a 2^63 - 1.


        ///Tipos flotantes

        float precio = 29.99f; //32 bits, rango de ±1.4e-45 a ±3.4028235e+38, precisión de aproximadamente 6-7 dígitos decimales.
        double pi = 3.141592653589793; //64 bits, rango de ±4.9e-324 a ±1.7976931348623157e+308, precisión de aproximadamente 15 dígitos decimales.

        ///Tipos booleano:

        boolean esMayor = true; //1 bit, representa valores true o false.

        ///Tipo carácter:
        char inicial = 'A';

        
        System.out.println("!hola java");
    }
}