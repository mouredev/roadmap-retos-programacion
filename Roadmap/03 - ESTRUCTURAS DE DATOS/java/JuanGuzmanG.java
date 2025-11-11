
import java.util.*;

public class JuanGuzmanG {

    public static void main(String args[]) {
        System.out.println("=== ARRAYLIST ===");
        //ideal para muchas lecturas
        ArrayList<String> numeros = new ArrayList<>();
        //add
        numeros.add("b2");
        numeros.add("c3");
        System.out.println("lista original");
        listar(numeros);
        //observar
        System.out.println("get: posicion 1:"+numeros.get(1));
        //remover
        numeros.remove("b2");
        System.out.println("remover posicion 1");
        listar(numeros);
        //actualizar
        numeros.set(0, "v2");
        System.out.println("actualizado posicion 0 con 4");
        listar(numeros);
        
        System.out.println("se agrega valores:");
        numeros.add("v1");
        numeros.add("a3");
        numeros.add("b3");
        listar(numeros);
        
        System.out.println("lista:");
        System.out.println(numeros);
        
        System.out.println("invertir");
        System.out.println(numeros.reversed());
        
        System.out.println("ordenar");
        Collections.sort(numeros);
        listar(numeros);
        
        System.out.println("=== LINKEDLIST ===");
        //ideal para muchas inserciones y eliminaciones
        LinkedList<String> linkedlist = new LinkedList<>();
        linkedlist.add("linkedin");
        linkedlist.add("prueba");
        linkedlist.remove("prueba");
        System.out.println(linkedlist);
        
        
        System.out.println("=== HASHSET ===");
        //ideal solo si importa evitar duplicados
        //muy rapido
        HashSet<String> cars = new HashSet<>();
        cars.add("carro1");
        cars.add("carro2");
        cars.remove("carro2");
        System.out.println(cars);
        System.out.println("modificar carro1 por carro11");
        if(cars.contains("carro1")){
            cars.remove("carro1");
            cars.add("carro11");
            System.out.println(cars);
        }
        cars.add("carro2");
        System.out.println(cars);
        
        System.out.println("=== LINKEDHASHSET===");
        //ideal para orden se mantiene tal como se agrega
        //levemente mas lento que hashset
        //estructura hashTable + LinkedList
        //comun en orden de inserción
        LinkedHashSet<Integer> ordenLinkedHashSet = new LinkedHashSet<>();
        ordenLinkedHashSet.add(5);
        ordenLinkedHashSet.add(2);
        ordenLinkedHashSet.add(1);
        System.out.println(ordenLinkedHashSet);
        
        System.out.println("===TREESET===");
        //ideal siempre ordenado automaticamente
        //lento, usa estructura Arbol rojo-negro
        //permite null con restricciones
        //comun en ordenamiento
        TreeSet<Integer> arbol = new TreeSet<>();
        arbol.add(2);
        arbol.add(3);
        arbol.add(4);
        arbol.add(1);   
        System.out.println(arbol);
        
        //forma de usar null
        Comparator<Integer> comparator = Comparator.nullsFirst(Integer::compareTo);
        TreeSet<Integer> set = new TreeSet<>(comparator);
        set.add(1);
        set.add(2);
        set.add(null);
        System.out.println(set);
        
        System.out.println("===HASHMAP===");
        //velocidad y sin importar el orden.
        HashMap<String, Integer> edades = new HashMap<>();
        edades.put("ana", 20);
        edades.put("juan", 10);
        System.out.println(edades);
        System.out.println("edad de ana: "+edades.get("ana"));
        
        System.out.println("===LinkedHashMap===");
        //velocidad y mantiene el orden de inserción
        LinkedHashMap<Integer,String> paciente = new LinkedHashMap<>();
        paciente.put(1, "paciente1");
        paciente.put(2, "paciente2");
        paciente.put(0, "paciente0");
        paciente.put(3, "paciente3");
        System.out.println(paciente);
        
        System.out.println("===TREEMAP===");
        //llaves ordenadas y operaciones de rango (llaves entre)
        TreeMap<Integer, String> estudiantes = new TreeMap<>();
        estudiantes.put(1, "juan");
        estudiantes.put(3, "maria");
        estudiantes.put(2, "pepe");
        System.out.println(estudiantes);
        
        System.out.println("===QUEUE===");
        //sistema de turnos, proceso de orden de llegada
        //FIFO First in, First Out
        //offer si no tiene espacio regresa un false - recomendado en colas sin limites
        //add si no tiene espacio regresa una IllegalStateException - colas con capacidad limitada
        Queue<String> cola = new LinkedList<>();
        cola.offer("ana");
        cola.add("pepe");
        System.out.println(cola);
        System.out.println(cola.poll());
        System.out.println(cola.poll());
        
        System.out.println("=== STACK ===");
        //obsoleta
        //sistema LIFO last in, first out
        Stack<String> pila = new Stack<>();
        pila.push("A");
        pila.push("B");
        System.out.println("completa");
        System.out.println(pila);
        pila.pop();
        System.out.println("pop");
        System.out.println(pila);
        
        System.out.println("=== DEQUE ===");
        Deque<String> pilaDeque = new ArrayDeque<>();
        pilaDeque.push("A");
        pilaDeque.push("B");
        System.out.println("completa");
        System.out.println(pilaDeque);
        pilaDeque.pop();
        System.out.println("pop");
        System.out.println(pilaDeque);
    }

    static void listar(ArrayList<String> numeros) {
        for (String num : numeros) {
            System.out.println(num);
        }
    }
}
