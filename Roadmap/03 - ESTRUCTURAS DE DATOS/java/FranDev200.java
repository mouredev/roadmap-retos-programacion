import java.util.*;
import java.util.stream.Stream;

public class FranDev200 {

    static HashMap<Integer, String> contactList = new HashMap<>();
    static Scanner scan = new Scanner(System.in);

    static void main() {

        /*

        - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
        - Utiliza operaciones de inserción, borrado, actualización y ordenación.

         */

        // ARRAYLIST
        ArrayList<String> months = new ArrayList<>();
        months.add("Enero");
        months.add("Febrero");
        months.add("Marzo");
        months.add("Abril");
        months.add("Mayo");
        months.add("Junio");
        months.add("Julio");
        months.add("Agosto");
        months.add("Septiembre");
        months.add("Octubre");
        months.add("Noviembre");
        months.add("Diciembre");

        System.out.println("Meses del año");
        System.out.println("=============");
        for(String month : months){
            System.out.println(month);
        }

        months.remove(1);
        months.remove(2);

        System.out.println("\nMeses del año (despues de borrar 2)");
        System.out.println("===================================");
        for(String month : months){
            System.out.println(month);
        }

        months.set(1, "Febrero");

        System.out.println("\nMeses del año (despues de modificar 1)");
        System.out.println("======================================");
        months.forEach(System.out::println);

        System.out.println("\nMeses del año (Ordenados por nombre)");
        System.out.println("=======================================");

        sortMonthsByName(months).toList().forEach(System.out::println);

        /*
        Este bloque de codigo es lo mismo que lo de arriba
        for (String month: sortMonthsByName(months).toList()){
            System.out.println(month);
        }
        */
        months.clear();
        System.out.println("\nMeses del año (despues de borrar todos)");
        System.out.println("=======================================");
        for(String month : months){
            System.out.println(month);
        }
        months.forEach(System.out::println);

        // HASHSET
        HashSet<Integer> phoneNumber = new HashSet<>();
        phoneNumber.add(123456789);
        phoneNumber.add(987654321);
        phoneNumber.add(111222333);
        phoneNumber.add(444555666);
        phoneNumber.add(777888999);
        phoneNumber.add(676767676);

        System.out.println("\nTelefonos");
        System.out.println("=========");
        for(int number : phoneNumber){
            System.out.println(number);
        }

        phoneNumber.remove(phoneNumber.stream().toList().getFirst()); // Podria haber puesto el numero de telefono también
        System.out.println("\nTelefonos (Después de borrar 1)");
        System.out.println("===============================");
        for(int number : phoneNumber){
            System.out.println(number);
        }

        phoneNumber.add(444555666);
        phoneNumber.add(676767676);
        System.out.println("\nTelefonos (Intento de duplicados)");
        System.out.println("=================================");
        for(int number : phoneNumber){
            System.out.println(number);
        }

        System.out.println("\nTelefonos (Ordenados)");
        System.out.println("=================================");
        List<Integer> phoneOrdered = phoneNumber.stream().sorted(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {

                return o1.compareTo(o2);

            }
        }).toList();
        for(int number : phoneOrdered){
            System.out.println(number);
        }

        phoneNumber.clear();
        System.out.println("\nTelefonos (Despúes de borrarlos)");
        System.out.println("=================================");
        for(int number : phoneNumber){
            System.out.println(number);
        }

        System.out.println("\nTelefonos (Comprobar si existe un telefono)");
        System.out.println("=================================");
        System.out.println(phoneNumber.contains(111222333));

        /*
            En los HashSet no se puede editar un valor en concreto, debido a su estructura interna.
         */

        // HASHMAP
        HashMap<String, String[]> identity = new HashMap<>();
        identity.put("09834674Q", new String[]{"Francisco", "Baviano", "Ocampo"});
        identity.put("09225664R", new String[]{"Pedro", "López", "Dúrez"});
        identity.put("09236656L", new String[]{"Inmaculada", "Calvo", "Chicharro"});
        identity.put("09979571X", new String[]{"Zaira", "Herrán", "Gonzalez"});
        identity.put("09675674N", new String[]{"Jesus", "García", "Ocampos"});

        System.out.println("\nDNI y su nombre y apellidos");
        System.out.println("=================================");
        for(Map.Entry<String, String[]> person: identity.entrySet()){
            String[] name = person.getValue();
            System.out.println(person.getKey() + " --> " + name[0] + " " + name[1] + " " + name[2]);
        }

        System.out.println("\nDNI y su nombre y apellidos (Otra forma de mostrarlo)");
        System.out.println("=================================");
        for(Map.Entry<String, String[]> person: identity.entrySet()){
            System.out.println(person.getKey() + " --> " + Arrays.stream(person.getValue()).toList());
        }

