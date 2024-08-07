/*
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

public class JesusEs1312 {
    public static void main(String[] args) {
        // Ejemplo de acceso a caracteres específicos
        String cadena = "Hola mundo";
        System.out.println(cadena.charAt(0)); // H
        System.out.println(cadena.charAt(1)); // o
        System.out.println(cadena.charAt(2)); // l
        System.out.println(cadena.charAt(3)); // a

        // Ejemplo de longitud
        System.out.println(cadena.length()); // 10

        // Ejemplo de concatenación
        String cadena2 = "Hola";
        String cadena3 = " mundo";
        System.out.println(cadena2 + cadena3); // Hola mundo
        System.out.println(cadena2.concat(cadena3)); // Hola mundo

        // Ejemplo de repetición
        System.out.println(cadena2.repeat(3)); // HolaHolaHola

        // Ejemplo de recorrido
        for (int i = 0; i < cadena.length(); i++) {
            System.out.println(cadena.charAt(i));
        }

        // Ejemplo de conversión a mayúsculas y minúsculas
        System.out.println(cadena.toUpperCase()); // HOLA MUNDO
        System.out.println(cadena.toLowerCase()); // hola mundo

        // Ejemplo de reemplazo
        System.out.println(cadena.replace("Hola", "Adiós")); // Adiós mundo

        // Ejemplo de división
        String[] palabras = cadena.split(" ");
        for (String palabra : palabras) {
            System.out.println(palabra);
        }

        // Ejemplo de unión
        String[] palabras2 = {"Hola", "mundo"};
        System.out.println(String.join(" ", palabras2)); // Hola mundo

        // Ejemplo de interpolación
        String nombre = "Juan";
        int edad = 25;
        System.out.println("Hola, mi nombre es " + nombre + " y tengo " + edad + " años");
        System.out.println(String.format("Hola, mi nombre es %s y tengo %d años", nombre, edad));

        // Ejemplo de verificación
        System.out.println(cadena.contains("Hola")); // true
        System.out.println(cadena.startsWith("Hola")); // true
        System.out.println(cadena.endsWith("mundo")); // true

        // Ejemplo de funciones extra
        funcionExtra("oso", "oso");
    }

    public static void funcionExtra(String palabra1, String palabra2) {
        // Palíndromos
        System.out.println(palabra1.equals(new StringBuilder(palabra1).reverse().toString()) ? "Es palíndromo" : "No es palíndromo");
        System.out.println(palabra2.equals(new StringBuilder(palabra2).reverse().toString()) ? "Es palíndromo" : "No es palíndromo");

        // Anagramas
        char[] palabra1Array = palabra1.toCharArray();
        char[] palabra2Array = palabra2.toCharArray();
        Arrays.sort(palabra1Array);
        Arrays.sort(palabra2Array);
        System.out.println(Arrays.equals(palabra1Array, palabra2Array) ? "Son anagramas" : "No son anagramas");

        // Isogramas
        System.out.println(palabra1.length() == palabra1.chars().distinct().count() ? "Es isograma" : "No es isograma");
        System.out.println(palabra2.length() == palabra2.chars().distinct().count() ? "Es isograma" : "No es isograma");

    }
}
