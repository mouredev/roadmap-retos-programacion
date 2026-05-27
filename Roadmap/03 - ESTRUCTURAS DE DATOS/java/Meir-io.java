import java.util.*;

public class Meir {
    public static void main(String[] args) {

        int[] array = {5, 3, 1, 4, 2};
        array[0] = 10;
        Arrays.sort(array);
        System.out.println("Array: " + Arrays.toString(array));

        ArrayList<String> lista = new ArrayList<>();
        lista.add("Java");
        lista.add("Python");
        lista.add("Kotlin");
        lista.set(1, "JavaScript");
        lista.remove("Kotlin");
        Collections.sort(lista);
        System.out.println("ArrayList: " + lista);

        LinkedList<Integer> linked = new LinkedList<>();
        linked.add(3);
        linked.addFirst(1);
        linked.addLast(5);
        linked.set(1, 2);
        linked.remove(Integer.valueOf(5));
        Collections.sort(linked);
        System.out.println("LinkedList: " + linked);

        HashMap<String, Integer> mapa = new HashMap<>();
        mapa.put("edad", 25);
        mapa.put("año", 2026);
        mapa.put("edad", 30);
        mapa.remove("año");
        TreeMap<String, Integer> mapaOrdenado = new TreeMap<>(mapa);
        System.out.println("HashMap ordenado: " + mapaOrdenado);

        HashSet<Integer> conjunto = new HashSet<>();
        conjunto.add(5);
        conjunto.add(3);
        conjunto.add(1);
        conjunto.remove(3);

        conjunto.remove(5);
        conjunto.add(10);
        List<Integer> conjuntoOrdenado = new ArrayList<>(conjunto);
        Collections.sort(conjuntoOrdenado);
        System.out.println("HashSet ordenado: " + conjuntoOrdenado);

        Stack<String> pila = new Stack<>();
        pila.push("primero");
        pila.push("segundo");
        pila.push("tercero");
        pila.set(0, "actualizado");
        pila.pop();
        System.out.println("Stack: " + pila);

        Queue<Integer> cola = new LinkedList<>();
        cola.offer(3);
        cola.offer(1);
        cola.offer(2);
        cola.poll();
        List<Integer> colaOrdenada = new ArrayList<>(cola);
        Collections.sort(colaOrdenada);
        System.out.println("Queue ordenada: " + colaOrdenada);

        TreeMap<String, Integer> arbol = new TreeMap<>();
        arbol.put("banana", 2);
        arbol.put("manzana", 5);
        arbol.put("pera", 1);
        arbol.put("banana", 10);
        arbol.remove("pera");
        System.out.println("TreeMap: " + arbol);


        //Extra
        HashMap<String, String> Agenda = new HashMap<>();

        while (true) {
        System.out.println("Que operacion quieres realizar? ");
        System.out.println("1. Buscar contacto");
        System.out.println("2. Agregar contacto");
        System.out.println("3. Modificar contacto");
        System.out.println("4. Eliminar contacto");
        System.out.println("5. Salir");
        System.out.print("Ingrese una opcion: ");
        Scanner entrada = new Scanner(System.in);
        String operacion = entrada.nextLine();

        String numero = null;
        String nombre = null;
        switch (operacion) {
            case "1":
                System.out.println("Ingrese el nombre del contacto: ");
                nombre = entrada.nextLine();
                if (Agenda.get(nombre) == null) {
                    System.out.println("Contacto no encontrado");
                    break;
                }
                System.out.println(Agenda.get(nombre));
                break;
            case "2":
                System.out.println("Ingrese el nombre del contacto: ");
                nombre = entrada.nextLine();
                System.out.println("Ingrese el numero del contacto: ");
                numero = entrada.nextLine();
                if (numero.length() > 11 || !numero.matches("\\d+")) {
                    System.out.println("Numero demasiado grande o no es un numero");
                    break;
                }
                Agenda.put(nombre, numero);
                System.out.println("Contacto agregado: " + nombre + " " + numero);
                break;

            case "3":
                System.out.println("Ingrese el nombre del contacto a editar: ");
                nombre = entrada.nextLine();
                if (Agenda.get(nombre) != null) {
                    System.out.println("Ingrese el nuevo nombre del contacto: ");
                    nombre = entrada.nextLine();
                    System.out.println("Ingrese el nuevo numero del contacto: ");
                    numero = entrada.nextLine();
                    if (numero.length() > 11 || !numero.matches("\\d+")) {
                        System.out.println("Numero demasiado grande o no es un numero");
                        break;
                    }
                    Agenda.put(nombre, numero);
                    System.out.println("Contacto editado: " + nombre + " " + numero);
                } else {
                    System.out.println("Contacto no encontrado");
                }
                break;

            case "4":
                System.out.println("Ingrese el nombre del contacto a eliminar: ");
                nombre = entrada.nextLine();
                if (Agenda.get(nombre) != null) {
                    Agenda.remove(nombre);
                    System.out.println("Contacto eliminado");
                } else {
                    System.out.println("Contacto no encontrado");
                }
                break;
                case "5":
                System.out.println("Saliendo...");
                entrada.close();
                return;
                default:
                System.out.println("Operacion no valida");
        }
        }
    }
}
