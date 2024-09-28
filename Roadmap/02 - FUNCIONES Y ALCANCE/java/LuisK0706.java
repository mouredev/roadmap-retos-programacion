public class Ejercicio02 {

    //Creando una variable global (La variables globales se pueden usar en cualquier lugar del codigo)
    public static String mi_variable = "Variable global";
    public static void main(String[] args) {
        funcion1();
        suma(5, 7);
        System.out.println(concatenar_cadenas("Hola", "mundo"));
        System.out.println(variable_global());
        variable_local();

        //Ejemplo de una funcion ya creada de java.

        //Funcion length (Se utiliza para mostrar el largo de una cadena)
        String mi_cadena = "Luis King";
        System.out.println("El tamaño de la cadena es: " + mi_cadena.length());


        // Mostrando ejercicio extra 
        System.out.println("Se mostraron: " + Extra("mi_cadena1", "mi_cadena2") + " numeros en lugar de las cadenas");

        

    }

    //Funcion sin parametros ni retornos
    public static void funcion1(){
        System.out.println("Esto es una funcion sin parametros ni retornos");
    }

    //Funcion con parametros
    public static void suma(int num1, int num2){
        int suma;
        suma = num1 + num2;
        System.out.println("La suma es: " + suma);
    }

    // Funcion con parametros y retornos
    public static String concatenar_cadenas(String cadena1, String cadena2){
        return cadena1 + " " + cadena2;
    }

    // Utilizando una variable global
    public static String variable_global(){
       return mi_variable;
    }


    //Funcion con una variable local 
    public static void variable_local(){
        //Creando una variable local (Las variables locales solo se pueden utilizar en la funcion donde se crearon)
        int variable_local = 7;
        System.out.println(variable_local);
    }

    /*
     * DIFICULTAD EXTRA (opcional):
     * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
     * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
     *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
     *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
     *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
     *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos
     */

     public static int Extra(String cadena1, String cadena2){
        int contador = 0;
        for (int i = 0; i <= 100; i++){
            if (i % 3 == 0){
                System.out.println(cadena1);
            }
            else if (i % 5 == 0){
                System.out.println(cadena2);
            }
            else if (i % 3 == 0 && i % 5 == 0){
                System.out.println(cadena1 + cadena2);
            }
            else{
                System.out.println(i);
                contador++;
            }
        }

        return contador;
     }
}
