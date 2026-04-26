import java.util.*;

public class Meir {
    public static void main(String[] args) {
        int[] numeros = {1, 2, 3, 4, 5};
        System.out.println(numeros[2]);

        ArrayList<String> lista = new ArrayList<>();
        lista.add("Hola");
        lista.add("Mundo");
        lista.remove("Hola");
        System.out.println(lista);

        LinkedList<Integer> lista2 = new LinkedList<>();
        lista2.add(1);
        lista2.addFirst(0);
        lista2.addLast(2);
        System.out.println(lista2);

        HashMap<String, Integer> mapa = new HashMap<>();
        mapa.put("Hola", 1);
        mapa.put("Mundo", 2);
        System.out.println(mapa.get("Mundo"));


        HashSet<String> conjunto = new HashSet<>();
        conjunto.add("Java");
        conjunto.add("Java"); // ignorado
        conjunto.add("Python");
        System.out.println(conjunto);

        Stack<Integer> pila = new Stack<>();
        pila.push(1);
        pila.push(2);
        pila.push(3);
        System.out.println(pila.pop());

        Queue<String> cola = new LinkedList<>();
        cola.offer("Hola");
        cola.offer("Mundo");
        System.out.println(cola.poll());

        TreeMap<String, Integer> arbol = new TreeMap<>();
        arbol.put("A", 1);
        arbol.put("B", 2);
        arbol.put("C", 3);
        System.out.println(arbol);



    }

}