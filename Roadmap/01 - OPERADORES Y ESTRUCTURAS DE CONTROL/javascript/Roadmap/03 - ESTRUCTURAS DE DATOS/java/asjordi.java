import java.util.*;

public class Main {

    public static void main(String[] args) {

//        Arrays
        int[] numeros = new int[3];
        numeros[0] = 10; // Insertar
        numeros[1] = 2; // Actualizar
        Arrays.sort(numeros); // Ordenar forma ascendente

//        ArrayList
        List<String> list = new ArrayList<>();
        list.add("Java"); // Insertar
        list.add("Python"); // Insertar
        list.set(1, "C#"); // Actualizar
        list.remove(1); // Borrar
        list.get(0); // Obtener elemento
        Collections.sort(list); // Ordenar forma ascendente
        list.sort(Collections.reverseOrder()); // Ordenar forma descendente

//        LinkedList
        List<Integer> linkedList = new LinkedList<>();
        linkedList.add(1); // Insertar
        linkedList.add(2); // Insertar
        linkedList.set(1, 3); // Actualizar
        linkedList.remove(1); // Borrar
        linkedList.get(0); // Obtener elemento
        Collections.sort(linkedList); // Ordenar forma ascendente
        linkedList.sort(Collections.reverseOrder()); // Ordenar forma descendente

//        Stack
        Stack<Integer> stack = new Stack<>();
        stack.push(1); // Insertar
        stack.push(2); // Insertar
        stack.pop(); // Borrar
        stack.peek(); // Obtener elemento

//        Queue
        Queue<Integer> queue = new LinkedList<>();
        queue.add(1); // Insertar
        queue.offer(3); // Insertar
        queue.remove(); // Borrar
        queue.peek(); // Obtener elemento

//        HashMap
        Map<Integer, String> map = new HashMap<>();
        map.put(1, "Java"); // Insertar
        map.put(2, "Python"); // Insertar
        map.replace(2, "C#"); // Actualizar
        map.remove(2); // Borrar

//        HashSet
        Set<String> hashSet = new HashSet<>();
        hashSet.add("Java"); // Insertar
        hashSet.add("Python"); // Insertar
        hashSet.remove("Python"); // Borrar
        hashSet.stream().sorted(); // Ordenar forma ascendente

//        TreeSet
        TreeSet<Integer> treeSet = new TreeSet<>();
        treeSet.add(1); // Insertar
        treeSet.add(2); // Insertar
        treeSet.remove(2); // Borrar
        treeSet.first(); // Obtener primer elemento
        treeSet.last(); // Obtener ultimo elemento
        treeSet.stream().sorted(Collections.reverseOrder()); // Ordenar forma descendente

//        TreeMap
        TreeMap<String,Integer> scores=new TreeMap<>();
        scores.put("Juan", 100); // Insertar
        scores.put("Maria", 90); // Insertar
        scores.put("Pedro", 80); // Insertar
        scores.replace("Maria", 95); // Actualizar
        scores.remove("Pedro"); // Borrar
        scores.get("Juan"); // Obtener elemento
        scores.firstEntry(); // Obtener primer elemento
        scores.lastEntry(); // Obtener ultimo elemento
        scores.entrySet().stream().sorted(Map.Entry.comparingByValue()); // Ordenar forma ascendente
        scores.entrySet().stream().sorted(Map.Entry.comparingByValue(Collections.reverseOrder())); // Ordenar forma descendente

        agenda();

    }