        System.out.println("\nDNI y su nombre y apellidos (Ordenador por DNI)");
        System.out.println("=================================");
        for(Map.Entry<String, String[]> person: sortByDNI(identity).toList()){
            String[] name = person.getValue();
            System.out.println(person.getKey() + " --> " + name[0] + " " + name[1] + " " + name[2]);
        }

        identity.remove("09225664R");
        System.out.println("\nDNI y su nombre y apellidos(Después de eliminar a una persona)");
        System.out.println("=================================");
        for(Map.Entry<String, String[]> person: identity.entrySet()){
            String[] name = person.getValue();
            System.out.println(person.getKey() + " --> " + name[0] + " " + name[1] + " " + name[2]);
        }

        identity.put("09675674N", new String[]{"David", "Baviano", "Ocampo"});
        System.out.println("\nDNI y su nombre y apellidos(Después de editar a una persona)");
        System.out.println("=================================");

        sortByDNI(identity).toList().forEach(person -> {
            String[] name = person.getValue();
            System.out.println(person.getKey() + " --> " + name[0] + " " + name[1] + " " + name[2]);
        });


        /*

          DIFICULTAD EXTRA (opcional):
          Crea una agenda de contactos por terminal.
          - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
          - Cada contacto debe tener un nombre y un número de teléfono.
          - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
            los datos necesarios para llevarla a cabo.
          - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
            (o el número de dígitos que quieras)
          - También se debe proponer una operación de finalización del programa.

         */

        int choice;

