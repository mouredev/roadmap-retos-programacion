import java.util.Arrays;

public class Karolle {
    public static void main(String[] args) {
        // Operaciones con Strings
        String cadena = "Hola Mundo";
        System.out.println("Longitud: " + cadena.length());
        System.out.println("Carácter específico: " + cadena.charAt(0));
        System.out.println("Subcadena: " + cadena.substring(0, 4));
        System.out.println("Concatenación: " + cadena.concat(" de Java"));
        System.out.println("Mayúsculas: " + cadena.toUpperCase());
        System.out.println("Minúsculas: " + cadena.toLowerCase());
        System.out.println("Reemplazo: " + cadena.replace('o', 'a'));
        String[] division = cadena.split(" ");
        System.out.println("División: " + Arrays.toString(division));
        String union = String.join("-", division);
        System.out.println("Unión: " + union);
        
        // Verificación de palíndromos, anagramas e isogramas
        String palabra1 = "amor";
        String palabra2 = "roma";
        
        System.out.println("¿Son palíndromos? " + esPalindromo(palabra1, palabra2));
        System.out.println("¿Son anagramas? " + esAnagrama(palabra1, palabra2));
        System.out.println("¿Son isogramas? " + (esIsograma(palabra1) && esIsograma(palabra2)));
    }

    static boolean esPalindromo(String palabra1, String palabra2) {
        return new StringBuilder(palabra1).reverse().toString().equals(palabra2);
    }

    static boolean esAnagrama(String palabra1, String palabra2) {
        char[] array1 = palabra1.toCharArray();
        char[] array2 = palabra2.toCharArray();
        Arrays.sort(array1);
        Arrays.sort(array2);
        return Arrays.equals(array1, array2);
    }

    static boolean esIsograma(String palabra) {
        for (int i = 0; i < palabra.length(); i++) {
            for (int j = i + 1; j < palabra.length(); j++) {
                if (palabra.charAt(i) == palabra.charAt(j)) {
                    return false;
                }
            }
        }
        return true;
    }
}
