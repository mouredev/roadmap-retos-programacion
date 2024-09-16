import java.util.ArrayList;
import java.util.Arrays;
import java.util.Enumeration;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;
import java.util.NoSuchElementException;
import java.util.Set;
import java.util.Spliterator;
import java.util.Spliterators;
import java.util.Vector;
import java.util.stream.IntStream;

public class simonguzman {
    public static void main(String[] args) {
        bucleFor();
        bucleWhile();
        bucleForEachArray();
        bucleDoWhile();
        iteradorConjunto();
        streamApi();
        bucleIterator();
        bucleEnumeration();
        bucleListIterator();
        bucleIteratorIterable();
        bucleSpliterator();
        bucleArrayIterator();
        bucleEnumerator();
        bucleCursor();
        buclePeekingIterator();
    }

    static void bucleFor(){
        for (int i = 1; i <= 10; i++){
            System.out.println(i);
        }
    }

    static void bucleWhile(){
        int i = 1;
        while(i <=10){
            System.out.println(i);
            i++;
        }
    }

    static void bucleForEachArray(){
        int [] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        for (int number : numbers){
            System.out.println(number);
        }
    }

    static void bucleDoWhile(){
        int i = 1;
        do{
            System.out.println(i);
            i++;
        }while(i <= 10);
    }

    static void iteradorConjunto(){
        Set<Integer> numbers = new HashSet<>();
        for (int i = 1; i <= 10; i++){
            numbers.add(i);
        }
        for (Integer number : numbers){
            System.out.println(number);
        }
    }

    static void streamApi(){
        IntStream.range(1, 11).forEach(System.out::println);
    }

    static void bucleIterator(){
        List<Integer> numbers = new ArrayList<>();
        for(int i = 1; i <=10; i++){
            numbers.add(i);
        }
        Iterator<Integer> iterator = numbers.iterator();
        while(iterator.hasNext()){
            System.out.println(iterator.next());
        }
    }

    static void bucleEnumeration(){
        Vector<Integer> numbers = new Vector<>();
        for (int i = 0; i <= 10; i++){
            numbers.add(i);
        }
        Enumeration<Integer> enumeration = numbers.elements();
        while (enumeration.hasMoreElements()) { 
            System.out.println(enumeration.nextElement());
        }
    }

    static void bucleListIterator(){
        List<Integer> numbers = new ArrayList<>();
        for (int i = 1; i <= 10; i++){
            numbers.add(i);
        }
        ListIterator<Integer> listIterator =  numbers.listIterator();
        while (listIterator.hasNext()) { 
            System.out.println(listIterator.next());
        }
    }

    static void bucleIteratorIterable(){
        Iterable<Integer> numbers = new Iterable<Integer>() {
            @Override
            public Iterator<Integer> iterator() {
                return new Iterator<Integer>() {
                    int i = 1;
                    @Override
                    public boolean hasNext() {
                        return i <= 10;
                    }
                    @Override
                    public Integer next() {
                        return i++;
                    }
                };
            }
        };
        for (Integer number : numbers){
            System.out.println(number);
        }
    }

    static void bucleSpliterator(){
        int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        Spliterator<Integer> spliterator = Arrays.spliterator(numbers);
        spliterator.forEachRemaining(System.out::println);
    }

    static void bucleArrayIterator(){
        Integer[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        Iterator<Integer> arrayIterator = ArrayIterator.iterator(numbers);
        while (arrayIterator.hasNext()) {
            System.out.println(arrayIterator.next());
        }
    }

    static void bucleEnumerator(){
        Enumeration<Integer> enumeration = Enumerator.enumeration((new Integer[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}));
        while (enumeration.hasMoreElements()) {
            System.out.println(enumeration.nextElement());
        }   
    }

    static void bucleCursor(){
        Iterator<Integer> cursor = Cursor.cursor((new Integer[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}));
        while (cursor.hasNext()) {
            System.out.println(cursor.next());
        }
    }

    static void buclePeekingIterator(){
        Iterator<Integer> peekingIterator = PeekingIterator.peekingIterator((new Integer[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}));
        while (peekingIterator.hasNext()) {
            System.out.println(peekingIterator.next());
        }
    }

    static class ArrayIterator{
        public static <T> Iterator<T> iterator(T[] array) {
        return new Iterator<T>() {
            private int index = 0;

            @Override
            public boolean hasNext() {
                return index < array.length;
            }

            @Override
            public T next() {
                if (!hasNext()) {
                    throw new NoSuchElementException();
                }
                return array[index++];
            }
        };
    }
    }

    static class Enumerator{
        public static <T> Enumeration<T> enumeration(T[] array) {
        return new Enumeration<T>() {
            private int index = 0;

            @Override
            public boolean hasMoreElements() {
                return index < array.length;
            }

            @Override
            public T nextElement() {
                if (!hasMoreElements()) {
                    throw new NoSuchElementException();
                }
                return array[index++];
            }
        };
    }
    }

    static class Cursor{
        public static <T> Iterator<T> cursor(T[] array) {
        return new Iterator<T>() {
            private int index = 0;

            @Override
            public boolean hasNext() {
                return index < array.length;
            }

            @Override
            public T next() {
                if (!hasNext()) {
                    throw new NoSuchElementException();
                }
                return array[index++];
            }
        };
    }
    }

    static class PeekingIterator{
        public static <T> Iterator<T> peekingIterator(T[] array) {
            return new Iterator<T>() {
                private int index = 0;
                private T peekedElement = null;
    
                @Override
                public boolean hasNext() {
                    return index < array.length;
                }
    
                @Override
                public T next() {
                    if (!hasNext()) {
                        throw new NoSuchElementException();
                    }
                    if (peekedElement != null) {
                        T element = peekedElement;
                        peekedElement = null;
                        return element;
                    }
                    return array[index++];
                }
    
                public T peek() {
                    if (!hasNext()) {
                        throw new NoSuchElementException();
                    }
                    if (peekedElement == null) {
                        peekedElement = array[index];
                    }
                    return peekedElement;
                }
            };
        }
    }
}
