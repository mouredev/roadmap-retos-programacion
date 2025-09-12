import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Qv1ko {

    public static void main(String[] args) {
        program("provide", "seasonal");
    }

    private static void program(String word1, String word2) {

        System.out.println(isPalindrome(word1) ? "The word " + word1 + " is a palindrome" : "The word " + word1 + " is not a palindrome");
        System.out.println(isPalindrome(word2) ? "The word " + word2 + " is a palindrome" : "The word " + word2 + " is not a palindrome");

        System.out.println(areAnagrams(word1, word2) ? "The words " +  word1 + " and " +  word2 + " are anagrams" : "The words " +  word1 + " and " +  word2 + " are not anagrams");

        System.out.println(isIsogram(word1) ? "The word " + word1 + " is an isogram" : "The word " + word1 + " is not an isogram");
        System.out.println(isIsogram(word2) ? "The word " + word2 + " is an isogram" : "The word " + word2 + " is not an isogram");

    }

    private static boolean isPalindrome(String word) {

        int len = word.length();

        for (int i = 0; i < len / 2; i++) {
            if (word.charAt(i) != word.charAt(len - i - 1)) {
                return false;
            }
        }

        return true;

    }

    private static boolean areAnagrams(String word1, String word2) {

        if (word1.length() != word2.length()) {
            return false;
        }

        char[] lettersWord1 = word1.toCharArray();
        char[] lettersWord2 = word2.toCharArray();

        Arrays.sort(lettersWord1);
        Arrays.sort(lettersWord2);

        return Arrays.equals(lettersWord1, lettersWord2);

    }

    public static boolean isIsogram(String word) {

        Set<Character> letters = new HashSet<>();

        for (char letter : word.toCharArray()) {
            if (!letters.add(letter)) {
                return false;
            }
        }

        return true;

    }

}
