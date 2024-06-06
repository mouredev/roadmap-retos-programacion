package org.example;/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

import java.util.Arrays;

public class estuardodev {
    public static void main(String[] args) {
        operaciones("C#", "Python");
        System.out.println("\n-- Dificultad Extra --\n");
        dificultadExtra("Palindromo", "Isograma");
        System.out.println("\n----\n");
        dificultadExtra("Ana", "OlLo");
    }

    private static void operaciones(String texto1, String texto2) {
        // Acceso a caracteres
        System.out.println("-- Acceso a Indices de un texto --");
        System.out.println("Indice 0 del Texto 1: " + texto1.charAt(0));
        System.out.println("Indice 3 del Texto 2: " + texto2.charAt(3) + "\n");

        // Crear subcadenas
        System.out.println("-- Crear Subcadenas --");
        System.out.println("Subcadena del texto 1: " + texto1.substring(1));
        System.out.println("Subcadena del texto 2: " + texto2.substring(3) + "\n");

        // Longitudes
        System.out.println("-- Longitudes --");
        System.out.println("Longitud del texto 1: " + texto1.length());
        System.out.println("Longitud del texto 2: " + texto2.length() + "\n");

        // Concatenación de cadenas
        System.out.println("-- Concatenación --");
        System.out.println("Forma 1:" + texto1 + " " + texto2);
        System.out.println("Forma 2: " + texto1 + " " + texto2 + "\n");

        // Repetición
        System.out.println("-- Repetición --");
        for (int i = 0; i < 3; i++) {
            System.out.println(texto1);
        }
        for (int i = 0; i < 3; i++) {
            System.out.println(texto2);
        }

        // Recorrido
        System.out.println("\n-- Recorrido --");
        for (char i : texto1.toCharArray()) {
            System.out.println(i);
        }

        // Conversión a mayúsculas
        System.out.println("\n-- Conversión a mayúsculas --");
        System.out.println(texto1.toUpperCase());
        System.out.println(texto2.toUpperCase());

        // Conversión a minúsculas
        System.out.println("\n-- Conversión a minúsculas --");
        System.out.println(texto1.toLowerCase());
        System.out.println(texto2.toLowerCase());

        // Reemplazo
        System.out.println("\n-- Reemplazo --");
        System.out.println(texto1.replace('#', '+'));
        System.out.println(texto2.replace('o', '0'));

        // Unión
        System.out.println("\n-- Unión --");
        System.out.println(texto1.concat(texto2));

        // Interpolación
        System.out.println("\n-- Interpolación --");
        System.out.println("Lenguaje 1 es: " + texto1 + " y el 2 es: " + texto2);

        // Verificación
        System.out.println("\n-- Verificación --");
        System.out.println(texto1.equals(texto2));
    }

    // Dificultad Extra

    // Anagrama
    static boolean esAnagrama(String texto1, String texto2) {
        char[] arreglo1 = texto1.toLowerCase().toCharArray();
        char[] arreglo2 = texto2.toLowerCase().toCharArray();

        Arrays.sort(arreglo1);
        Arrays.sort(arreglo2);

        return Arrays.equals(arreglo1, arreglo2);
    }
    private static void dificultadExtra(String texto1, String texto2) {
        if (esAnagrama(texto1, texto2   )) {
            System.out.println("Los textos son anagramas.");
        } else {
            System.out.println("Los textos no son anagramas");
        }

        // Palíndromos
        String txt1 = texto1.toLowerCase();
        String txt2 = texto2.toLowerCase();

        if (txt1.equals(new StringBuilder(txt1).reverse().toString())) {
            System.out.println(texto1 + " es palíndromo.");

            if (txt2.equals(new StringBuilder(txt2).reverse().toString())) {
                System.out.println(texto2 + " es palíndromo.");
            } else {
                System.out.println(texto2 + " no es palíndromo.");
            }
        } else if (txt2.equals(new StringBuilder(txt2).reverse().toString())) {
            System.out.println(texto1 + " no es palíndromo.");
            System.out.println(texto2 + " es palíndromo.");
        } else {
            System.out.println(texto1 + " no es palíndromo.");
            System.out.println(texto2 + " no es palíndromo.");
        }

        // Isogramas
        String text1 = texto1.toLowerCase();
        String text2 = texto2.toLowerCase();

        if (text1.length() == text1.chars().distinct().count()) {
            System.out.println(texto1 + " es Isograma");
        } else {
            System.out.println(texto1 + " no es Isograma");
        }

        if (text2.length() == text2.chars().distinct().count()) {
            System.out.println(texto2 + " es Isograma");
        } else {
            System.out.println(texto2 + " no es Isograma");
        }
    }
}
