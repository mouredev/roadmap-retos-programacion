
public class Marianoemir {

    /* Esto es un comentario multilinea.
    EJERCICIO:    
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"*/
    
    //      Esto es un comentario de una linea.
    //https://www.java.com/es/ sitio oficial de java 
    
    //Hay una tercera forma de comentar con la sintaxis /***/ llamada Javadoc sirve para describir las clases, métodos, constructores, campos y otros elementos del código, 
    
    public static void main(String[] args) {
        //Variable
        int variable = 10;
        //Constante en Java, el valor de una constante, una vez asignado, no puede ser cambiado durante la ejecución del programa
        final short Cons = 20;

        //Byte   Tamaño: 8 bits  Rango: -128 a 127 Uso: Pequeños números enteros.  
        byte byt = 127;

        //short  Tamaño: 16 bits Rango: -32,768 a 32,767 Uso: Números enteros más grandes que byte
        short corto = 30000;

        //int Tamaño: 32 bits Rango: -2,147,483,648 a 2,147,483,647 Uso: Números enteros estándar.
        int entero = 4000;

        //long Tamaño: 64 bits Rango: -9,223,372,036,854,775,808 a 9,223,372,036,854,775,807 Uso: Números enteros muy grandes.
        long largo = 15000000000L;

        //float Tamaño: 32 bits Rango: Aproximadamente ±3.40282347E+38F (6-7 dígitos decimales) Uso: Números en punto flotante de precisión simple.
        float decimal = 39f;
        
        //double Tamaño: 64 bits Rango: Aproximadamente ±1.79769313486231570E+308 (15 dígitos decimales) Uso: Números en punto flotante de precisión doble.
        double dou = 439.99D;
        //char Tamaño: 16 bits Rango: 0 a 65,535 (representa un solo carácter Unicode) Uso: Almacena caracteres individuales.
        char caracter = '#'; //Puede representar un simbolo unicode una letra en minuscula o mayuscula ejemplo 'a' o 'A'
        char simbolo = '\u0024'; // '\u0024' es el código Unicode para '$'
        //boolean Tamaño: 1 bit (aunque su tamaño real puede ser dependiente de la implementación) Rango: true o false Uso: Almacena valores lógicos.
        boolean estado = true; //boolean viene por default en false
      
        System.out.println("¡Hola, java!");
    }
}
