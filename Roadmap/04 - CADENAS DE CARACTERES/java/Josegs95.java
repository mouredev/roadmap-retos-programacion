import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Josegs95 {
    public static void main(String[] args) {
        //Operaciones con cadenas
        String miString = "Esta es mi cadena";
        System.out.println(miString); //Out: Esta es mi cadena

        //Acceso a un carácter en especifico
        System.out.println(miString.charAt(2)); //Out: t

        //Crear una subcadena
        String miSubString = miString.substring(11);
        System.out.println(miSubString); //Out: cadena

        //Longitud de una cadena
        System.out.println(miSubString.length()); //Out: 6

        //Concadenación
        System.out.println(miString.concat(" concadenada")); //Out: Esta es mi cadena concadenada

        //Repetición
        System.out.println(miSubString.repeat(2)); //Out: cadenacadena

        //Búsqueda de una cadena
        System.out.println(miString.contains("mi")); //Out: true

        //Búsqueda del índice de una cadena
        System.out.println(miString.indexOf("cadena")); //Out: 11

        //Conversión a mayúsculas y minúsculas
        System.out.println(miString.toUpperCase()); //Out: ESTA ES MI CADENA
        System.out.println(miString.toLowerCase()); //Out: esta es mi cadena

        //Comparación de cadenas
        System.out.println(miString.equals(miSubString)); //Out: false

        //Verificación si empieza o termina por una cadena
        System.out.println(miString.startsWith("Esta")); //Out: true
        System.out.println(miString.endsWith("subcadena")); //Out: false

        //Reemplazo de carácteres o cadenas
        System.out.println(miString.replace(' ', '_')); //Esta_es_mi_cadena

        //División de una cadena por un patrón
        String[] division = miString.split(" ");
        System.out.println(Arrays.toString(division)); //Out: [Esta, es, mi, cadena]

        //Eliminación de espacios
        String cadEspacios = "   Esta es mi cadena con espacios en blanco ";
        System.out.println(cadEspacios.trim()); //Out: "Esta es mi cadena con espacios en blanco"
        System.out.println(cadEspacios.strip()); //Out: "Esta es mi cadena con espacios en blanco"
        System.out.println(cadEspacios.stripLeading()); //Out: "Esta es mi cadena con espacios en blanco "
        System.out.println(cadEspacios.stripTrailing()); //Out: "   Esta es mi cadena con espacios en blanco"

        //Formateo e interpolación
        double nPi = 3.141592;
        System.out.println(String.format("%.2f", nPi)); //Out: 3,14
        String nombre = "Jose";
        String lenguaje = "Java";
        System.out.println(String.format("Hola, soy %s y estoy escribiendo en %s", nombre, lenguaje));
                            //Out: Hola, soy Jose y estoy escribiendo en Java

        //Separación en lista de caracteres
        char[] caracteres = miSubString.toCharArray();
        System.out.println(Arrays.toString(caracteres)); //Out: [c, a, d, e, n, a]

        //Transformación de una lista de cadenas en una sola cadena
        String[] cadenas = {"Mi", "cadena", "separada"};
        System.out.println(String.join(" ", cadenas)); //Out: Mi cadena separada

        //Reto
        System.out.println("\n");
        retoFinal("rayar", "popolele");
    }

    public static void retoFinal(String word1, String word2){
        System.out.println("¿La palabra '" + word1 + "' es un palíndromo?: " + isPalindrome(word1));
        System.out.println("¿La palabra '" + word2 + "' es un palíndromo?: " + isPalindrome(word2));
        System.out.println("¿La palabra '" + word1 + "' es un anagrama de " + word2 + "?: " + areAnagram(word1, word2));
        System.out.println("¿La palabra '" + word1 + "' es un isograma?: " + isIsogram(word1));
        System.out.println("¿La palabra '" + word2 + "' es un isograma?: " + isIsogram(word2));
    }

    private static boolean isPalindrome(String w1){
        StringBuilder sb = new StringBuilder();
        sb.append(w1);
        return sb.reverse().toString().equals(w1);
    }

    private static boolean areAnagram(String w1, String w2){
        char[] charArray1 = w1.toCharArray();
        char[] charArray2 = w2.toCharArray();
        Arrays.sort(charArray1);
        Arrays.sort(charArray2);

        return Arrays.equals(charArray1, charArray2);
    }

    private static boolean isIsogram(String w1){
        Map<Character, Integer> letters = new HashMap<>();
        for (Character c : w1.toCharArray())
            letters.put(c, letters.get(c) == null ? 1 : (letters.get(c) + 1));
        for (Map.Entry<Character, Integer> entry : letters.entrySet()){
            if (letters.get(w1.charAt(0)) != entry.getValue())
                return false;
        }

        return true;
    }
}