    /**
     * Crea una agenda de contactos por terminal.
     * Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
     * Cada contacto debe tener un nombre y un número de teléfono.
     * El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
     * los datos necesarios para llevarla a cabo.
     * El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
     * (o el número de dígitos que quieras)
     * También se debe proponer una operación de finalización del programa.
     */
    public static void agenda() {
        Scanner sc = new Scanner(System.in);
        ContactoRepositorio repo = new ContactoRepositorio();
        System.out.println("Bienvenido a la agenda de contactos");

        Contacto contacto;
        int opcion, id;

        while (true) {
            mostrarMenu();
            opcion = sc.nextInt();
            sc.nextLine();

            switch (opcion) {
                case 1:
                    contacto = new Contacto();
                    System.out.print("Introduce el nombre del contacto: ");
                    contacto.setNombre(sc.nextLine());
                    System.out.print("Introduce el teléfono del contacto: ");
                    contacto.setTelefono(sc.nextLong());
                    if (repo.insertar(contacto)) System.out.println("Contacto insertado correctamente -> " + contacto);
                    sc.nextLine();
                    break;
                case 2:
                    System.out.print("Introduce el id del contacto a actualizar: ");
                    id = sc.nextInt();
                    sc.nextLine();
                    System.out.print("Introduce el nombre actualizado: ");
                    String n = sc.nextLine();
                    System.out.print("Introduce el teléfono actualizado: ");
                    long tel = sc.nextLong();
                    if (repo.actualizar(id, n, tel)) System.out.println("Contacto actualizado correctamente -> " + repo.buscarPorId(id));
                    sc.nextLine();
                    break;
                case 3:
                    System.out.print("Introduce el id del contacto a actualizar: ");
                    id = sc.nextInt();
                    sc.nextLine();
                    if (repo.eliminar(id)) System.out.println("Contacto eliminado correctamente");
                    break;
                case 4:
                    System.out.print("Introduce el nombre del contacto");
                    String nombre = sc.nextLine();
                    Contacto c = repo.buscar(nombre);
                    if (c == null) System.out.println("No se ha encontrado el contacto");
                    else System.out.print(c);
                    break;
                case 5:
                    System.out.println("--- Contactos ---");
                    System.out.println("Total contactos: " + repo.getTotalContactos());
                    repo.getContactos().forEach(System.out::println);
                    break;
                case 6:
                    System.out.println("Adiós");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Opción no válida");
                    break;
            }
        }

    }

    public static void mostrarMenu() {
        System.out.println("¿Qué quieres hacer?");
        System.out.println("1. Insertar contacto");
        System.out.println("2. Actualizar contacto");
        System.out.println("3. Eliminar contacto");
        System.out.println("4. Buscar contacto");
        System.out.println("5. Ver contactos");
        System.out.println("6. Salir");
    }

}

class Contacto {

    private String nombre;
    private long telefono;
    private final int id;
    private static int lastId = 0;

    public Contacto() {
        this.id = ++lastId;
    }

    public Contacto(String nombre, long telefono) {
        this();
        this.nombre = nombre;
        this.telefono = telefono;
    }

    public int getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setTelefono(long telefono) {
        this.telefono = telefono;
    }

    @Override
    public String toString() {
        return "Contacto{" +
                "nombre='" + nombre + '\'' +
                ", telefono=" + telefono +
                ", id=" + id +
                '}';
    }
}

class ContactoRepositorio {

        private List<Contacto> contactos;

        public ContactoRepositorio() {
            this.contactos = new ArrayList<>();
        }

        public boolean insertar(Contacto contacto) {
            this.contactos.add(contacto);
            return true;
        }

        public boolean actualizar(int id, String nombre, long telefono) {
            Contacto c = buscarPorId(id);
            c.setNombre(nombre);
            c.setTelefono(telefono);
            return true;
        }

        public boolean eliminar(int id) {
            this.contactos.remove(buscarPorId(id));
            return true;
        }

        public Contacto buscar(String nombre) {
            return this.contactos.stream().filter(contacto -> contacto.getNombre().equals(nombre)).findFirst().orElse(null);
        }

        public Contacto buscarPorId(int id) {
            return this.contactos.stream().filter(contacto -> contacto.getId() == id).findFirst().orElse(null);
        }

        public List<Contacto> getContactos() {
            return contactos;
        }

        public int getTotalContactos() {
            return this.contactos.size();
        }
}
