public class chartypes {

  public static void main(String[] args) {

    // Exercise
    try {
      System.out.println(10 / 0);
    } catch (ArithmeticException e) {
      System.out.println(e.getMessage());
    }

    System.out.println("/////////////////EXTRA: ///////////////////////");
    // Extra

    int[] numbers = { 2, 3, };
    int[] numbs = { 1, 3, 2, 3, 0 };

    try {
      myFunction(numbers, 1.8f);
      System.out.println("1 jejeje");
    } catch (ArrayIndexOutOfBoundsException | MyException e) {
      System.out.println(e.getMessage());
    }

    try {
      myFunction(new int[] { 2, 3, 4, 5, 1 }, -1.8f);
      System.out.println("2 jejeje");
    } catch (MyException e) {
      System.out.println(e.getMessage());
    }

    try {
      myFunction(numbs, 51.8f);
      System.out.println("Any error has ocurred ");
    } catch (ArithmeticException | MyException e) {
      System.out.println(e.getMessage());
    }

    System.out.println("Program finished");
  }

  public static void myFunction(int[] numbers, float floatNumber)
      throws MyException, ArrayIndexOutOfBoundsException, ArithmeticException {
    int x = numbers[0];
    int y = numbers[4];
    int res = x / y;

    if (floatNumber < 0)
      throw new MyException("Number cannot be less than zero");

    System.out.println("end of the function");
  }

}

class MyException extends Exception {
  public MyException(String message) {
    super(message);
  }
}
