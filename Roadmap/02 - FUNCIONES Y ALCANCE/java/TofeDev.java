public class TofeDev {
    //--- Variables Globales
    static int globalVariable1 = 100;
    static int globalVariable2 = 20;
    public static void main(String[] args) {
        
        //Función básica / Sin retorno ni parámetros
        bienvenida();

        //Función con parámetro
        estadoClima("soleado");

        //Función con varios parámetros
        parejaMesa("José Hernandez", "María Valdez");

        //Función con retorno
        int resultadoSuma = sumar(globalVariable1, globalVariable2);
        System.out.println("Resultado de la suma: " + resultadoSuma);

        //--- Variables locales
        int localVariable1 = 5;
        int localVariable2 = 20;

        //Funciones dentro de funciones
        int[] resultado2 = funcionDoble(localVariable1, localVariable2);
        System.out.println("Los resultados son: " + resultado2[0] + " (suma) y " + resultado2[1] + " (multiplicación)");

        //Dificultad Extra
        Extra("FIZZ", "BUZZ");

    }

    //Función básica / Sin retorno ni parámetros
    public static void bienvenida() {
        System.out.println("Les damos la bienvenida a nuestra casa");
    }

    //Función con parámetro 
    public static void estadoClima(String clima) {
        System.out.println("Hoy el clima está " + clima);
    }

    //Función con varios parámetros
    public static void parejaMesa(String p1, String p2) {
        System.out.println("Esta mesa está reservada para " + p1 + " y " + p2);
    }

    //Funciones con retorno
    public static int sumar(int a, int b) {
        return a + b;
    }

    public static int multiplicacion(int c, int d) {
        return c * d;
    }

    //Funciones dentro de funciones
    public static int[] funcionDoble(int e, int f) {
        int g = sumar(e, f);
        int h = multiplicacion(e, f);
        return new int[] {g, h};

    }

   /* 
    * DIFICULTAD EXTRA
    * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos. 
    */

    public static void Extra(String cadena1, String cadena2) {
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(cadena1 + cadena2);
            } else if (i % 3 == 0) {
                System.out.println(cadena1);
            } else if (i % 5 == 0) {
                System.out.println(cadena2);
            } else {
                System.out.println(i);
            }
        }
    }
}
