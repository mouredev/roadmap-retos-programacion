/**
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 * 
 * @version v1.0
 * 
 * @since 20/06/2024
 * 
 * @author GlossyPath
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class GlossyPath {
    
    public static void main(String[] args) {
        
        String cadena = "Premature optimization is the root of all evil.";
        String cadena2 ="listen silent";

        //acceso a caracteres específicos.
        System.out.println("Primer caracter de la cadena es: " + cadena.charAt(0));

        //acceso a subcadenas específicos. Tenemos varias maneras.
        //indice que comenzamos en adelante.
        System.out.println("Imprimimos desde el primer caracter en adelante. ->" + cadena.substring(1));

        //desde donde hasta donde.
        System.out.println("Imprimimos desde el noveno caracter hasta el bigésimo segundo. ->" +  cadena.substring(9, 22));

        //tamaño de la cadena.
        System.out.println("Longitud de la cadena es de: " +cadena.length() + "caracteres");

        //concatenación de cadenas.
        System.out.println(cadena.concat(" Try to avoid it."));

        //repetición de la cadena las veces que marquemos al método repeat().
        System.out.println(cadena.substring(0).repeat(2));

        //recorremos las palabras y buscamos la primera(findFirst) palabra donde tengamos el caracter 'i' en una posición mayor que 1.
        System.out.println(Arrays.stream(cadena.split("\\s+")).filter(s-> s.indexOf('i')> 1).findFirst());

        //convertimos los caracteres de la cadena a mayusculas
        System.out.println(cadena.toUpperCase());

        //convertimos los caracteres de la cadena a minúsculas
        System.out.println(cadena.toLowerCase());

        //intercambiamos el primer elemento por el segundo.
        System.out.println(cadena.replaceAll("\\s+", "-"));
        System.out.println(cadena.replaceAll("i", "-"));

        //intercambiamos el primer caracter por el segundo
        System.out.println(cadena.replace('a', 'A'));
       
        //divide en partes el String y devuelve el tercero
        System.out.println(cadena.split("\\s+")[3]);

        //cogemos un array y lo unimos
        String[] palabras = {"Try", "to", "avoid", "it"};
        System.out.println(String.join(" ", palabras));

        //interpolamos frase/palabra a partir del décimo caracter.
        System.out.println(String.format("Early %s", cadena.substring(10)));

        //comprovamos si la cadena contiene el argumento pasado
        System.out.println(cadena.contains("evil"));

        //comprovamos si el índice pasado como argumento empieza en 'o' el indice en adelante acaba en '.'
        System.out.println(cadena.substring(10).endsWith("."));
        System.out.println(cadena.substring(10).startsWith("o"));

        //llamamos al método para comprobar si la palabra pasada como argumento es un palíndromo.
        System.out.println(isPalindromo("ANNA"));

        //llamamos al método para comprobar si la palabra pasada como argumento es un isograma.
        System.out.println(isIsograma("ANNA"));

        //llamamos al método para comprobar si algunas de las palabras pasadas como argumento son anagrama entre ellas.
        System.out.println(isAnagrama(cadena2));
        System.out.println(isAnagrama(cadena));

    }

    /**
         *  DIFICULTAD EXTRA (opcional):
         * Crea un programa que analice dos palabras diferentes y realice comprobaciones
         * para descubrir si son:
         * - Palíndromos
         * - Anagramas
         * - Isogramas
         * 
         */

    /*
     * Descripción: método para averiguar si la palabra pasada es un palíndromo
     */
    public static boolean isPalindromo(String palabra) {

        return palabra.equals(new StringBuilder(palabra).reverse().toString());
    }

    /*
     * Descripción: método para averiguar si la palabra pasada es un palíndromo
     */
    public static boolean isIsograma(String palabra) {

        return palabra.chars().distinct().count() == palabra.length();
    }

    /*
     * Descripción: método para averiguar si la frase/palabras pasadas son un anagrama.
     */
     public static boolean isAnagrama(String cadena) {

        List<String>palabras = new ArrayList<>();

        if(cadena == null || cadena.isEmpty()){
            return false;
        }

        String[] palabrasArray = cadena.trim().split("\\s+");

        palabras = Arrays.asList(palabrasArray);

        for(int i = 0; i<palabras.size()-1; i++){

            char[] palabra = palabras.get(i).toCharArray();
            char[] palabraSiguiente = palabras.get(i+1).toCharArray();

            Arrays.sort(palabra);
            Arrays.sort(palabraSiguiente);

            if(!Arrays.equals(palabra, palabraSiguiente)){
                return false;
            }
        }
        return true;
     }

}