        do{

            System.out.println("\nAGENDA PERSONAL, que desea hacer:");
            System.out.println("---------------------------------");
            System.out.println("1 - Agregar un contacto.");
            System.out.println("2 - Buscar contactos.");
            System.out.println("3 - Actualizar un contacto.");
            System.out.println("4 - Eliminar un contacto.");
            System.out.println("5 - Salir.");
            System.out.println("---------------------------------");
            System.out.print("Eleccion: ");


            try {
                choice = Integer.parseInt(scan.nextLine());

                if(choice > 0 && choice < 6){
                    options(choice);
                }else{
                    System.out.println("Selecciona un numero correcto.");
                }

            } catch (NumberFormatException e) {
                System.out.println("Introduzca un número.");
                choice = 0;
            }

        }while (choice != 5);

    }

    // Metodo para ordenar los meses del ArrayList
    private static Stream<String> sortMonthsByName(ArrayList<String> months) {
        return months.stream().sorted((o1, o2) -> o1.compareTo(o2));
    }

    // Metodo para ordenar el HashMap
    public static Stream<Map.Entry<String, String[]>> sortByDNI(HashMap<String, String[]> persons) {
        return persons.entrySet().stream().sorted((o1, o2) ->
                o1.getKey().compareTo(o2.getKey()));

    }

    // EJERCICIO EXTRA
    public static void options(int choice) {

        switch (choice){
            case 1:

                addContact();
                break;

            case 2:

                if(!contactList.isEmpty()){
                    search();
                }else{
                    System.out.println("Añade un contacto primero.");
                }

                break;

            case 3:

                if(!contactList.isEmpty()){
                    editContact();
                }else{
                    System.out.println("Añade un contacto primero.");
                }

                break;

            case 4:

                if(!contactList.isEmpty()){
                    deleteContact();
                }else{
                    System.out.println("Añade un contacto primero.");
                }

                break;

            case 5:

                System.out.println("SALIENDO...");
                break;
        }


    }

    private static void addContact() {

        int number = 0;
        String name = "";
        String checkNum = "";

        do{
            System.out.print("Introduce el número (9 digitos): ");

            try {
                number = Integer.parseInt(scan.nextLine());
                checkNum = String.valueOf(number);
                if(checkNum.length() != 9){
                    System.out.println("Longitud incorrecta.");

                }else{
                    if(contactList.containsKey(number)){
                        System.out.println("Ese número ya existe.");
                    }else{
                        System.out.print("Introduce el nombre del contacto: ");
                        name = scan.nextLine();
                    }

                }
            } catch (NumberFormatException e) {
                System.out.println("Formato incorrecto.");
            }
        }while(checkNum.length() != 9 || contactList.containsKey(number));

        contactList.put(number, name);
        System.out.println("Contacto guardado.");
    }

    private static void search() {
        int choice = 0;

        do{
            System.out.println("\nBuscar por:");
            System.out.println("-----------");
            System.out.println("1 - Número.");
            System.out.println("2 - Nombre.");
            System.out.println("-----------");
            System.out.print("Respuesta: ");

            try {
                choice = Integer.parseInt(scan.nextLine());

                if(choice == 1 || choice == 2){
                    searchContact(choice);
                }else{
                    System.out.println("Elección incorrecta.");
                }

            } catch (NumberFormatException e) {
                System.out.println("Introduzca un número.");
            }
        }while (choice != 1 && choice != 2);
    }

    private static void searchContact(int choice) {

        int num;
        String name;
        if(choice == 1){
            try {
                System.out.print("Introduce el número o parte de él: ");
                num = Integer.parseInt(scan.nextLine());
                for (Map.Entry<Integer, String> contact: searchByNum(contactList, num).toList()){
                    System.out.println(contact.getValue() + " --> " + contact.getKey());
                }

            } catch (NumberFormatException e) {
                System.out.println("Formato incorrecto.");
            }
        }else if (choice == 2) {
            System.out.print("Introduce el nombre o parte de él: ");
            name = scan.nextLine();
            for (Map.Entry<Integer, String> contact: searchByName(contactList, name).toList()){
                System.out.println(contact.getValue() + " --> " + contact.getKey());
            }
        }

    }

    private static Stream<Map.Entry<Integer, String>> searchByNum(HashMap<Integer, String> contacts, int numToSearch){

        String num = String.valueOf(numToSearch);
        return contacts.entrySet().stream().filter(
                entry -> entry.getKey().toString().contains(num)
        );

    }

    private static Stream<Map.Entry<Integer, String>> searchByName(HashMap<Integer, String> contacts, String nameToSearch){

        return contacts.entrySet().stream().filter(
                entry -> entry.getValue().toLowerCase().contains(nameToSearch.toLowerCase())
        );

    }

    private static void deleteContact(){
        int number = 0;
        String checkNum = "";
        do{
            System.out.print("Introduce el número a eliminar: ");

            try {
                number = Integer.parseInt(scan.nextLine());
                checkNum = String.valueOf(number);
                if(checkNum.length() != 9){
                    System.out.println("Longitud incorrecta.");

                }else{
                    if(!contactList.containsKey(number)){
                        System.out.println("Ese número no existe.");
                    }
                }
            } catch (NumberFormatException e) {
                System.out.println("Formato incorrecto.");
            }
        }while(checkNum.length() != 9 || !contactList.containsKey(number));

        contactList.remove(number);
        System.out.println("Contacto eliminado.");
    }

    private static void editContact(){

        System.out.println("LISTA DE CONTACTOS (" + contactList.entrySet().stream().toList().size() + " contactos)");
        System.out.println("=================================");
        for (Map.Entry<Integer, String> contact: contactList.entrySet().stream().toList()){
            System.out.println(" - " + contact.getKey() + " --> " + contact.getValue());
        }

        int number = 0;
        String checkNum = "";
        do{
            System.out.print("Introduce el número del contacto a editar: ");

            try {
                number = Integer.parseInt(scan.nextLine());
                checkNum = String.valueOf(number);
                if(checkNum.length() != 9){
                    System.out.println("Longitud incorrecta.");

                }else{
                    if(!contactList.containsKey(number)){
                        System.out.println("Ese número no existe.");
                    }
                }
            } catch (NumberFormatException e) {
                System.out.println("Formato incorrecto.");
            }
        }while(checkNum.length() != 9 || !contactList.containsKey(number));

        int choice = 0;

        do{
            System.out.println("\n¿Qué quiere editar?");
            System.out.println("-------------------");
            System.out.println("1 - Número.");
            System.out.println("2 - Nombre.");
            System.out.println("-----------");
            System.out.print("Respuesta: ");

            try {
                choice = Integer.parseInt(scan.nextLine());

                if(choice == 1){
                    editNumber(number);
                } else if (choice == 2) {
                    editName(number);
                } else{
                    System.out.println("Elección incorrecta.");
                }

            } catch (NumberFormatException e) {
                System.out.println("Introduzca un número.");
            }
        }while (choice != 1 && choice != 2);

    }

    private static void editName(int number) {

        System.out.print("Introduzca un nombre nuevo: ");
        String name = scan.nextLine();
        contactList.put(number, name);
        System.out.println("Contacto modificado.");
    }

    private static void editNumber(int number) {

        int newNumber = 0;
        String name = "";
        String checkNum = "";

        do{
            System.out.print("Introduce el nuevo número (9 digitos): ");

            try {
                newNumber = Integer.parseInt(scan.nextLine());
                checkNum = String.valueOf(newNumber);
                if(checkNum.length() != 9){
                    System.out.println("Longitud incorrecta.");

                }else{
                    if(contactList.containsKey(newNumber)){
                        System.out.println("Ese numero ya existe.");
                    }

                }
            } catch (NumberFormatException e) {
                System.out.println("Formato incorrecto.");
            }
        }while(checkNum.length() != 9 || contactList.containsKey(newNumber));

        name = contactList.get(number);
        contactList.put(newNumber, name);
        contactList.remove(number);

        System.out.println("Contacto modificado.");
    }


}
