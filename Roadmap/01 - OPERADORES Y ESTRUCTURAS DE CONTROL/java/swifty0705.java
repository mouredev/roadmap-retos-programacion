package com.mouredev.retosprogramacion.roadmap.uno;

import java.util.ArrayList;
import java.util.List;

public class swifty0705 {
    public static void main(String[] args) {
        int a = 1;
        int b = 2;
        int c = 2;

        //comparación
        System.out.println( "a es igual a b?: " + (a == b));
        System.out.println( "a es diferente de b?: " + (a != b));

        System.out.println( "a es mayor a b?: " + (a > b));
        System.out.println( "a es menor a b?: " + (a < b));

        System.out.println( "b es mayor o igual a c?: " + (b >= c));
        System.out.println( "b es menor o igual a c?: " + (b <= c));

        //Aritmeticos
        a +=b;
        System.out.println("la suma de a + b es" +a);
        a -= b;
        System.out.println("la resta de a - b es" +a);
        a *=b;
        System.out.println("la multiplicación de a * b es" +a);
        a /= c;
        System.out.println("la division de a / c es" +a);
        a %= c;
        System.out.println("el modulo de a % c es" +a);

        //logicos
        System.out.println("Ambas son verdad?" + ( (a == b) && (a != b) ) );
        System.out.println("Alguna es verdadera" + ( (a == b) || (a != b) ) );
        System.out.println("Esta es de verdad?" + ( (a == b) ) );
        System.out.println("y con este cambio" + ( !(a == b) ) );

        //Asignación
        System.out.println("el valor actual de c es "+ c);
        c++;
        System.out.println("el valor actual de c es "+ c);

        //identidad
        /*
         instanceof se puede usar
         el operador de comparación == tambien
         */

        //pertinencia, no existe tal cual pero con librerias es posible usarlo. es "contains" en List

        List<String> frutas = new ArrayList<>();
        frutas.add("manzana");
        frutas.add("naranja");
        frutas.add("pera");

        System.out.println(frutas.contains("manzana")); // Imprime "true"
        System.out.println(frutas.contains("uva")); // Imprime "false"

        //

    }
}
