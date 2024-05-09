import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class Worlion {
    /*
 * EJERCICIO: #04 CADENAS DE CARACTERES
 */

    public static void main(String[] args) {
        new Worlion().run();
    }
    
    public void run() {
        base();
        analiceWords("arroz", "zorra");
    }

    public void base() {
        String cadena = "Hola Mundo";
        System.out.println("Cadena original: " + cadena);

        // Acceso a caracteres específicos
        System.out.println("Primer caracter: " + cadena.charAt(0));
        System.out.println("Último caracter: " + cadena.charAt(cadena.length() - 1));

        // Subcadenas
        System.out.println("Subcadena desde la posición 5: " + cadena.substring(5));
        System.out.println("Subcadena desde la posición 5 hasta la 7: " + cadena.substring(5, 8));

        // Longitud
        System.out.println("Longitud de la cadena: " + cadena.length());

        // Concatenación
        System.out.println("Concatenación: " + cadena.concat(" desde Java"));

        // Repetición
        System.out.println("Repetición: " + cadena.repeat(3));

        // Recorrido
        for (int i = 0; i < cadena.length(); i++) {
            System.out.println("Caracter en la posición " + i + ": " + cadena.charAt(i));
        }

        // Conversión a mayúsculas y minúsculas
        System.out.println("Mayúsculas: " + cadena.toUpperCase());
        System.out.println("Minúsculas: " + cadena.toLowerCase());

        // Reemplazo
        System.out.println("Reemplazo de 'Hola' por 'Adiós': " + cadena.replace("Hola", "Adiós"));

        // División
        String[] palabras = cadena.split(" ");
        for (String palabra : palabras) {
            System.out.println("Palabra: " + palabra);
        }

        // Unión
        System.out.println("Unión de palabras: " + String.join(" ", palabras));

        // Interpolación
        String nombre = "Mundo";
        System.out.println("Interpolación: Hola " + nombre);

        // Verificación
        System.out.println("¿La cadena contiene 'Mundo'?: " + cadena.contains("Mundo"));
    }
 /*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

    public void analiceWords(String word1, String word2) {

        System.out.println(" \n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n");

        System.out.println("Analizando las palabas: '" + word1 + "'' y '" + word2+"'");

        System.out.println("Es palíndromo '"+ word1 +"'': " + palindrome(word1));
        System.out.println("Es palíndromo '"+ word2 +"'': " + palindrome(word2));
        System.out.println("Son anagramas: " + anagram(word1, word2));
        System.out.println("Es isograma '"+ word1 +"'': " + isogram(word1));
        System.out.println("Es isograma '"+ word2 +"'': " + isogram(word2));

    }

    private boolean palindrome(String word){
        return new StringBuilder(word).reverse().toString().equals(word);
    }
    private boolean anagram(String word1, String word2) {
        String w1 = word1.chars().sorted().collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append).toString();
        String w2 = word2.chars().sorted().collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append).toString();

        return w1.equals(w2);
    }
    private boolean isogram(String word) {
        HashMap<Character, Integer> map = new HashMap<>();

        word.chars().forEach( c -> map.merge( (char)c, 1, Integer::sum));

        Integer first = map.values().stream().findFirst().get();

        return map.values().stream().allMatch(c -> c.equals(first));
    }
}
