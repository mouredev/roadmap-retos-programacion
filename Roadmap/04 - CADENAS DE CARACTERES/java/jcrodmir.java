import java.util.*;

public class Strings {

    //Strings are Immutable must assignment to replace the value,
    static String  word="A new World with many words";
    static String word2= "Pepe";

    public static void main(String[] args) {
        //charAt
        System.out.println("Method charAt return Character: " + word.charAt(1));

        System.out.println("Method length return int: " + word.length());

        System.out.println("Method Format return String with the format that will us: " + String.format("Format String %s and decimal %d", word2, 15));

        System.out.println("Method subString return String: " + word.substring(6, 11));

        System.out.println("Method contains return boolean: " + word.contains("World"));

        System.out.println("Method join return String with the new element: " + String.join("/", word, word2));

        System.out.println("Method equals return boolean: " + word.equals(word2));

        System.out.println("Method equalsignoreCase return boolean : " + word.equalsIgnoreCase(word2));
        ////////////////////////////////////////////////////////////////////////////////////////
        System.out.println("Method replace return String: " + word.replace("o", "a"));

        System.out.println("Method split return array: " + Arrays.toString(word.split("\\s")));//Make an Array with each word for the sentence

        System.out.println("Method intern return String: " + word2.intern());//It returns an interned string

        System.out.println("Method indexOf return int: " + word.indexOf("World"));//The beginning for the Word "World" when not find is -1

        System.out.println("Method toLowerCase return String: " + word.toLowerCase());

        System.out.println("Method toUpperCase return String: " + word.toUpperCase());

        System.out.println("Method trim return String: " + word.trim());

        System.out.println("Method valueOf return String: " + String.valueOf(123));//Convert the int to String

        System.out.println("Method valueOf return String: " + word.concat(word2));

        System.out.println("Method valueOf return String: " + word.compareTo(word2));//With the result 0 we know that are equals


        //To compare two Strigs we can use ==,equals and compareTo()

        //StringBuffer is the same that builder but is synchronised and protect the thread

        //StringBuilder To create a mutable String
        System.out.println("****************StringBuilder***************");
        StringBuilder sb=new StringBuilder("Example for StringBuilder");
        sb.append(" other String Append");
        System.out.println("Method Append  add something: " + sb.toString());
        sb.insert(0,"1. ");
        System.out.println("Method Insert add something in the index: " + sb.toString());

        sb.replace(28,sb.length()," new String");
        System.out.println("Method replace: " + sb.toString());
        sb.delete(0,2);
        System.out.println("Method delete with start to end: " + sb.toString());
        sb.reverse();
        System.out.println("Method reverse: " + sb.toString());
        sb.reverse();
        System.out.println("Method capacity give us the capacity for the builder " + sb.capacity());


        //Extra
        System.out.println("EXTRA EXERCISE");
        Scanner sc1= new Scanner(System.in);
        System.out.println("First word: ");
        String firstWord= sc1.next();
        Scanner sc2= new Scanner(System.in);
        System.out.println("Second word: ");
        String secondWord= sc1.next();

        StringBuilder sbPalindrome=new StringBuilder(firstWord).reverse();

        if(sbPalindrome.toString().equals(secondWord)){
            System.out.println("They are Palindrome");
        }
        else{
            System.out.println("They are not Palindrome");
        }


        if(Arrays.equals(firstWord.chars().sorted().toArray(), secondWord.chars().sorted().toArray())){
            System.out.println("They are Anagram");
        }
        else{
            System.out.println("They are not Anagram");
        }


        if(isIsogram(firstWord)){
            System.out.println("The first word is an Isogram");
        }else{
            System.out.println("The first word is not an Isogram");
        }



    }

    public static boolean isIsogram(String word) {

        Map<Character, Integer> charCount = new HashMap<>();

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }

        int frequency = charCount.get(word.charAt(0));

        for (int count : charCount.values()) {
            if (count != frequency) {
                return false;
            }
        }
        return true;
    }
}