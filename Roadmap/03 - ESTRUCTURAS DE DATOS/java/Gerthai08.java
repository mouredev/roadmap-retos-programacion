import java.util.*;
public class Gerthai08 {

    //Map para almacenar los contactos (nombre -> número de teléfono)
    private static Map<String, String> contacts = new HashMap<>();
    private static final int maxPhoneNumbers = 11; //límite de dígitos

    public static void main(String[] args) {

        //ARRAYS
        //Array de String
        String[] arrayString = {"Juan", "Pedro", "Esteban"};
        //Array de Números
        int[] arrayNumber = {1, 2, 24, 37, 50};
        //Modificando elemento de array
        arrayNumber[0] = 3;
        //Array de varios subindices
        int[][] arraySubindices = {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 0}};
        //Acceder a una Array
        System.out.println("=====Accediendo a Array=====");
        System.out.println(arrayNumber[4]);
        System.out.println(arrayString[0]);
        //Recorrer array
        System.out.println("=====Recorriendo Array=====");
        for (int i : arrayNumber) {
            System.out.println(i);
        }
        //Recorrer array subindices
        System.out.println("=====Recorriendo Array Subindices=====");
        for (int i = 0; i < arraySubindices.length; i++) {
            for (int j = 0; j < arraySubindices[i].length; j++) {
                System.out.print(arraySubindices[i][j] + " ");
            }
            System.out.println();
        }

        //LIST
        //ArrayList
        List<String> listaObjetos = new ArrayList<String>();
        //Agregar elementos
        listaObjetos.add("Guante");
        listaObjetos.add("Cartera");
        listaObjetos.add("Libro");
        //Acceder al elemento
        System.out.println("=====Acceder a elementos de una ArrayList=====");
        System.out.println(listaObjetos.get(0)); //Accede al elemento "Guante"
        //cambiar elemento
        System.out.println("=====Se cambió el elemento de la ArrayList=====");
        listaObjetos.set(1,"Celular"); //El elemento "Cartera" ahora es "Celular"
        System.out.println(listaObjetos.get(1));
        //Tamaño de ArrayList
        System.out.println("=====Tamaño de ArrayList=====");
        System.out.println(listaObjetos.size());
        //Recorrer ArrayList
        System.out.println("=====Recorriendo ArrayList =====");
        Collections.sort(listaObjetos); //Método para ordenar alfabéticamente
        for(String i : listaObjetos){
            System.out.println(i);
        }
        //Elimina un elemento de la lista
        listaObjetos.remove(1); //se elimina el objeto celular
        //Elimina todos los objetos de la lista
        listaObjetos.clear();

        //LinkedList
        //Se comporta de la misma manera que ArrayList pero esta son "Listas enlazadas"
        //Disponen de métodos que hacen mas eficientes la manipulación de las mismas
        List<String> listaEnlazada = new LinkedList<String>();
        //Agregar elementos
        listaEnlazada.add("Juan");
        listaEnlazada.add("marcos");
        listaEnlazada.add("Pedro");
        //Agregar elemento al comienzo de la lista
        listaEnlazada.addFirst("Nombre Primero");
        //Agregar elemento al final de la lista
        listaEnlazada.addLast("Nombre Ultimo");
        //Traer elemento que está al Principio de la lista
        System.out.println("=====Traer elemento que está al Principio de la LinkedList=====");
        System.out.println(listaEnlazada.getFirst());
        //Traer elemento que está al Final de la lista
        System.out.println("=====Traer elemento que está al Final de la LinkedList=====");
        System.out.println(listaEnlazada.getLast());
        //Eliminar elemento que está al Principio de la lista
        System.out.println("=====Eliminar elemento que está al Principio de la LinkedList=====");
        System.out.println(listaEnlazada.removeFirst());
        //Eliminar elemento que está al Final de la lista
        System.out.println("=====Eliminar elemento que está al Final de la LinkedList=====");
        System.out.println(listaEnlazada.removeLast());

        //SET
        //HashSet
        //Instanciando el objeto HashSet (desordenado)
        HashSet<String> listaHashSet = new HashSet<String>();
        listaHashSet.add("Volvo");
        listaHashSet.add("BMW");
        listaHashSet.add("Ford");
        listaHashSet.add("BMW");  // Duplicate
        listaHashSet.add("Mazda");
        //Llamando a la lista
        System.out.println("=====Llamando a la lista HashSet=====");
        System.out.println(listaHashSet);
        //Comprobar si existe el elemento
        System.out.println("=====Comprobando si existe el elemento HashSet=====");
        System.out.println(listaHashSet.contains("Ford"));
        //Eliminando un elemento
        listaHashSet.remove("Ford");
        //Tamaño de HashSet
        System.out.println("=====Tamaño de HashSet=====");
        System.out.println(listaHashSet.size());
        //Eliminar todos los elementos
        listaHashSet.clear();
        //TreeSet (Conjunto ordenado)
        //es lo mismo que hash pero con la condición entre parentecis
        //LinkedHashSet (Ordenado por inserción)

