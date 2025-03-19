package org.example;

// Sitio web oficial Java: https://dev.java

//Comentario de una linea

/*
* Comentario de multiples lineas
* */


/**
 * JavaDoc que permite de cierta forma documentar clases, funciones(metodos para los puristas XD)...
 */
public class Main {
    public static void main(String[] args) {
        //forma antigua y estandar
        String name1;

        //forma nueva aunque requiere inicializar al momento de declarar
        var name2 = "";

        //constante
        final int num1;

        //Variable primitivas
        char c = 'c';//acepta cualquier caracter Unicode
        int i = 50;//acepta enteros con signo desde -2.147.483.648 hasta 2.147.483.649
        short s = -32768;// acepta enteros con signo desde -32.768 hasta 32.767
        long l = -9223372036854775808L;// acepta enteros con signo desde -9.223.372.036.854.775.808 hasta 9.223.372.038.854.775.807
        float f = 7.233433f;// acepta hasta 6 decimales
        double d = 3.14159;// acepta hasta 14 decimales
        boolean b = true;//True or false
        byte byte1 = -128;// acepta enteros con signo desde -128 hasta 127

        System.out.println("¡Hola, Java!");

    }
}