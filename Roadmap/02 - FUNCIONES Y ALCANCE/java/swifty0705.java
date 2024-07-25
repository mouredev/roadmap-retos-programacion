package com.mouredev.retosprogramacion.roadmap.dos;

import java.util.Scanner;

public class swifty0705 {
    public static void main(String[] args) {
        bienvenida();
        int primeraSuma = suma(1,2);
        System.out.println(primeraSuma);
        int resultadoResta = resta(8,9);
        System.out.println(resultadoResta);
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el primer texto: ");
        String primerString = sc.nextLine();
        System.out.println("Ingrese el segundo texto: ");
        String segString = sc.nextLine();
        System.out.println("Cantidad  de veces: "+ hardMode(primerString,segString));
    }

    public static int suma(int a, int b){
        return a + b;
    }
    public static void bienvenida(){
        System.out.println("Bienvenido al reto dos");
    }
    public static int resta(int a, int b){
//        int impresion(){
//            return 5;
//        }
//        return a-b- impresion();
        // java no permite metodo dentro de metodo
        return a - b;

    }


    public static int hardMode(String a, String b){
        int j = 0;
        for (int i = 0; i < 100; i++){
            if(i%3==0 && i%5==0){
                System.out.println(a + " " + b);
            } else if(i %3==0) {
                System.out.println(a);
            } else if(i %5==0) {
                System.out.println(b);
            }else {
                j++;
            }
        }
        return j;
    }

    public static String funcion(String primeraMitadDelTexto, String segundaMitadDelTexto) {
        String inicioDelTexto = """

                   Era un texto incompleto

                """;
        String textoUnico = inicioDelTexto + primeraMitadDelTexto + " " + segundaMitadDelTexto;
        return textoUnico;
    }


}
