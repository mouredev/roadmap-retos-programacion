import java.util.Arrays;
import java.util.Scanner;

public class FranDev200 {

    static void main() {
    /*
        Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
        en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
        - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
        conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...

     */

        String string = "Hola, Java!";

        System.out.println("Mayusculas: " + string.toUpperCase());
        System.out.println("Minusculas: " + string.toLowerCase());
        System.out.println("Caracter de la posicion 5: " + string.charAt(5)); // Espacio en blanco
        System.out.println("Caracter de la posicion 0: " + string.charAt(0));
        System.out.println("Comparacion ignorando mayusculas y minusculas: " + string.equalsIgnoreCase("Hola, java!"));
        System.out.println("Comparacion contando mayusculas y minusculas: " + string.equals("Hola, java!"));
        System.out.println("Concatenacion: " + string.concat(". Adios, Python!") );
        System.out.println("¿Contiene \"ol\"?: " + string.contains("ol"));
        System.out.println("¿Contiene \"java\"?: " + string.contains("java"));
        System.out.println("Acaba en \"Java\": " + string.endsWith("Java"));
        System.out.println("Posicion de la letra 'a': " + string.indexOf('a'));
        System.out.println("¿Está en blanco?: " + string.isBlank());
        string = " ";
        System.out.println("¿Está vacío?: " + string.isEmpty()); // Los espacios cuentan como contenido, asi que no esta vacio.
        string = "Hola, Java!";
        System.out.println("Cuantos caracteres tiene: " + string.length());
        System.out.println("Repetir la cadena: " + string.repeat(3));
        System.out.println("Remplazar caracteres: " + string.replace("a", "o"));
        System.out.println("Pasar una cadena a array: " + Arrays.stream(string.split(",")).toList());
        System.out.println("Caracteres entre la posicion 3 y 7: " + string.substring(3, 7));
        string = "   Hola, Java!        ";
        System.out.println(string);
        System.out.println(string.trim()); // Elimina los espacios al principio y final de la cadena
        string = string.trim();
        System.out.println("¿Empieza por \"h\"?: " + string.startsWith("h"));
        System.out.println("¿Empieza por \"Ho\"?: " + string.startsWith("Ho"));

        /*
            DIFICULTAD EXTRA (opcional):
            Crea un programa que analice dos palabras diferentes y realice comprobaciones
            para descubrir si son:
            - Palíndromos
            - Anagramas
            - Isogramas
         */

        Scanner scan = new Scanner(System.in);
        System.out.print("Introduce la primera palabra: ");
        String word1 = scan.nextLine();
        System.out.print("Introduce la segunda palabra: ");
        String word2 = scan.nextLine();

        System.out.println("¿Las palabras introducidas son palíndromos?: ");
        System.out.println(word1 + ": " + palindromo(word1));
        System.out.println(word2 + ": " + palindromo(word2));
        System.out.println("¿Las palabras introducidas son anagramas?: ");
        System.out.println(anagrama(word1, word2));
        System.out.println("¿Las palabras introducidas son isogramas?: ");
        System.out.println(word1 + ": " + isograma(word1));
        System.out.println(word2 + ": " + isograma(word2));

    }

    public static boolean palindromo(String word){

        boolean result = false;
        char[] charSequence = word.toLowerCase().toCharArray();
        for(int i = charSequence.length - 1, j = 0; i >= 0; i--, j++){
            if(charSequence[i] == charSequence[j]){
                result = true;
            }else {
                result = false;
                break;
            }
        }
        return result;
    }

    public static boolean anagrama(String word1, String word2){

        if(word1.length() != word2.length()){
            return false;
        }

        boolean result = false;

        for(int i = 0; i < word1.length(); i++){
            for(int j = 0; j < word2.length(); j++){
                if(word1.toLowerCase().charAt(i) == word2.toLowerCase().charAt(j)){
                    result = true;
                    break;
                }else{
                    result = false;
                }
            }

            if(result == false){
                break;
            }

        }
        return result;

    }

    public static boolean isograma(String word){
        boolean result = false;
        int letterCounter = 0;
        char[] charSequence = word.toLowerCase().toCharArray();
        char[] charSequence2 = word.toLowerCase().toCharArray();
        for(int i = 0; i < charSequence.length; i++){
            letterCounter = 0;
            for (int j = 0; j < charSequence2.length; j++){

                if(word.toLowerCase().charAt(j) == charSequence[i]){
                    letterCounter++;
                }

            }

            if(letterCounter == 1){
                result = true;
            }else if( letterCounter > 1){
                result = false;
                break;
            }else{
                result = false;
            }

        }
        return result;
    }

}
