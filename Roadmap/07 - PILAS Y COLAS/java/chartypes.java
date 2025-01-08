import java.util.EmptyStackException;
import java.util.LinkedList;
import java.util.NoSuchElementException;
import java.util.Queue;
import java.util.Stack;

public class chartypes {

  public static void main(String[] args) {
    System.out.println("Exercise");
    queue();
    System.out.println();
    stack();
    System.out.println("\n///////////////////////////////////////\n");
    System.out.println("Extra:");

    System.out.println("Printer:");
    MyPrinter.addSheet("hmm..");
    MyPrinter.addSheet("test");
    MyPrinter.addSheet("imprimir");
    MyPrinter.addSheet("test2");
    MyPrinter.addSheet("ImpRimir");
    MyPrinter.addSheet("IMPRIMIR");
    MyPrinter.addSheet("ImpRimir");
    MyPrinter.addSheet("ImpRimir");

    System.out.println();

    System.out.println("Browser:");
    Browser.browser("github");
    Browser.browser("carlosperezm.com");
    Browser.browser("atras");
    Browser.browser("mouredev");
    Browser.browser("atras");
    Browser.browser("adelante");

  }

  static void queue() {
    Queue<Integer> myQueue = new LinkedList<>();
    myQueue.add(5);
    myQueue.add(0);
    myQueue.add(1131);
    myQueue.add(12);
    System.out.println("Queue: " + myQueue);
    System.out.println("peek:" + myQueue.peek());

    myQueue.remove();
    System.out.println("whole queue: " + myQueue);
    System.out.println("peek:" + myQueue.peek());

    System.out.println("is empty?: " + myQueue.isEmpty());
    System.out.println("size: " + myQueue.size());

  }

  static void stack() {
    Stack<String> myStack = new Stack<>();

    myStack.push("1st element of my stack");
    myStack.push("2nd element of my stack");
    myStack.push("3rd element of my stack");
    myStack.push("4th element of my stack");

    System.out.println("Stack: " + myStack);
    myStack.pop();
    System.out.println("Stack after popping: " + myStack);
    System.out.println("Stack peek: " + myStack.peek());

    System.out.println("is empty?: " + myStack.isEmpty());
    System.out.println("size: " + myStack.size());

  }
}

class MyPrinter {
  static private Queue<String> printer = new LinkedList<>();

  static void addSheet(String text) {

    if (text.toLowerCase().equals("imprimir")) {
      String peek = printer.peek();
      if (peek == null)
        System.out.println("No more elements in the printer");
      else {
        System.out.println(printer.peek());
        printer.remove();
      }
    } else
      printer.add(text);

  }
}

class Browser {
  static private Stack<String> history = new Stack<>();

  static void browser(String text) {
    String lastestItem = "";
    if (text.toLowerCase().equals("atras")) {
      try {
        System.out.println(history.get(history.size() - 2));

      } catch (EmptyStackException e) {
        System.out.println("No more elements in the browser");
      }
    } else if (text.toLowerCase().equals("adelante")) {
      lastestItem = history.pop();
      System.out.println(lastestItem);

    } else {
      history.push(text);

    }
  }

}
