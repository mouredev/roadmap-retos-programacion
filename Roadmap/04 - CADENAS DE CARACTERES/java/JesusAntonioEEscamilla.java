/** #04 - Java -> Jesus Antonio Escamilla */

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class JesusAntonioEEscamilla {
    public static void main(String[] args) {
    //---EJERCIÓ---
    // Cadenas de caracteres
        //--STRING--
        String str = "Hola Mundo";
        System.out.println("STRING -> " + str);
        char ch = str.charAt(3);
        System.out.println("Carácter -> " + ch);

        //--SUB-CADENA--
        String subStr = str.substring(5, 10);
        System.out.println("Sub-Cadena -> " + subStr);

        //--LONGITUD--
        int length = str.length();
        System.out.println("Longitud -> " + length);

        //--CONCATENACIÓN--
        String str1 = "Jesus";
        String resultado = str.concat(", soy " + str1);
        System.out.println("Concatenación -> " + resultado);

        //--REPETICIÓN--
        //No hay método directo en Java, pero se puede usar StringBuilder
        String repeated = str.repeat(3);
        System.out.println("Repetición -> " + repeated);

        //--MAYÚSCULAS Y MINÚSCULAS--
        String upper = str.toUpperCase();
        String lower = str.toLowerCase();
        System.out.println("Mayúsculas -> " + upper);
        System.out.println("Minúsculas -> " + lower);

        //--REMPLAZO--
        String replaced = str.replace("Mundo", "Java");
        System.out.println("Remplazo -> " + replaced);

        //--DIVISION--
        String str__ = "Hola,Mundo,Java";
        String[] parts = str__.split(",");
        System.out.println("Division -> " + Arrays.toString(parts));

        //--UNION--
        String[] words = {"Hola", "Mundo", "Java"};
        String joined = String.join("", words);
        System.out.println("Union -> " + joined);

        //--INTERPOLACIÓN--
        String nombre = "Antonio";
        String str_ = String.format("Hola %s", nombre);
        System.out.println("Interpolación -> " + str_);

        //--VERIFICACIÓN--
        // -IGUALDAD-
        String str3 = "Hola Mundo";
        boolean isEqual = str.equals(str3);
        System.out.println("Verificación-Igualdad (Hola Mundo = Hola Mundo) -> " + isEqual);

        // -EMPIEZA-
        boolean startsWith = str.startsWith("Hola");
        System.out.println("Verificación-Principio (Hola Mundo = Hola) -> " + startsWith);

        // -TERMINA-
        boolean endsWith = str.endsWith("Mundo");
        System.out.println("Verificación-Termina (Hola Mundo = Mundo) -> " + endsWith);

        // -CONTIENE-
        boolean contains = str.contains("Mundo");
        System.out.println("Verificación-Contiene (Hola Mundo = Hola-Mundo) -> " + contains);

    //---EXTRA---
        EXTRA("radar", "roma");
    }

    /**-----DIFICULTAD EXTRA-----*/

    public static void EXTRA(String palabra1, String palabra2) {
        palabra1 = palabra1.toLowerCase();
        palabra2 = palabra2.toLowerCase();
        System.out.println("Palíndromo");
        System.out.println(palabra1 + " es un Palíndromo: " + esPalíndromo(palabra1));
        System.out.println(palabra2 + " es un Palíndromo: " + esPalíndromo(palabra2));
        
        System.out.println("Anagrama");
        System.out.println(palabra1 + " y " + palabra2 + " son Anagramas: " + sonAnagramas(palabra1, palabra2));
        
        System.out.println("Isograma");
        System.out.println(palabra1 + " es un Isograma: " + esIsograma(palabra1));
        System.out.println(palabra2 + " es un Isograma: " + esIsograma(palabra2));
    }

    public static boolean esPalíndromo(String word){
        word = word.toLowerCase();
        String invert = new StringBuilder(word).reverse().toString();
        return word.equals(invert);
    }

    public static boolean sonAnagramas(String word1, String word2){
        word1 = word1.toLowerCase();
        word2 = word2.toLowerCase();
        if(word1.length() != word2.length()){
            return false;
        }
        char[] array1 = word1.toCharArray();
        char[] array2 = word2.toCharArray();
        Arrays.sort(array1);
        Arrays.sort(array2);
        return Arrays.equals(array1, array2);
    }

    public static boolean esIsograma(String word){
        Set<Character> character = new HashSet<>();
        for (char c : word.toCharArray()) {
            if (character.contains(c)) {
                return false;
            }
            character.add(c);
        }
        return true;
    }

    /**-----DIFICULTAD EXTRA-----*/
}