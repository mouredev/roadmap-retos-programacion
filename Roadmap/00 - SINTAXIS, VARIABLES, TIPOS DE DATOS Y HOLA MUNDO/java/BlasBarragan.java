/**
 * * EJERCICIO #00 - SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 * 
 * @version v1
 * 
 * @since 06/01/2024
 * 
 * @author Blas Barragán
 * 
 */
 public class BlasBarragan {
    public static void main(String[] args) {
            
        // WEB OFICIAL
            // https://www.java.com/
        
        // COMENTARIOS
            // Comentario simple (1 linea)
                // Se encabeza cada linea por "//"
            // Comentario compuesto (multilinea)
                /*
                * La primera linea se encabeza con "/**"
                * Las lineas interiores iran siempre precedidas de "*"
                * Y la linea final de cierre del comentario, unicamente contendrá 
                */ 
            // Comentario de documentación (multilinea)
                /** <- Como el anterior pero con un "*" extra.
                 * Este tipo de comentario multilinea, se usa para describir el código.
                 * Podemos generar tantas lineas com queramos y también,
                 * añadir tags usando "@" como los que se ven en la cabecera de este archivo.
                 */

        // DECLARACIÓN DE VARIABLES
            /**
             * Todas las variables en su definición iran precedidas de su tipo de dato.
             * Y seguirán la siguiente extructura: "tipoDatoVariable nombreVariable = valorVariable;"
             * Es recomendable declarar una variable por linea e inicializarlas donde esten declaradas.
             * Pueden declararse en cualquier parte del programa, pero siempre antes de que sea usada.
             * Por connvención, se declararán utilizando camelCase y al inicio del bloque correspondiente.
             */
            // Variables
            int variable; // Si no inicializamos la variable, el sistema le atribuye un valor por defecto.
            int variableInicializada = 0; // Al inicializar la variable, se le atribuye el valor declarado.
            final int VARIABLE = 0; // Las variables constantes se declaran en MAYUSCULAS, van precedidas de la palabra "final" y siempre hay que inicializarlas.

        // DATOS PRIMITIVOS
            // Numericos
            byte varByte = 1; // Enteros muy cortos. => Numeros de -128 a 127. Valor por defecto "0".
            short varShort = 2; // Enteros cortos. => Numeros de -32.768 a 32.768. Valor por defecto "0".
            int varInt = 3; // Enteros. => Numeros de -2.147.483.648 hasta 2.147.483.647. Valor por defecto "0".
            long varLong = 4L; // Su valor, siempre irá terminado con "L". Enteros largos. => Números desde -9.223.372.036.854.775.808 hasta 9.223.372.038.854.775.807. Valor por defecto "0L".
            // Decimales
            float varFloat = 1.0F; // Su valor, siempre irá terminado con "f". Numeros de hasta 7 decimales. => Desde +/-1.4E-45 a +/-3.4E38. Valor por defecto "0.0f".
            double varDouble = 2.0d; // Su valor, siempre irá terminado con "d". Numeros de hasta 16 decimales. => Desde +/-4.9E-324 a +/-1.7E308. Valor por defecto "0.0d".
            // Caracteres
            char varChar = 'A'; // Su valor siempre irá entre comillas simples 'X'. Caracter ASCII o Unicode de \u0000 a \uFFFF. 
            // Datos Lógicos
            boolean varLogico = true; // Valor true o false. Valor por defecto false.

        // CADENAS DE TEXTO
            /* 
            * En JAVA, las variables String existen en forma de clase que representa cadenas de caracteres.
            */ 
            String varCadena = "Soy una String"; // Su valor siempre irá entre comillas dobles "X". Valor por defecto "null".
        
        // IMPRESION POR TERMINAL
            System.out.println("¡Hola, JAVA!");

    }
 }
