import java.util.*;
import java.util.stream.Collectors;

/**
 * #04 CADENAS DE CARACTERES
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    /**
     * Operaciones<p>
     * Concatenación, Repeat, ChartAt, Length, Substring
     */
    private static final String STRING_1 = "Hola";
    private static final String STRING_2 = "Java";
    private static final String STRING_3 = "\s Road to World Cup  \n";

    public static void main(String[] args) {

        System.out.println(STRING_1 + ", " + STRING_2 + "!");//Concatenación
        System.out.println(STRING_1.repeat(3));//Repeat
        System.out.println(STRING_1.charAt(2));//ChartAt
        System.out.println(STRING_1.length());//Length

        System.out.println(STRING_1.substring(1, STRING_1.length() - 1));//Substring
        System.out.println(STRING_1.contains("ol"));//Contains

        System.out.println(STRING_1.toLowerCase());//toLowerCase
        System.out.println(STRING_1.toUpperCase());//toUpperCase

        System.out.println(STRING_1.replace("H", "S"));//replace

        System.out.println("----- STRIP AND TRIM ------");
        System.out.println("'" + STRING_3 + "'");
        System.out.println("'" + STRING_3.strip() + "'");//strip
        System.out.println("'" + STRING_3.stripLeading() + "'");
        System.out.println("'" + STRING_3.stripTrailing() + "'");
        System.out.println("'" + STRING_3.stripIndent() + "'");
        System.out.println("'" + STRING_3.trim() + "'");//trim

        System.out.println("----- REPLACE AND SPLIT ------");
        System.out.println("'" + STRING_3.replace(" ", "") + "'");//replace
        System.out.println("'" + STRING_3.replaceAll("[oa]", "u") + "'");//replaceAl
        System.out.println(Arrays.stream(STRING_3.split("o")).toList());//split

        System.out.println("----- REVERSE ------");
        StringBuilder sb = new StringBuilder(STRING_3);
        System.out.println(sb.reverse());//reverse

        System.out.println(STRING_2.startsWith("Ja"));
        System.out.println(STRING_1.endsWith("la"));

        System.out.println(STRING_3.indexOf("o"));//indexOf
        System.out.println(STRING_3.lastIndexOf("o"));
        System.out.println(STRING_3.indexOf("ad"));

        System.out.printf("Esto es una interpolación: %s, %s!%n", STRING_1, STRING_2);//interpolación

        System.out.println(Arrays.stream(STRING_2.split("")).sorted().toList());//transformar a lista ordenada

        System.out.println(STRING_2.chars()//transformar a lista ordenada
                .mapToObj(c -> (char) c)
                .sorted()
                .toList());

        /*
         * DIFICULTAD EXTRA
         * Palíndromos
         * Anagramas
         * Isogramas
         */
        System.out.println();
        System.out.println("DIFICULTAD EXTRA:\n");

        String text1 = "Anita lava la tina";
        String text2 = "Radar";
        System.out.println("¿'" + text1 + "' es un palíndromo? : " + isPalindrome(text1));
        System.out.println("¿'" + text2 + "' es un palíndromo? : " + isPalindrome(text2));

        String text3 = "Listen";
        String text4 = "Silent";
        System.out.println("¿El conjunto de '" + text3 + "' y '" + text4 + "' es un anagrama? : "
                + isAnagram(text3, text4));

        String text5 = "Yuxtaponer";
        System.out.println("¿'" + text5 + "' es un heterograma? : " + isHeterogram(text5));

        String text6 = "Intestines";
        System.out.println("¿'" + text6 + "' es un isograma? : " + isIsogram(text6));
    }

    private static boolean isPalindrome(String text) {
        text = text.replace(" ", "").toLowerCase();
        StringBuilder sb = new StringBuilder(text);
        return sb.reverse().toString().equals(text);
    }

    private static boolean isAnagram(String text1, String text2) {
        return sorted(text1.toLowerCase()).equals(sorted(text2.toLowerCase()));
    }

    private static String sorted(String text) {
        return text.chars()
                .mapToObj(c -> (char) c)
                .sorted()
                .toList()
                .toString();
    }

    private static boolean isHeterogram(String text) {
        long sizeText = text.length();
        Set<Character> textSet = getSet(text);
        return sizeText == textSet.size();
    }

    private static Set<Character> getSet(String text) {
        return text.toLowerCase()
                .chars()
                .mapToObj(c -> (char) c)
                .collect(Collectors.toSet());
    }

    private static boolean isIsogram(String text) {
        Map<Character, Integer> diccionario = new HashMap<>();
        Set<Character> setText = getSet(text.toLowerCase());
        if (text.length() % setText.size() != 0) {
            return false;
        }
        setText.forEach(k -> diccionario.put(k, countLetters(text.toLowerCase(), k)));
        return new HashSet<>(diccionario.values()).size() == 1;
    }

    private static Integer countLetters(String text, Character k) {
        return (int) text.toLowerCase().chars().mapToObj(c -> (char) c)
                .filter(c -> c.equals(k))
                .count();
    }

}
