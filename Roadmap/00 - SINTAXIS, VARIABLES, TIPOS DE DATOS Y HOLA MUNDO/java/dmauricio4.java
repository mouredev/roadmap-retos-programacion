package com.dm4.roadmap;



public class Roadmap00_SintaxisVariables {

    public static void main(String[] args) {

        //Sitio oficial de Java: https://java.com/es/

        /*
        Comentario de
        varias
        lineas
         */

        /**
         Este tipo de comentarios
         los utiliza la
         herramienta javadoc
         */

        //Crea una variable (y una constante si el lenguaje lo soporta).
        String miVariable = "Mi primera variable";
        String MY_CONSTANTE = "My primera constante";

        //Crea variables representando todos los tipos de datos primitivos.
        byte valorByte = 6;
        short valorShort = 10;
        int numero = 100;
        long numeroLong = 100000000;
        float valorFloat = 10.20f;
        double precioFinal = 10.25;
        boolean verdadero = true;
        boolean falso = false;
        char caracter = 'A';
        String texto = "JAVA";

        //Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
        System.out.println("¡Hola, " + texto + "!");

    }
    
}
