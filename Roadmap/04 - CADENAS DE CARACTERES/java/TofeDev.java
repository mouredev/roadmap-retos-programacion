import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class TofeDev {
    public static void main(String[] args) {
        
        String texto = "El día de hoy está soleado";
        String texto2 = "puede que hoy llueva";

        //Acceso a un caracter específico
        char caracter = texto.charAt(3);
        System.out.println(caracter); //d

        //Subcadena
        String subcadena = texto.substring(14, 26);
        System.out.println(subcadena); //está soleado

        //Longitud
        int longitud = texto.length();
        System.out.println(longitud); //26

        //Concatenación
        String concatenacion = texto + " y " + texto2;
        System.out.println(concatenacion);

        //División
        String[] division = "rojo, amarillo, azul, morado".split(", ");
        for (int i = 0; i <division.length; i++) {
            System.out.println(division[i]);
        }

        //Conversión mayúsculas
        String mayuscula = texto.toUpperCase();
        System.out.println(mayuscula);

        //Conversión minúscula
        String minuscula = texto.toLowerCase();
        System.out.println(minuscula);

        //Reemplazo
        String reemplazado = texto.replace("soleado", "nublado");
        System.out.println(reemplazado);

        //Verificación
        boolean contiene = texto.contains("hoy");
        System.out.println(contiene); //true

        /* DIFICULTAD EXTRA (opcional):
        * Crea un programa que analice dos palabras diferentes y realice comprobaciones
        * para descubrir si son:
        * - Palíndromos
        * - Anagramas
        * - Isogramas
        */ 

        String palabra1 = "reconocer";
        String palabra2 = "ballena";
        String palabra3 = "llenaba";
        String palabra4 = "cuervo";

        palindromo(palabra1); //True
        palindromo(palabra4); //False

        anagrama(palabra2, palabra3); //True
        anagrama(palabra3, palabra4); //False

        isograma(palabra4); //True
        isograma(palabra1); //False
    }

        //Palíndromo
    public static void palindromo(String palabra) {
        String palabraInvertida = "";
        for (int i = palabra.length() - 1; i >= 0; i--) {
            palabraInvertida += palabra.charAt(i);
        }
        if (palabra.equals(palabraInvertida)) {
            System.out.println("Es palíndromo");
        } else {
            System.out.println("No es palíndromo");
        }
    }

        //Anagrama
    public static void anagrama(String pal1,String pal2) {
        char[] chars1 = pal1.toLowerCase().toCharArray();
        char[] chars2 = pal2.toLowerCase().toCharArray();
        Arrays.sort(chars1);
        Arrays.sort(chars2);
        if (Arrays.equals(chars1, chars2)) {
            System.out.println("Es un anagrama");
        } else {
            System.out.println("No es un anagrama");
        }
    }

        //Isograma
    public static void isograma(String palabra) {
        Set<Character> letras = new HashSet<>();
        char[] cadenaToChar = palabra.toCharArray();
        for(char letra : cadenaToChar){
           letras.add(letra);
        }
        if (palabra.length() == letras.size()) {
            System.out.println("Es un isograma");
        } else {
            System.out.println("No es un isograma");
        }
    }
}
