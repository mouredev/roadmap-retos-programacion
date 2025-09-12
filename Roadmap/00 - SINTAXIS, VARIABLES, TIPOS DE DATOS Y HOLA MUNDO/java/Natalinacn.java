package com.example.headfirstjava;

import org.springframework.boot.SpringApplication;

public class Natalinacn {

    public static void main(String[] args) {
        SpringApplication.run(HeadFirstjavaApplication.class, args);
/*COMENTARIO MULTILINEA

EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"*/

        // COMENTARIO DE UNA LINEA
        // Información sobre descargas, documentación, tutoriales y recursos relacionados con Java:
        // https://www.java.com/en/
        // Información técnica y recursos para desarrolladores: https://www.oracle.com/java/

        /**
         * COMENTARIO DE DOCUMENTACIÓN (javadoc)
         * @author natalin
         * @version 1.0
         */

        //VARIABLES Y CONSTANTES
        String variable = "Variable";
        final String MI_CONSTANTE = "Constante";


        //TIPOS DE DATOS PRIMITIVOS

        byte tipoByte = 100; //Tamaño: 8 bits. Rango -128 a 127
        short tipoShort = 10000; //Tamaño: 16 bits. Rango: -32.768 a 32.767
        int tipoInt = 100000; //Tamaño: 32 bits. Rango: -2147483648 a 2147483647
        long tipoLong = 100000L; //Tamaño: 34 bits. Rango: 2^63 a 2^63-1
        float tipoFloat = 234.5f; //Tamaño: 32 bits. Rango: aproximadamente ±3.40282347E+38F (6-7 dígitos decimales). Float: Se usa cuando el ahorro de memoria es importante y la precisión de 6-7 dígitos decimales es suficiente.
        double tipoDouble = 123.4; //Tamaño: 64 bits. Rango: aproximadamente ±1.79769313486231570E+308 (15-16 dígitos decimales). Double: Se usa para la mayoría de los cálculos de punto flotante debido a su mayor precisión y rango.
        boolean tipoBoolean = true; // Tamaño: 1 bit (teóricamente). Valores posibles: true o false
        char tipoChar = 'A'; // Tamaño: 16 bits. Rango: '\u0000' (o 0) a '\uffff' (o 65,535)


        //Imprimir
        String lenguaje = "Java";

        System.out.println("¡Hola, " + lenguaje + "!");
    }
}