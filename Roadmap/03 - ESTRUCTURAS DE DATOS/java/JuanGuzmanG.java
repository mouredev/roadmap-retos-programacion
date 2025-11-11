
import java.util.*;

public class JuanGuzmanG {
    private static final int maxDigitos = 11;
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== ARRAYLIST ===");
        //ideal para muchas lecturas
        ArrayList<String> numeros = new ArrayList<>();
        //add
        numeros.add("b2");
        numeros.add("c3");
        System.out.println("lista original");
        listar(numeros);
        //observar
        System.out.println("get: posicion 1:" + numeros.get(1));
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
        if (cars.contains("carro1")) {
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
        System.out.println("edad de ana: " + edades.get("ana"));

        System.out.println("===LinkedHashMap===");
        //velocidad y mantiene el orden de inserción
        LinkedHashMap<Integer, String> paciente = new LinkedHashMap<>();
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

        /*        
        * DIFICULTAD EXTRA (opcional):
        * Crea una agenda de contactos por terminal.
        * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
        * - Cada contacto debe tener un nombre y un número de teléfono.
        * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
        *   los datos necesarios para llevarla a cabo.
        * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
        *   (o el número de dígitos que quieras)
        * - También se debe proponer una operación de finalización del programa.
         */
        Map<String, String> contactos = new HashMap<>();
        contactos.put("ana", "32919382");

        boolean on = true;
        while (on) {
            String telefono ="";
            String nombre = "";
            System.out.println("Agenda de contactos, seleccione la operación");
            System.out.println(" 1. búsqueda");
            System.out.println(" 2. inserción");
            System.out.println(" 3. actualización");
            System.out.println(" 4. eliminación");
            System.out.println(" 5. lista completa");
            System.out.print("Opción: ");
            
            int opcion;
            try {
                opcion = Integer.parseInt(sc.nextLine().trim());
            } catch (NumberFormatException e) {
                System.out.println("opcion invalida, intente de nuevo");
                continue;
            }
            
            if(opcion<1 || opcion>6){
                System.out.println("opcion fuera de menu, intente den uevo \n");
                continue;
            }
            
            switch(opcion){
                case 1 -> {
                    System.out.println("Ingrese el nombre: ");
                    nombre = sc.nextLine().trim().toLowerCase();
                    if(contactos.containsKey(nombre)){
                        System.out.println(nombre+" Numero: "+contactos.get(nombre));
                    } else {
                        System.out.println("No se encontro este contacto");
                    }
                }
                case 2 -> {
                    System.out.println("Ingrese el nombre del nuevo contacto");
                    nombre = sc.nextLine().trim().toLowerCase();
                    if(nombre.isEmpty()){
                        System.out.println("Nombre invalido");
                        break;
                    } else if(contactos.containsKey(nombre)){
                        System.out.println("ya existe un usuario con este nombre");
                        break;
                    }
                    System.out.println("Ingrese el numero del nuevo contacto, maximo 11 numeros");
                    telefono = sc.nextLine().trim();
                    if(validarTelefono(telefono)==null){
                        System.out.println("Telefono no valido");
                        break;
                    }
                    contactos.put(nombre,telefono);
                    System.out.println("Se guardo: "+ nombre +" con el telefono: "+telefono);
                }
                case 3 -> {
                    System.out.println("Ingrese el nombre del contacto a modificar:");
                    nombre = sc.nextLine().trim().toLowerCase();
                    if(nombre.isEmpty()){
                        System.out.println("Nombre invalido");
                        break;
                    }
                    if(contactos.containsKey(nombre)){
                        System.out.println("Ingrese el nuevo telefono");
                        telefono = sc.nextLine().trim();
                        if(validarTelefono(telefono)==null){
                            System.out.println("telefono no valido");
                            break;
                        }
                    }else{
                        System.out.println("No se encontro contacto con este nombre");
                        break;
                    }
                    System.out.println("el contacto: "+ 
                            nombre +" con telefono: "+ contactos.containsKey(nombre));
                    contactos.put(nombre, telefono);
                    System.out.println("ahora contiene el numero: "+ contactos.containsKey(nombre));
                }
                case 4 -> {
                    System.out.println("ingrese el nombre del contacto a eliminar:");
                    nombre = sc.nextLine().trim().toLowerCase();
                    if(contactos.containsKey(nombre)){
                        contactos.remove(nombre);
                        System.out.println("contacto eliminado");
                    } else {
                        System.out.println("No se encontro contacto con este nombre");
                        break;
                    }
                }
                case 5 -> {
                    System.out.println(contactos);
                }
            }
            
            System.out.println("¿Dese finalizar? si[y] o no[n]");
            String finalizar = sc.nextLine().trim();
            if(finalizar.equalsIgnoreCase("y")){
                on = false;
            }
        }
        System.out.println("finalizo el programa");
        sc.close();
    }

    static String validarTelefono(String t){
        if(t.matches("\\d+") && t.length() <= maxDigitos){
            return t;
        } else {
            return null;
        }
    }
    
    static void listar(ArrayList<String> numeros) {
        for (String num : numeros) {
            System.out.println(num);
        }
    }
}
