import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

public class Ldre3 {
    public static void main(String[] args) {
        String cadena = "Cadena";
        System.out.println(cadena.replace("a","m"));
        System.out.println(cadena.toLowerCase());
        System.out.println(cadena.toUpperCase());
        System.out.println(cadena.concat("cadena"));
        System.out.println(cadena.charAt(2));
        System.out.println(cadena.substring(1,3));
        System.out.println(cadena.contains("en"));
        System.out.println(cadena.repeat(3));
        System.out.println(Arrays.toString(cadena.split("")));
        System.out.println(anagram("Caca","Ioio"));
        System.out.println(anagram("Perro","Rrope"));
        System.out.println(isogram("Perro"));
        System.out.println(isogram("paolpola"));
    }
    /*
     * EJERCICIO:
     * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
     * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
     * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
     *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
     *   interpolación, verificación...

     */


    /*

     * DIFICULTAD EXTRA (opcional):
     * Crea un programa que analice dos palabras diferentes y realice comprobaciones
     * para descubrir si son:
     * - Palíndromos
     * - Anagramas
     * - Isogramas
     */

    private static boolean palindrome (String cadena1){
      return cadena1.contentEquals(new StringBuilder(cadena1).reverse());
    };
    private static boolean anagram (String cadena1, String cadena2){
        if(cadena1.length()!=cadena2.length()) return false;
        String str1 = cadena1.toLowerCase().chars().sorted().collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append).toString();
        String str2 = cadena2.toLowerCase().chars().sorted().collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append).toString();

        return str1.equals(str2);
    }

    private static boolean isogram(String cadena) {
        Map<Character, Long> collect = cadena.chars().mapToObj(c -> (char) c)
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
        return collect.values().stream().allMatch(x -> x.equals(collect.get(cadena.charAt(0))));
    }

}