import java.util.*;

public class danhingar {

    public static void main(String[] args) {
        String cadena = "Hola";
        String cadena1 = "Mundo";

        //Concatenación
        System.out.println(cadena.concat(" ").concat(cadena1));
        System.out.println(cadena+" "+cadena1);

        //Longitud
        System.out.println("Longitd cadena: "+cadena.length());

        //Repetición
        System.out.println(cadena.concat(" ").repeat(3));

        //Indexación
        System.out.println(cadena.charAt(3));

        //Porción
        System.out.println(cadena.substring(2));
        System.out.println(cadena.substring(0,1));
      
        //Búsqueda
        System.out.println(cadena.contains("l"));

        //Reemplazo
        System.out.println(cadena.replace("a", "o"));

        //Division
        System.out.println(List.of(cadena1.split("n")));
        System.out.println(List.of(cadena1.splitWithDelimiters("n",cadena1.indexOf("n"))));
        System.out.println(List.of(cadena1.split("[ud]")));

        //Mayusculas y minuscuulas
        System.out.println(cadena.toUpperCase());
        System.out.println(cadena.toLowerCase());
        
        //Eliminar espacion en blanco
        String cadena3 ="hola mundo ";
        System.out.println(cadena3.stripTrailing());
        System.out.println(cadena3.trim());
        System.out.println(cadena3.strip());

        //Búsqueda al principio y final
        System.out.println(cadena3.startsWith("hol"));
        System.out.println(cadena3.endsWith("la"));
        System.out.println(cadena1.startsWith("Mu"));
        System.out.println(cadena3.trim().endsWith("do"));

        //Búsqueda por posición
        System.out.println("Hola Mundo, Java!".indexOf("Mundo"));

        //Interpolación
        System.out.println(String.format("Hola %s, %s!", cadena1,"Java"));

        //Transformación en lista
        System.out.println(cadena3.toCharArray()[0]);

        //Transformacion a cadena
        List<String> list = List.of(cadena,cadena1);
        System.out.println(String.join(" ", list));

        //Comprobaciones varias
        System.out.println(cadena.isBlank());
        System.out.println(cadena.isEmpty());
        System.out.println(cadena.matches("d"));
        System.out.println(cadena.equalsIgnoreCase(cadena1));

        //EXTRA
        check("roma", "amor");
    
    }

    private static void check(String word1,String word2){
        isPalindrome(word1,word2);
        isAnagram(word1,word2);
        isIsogram(word1,word2);
    }

    private static void isPalindrome(String word1,String word2){
        
        System.out.println(String.format("¿%s es un palíndromo?: %b", word1,checkPalindrome(word1)));
        System.out.println(String.format("¿%s es un palíndromo?: %b", word2,checkPalindrome(word2)));
    }

    private static boolean checkPalindrome(String word) {
       String reverseWord ="";
       for(int i=word.length()-1;i>=0;i--){
        reverseWord+=word.charAt(i);
       }
       return word.equals(reverseWord);
      
    }

    private static void isAnagram(String word1,String word2){
        System.out.println(String.format("¿%s y %s son anagramas?: %b", word1,word2,checkAnagram(word1,word2)));
    }

    private static Object checkAnagram(String word1,String word2) {
        char[] letters1 = word1.replace(" ", "").toCharArray();
        char[] letters2 = word2.replace(" ", "").toCharArray();
        Arrays.sort(letters1);
        Arrays.sort(letters2);
        return Arrays.equals(letters1, letters2);
    }

    private static void isIsogram(String word1,String word2){
        System.out.println(String.format("¿%s es un isodrama?: %b", word1,checkIsogram(word1)));
        System.out.println(String.format("¿%s es un isodrama?: %b", word2,checkIsogram(word2)));
    }

    private static Object checkIsogram(String word1) {
        for(int i=0; i<word1.length()-1;i++){
            char letter =word1.charAt(i);
            if(word1.indexOf(letter)!=word1.lastIndexOf(letter)){
                return false;
            }
        }
        return true;
    }
    
}
