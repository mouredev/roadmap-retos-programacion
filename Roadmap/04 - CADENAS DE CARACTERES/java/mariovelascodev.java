import java.util.ArrayList;
import java.util.Collections;

public class mariovelascodev {

    public static void main(String[] args) {
         String greeting = "Hola, Java";

         //Longitud del string
        System.out.println("Longitud de la cadena de texto: "+greeting.length());

        //Métodos para poner toda la cadena en mayúsculas y en minúsculas
        System.out.println(greeting);
        System.out.println(greeting.toUpperCase());
        System.out.println(greeting.toLowerCase());

        //Encontrar carácter en una cadena
        System.out.println("El primer carácter 'a' en la cadena \""+greeting+"\" esta en el indice: "
                +greeting.indexOf("a"));

        System.out.println("El último carácter 'a' en la cadena \""+greeting+"\" esta en el indice: "
                +greeting.lastIndexOf("a"));

        System.out.println("En el indice 6 de la cadena\""+greeting+"\" contiene la letra: "+greeting.charAt(6));

        //Comparación de cadenas
        String farewell = "Adios, Java";
        String greetingUppercase = greeting.toUpperCase();

        System.out.println("\""+greeting+"\" es igual que \""+farewell+"\": "+greeting.equals(farewell));
        System.out.println("\""+greeting+"\" es igual que \""+farewell+"\": "+greeting.equalsIgnoreCase(farewell));

        System.out.println("\""+greeting+"\" es igual que \""+greetingUppercase+"\": "
                +greeting.equals(greetingUppercase));
        System.out.println("\""+greeting+"\" es igual que \""+greetingUppercase+"\": "
                +greeting.equalsIgnoreCase(greetingUppercase));

        //Eliminar espacios en blanco
        String greetingWithSpaces = "   Hola, Java  ";
        System.out.println("Antes: [" + greetingWithSpaces + "]");
        System.out.println("Despues:  [" + greetingWithSpaces.trim() + "]");

        //Devolver valor Unicode
        int firstUnicodeValue = greeting.codePointAt(0);
        int secondUnicodeValue = greeting.codePointBefore(3);

        System.out.println("El carácter Unicode de la posición 0 en la cadena \""+greeting+"\" es: "
                +firstUnicodeValue);
        System.out.println("El carácter Unicode despues de la posición 3 en la cadena \""+greeting+"\" es: "
                +secondUnicodeValue);

        //Concatenar cadenas
        String concatString = greeting.concat(farewell);
        System.out.println(concatString);

        //Ver si cadena contiene caracteres
        System.out.println("La cadena \""+greeting+"\" contiene la palabra 'Java': "+greeting.contains("Java"));
        System.out.println("La cadena \""+greeting+"\" contiene la palabra 'JavaScript': "
                +greeting.contains("JavaScript"));
        System.out.println("La cadena \""+greeting+"\" contiene la palabra 'java': "
                +greeting.contentEquals("java"));

        //Ver si la cadena termina o empieza con los caracteres especificados
        System.out.println("La cadena \""+greeting+"\" termina por 'ava': "+greeting.endsWith("ava"));
        System.out.println("La cadena \""+greeting+"\" termina por 'e': "+greeting.endsWith("e"));

        System.out.println("La cadena \""+greeting+"\" empieza por 'Hol': "+greeting.startsWith("Hol"));
        System.out.println("La cadena \""+greeting+"\" empieza por 'o': "+greeting.startsWith("o"));

        //Formateo de cadena
        String myStr = "¡Hola %s! Un kilobyte es %,d bytes.";
        String result = String.format(myStr, "Mundo", 1024);
        System.out.println(result);

        //Ver si una cadena está vacía
        String emptyString = "";
        System.out.println("¿La cadena está vacía? "+greeting.isEmpty()+" devuelve falso si la cadena no está vacía");
        System.out.println("¿La cadena está vacía? "+emptyString.isEmpty()+" devuelve verdadero si la cadena está vacía");

        //Unir con separador específico
        String fruits = String.join(" ", "Orange", "Apple", "Mango");
        System.out.println(fruits);

        //Reemplazar valor específicado
        String newGreeting = greeting.replace("J", "L");
        System.out.println(newGreeting);

        String text = "I love cats. Cats are very easy to love. Cats are very popular.";
        String replace_word = text.replaceAll("(?i)cats", "Dog");
        System.out.println(replace_word);

        //Subcadenas
        String substringGreeting = greeting.substring(0, 4);
        String otherSubstringGreeting = greeting.substring(6);

        System.out.println(substringGreeting);
        System.out.println(otherSubstringGreeting);

        /*Extra*/
        System.out.println("----------EXTRA----------");
        /*
         * Crea un programa que analice dos palabras diferentes y realice comprobaciones
         * para descubrir si son:
             * - Palíndromos
             * - Anagramas
             * - Isogramas
        */

        palindrome("amad", "dama");
        palindrome("casa", "barco");

        anagram("nacionalista", "altisonancia");
        anagram("nacimiento", "cimiento");
        anagram("the alias men", "alan smithee");

        isogram("casa");
        isogram("murcielago");

    }

    public static void palindrome(String word1, String word2){
        String reversedWord1 = " ";
        for (int i =word1.length()-1; i >= 0; i--) {
            reversedWord1 += word1.charAt(i);
        }
        if (reversedWord1.trim().equals(word2)) {
            System.out.println("Las palabras introducidas son palíndromos");
        }else {
            System.out.println("Las palabras introducidas no son palíndromos");
        }
    };

    public static void anagram(String word1, String word2){
        ArrayList<String> listWord1 = new ArrayList<String>();
        ArrayList<String> listWord2 = new ArrayList<String>();

        //Metemos los caracteres de la cadena en un string
        for(int i = 0; i < word1.length(); i++){
            listWord1.add(word1.charAt(i) + "");
        }

        for(int i = 0; i < word2.length(); i++){
            listWord2.add(word2.charAt(i) + "");
        }

        //Ordenamos los ArrayList y lo guardamos en una variable string para comparar
        Collections.sort(listWord1);
        Collections.sort(listWord2);

        String sortWord1 = "";
        String sortWord2 = "";
        for(String letter1 : listWord1){
            sortWord1 += letter1;
        }

        for(String letter2 : listWord2){
            sortWord2 += letter2;
        }

        //Comparamos las dos cadenas introducidas quitando los espacios en blanco
        if(sortWord1.trim().equals(sortWord2.trim())){
            System.out.println("Las palabra introducidas son un anagrama");
        }
        else{
            System.out.println("Las palabras introducidas no son un anagrama");
        }
    };

    public static void isogram(String word){
        String saveWord = "";

        boolean isIsogram = true;

        //Recorremos la palabra y comprobamos si tiene letras repetidas
        for(int i = 0; i < word.length(); i++){
            if (saveWord.contains(word.charAt(i) + "")) {
                isIsogram = false;
            }else{
                saveWord += word.charAt(i);
            }
        }
        if (isIsogram) {
            System.out.println("La palabra "+word+" es un isograma");
        }else{
            System.out.println("La palabra "+word+" no es un isograma");
        }
    };
}
