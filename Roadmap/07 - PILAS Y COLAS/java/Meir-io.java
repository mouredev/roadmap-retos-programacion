import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

public class Meir {
    public static void main(String[] args) {


        //pila
     Stack<Integer> stack = new Stack();

     stack.push(1);
     stack.push(2);
     stack.push(3);
     stack.push(4);
     stack.push(5);

        System.out.println("Stack (pila)");
        System.out.println(stack);
     System.out.println(stack.pop());
     System.out.println(stack+ "\n");


     //cola
     Queue<Integer> queue = new LinkedList<>();
     queue.add(1);
     queue.add(2);
     queue.add(3);
     queue.add(4);
     queue.add(5);

        System.out.println("Queue (cola)");
        System.out.println(queue);
        System.out.println(queue.remove());
        System.out.println(queue );


        //Extra Paginas web
        Scanner sc = new Scanner(System.in);
        Stack<String> stack2 = new Stack<>();
        stack2.push("https://www.google.com/");
        int apuntador = -1;
        while (true){
            System.out.println("Ingresa una url o escribe adelante/atras/salir");
            String s = sc.nextLine();
            if (s.equals("atras")) {
                if (apuntador > 0) {
                    System.out.println(stack2.get(apuntador - 1));
                    apuntador--;
                }
                else {
                    System.out.println("Ya no hay mas urls");
                }
            }
            else if (s.equals("adelante")) {
                if (apuntador < stack2.size()-1) {
                    System.out.println(stack2.get(apuntador + 1));
                    apuntador++;
                }
                else {
                    System.out.println("Ya no hay mas urls");
                }
            }
            else if (s.equals("salir")){
                System.out.println("Saliendo...");
                break;
            }
            else {
                stack2.push(s);
            }
        }

        //Impresora
        Queue<String> queue2 = new LinkedList<>();
        queue2.add("Hola");
        queue2.add("Mundo");
        queue2.add("!");

        while (true) {
            System.out.println("añade un documento o imprimir o salir: ");
            String s = sc.nextLine();

            if (s.equals("imprimir")) {
                if (queue2.isEmpty()) {
                    System.out.println("No hay documentos");
                }
                else {
                    System.out.println(queue2.remove());
                }
            }
            else if (s.equals("salir")) {
                System.out.println("Saliendo...");
                break;
            }
            else {
                queue2.add(s);
            }
        }
    }
}