        //MAP
        //HashMap
        //Agregar elementos
        HashMap<String,String> listHashMap = new HashMap<>();
        listHashMap.put("England", "London");
        listHashMap.put("India", "New Dehli");
        listHashMap.put("Austria", "Wien");
        listHashMap.put("Norway", "Oslo");
        listHashMap.put("USA", "Washington DC");
        //Acceder a un elemento
        System.out.println("=====Accediendo al elemento HashMap=====");
        System.out.println(listHashMap.get("England"));
        //Eliminar elemento
        listHashMap.remove("England");
        //Tamaño de HashMap
        System.out.println("=====Tamaño de HashMap=====");
        System.out.println(listHashMap.size());
        //Recorrer HashMap
        System.out.println("=====Recorrer HashMap por claves=====");
        for(String i : listHashMap.keySet()){
            System.out.println(i);
        }
        System.out.println("=====Recorrer HashMap por valores=====");
        for(String i : listHashMap.values()){
            System.out.println(i);
        }
        System.out.println("=====Recorrer HashMap por clave-valor=====");
        for(String i : listHashMap.keySet()){
            System.out.println("key: " + i + "| value: " + listHashMap.get(i));
        }
        //Treemap (ordenado por clave)
        //LinkedHashMap (odenado por inserción)

        extra();
    }

    public static void extra() {
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        System.out.println("!bienvenido a la agenda de contactos¡");

        while (running) {
            System.out.println("\n¿Qué deseas hacer?");
            System.out.println("1. Insertar contacto");
            System.out.println("2. Buscar contacto");
            System.out.println("3. Actualizar contacto");
            System.out.println("4. Eliminar contacto");
            System.out.println("5. Mostrar todos los contactos");
            System.out.println("6. Salir");
            System.out.print("Selecciona una opción: ");

            String option = scanner.nextLine();

            switch (option){
                case "1":
                    insertContact(scanner);
                    break;
                case "2":
                    seachContact(scanner);
                    break;
                case "3":
                    updateContact(scanner);
                    break;
                case "4":
                    deleteContact(scanner);
                    break;
                case "5":
                    showAllContacts();
                    break;
                case "6":
                    running = false;
                    System.out.println("¡Hasta luego!");
                    break;
                default:
                    System.out.println("Opción no válida. Inténtalo de nuevo.");
            }
        }
        scanner.close();
    }

    //Metodo para insertar contacto
    private static void insertContact(Scanner scanner){
        String name = pedirDato(scanner,"Introduzca el nombre del contacto: ");

        if (contacts.containsKey(name)){
            System.out.println("Este contacto ya existe.");
            return;
        }

            System.out.println("Introduzca el numero del contacto.");
            String phone = scanner.nextLine().trim();

        if (isValidPhone(phone)){
            contacts.put(name,phone);
            System.out.println("Contacto agregado correctamente.");
        }else{
            System.out.println("Número de teléfono no válido. Debe ser numérico y tener hasta " + maxPhoneNumbers + " dígitos.");
        }
    }

    //Metodo para buscar cotacto
    private static void seachContact(Scanner scanner){
        String name = pedirDato(scanner,"Introduce el nombre del contacto a buscar: ");

        if(contacts.containsKey(name)){
            System.out.println("Contacto encontrado: " + name + " -> " + contacts.get(name));
        }else{
            System.out.println("No se encontro ningun contacto con este nombre.");
        }
    }

    //Metodo para actualizar los contactos
    private static void updateContact(Scanner scanner){
        String name = pedirDato(scanner,"Introduce el nombre del contacto a actualizar: ");

        if (contacts.containsKey(name)){
            System.out.println("Introduce el numero numero de teléfono: ");
            String newPhone = scanner.nextLine().trim();

            if (isValidPhone(newPhone)){
                contacts.put(name,newPhone);
                System.out.println("El contacto se actualizó correctamente.");
            }else{
                System.out.println("El teléfono no es valido.");
            }
        }else{
            System.out.println("No se encontró ningún contacto con ese nombre.");
        }
    }

    //Metodo para eliminar un contacto
    private static void deleteContact(Scanner scanner){
        String name = pedirDato(scanner,"Introduce el nombre del contacto a eliminar.");

        if (contacts.containsKey(name)){
            contacts.remove(name);
            System.out.println("Contacto eliminado correctamente.");
        }else{
            System.out.println("No se encontró ningún contacto con ese .");
        }
    }

    //Metodo para mostrar todos los contactos
    private static void showAllContacts(){
        if(contacts.isEmpty()){
            System.out.println("No hay contactos en la agenda.");
        }else{
            System.out.println("Lista de contactos:");
            contacts.forEach((name,phone) -> System.out.println(name + " -> " + phone));
        }
    }

    // Método para validar un número de teléfono
    private static boolean isValidPhone(String phone){
        return phone.matches("\\d{1," + maxPhoneNumbers + "}");
    }

    //Metodo para introducir texto informativo y asignar nombre a la variable scanner
    private static String pedirDato(Scanner scanner, String mensaje){
        System.out.println(mensaje);
        return scanner.nextLine().trim();
    }
}