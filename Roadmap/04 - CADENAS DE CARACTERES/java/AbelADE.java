/**
 *Solución al ejercicio #04 CADENAS DE CARACTERES.
 * 
 * @author AbelADE
 */
public class AbelADE {

    public static boolean isPalindrome(String text) {
        String text2 = "";
        for (int i = (text.length() - 1); i >= 0; i--) {
            text2 += text.charAt(i);
        }
        return text.equals(text2);
    }

    public static boolean isAnagram(String text1, String text2) {
        if (text1.length() != text2.length()) {
            return false;
        }

        for (int i = 0; i < text1.length(); i++) {
            if (!text2.toLowerCase().contains(String.valueOf(text1.charAt(i)).toLowerCase())) {
                return false;
            }
        }

        return true;
    }

    public static boolean isHeterogram(String text) {
        for (int i = 0; i < text.length(); i++) {
            for (int j = i + 1; j < text.length(); j++) {
                if (text.charAt(i) == text.charAt(j)) {
                    return false;
                }
            }
        }
        return true;
    }

    public static boolean isIsogram(String text) {  
        HashSet<Integer> counters = new HashSet<>();
        boolean addCounter;
        
        int counter;
        for (int i = 0; i < text.length(); i++) {
            counter = 0;
            addCounter = false;
            String char1 = Character.toString(text.charAt(i)).toLowerCase();
            
            for (int j = i+1; j < text.length(); j++) {
                String char2 = Character.toString(text.charAt(j)).toLowerCase();
                if (char1.equals(char2)) {
                    counter++;
                    addCounter = true;
                }
            }
            
            if (addCounter) {
                counters.add(counter);
            }
        }
      
        return counters.size()==1;
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        /**
         * Muestra ejemplos de todas las operaciones que puedes realizar con
         * cadenas de caracteres en tu lenguaje.
         */

        String text = "Este es un texto de prueba";

        System.out.println("Opciones en Java: ");
        System.out.println();

        //Obtener un caracter según posición
        System.out.println("Caracter: " + text.charAt(0));

        //Diferencia de longitud entre un texto y otro
        System.out.println("Diferencia de longitud: " + text.compareTo("Este"));

        //Comparar si son iguales
        System.out.println("¿Son iguales? : " + text.equals("Este"));

        //Comparar si son iguales sin tener en cuenta las mayúsulas
        System.out.println("¿Son iguales? (ignorando mayúsculas): " + text.equalsIgnoreCase("este es un texto de prueba"));

        //Concatenar texto
        System.out.println("Concatenar texto: " + text.concat(" en Java"));

        //Para ver si contiene una subcadena
        System.out.println("¿Contiene el texto? : " + text.contains("Este"));

        //Para ver si termina por una subcadena
        System.out.println("¿Termina por? : " + text.endsWith("Este"));

        //Encontrar el íncide de una subcadena dentro del texto
        System.out.println("Indice de subcadena: " + text.indexOf("texto"));

        //Encontrar el íncide de un caracter dentro del texto
        System.out.println("Indice de caracter: " + text.indexOf('E'));

        //Para ver si no tiene contenido o solo tiene espacios en blanco
        System.out.println("¿No tiene contenido o solo tiene espacios en blanco? : " + text.isBlank());

        //Para ver si no tiene contenido
        System.out.println("¿No tiene contenido? : " + text.isEmpty());

        //Encontrar el último íncdice de una subcadena dentro del texto
        System.out.println("Último índice de subcadena: " + text.lastIndexOf("texto"));

        //Encontrar el último íncide de un caracter dentro del texto
        System.out.println("Último índice de caracter: " + text.lastIndexOf('E'));

        //Longitud del texto
        System.out.println("Longitud: " + text.length());

        //Repite el texto n veces
        System.out.println("Repite el texto: " + text.repeat(2));

        //Remplaza una subcadena dentro del texto por otra
        System.out.println("Remplaza texto: " + text.replace("Este es", "Soy"));

        //Comprueba si empieza por una subcadena
        System.out.println("¿Empieza por? : " + text.startsWith("Este"));

        //Devuelve la secuencia de caracteres que se encuentra entre los índices indicados
        System.out.println("Secuencia de caracteres (por índices): " + text.subSequence(0, 10));

        //Devuelve la subcadena que se encuentra entre los índices indicados
        System.out.println("Subcadena (por índices): " + text.substring(0, 10));

        //Devuelve el texto a partir del índice
        System.out.println("Texto a partir de índice: " + text.substring(10));

        //Texto en minúsculas
        System.out.println("Texto en minúsculas: " + text.toLowerCase());

        //Texto en mayúsculas
        System.out.println("Texto en mayúsculas: " + text.toUpperCase());

        /**
         * DIFICULTAD EXTRA (opcional):
         */
        System.out.println();
        System.out.println("DIFICULTAD EXTRA (opcional):");
        System.out.println();

        System.out.println("¿Es palíndromo? : " + isPalindrome("323"));

        System.out.println("¿Es anagrama? : " + isAnagram("Listen", "Silent"));

        System.out.println("¿Es heterograma? : " + isHeterogram("yuxtaponer"));

        System.out.println("¿Es isograma? : " + isIsogram("papelera"));
    }

}
