import java.util.LinkedList;
import java.util.List;

public class chartypes {

  public static void main(String[] args) {
    // Exercise
    System.out.println("--------------Excercise:---------------");
    MyClass object = new MyClass("Julio");
    object.printSomthing();
    object.belongs = "Carlos";
    object.printSomthing();
    System.out.println("--------------Extra:---------------");

    System.out.println("Queue");
    MyQueue<Integer> intQueue = new MyQueue<>();
    intQueue.addElement(4);
    intQueue.addElement(1);
    intQueue.printContent();
    intQueue.dropElement();
    System.out.println(intQueue.len());
    intQueue.printContent();

    System.out.println("\nStack");
    MyStack<String> strStack = new MyStack<>();
    strStack.pushElm("uno");
    strStack.pushElm("dos");
    strStack.pushElm("tres");
    strStack.printContent();
    strStack.remove();
    strStack.printContent();
    strStack.remove();
    System.out.println(strStack.len());
    strStack.printContent();

  }
}

class MyClass {
  public static String belongs = "Charlie";
  public String name;

  public MyClass(String name) {
    this.name = name;
  }

  public void printSomthing() {
    System.out.println("name: " + name);
    System.out.println("belongs to: " + belongs);
  }
}

class MyQueue<T> {
  private List<T> queue;

  public MyQueue() {
    queue = new LinkedList<>();
  }

  public void addElement(T item) {
    queue.addLast(item);

  }

  public void dropElement() {
    queue.removeFirst();
  }

  public int len() {
    return queue.size();
  }

  public void printContent() {
    System.out.println(queue);
  }

}

class MyStack<T> {
  private List<T> stack;

  public MyStack() {
    stack = new LinkedList<>();
  }

  public void pushElm(T item) {
    stack.addLast(item);
  }

  public void remove() {
    stack.removeLast();
  }

  public int len() {
    return stack.size();
  }

  public void printContent() {
    System.out.println(stack);
  }
}
