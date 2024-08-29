
import java.util.*;
public class simonguzman {
    public static void main(String[] args) {
        
        String str1 = " Hello ";
        String str2 = " Challenge # 03 ";
        String str3 = " character ";
        String str4 = " strings ";

        //Concatenar
        String concatenatedString = str1 + str2 + str3 + str4;
        System.out.println(concatenatedString);
        String concatenatedString2 = str1.concat(concatenatedString);
        System.out.println(concatenatedString2);
        
        //Obtener caracter en posicion especifica
        char ch = str1.charAt(2);
        System.out.println(ch);

        //Subcadena de una cadena
        String sub = str1.substring(2);
        System.out.println(sub);
        String sub2 = str1.substring(2, 4);
        System.out.println(sub2);

        //Longitud de una cadena
        int len = str1.length();
        System.out.println(len);

        //comparando 2 cadenas(sensible a las mayusculas)
        boolean isEqual = str1.equals(" HELLO ");
        System.out.println(isEqual);
        //Comparando 2 cadenas(sin importar las mayusculas)
        boolean isEqual2 = str1.equalsIgnoreCase(" HELLO ");
        System.out.println(isEqual2);

        //Comparacion alfabetica de 2 cadenas(sensible a mayusculas)
        int compare = str1.compareTo(" hello ");
        System.out.println(compare);
        //Comparacion alfabetica de 2 cadenas(sin importar las mayusculas)
        int compare2 = str1.compareToIgnoreCase(" hello ");
        System.out.println(compare2);

        //Repetir una cadena
        String repeatString = str1.repeat(3);
        System.out.println(repeatString);

        //Reemplazar caracteres
        String charReplaced = str1.replace("l", "d");
        System.out.println(charReplaced);
        //Reemplazar subcadenas
        String subStrReplaced = str1.replace("ell", "all");
        System.out.println(subStrReplaced);

        //Convertir a mayusculas
        String upper = str1.toUpperCase();
        System.out.println(upper);
        //Convertir a minusculas
        String lower = str1.toLowerCase();
        System.out.println(lower);

        //Eliminar espacios en blanco al inicio y al final
        String trimmed = str1.trim();
        System.out.println(trimmed);

        //Convertir a otros tipos de cadena
        String fromInt = str1.valueOf(123);
        System.out.println(fromInt);
        String fromChar = str1.valueOf('a');
        System.out.println(fromChar);

        //Si una cadena esta dentro de otra
        boolean contains = str1.contains("ell");
        System.out.println(contains);
        //Verificar si comienza con una subcadena
        boolean startsWith = str1.startsWith(" Hel");
        System.out.println(startsWith);
        //Verificar si termina con una subcadena
        boolean endsWith = str1.endsWith("llo ");
        System.out.println(endsWith);

        //Buscar posicion de una caracter o subcadena
        int index = str1.indexOf('l');
        System.out.println(index);
        int lastIndex = str1.lastIndexOf("l");
        System.out.println(lastIndex);
        int subIndex = str1.indexOf("ell");
        System.out.println(subIndex);

        //Verificar si una cadena esta vacia
        boolean isEmpty = str1.isEmpty();
        System.out.println(isEmpty);

        //Si una cadena es nula
        boolean isBlank = str1 == null;
        System.out.println(isBlank);

        //Recorrer cada caracter de la cadena
        for(int i = 0; i < str1.length(); i++){
            System.out.println(str1.charAt(i));
        }

        //Invertir una cadena
        String reversed = "";
        for(int i = str1.length() - 1; i >= 0; i--){
            reversed += str1.charAt(i);   
        }
        System.out.println(str1);
        System.out.println(reversed);

        ingresarPalabras();
    }

    //******************************** Ejercicio adicional ********************************/

    public static void ingresarPalabras(){
        Scanner scanner = new Scanner(System.in);
        String word1 = " ";
        String word2 = " "; 
        System.out.println("Ingrese la primer palabra: ");
        word1 = scanner.next();
        System.out.println("Ingrese la segunda palabra: ");
        word2 = scanner.next();
        palindromo(word1, word2);
        anagrama(word1, word2);
        isograma(word1, word2);
        scanner.close();
    }

    public static void anagrama(String word1, String word2) {
        String difOrderWord1 = ordenarPalabra(word1);
        String difOrderWord2 = ordenarPalabra(word2);

        if ( difOrderWord1.equals(difOrderWord2)){
            System.out.println("Las palabras son anagramas");
        }else{
            System.out.println("Las palabras no son anagramas");
        }
    }

    public static void isograma(String word1, String word2){
        boolean wordIsogram = verificarDuplicados(word1);
        boolean wordIsogram2 = verificarDuplicados(word2);
        if(wordIsogram){
            System.out.println("La palabra es isograma");
        }else{
            System.out.println("La palabra no es isograma");
        }

        if(wordIsogram2){
            System.out.println("La palabra es isograma");
        }else{
            System.out.println("La palabra no es isograma");
        }
    }

    public static void palindromo(String word1, String word2){
        String reverseWord1 = InvertirPalabra(word1);
        String reverseWord2 = InvertirPalabra(word2);

        if(word1.equals(reverseWord1)){
            System.out.println("Es palindromo");
        }else{
            System.out.println("No es palindromo");
        }
        if(word2.equals(reverseWord2)){
            System.out.println("Es palindromo");
        }else{
            System.out.println("No es palindromo");
        }
    }

    public static String InvertirPalabra(String word){
        String reverseWord = "";
        for (int i = word.length() - 1; i >= 0; i--){
            reverseWord += word.charAt(i);
        }
        return reverseWord;
    }

    public static String ordenarPalabra(String word){
        char [] sortWork = word.toCharArray();
        Arrays.sort(sortWork);

        String newWork = new String(sortWork);
        return newWork;
    }

    public static boolean verificarDuplicados(String word){
        Set characthers = new HashSet<>();
        for (int i = 0; i < word.length(); i++){
            char c = word.charAt(i);
            if(characthers.contains(c)){
                return false;
            }
            characthers.add(c);
        }
        return true;
    }

}
