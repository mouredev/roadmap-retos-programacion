public class Main {
    public static void main(String[] args) {
        Client client = new Client("Abel", 20);
        System.out.println(client);
        client.setAge(30);
        System.out.println(client);

        System.out.println("--------- DIFICULTAD EXTRA -------------");

        //Pilas
        Stack stack = new Stack();
        stack.push(30);
        stack.push(20);
        stack.push(10);
        System.out.println(stack);
        System.out.println("Tamaño: " + stack.size());
        stack.pop();
        System.out.println(stack);
        stack.pop();
        System.out.println(stack + "\n");

        //Colas
        Queue queue = new Queue();
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);
        System.out.println(queue);
        System.out.println("Tamaño: " + queue.size());
        queue.dequeue();
        System.out.println(queue);
        queue.dequeue();
        System.out.println(queue);
    }
}

class Client {
    // Atributos
    String name;
    int age;

    //Métodos de acceso y sobrescritura de atributos
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    // Constructor
    public Client(String name, int age) {
        this.name = name;
        this.age = age;
    }

    //Método para imprimir por pantalla
    @Override
    public String toString() {
        return "Cliente: " + name + ", Edad: " + age;
    }
}

class Stack{
    ArrayList<Object> stack;

    public Stack() {
        this.stack = new ArrayList<>();
    }

    public <T> void push(T valor){
        stack.add(valor);
    }

    public <T> T pop(){
        if (stack.isEmpty()){
            return null;
        }

        Object object = stack.get(stack.size()-1);
        stack.remove(stack.size()-1);
        return (T) object;
    }

    public int size(){
        return stack.size();
    }

    @Override
    public String toString() {
        String text = "Stack: \n";
        String separator = ", ";
        for(int i = 0; i<stack.size(); i++){
            if (i == stack.size()-1){
                separator = "";
            }
            text += stack.get(i) + separator;
        }

        return text;
    }
}

class Queue{
    ArrayList<Object> queue;

    public Queue() {
        this.queue = new ArrayList<>();
    }

    public <T> void enqueue(T valor){
        queue.add(valor);
    }

    public <T> T dequeue(){
        if (queue.isEmpty()){
            return null;
        }

        Object object = queue.get(0);
        queue.remove(0);
        return (T) object;
    }

    public int size(){
        return queue.size();
    }

    @Override
    public String toString() {
        String text = "Queue: \n";
        String separator = ", ";
        for(int i = 0; i<queue.size(); i++){
            if (i == queue.size()-1){
                separator = "";
            }
            text += queue.get(i) + separator;
        }
        return text;
    }
}
