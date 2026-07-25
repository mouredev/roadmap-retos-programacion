import java.util.*;

public class Josegs95 {
    public static void main(String[] args) {
        // Estructuras de datos

        //Arrays o arreglos
        //Son estructuras de datos bastante rígidas que no permiten la adicción o eliminación de elementos.
        //Su tamaño es especificado al crear el array, ya sea rellenándolo de elementos o especificando el tamaño
        String[] arrayVacio = new String [4]; //Creación de un array vacío con espacio de hasta 4 elementos
        String[] diasSemana = {"Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"};
        System.out.println(Arrays.toString(diasSemana));

        diasSemana[0] = "LUNES"; //Modificación
        System.out.println(Arrays.toString(diasSemana));

        Arrays.sort(diasSemana); //Ordenación gracias a la clase Arrays.
        System.out.println(Arrays.toString(diasSemana));

        //Listas
        //Hay muchos tipos de listas, cada una con sus peculiaridades, pero yo voy a mostrar la clase ArrayList
        ArrayList<Integer> tiradasDado = new ArrayList<>(); //Creación del objeto

        tiradasDado.add(5); //Inserción de un elemento
        tiradasDado.add(2);
        tiradasDado.add(6);
        System.out.println(tiradasDado);

        tiradasDado.set(0, 4); //Modificación de un elemento, en este caso, el primero (índice 0)
        System.out.println(tiradasDado);

        tiradasDado.remove(2); //Eliminación del tercer elemento de la lista
        System.out.println(tiradasDado);

        Collections.sort(tiradasDado); //Ordenación a través de la clase Collections
        System.out.println(tiradasDado);

        //Sets
        //Estructura de datos parecido a las listas pero que no permite la inserción de duplicados
        //Como no se puede acceder a un elemento en concreto, no se puede modificar a los mismos
        HashSet<String> colores = new HashSet<>(); //Creación del objeto

        colores.add("Azul"); //Inserción de elementos
        colores.add("Verde");
        colores.add("Blanco");
        System.out.println(colores);

        colores.remove("Blanco"); //Eliminación de un elemento
        System.out.println(colores);

            //Existe una clase que permite ordenar los set (SortedSet, o su subclase, TreeSet).

        //Mapas
        //Estructuras de datos que asocian un valor a una clave única. Los mapas no permiten la ordenación de
        //elementos por defecto (el usuario puede crear un método para esto)
        HashMap<String, Double> notasExamen = new HashMap<>(); //Creación del mapa

        notasExamen.put("Jose", 9.0); //Inserción de elementos
        notasExamen.put("Guillermo", 6.0);
        notasExamen.put("Rocío", 9.25);
        notasExamen.put("Antonio", 3.75);
        System.out.println(notasExamen);

        notasExamen.replace("Guillermo", 6.25); //Modificación de un elemento
        System.out.println(notasExamen);

        notasExamen.remove("Antonio"); //Eliminación de un elemento
        System.out.println(notasExamen);

        //
        System.out.println("\n\n");
        //

        retoFinal();
    }

    static Scanner sc;
    static String[] options = {"Ver Contactos", "Buscar Contacto", "Agregar Contacto", "Modificar Contacto",
            "Eliminar Contacto", "Salir del programa"};

    static Map<String, String> agenda;

    public static void retoFinal(){
        sc = new Scanner(System.in);
        agenda = new HashMap<>();
        boolean end = false;
        do{
            showMenu();

            System.out.print("Introduzca la operación que quiere realizar: ");
            String option = sc.nextLine();

            switch (option){
                case "1": //Ver contactos
                    showAgenda();
                    break;
                case "2": //Buscar contactos
                    searchContact();
                    break;
                case "3": //Añadir contactos
                    addContact(null);
                    break;
                case "4": //Modificar contactos
                    modifyContact();
                    break;
                case "5": //Borrar contactos
                    removeContact();
                    break;
                case "6": //Salir
                    end = true;
                    break;
                default:
                    System.out.println("Opción no válida. Introduzca un número de opción válido.");
            }
        }while(end == false);

        System.out.println("Cerrando la aplicación. Hasta otra!");
    }

    private static void showMenu(){
        System.out.println("----------------------------");
        for (int i = 0; i < options.length; i++){
            System.out.println((i+1) + ". " + options[i]);
        }
        System.out.println("----------------------------");
    }

    private static void showAgenda(){
        if (agenda.size() == 0)
            System.out.println("La agenda está vacía.");
        else {
            for (Map.Entry<String, String> entry : agenda.entrySet()){
                System.out.println("Contacto: " + entry.getKey() + ", Teléfono: " + entry.getValue());
            }
        }
    }

    private static void searchContact(){
        System.out.print("Introduzca el nombre del contacto que quiera buscar: ");
        String contact = sc.nextLine();
        String phone;
        if ((phone = agenda.get(contact)) == null)
            System.out.println("El contacto " + contact + " no existe.");
        else
            System.out.println("El telefono de " + contact + " es " + phone);
    }

    private static void addContact(String antiguoContacto){
        System.out.print("Introduzca el nombre del contacto: ");
        String contact = sc.nextLine();
        boolean correctOption = false;
        do {
            System.out.print("Introduzca el número de teléfono: ");
            String phone = sc.nextLine();
            if (phone.length() > 11){
                System.out.println("El número de teléfono no puede tener mas de 11 dígitos");
            } else {
                try {
                    Long.parseLong(phone);
                    correctOption = true;
                    if (antiguoContacto != null)
                        agenda.remove(antiguoContacto);
                    agenda.put(contact, phone);
                } catch (NumberFormatException e){
                    System.out.println("Error. Carácteres no númericos detectados.");
                }
            }
        } while (correctOption == false);
    }

    private static void modifyContact(){
        System.out.print("Introduzca el nombre del contacto que quiera modificar: ");
        String contacto = sc.nextLine();
        if (agenda.get(contacto) == null){
            System.out.println("Error. Ese contacto no existe en su agenda");
        } else {
            addContact(contacto);
        }

    }

    private static void removeContact(){
        System.out.print("Introduzca el nombre del contacto que quiera eliminar: ");
        String contact = sc.nextLine();
        if (agenda.remove(contact) == null)
            System.out.println("El contacto " + contact + " no existe.");
    }
}
