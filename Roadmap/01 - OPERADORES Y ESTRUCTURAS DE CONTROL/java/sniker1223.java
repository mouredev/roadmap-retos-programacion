import java.util.Arrays;
import java.util.List;

public class sniker1223 {

  public static void main(String[] args) {
    int i = 10;
    int x = 12;
    String name = "Sara";

    // Arithmetic Operators
    System.out.println("Arithmetic Operators");
    System.out.println("+ Addition: " + (1 + 2));
    System.out.println("- Substraction: " + (1 - 2));
    System.out.println("* Multiplication: " + (1 * 2));
    System.out.println("/ Division: " + (1 / 2));
    System.out.println("% Modulus: " + (1 % 2));
    System.out.println("++ Increment: " + (++i));
    System.out.println("-- Decrement: " + (--i));

    // Assignment Operators
    System.out.println("\nAssignment Operators");
    System.out.println("= Assigment: i = " + i);
    System.out.println("+= Addition assigment: i += " + (i += 2));
    System.out.println("-= Substraction assigment: i -= " + (i -= 2));
    System.out.println("*= Multiplication assigment: i *= " + (i *= 2));
    System.out.println("/= Division assigment: i /= " + (i /= 2));
    System.out.println("%= Modulus assigment: i %= " + (i %= 7));
    System.out.println("&= Bitwise AND assigment: i &= " + (i &= 12));
    System.out.println("|= Bitwise OR assigment: i |= " + (i |= 4));
    System.out.println("^= Bitwise XOR assigment: i ^= " + (i ^= 8));
    System.out.println(">>= right shift assigment: i >>= " + (i >>= 1));
    System.out.println("<<= left shift assigment: i <<= " + (i <<= 1));

    // Comparison Operators
    System.out.println("\nComparison Operators");
    System.out.println("> Greater than: " + i + "  > " + x + " = " + (i > x));
    System.out.println("> Less than: " + i + "  < " + x + " = " + (i < x));
    System.out.println("== Equal to: " + i + "  == " + x + " = " + (i == x));
    System.out.println("!= Equal to: " + i + "  != " + x + " = " + (i != x));
    System.out.println(">= Greater than: " + i + "  >= " + x + " = " + (i >= x));
    System.out.println("<= Less than: " + i + "  <= " + x + " = " + (i <= x));

    // Logical Operators
    System.out.println("\nLogical Operators");
    System.out.println("&& Logical AND: " + x + " < 5 && " + x + " < 10" + " = " + (x < 5 && x < 10));
    System.out.println("||  Logical OR: " + x + " < 5 || " + x + " < 20" + " = " + (x < 5 || x < 20));
    System.out.println("!  Logical NOT: !(" + x + " < 5 && " + x + " < 10)" + " = " + !(x < 5 || x < 10));

    // Miscellaneous Operators
    System.out.println("\nMiscellaneous Operators");
    System.out.println("?: Ternary operator: (" + i + " == 1 ? 20 : 30 value of i is : " + ((i == 1) ? 20 : 30));
    System.out.println("instanceof Instanceof operator: " + name + " instanceof String  = " + (name instanceof String));

    // CONTROL STRUCTURES
    System.out.println("\nCONTROL STRUCTURES");
    // If/Else/Else If
    System.out.println("If/Else/Else If");
    if (i > 2) {
      System.out.println(i + " is higher than 2");
    } else {
      System.out.println(i + " is lower or equal than 2");
    }
    // Switch
    System.out.println("\nSwitch");
    i = 3;
    switch (i) {
      case 0:
        System.out.println(i + " is equal to 0");
        break;
      case 1:
        System.out.println(i + " is equal to 1");
        break;
      default:
        System.out.println(i + " is either negative, or higher than 1");
        break;
    }

    // Loops
    System.out.println("\nLoops");
    System.out.println("for");
    for (int a = 1; a <= 10; a++) {
      System.out.println(a);
    }
    System.out.println("\nwhile");
    while (i <= 10) {
      System.out.println(i);
      i++;
    }

    // Break with foreach
    System.out.println("\nBreak");
    List<String> names = Arrays.asList("Sara", "Selena");
    String nameBreak = "Sara";
    for (String cadena : names) {
      if (cadena.equals(nameBreak)) {
        System.out.println(cadena);
        break;
      }

    }

    // Challenge. Print numbers between 10 and 55(included), even and odd but not
    // print 16 and multiple of 3.
    int n;
    for (n = 0; n <= 55; n++) {
      if (n >= 10 && n % 2 == 0 && n != 16 && !(n % 3 == 0) || n == 55) {
        System.out.println(n);
      }
    }
  }
}