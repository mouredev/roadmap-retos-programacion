import java.time.LocalDate;
import java.time.Period;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class Poo {
    public static void main(String[] args) {
        // creamos un objeto de la clase estudiante,
        Student s = new Student(120, "Amador", "Quispe", LocalDate.of(1992, 7, 13));
        System.out.println(s);

        System.out.println("Pilas personalizadas");
        DinamicStack<Integer> pilaNums = new DinamicStack<>();
        pilaNums.push(120);
        pilaNums.push(130);
        pilaNums.push(140);
        pilaNums.push(150);
        System.out.println(pilaNums.peek());
        System.out.println(pilaNums.size());
        System.out.println(pilaNums.pop());
        System.out.println(pilaNums.pop());
        System.out.println(pilaNums.size());
        pilaNums.forEach(System.out::print);
        System.out.println("Colas personalizadas");
        DinamicQueue<Integer> numbers = new DinamicQueue<>();
        System.out.println(numbers.enqueue(1));
        System.out.println(numbers.enqueue(2));
        System.out.println(numbers.enqueue(3));
        System.out.println(numbers.enqueue(4));
        System.out.println("Tamaño de cola antes de encolar " + numbers.size());
        System.out.println(numbers.dequeue());
        System.out.println("Tamaño de cola despues de encolar " + numbers.size());
        numbers.forEach(System.out::println);
    }
}

class Student {
    private int code;
    private String firstName;
    private String lastName;
    private LocalDate birthdate;
    private int age;

    public Student(int code, String firstName, String lastName, LocalDate birthdate) {
        this.code = code;
        this.firstName = firstName;
        this.lastName = lastName;
        this.birthdate = birthdate;
    }

    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public LocalDate getBirthdate() {
        return birthdate;
    }

    public void setBirthdate(LocalDate birthdate) {
        this.birthdate = birthdate;
    }

    public int getAge() {
        Period period = Period.between(birthdate, LocalDate.now());
        age = period.getYears();
        return age;
    }

    @Override
    public String toString() {
        return String.format("code=%d, firstName=%s, lastName=%s, age=%d ", code, firstName, lastName, getAge());
    }

}

class Node<T> {
    private T value;
    private Node<T> next;

    public Node(T value, Node<T> next) {
        this.value = value;
        this.next = next;
    }

    public T getValue() {
        return value;
    }

    public Node<T> getNext() {
        return next;
    }

    public void setNext(Node<T> next) {
        this.next = next;
    }
}

class DinamicStack<T> implements Iterable<T> {
    private Node<T> top = null;
    private int length = 0;

    T push(T element) {
        Node<T> newNode = new Node<T>(element, null);
        if (top == null) {
            top = newNode;
        } else {
            newNode.setNext(top);
            top = newNode;
        }
        length++;
        return top.getValue();
    }

    T pop() {
        if (top == null) {
            return null;
        }
        T delete = top.getValue();
        top = top.getNext();
        length--;
        return delete;
    }

    T peek() {
        if (top == null) {
            return null;
        }
        return top.getValue();
    }

    int size() {
        return length;
    }

    @Override
    public Iterator<T> iterator() {
        return new Iterator<T>() {
            Node<T> current = top;

            @Override
            public boolean hasNext() {
                return current != null;
            }

            @Override
            public T next() {
                if (!hasNext()) {
                    throw new NoSuchElementException("No hay más elementos en la pila");
                }
                T item = current.getValue();
                current = current.getNext();
                return item;

            }

        };
    }

}

class DinamicQueue<T> implements Iterable<T> {
    private int size = 0;
    private Node<T> first = null;
    private Node<T> last = null;

    public boolean isEmpty() {
        return first == null;
    }

    public T first() {
        if (isEmpty()) {
            return null;
        }
        return first.getValue();
    }

    public T enqueue(T element) {
        Node<T> newNode = new Node<>(element, null);
        if (isEmpty()) {
            first = newNode;
            last = newNode;
        } else {
            last.setNext(newNode);
            last = newNode;
        }
        size++;
        return newNode.getValue();
    }

    public T dequeue() {
        if (isEmpty()) {
            return null;
        }
        T item = first.getValue();
        first = first.getNext();
        size--;
        if (isEmpty()) {
            last = null;
        }
        return item;
    }

    public int size() {
        return this.size;
    }

    @Override
    public Iterator<T> iterator() {
        return new Iterator<T>() {
            private Node<T> current = first;

            @Override
            public boolean hasNext() {
                return current != null;
            }

            @Override
            public T next() {
                if (!hasNext()) {
                    throw new NoSuchElementException("No hay más elementos en la cola");
                }
                T item = current.getValue();
                current = current.getNext();
                return item;
            }

        };
    }
}
