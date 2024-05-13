
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class chartypes {

    // Strings Operations
    static void stringsOperations() {
        String text = "Hellodah";
        // Specific charracter
        System.out.println(text.charAt(0));
        // Concat
        System.out.println(text.concat(" world!"));
        // Substrings
        System.out.println(text.substring(2));
        // Length
        System.out.println(text.length());
        // Repeat
        System.out.println(text.repeat(2));
        // Upper Case
        System.out.println(text.toUpperCase());
        // Lower Case
        System.out.println(text.toLowerCase());
        // Replace
        System.out.println(text.replace('H', 'j'));
        // Union
        System.out.println(String.join(" - ", text, "world", "!", "!", "!"));
        // Division
        System.out.println(Arrays.toString(text.split("o")));
        // Contains
        System.out.println(text.contains("Hello"));
        System.out.println("\n-----------------------\nExercise:");

    }

    // Exercise Services
    static boolean isPalindrome(String text) {
        StringBuilder strBuilder = new StringBuilder();
        for (int i = text.length() - 1; i >= 0; i--) {
            strBuilder.append(text.charAt(i));
        }
        String reversedText = new String(strBuilder);
        return text.equalsIgnoreCase(reversedText);

    }

    static Map<Character, Integer> lettersCounter(String text) {
        Map<Character, Integer> counter = new HashMap<>();
        for (char character : text.toCharArray()) {
            counter.put(character, counter.getOrDefault(character, 0) + 1);
        }
        return counter;
    }

    static boolean isIsogram(String text) {
        Map<Character, Integer> counter = lettersCounter(text);

        int len = counter.get(text.charAt(0));

        for (int value : counter.values()) {
            if (value != len)
                return false;
        }
        return true;

    }

    static boolean isAnagram(String text1, String text2) {
        Map<Character, Integer> text1Counter = lettersCounter(text1);
        Map<Character, Integer> text2Counter = lettersCounter(text2);
        for (Map.Entry<Character, Integer> entry : text1Counter.entrySet()) {
            char letter = entry.getKey();
            int counter = entry.getValue();
            try {
                if (text2Counter.get(letter) != counter)
                    return false;

            } catch (NullPointerException e) {
                return false;
            }
        }
        return true;

    }

    static void exercise(String text1, String text2) {
        text1 = text1.toLowerCase();
        text2 = text2.toLowerCase();

        // Palindrome
        System.out.println("\nPALIDROME:");
        if (isPalindrome(text1))
            System.out.println("YES " + text1 + " is a palidrome");
        else
            System.out.println("NO " + text1 + " is NOT a palidrome");
        if (isPalindrome(text2))
            System.out.println("YES " + text2 + " is a palidrome");
        else
            System.out.println("NO " + text2 + " is NOT a palidrome");

        // Anagram
        System.out.println("\nANAGRAM:");
        if (isAnagram(text1, text2))
            System.out.println("YES " + text1 + " is a anagram of " + text2);
        else
            System.out.println("NO " + text1 + " is NOT a anagram of " + text2);

        // Isogram
        System.out.println("\nISOGRAM:");
        if (isIsogram(text1))
            System.out.println("YES " + text1 + " is a isogram");
        else
            System.out.println("NO " + text1 + " is NOt a isogram");
        if (isIsogram(text2))
            System.out.println("YES " + text2 + " is a isogram");
        else
            System.out.println("NO " + text2 + " is NOt a isogram");

    }

    public static void main(String[] args) {

        stringsOperations();
        exercise("reinier", "ambidextrously");
        exercise("angel", "glean");
        exercise("save", "vase");

    }
}
