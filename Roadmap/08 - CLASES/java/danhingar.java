import java.util.ArrayList;
import java.util.List;

public class danhingar {

    public static void main(String[] args) {
        Programmer p1 = new Programmer("JUAN", new ArrayList<>(), 32, "https://www.linkedin.com/p1");
        System.out.println(p1);
        p1.setName("PEPE");
        p1.setAge(23);
        p1.setLanguages(List.of("JAVA", "PYTHON"));
        System.out.println(p1);

        Stack myStack = new Stack();
        myStack.push("A");
        myStack.push("B");
        myStack.push("C");
        myStack.push("D");
        System.out.println(myStack.count());
        myStack.print();
        myStack.pop();
        myStack.pop();
        System.out.println(myStack.count());
        myStack.print();

        Queue myQueue = new Queue();
        myQueue.equeue("E");
        myQueue.equeue("F");
        myQueue.equeue("G");
        myQueue.equeue("H");
        System.out.println(myQueue.count());
        myQueue.print();
        System.out.println(myQueue.deequeue()); 
        System.out.println(myQueue.deequeue()); 
        System.out.println(myQueue.count());
        myQueue.print();

    }

    public static class Programmer {
        private String name;
        private List<String> languages;
        private Integer age;
        private String urlLinkedin;

        public Programmer(String name, List<String> languages, Integer age, String urlLinkedin) {
            this.name = name;
            this.languages = languages;
            this.age = age;
            this.urlLinkedin = urlLinkedin;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public List<String> getLanguages() {
            return languages;
        }

        public void setLanguages(List<String> languages) {
            this.languages = languages;
        }

        public Integer getAge() {
            return age;
        }

        public void setAge(Integer age) {
            this.age = age;
        }

        public String getUrlLinkedin() {
            return urlLinkedin;
        }

        public void setUrlLinkedin(String urlLinkedin) {
            this.urlLinkedin = urlLinkedin;
        }

        public String toString() {
            return "Programmer [name=" + name + ", languages=" + languages + ", age=" + age + ", urlLinkedin="
                    + urlLinkedin + "]";
        }
    }

    // EXTRA
    public static class Stack {

        List<Object> stack;

        public Stack() {
            stack = new ArrayList<>();
        }

        public void push(Object o) {
            stack.add(o);
        }

        public Object pop() {
            if (stack.size() > 1) {
                Object o = stack.get(stack.size() - 1);
                stack.remove(stack.size() - 1);
                return o;
            } else {
                return null;
            }

        }

        public Integer count() {
            return stack.size();
        }

        public void print() {
            for (Object object : stack.reversed()) {
                System.out.println(object);
            }
        }

    }

    public static class Queue {

        List<Object> queue;

        public Queue() {
            queue = new ArrayList<>();
        }

        public void equeue(Object o) {
            queue.add(o);
        }

        public Object deequeue() {
            if (queue.size() > 1) {
                Object o = queue.get(0);
                queue.remove(0);
                return o;
            } else {
                return null;
            }

        }

        public Integer count() {
            return queue.size();
        }

        public void print() {
            for (Object object : queue) {
                System.out.println(object);
            }
        }

    }

}
