import java.util.Arrays;
import java.util.List;

public class Jeigar2 {
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
    public static void main(String[] args) {
        String cadena = "La vida es bella porque Dios te ama siempre";
        System.out.println("acceso al 2º carácter específico " + cadena.charAt(1));
        System.out.println("subcadena del 24 al final " + cadena.substring(24));
        System.out.println("subcadena del 24 al 28 " + cadena.substring(24,28));
        System.out.println("longitud: " + cadena.length());
        System.out.println("concatenación " + cadena + " / " + cadena.substring(24));
        System.out.println("repetición " + cadena.substring(24,29).repeat(3));
        System.out.println("recorrido: " + Arrays.stream(cadena.split("\s")).filter(s->s.indexOf('o')>1).findFirst());
        System.out.println("Mayúsculas: " + cadena.toUpperCase());
        System.out.println("Minúsculas: " + cadena.toLowerCase());
        System.out.println("Reemplazo: \n" + cadena.replaceAll(".","-") + "\n" + cadena + "\n" + cadena.replaceAll(".", "-") );
        System.out.println("division: sexta palabra " + cadena.split("\s")[5]);
        System.out.println("Unión " + String.join(" ", "Dios,te,ama".split(",")));
        System.out.println("Interpolación: " + String.format("Deja que %s sea %s", cadena.substring(24,28), cadena.substring(24,28)));
        System.out.println("Verificación: " + cadena.contains("Dios"));
        System.out.println("Verificación: " + cadena.substring(24).startsWith("Dios"));
        System.out.println("Verificación: " + cadena.substring(0,28).endsWith("Dios"));
        String palindromo = "dabale arroz a la zorra el abad".replaceAll(" ", "");
        System.out.println("Es palindromo: " + isPalindromo(palindromo));
        System.out.println("Es isograma: " + isIsograma("hola"));
        System.out.println("Es anagrama: " + isAnagrama("roma amor mora"));
        System.out.println("Es anagrama: " + isAnagrama("roma amor mori"));
    }

    public static boolean isPalindromo(String cadena){
        return cadena.equals(new StringBuilder(cadena).reverse().toString());
    }

    public static boolean isIsograma(String cadena){
        return cadena.chars().distinct().count() == cadena.length();
    }

    public static boolean isAnagrama(String cadena) {
        boolean continuar = false;
        String[] palabras = cadena.split(" ");
        if (palabras != null && palabras.length > 0) {
            List<String> listaPalabras = Arrays.asList(palabras);
            int totalPalabras = listaPalabras.size();
            int totalLetrasPrimeraPalabra = listaPalabras.getFirst().length();
            String primeraPalabra = listaPalabras.getFirst();
            long totalPalabrasCoincidenLargo = listaPalabras.stream().filter(s -> s.length() == totalLetrasPrimeraPalabra).count();
            continuar = (totalPalabras == totalPalabrasCoincidenLargo);

            boolean[][] posicionBool = new boolean[totalLetrasPrimeraPalabra][totalPalabras];

            if (continuar) {
                // comprobar todas las palabras y letras
                for (int letra = 0; letra < totalLetrasPrimeraPalabra; letra++) {
                    for (int palabra = 1; palabra < totalPalabras; palabra++) {
                        posicionBool[letra][palabra] = palabras[palabra].indexOf(primeraPalabra.charAt(letra)) >= 0;
                    }
                }
            }
            // comprobar si hay algun valor false
            for (int letra = 0; letra < totalLetrasPrimeraPalabra; letra++) {
                for (int palabra = 1; palabra < totalPalabras; palabra++) {
                    if (!posicionBool[letra][palabra]) {
                        return false;
                    }
                }
            }
        }
        return continuar;
    }
}
