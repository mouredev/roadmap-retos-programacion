import java.util.Arrays;

public class SandLeon {
    public static void main(String[] args) {

        String text = " Los sueños no funcionan a menos que tu trabajes en ellos. ";
        String text2 = "Cada dia es una nueva oportunidad para intentarlo otra vez.";

        //Longitud del texto, incluye espacios.
        System.out.println("Longitud de cadena: " + text.length());

        //Comparar dos cadenas.
        System.out.println("Comparar cadenas: " + text.equals(text2));
        System.out.println("Comparar cadenas ignorando case: " + text.equalsIgnoreCase(text2));//Ignorando mayúsculas y minúsculas.

        // Convierte a array de caracteres.
        System.out.println(Arrays.toString(text.toCharArray()));

        // Transforma a Mayúsculas o Minúsculas.
        System.out.println("Texto en Mayúsculas: " + text.toUpperCase());
        System.out.println("Texto en minúsculas: " + text2.toLowerCase());

        //Devuelve true solo si toda la cadena cumple exactamente con el patrón
        System.out.println("Cumple el patron? " + text2.matches("[a-z]+\\d+"));   //[a-z] Cualquier letra de a hasta z en minúscula.
        // \\d , un dígito numérico.

        //Devuelve tru o false si contiene la cadena "x".
        System.out.println("Contiene \"trabajes\" : " + text.contains("trabajes"));

        //Comprobar si está vacío.
        System.out.println("Está vacío?: " + text2.isEmpty());

        //Elimina espacios al principio y al final.
        System.out.println(text);
        System.out.println(text.trim());

        //Reemplazar
        System.out.println("Hola me llamo Sandra".replace("a","e"));
        System.out.println(text.replace("sueños","duendes"));

        //Repetición cadenas
        System.out.println("Vacaciones ".repeat(4));

        // Dar formato
        String name = "Sandra";
        int age = 35;
        System.out.printf("Hola, %s. tengo %d años.%n", name, age);

        //Substraer subcadena
        System.out.println(text2.substring(6));//Desde posición 6 hasta final.(Los espacios cuentan.)

        //Acceso a un caracter.
        System.out.println(text2.charAt(5));//por indice 5
        System.out.println(text.charAt(text.length()-2));//Penúltima posición.

        //Concatenar
        System.out.println(text + " " + text2);

        // DIFICULTAD EXTRA

        //Palíndromo.
        System.out.println(isPalindrome("Farolillo"));
        System.out.println(isPalindrome("reconocer"));

        //Anagrama
        System.out.println(isAnagram("caseta","alfombra"));
        System.out.println(isAnagram("Riesgo","sergio"));

        //Isograma.
        System.out.println(isIsogram("Abecedario"));
        System.out.println(isIsogram("plumero"));



    }

    /* DIFICULTAD EXTRA (opcional):
     * Crea un programa que analice dos palabras diferentes y realice comprobaciones
     * para descubrir si son:
     * - Palíndromos
     * - Anagramas
     * - Isogramas
     */

    //PALÍNDROMO

    public static boolean isPalindrome(String str1){
        System.out.println("La palabra " + "\"" + str1 + " \"  es palíndromo?");
        return  str1.equals(new StringBuilder(str1).reverse().toString());
    }

    //ANAGRAMA
    public static boolean isAnagram(String str1, String str2){

        System.out.println("La palabra " + "\"" + str1 + "\" y  \"" + str2 +"\" " + "son anagrama?");

        //  Quitar espacios y convertimos todo a minúsculas.
        str1 = str1.replaceAll("\\s", "").toLowerCase();
        str2 = str2.replaceAll("\\s", "").toLowerCase();

        if(str1.length() != str2.length()){
            return false;
        }
        // Crear arrays de chars para ordenarlos.
        char[] array1 = str1.toCharArray();
        char [] array2 = str2.toCharArray();
        //Ordenar arrays.
        Arrays.sort(array1);
        Arrays.sort(array2);
        // Comparación arrays.
        return Arrays.equals(array1,array2);
    }

    //ISOGRAMA

    public static boolean isIsogram(String str1){

        System.out.println("La palabra " + "\"" + str1 + " \"  es isograma?");

        //Ignorar espacios, tildes y mayúsculas.
        str1 = str1.toLowerCase().replaceAll("[^a-záéíóúüñ]", "");
        return str1.length() == str1.chars().distinct().count();
    }

}
