// #04 CADENAS DE CARACTERES

// Ejercicio

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        // Acceso a caracteres específicos:
        String cadena = "Hola, mundo!";
        char primerCaracter = cadena.charAt(0);
        System.out.println("Primer caracter: " + primerCaracter);

        // Subcadenas:
        String subcadena = cadena.substring(0, 4);
        System.out.println("Subcadena: " + subcadena);

        // Longitud:
        int longitud = cadena.length();
        System.out.println("Longitud: " + longitud);

        // Concatenación:
        String concatenacion = cadena.concat(" Java");
        System.out.println("Concatenación: " + concatenacion);

        // Repetición:
        String repeticion = cadena.repeat(3);
        System.out.println("Repetición: " + repeticion);

        // Recorrido
        for (int i = 0; i < cadena.length(); i++) {
            char caracter = cadena.charAt(i);
            System.out.println("Caracter: " + i + " - " + caracter);
        }

        // Conversión a mayúsculas y minúsculas
        String mayusculas = cadena.toUpperCase();
        String minusculas = cadena.toLowerCase();
        System.out.println("Mayúsculas: " + mayusculas);
        System.out.println("Minúsculas: " + minusculas);

        // Reemplazo:
        String reemplazada = cadena.replace("mundo", "Java");
        System.out.println("Reemplazada: " + reemplazada);

        // División:
        String[] division = cadena.split(",");
        System.out.println("Division: " + Arrays.toString(division));

        // Unión
        String[] arrayDePalabras = { "Hola", "mundo", "Java" };
        String union = String.join(" ", arrayDePalabras);
        System.out.println("Union: " + union);

        // Interpolación
        String interpolacion = String.format("Saludo: %s, Lenguaje: %s", arrayDePalabras[0], arrayDePalabras[2]);
        System.out.println("Interpolación: " + interpolacion);

        // Verificación
        boolean empiezaConHola = cadena.startsWith("Hola");
        boolean terminaConMundo = cadena.endsWith("mundo!");
        System.out.println("Empieza con Hola: " + empiezaConHola);
        System.out.println("Termina con mundo: " + terminaConMundo);

        comprobarPalabra("Java", "Kotlin");
    }

    private static void comprobarPalabra(String palabra1, String palabra2) {
        System.out.println("Es palindromo: " + esPalindromo(palabra1, palabra2));
        System.out.println("Es anagrama: " + esAnagrama(palabra1, palabra2));
        System.out.println("Es isogama: " + esIsogama(palabra1, palabra2));
    }

    private static boolean esPalindromo(String palabra1, String palabra2) {
        if (palabra1.length() != palabra2.length()) {
            return false;
        }
        return palabra1.toLowerCase().equals(new StringBuilder(palabra2.toLowerCase()).reverse().toString());
    }

    private static boolean esAnagrama(String palabra1, String palabra2) {
        if (palabra1.length() != palabra2.length()) {
            return false;
        }
        char[] chars1 = palabra1.toLowerCase().toCharArray();
        char[] chars2 = palabra2.toLowerCase().toCharArray();
        Arrays.sort(chars1);
        Arrays.sort(chars2);
        return Arrays.equals(chars1, chars2);
    }

    private static boolean esIsogama(String palabra1, String palabra2) {
        if (palabra1.length() != palabra2.length()) {
            return false;
        }
        Map<Character, Integer> charCounter = new HashMap<>();
        for (char c : palabra1.toLowerCase().toCharArray()) {
            charCounter.put(c, charCounter.getOrDefault(c, 0) + 1);
        }

        for (char c : palabra2.toLowerCase().toCharArray()) {
            if (charCounter.containsKey(c)) {
                charCounter.put(c, charCounter.get(c) - 1);
            } else {
                return false;
            }
        }
        return charCounter.values().stream().allMatch(value -> value == 0);
    }
}