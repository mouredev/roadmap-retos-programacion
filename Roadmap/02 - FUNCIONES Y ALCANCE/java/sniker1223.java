import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class sniker1223 {
  // Global variable
  static int count = 0;

  public static void main(String[] args) {

    // examples of functions
    noParameterNoReturn();
    greet("Sniker");
    System.out.println("This function has return: " + add(1, 2));
    System.out.println("This function contains a function.: " + calculate(0, 10));

    // Local variable
    List<String> words = Arrays.asList("THE", "QUICK", "BROWN", "FOX");

    List<String> lowercaseWords = words.stream()
        .map(word -> word.toLowerCase())
        .collect(Collectors.toList());
    System.out.println("toLowerCase() function: " + lowercaseWords);
    System.out.println("Local variable: " + words);
    System.out.println("Global variable: " + count);
    // Challenge
    System.out
        .println("Number of times the number has been printed: " + printNumbersAndStrings1to100("Star", "Wars"));
  }

  // function no parameter and no Return
  public static void noParameterNoReturn() {
    System.out.println("Function no parameter and no Return!");
  }

  // with one or more parameters
  public static void greet(String name) {
    System.out.println("Hello, " + name + "! This function has one parameters");
  }

  // function has return
  public static int add(int number1, int number2) {
    return number1 + number2;
  }

  public static int calculate(int number1, int number2) {
    return add(number1, number2);
  }

  public static int printNumbersAndStrings1to100(String text1, String text2) {
    for (int i = 1; i <= 100; i++) {
      if (i % 3 == 0 && i % 5 == 0) {
        System.out.println(text1 + text2);
      } else if (i % 3 == 0) {
        System.out.println(text1);
      } else if (i % 5 == 0) {
        System.out.println(text2);
      } else {
        System.out.println(i);
        count++;
      }
    }
    return count;
  }
}
