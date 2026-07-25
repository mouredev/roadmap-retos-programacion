import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

public class mariovelascodev {
    public static void main(String[] args) {
        //Estructuras de datos

        //Arrays
        System.out.println("Arrays");
        int [] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

        //Acceso elemento indicado
        System.out.println(numbers[3]);

        // Cambiar elemento
        numbers[3] = 12;
        System.out.println(numbers[3]);

        //Ver longitud
        System.out.println(numbers.length);

        System.out.println("-----------------------\n");

        //ArrayList
        System.out.println("ArrayList");
        //Creación del ArrayList
        ArrayList<String> cars = new ArrayList<>();

        //Inserción de datos
        cars.add("Volvo");
        cars.add("Toyota");
        cars.add("Ford");
        cars.add("BMW");
        cars.add("Mazda");

        System.out.println(cars);

        //Ver tamaño del ArrayList
        System.out.println(cars.size());

        //Acceso al elemento
        System.out.println(cars.get(1)); //Accede al elemento del indice 1
        System.out.println(cars.getFirst()); //Acede al primer elemento
        System.out.println(cars.getLast()); //Accede al último elemento

        //Cambiar valor de algún elemento
        cars.set(0, "Opel");
        System.out.println(cars);

        //Eliminar elemento
        cars.remove(3);
        System.out.println(cars);

        cars.clear(); //Vaciaria el ArrayList
        System.out.println(cars);

        System.out.println("-----------------------\n");

        //HashSet
        System.out.println("HashSet");

        //Creación del HashSet
        HashSet<Integer> setNumbers = new HashSet<Integer>();

        //Añadir elemento
        setNumbers.add(1);
        setNumbers.add(2);
        setNumbers.add(3);
        setNumbers.add(4);
        setNumbers.add(5);

        System.out.println(setNumbers);

        //Comprobar si un elemento existe
        System.out.println(setNumbers.contains(3));

        //Ver tamaño del HashSet
        System.out.println(setNumbers.size());

        //Eliminar elemento
        setNumbers.remove(3); //Elimina el elemento indicado
        System.out.println(setNumbers);

        setNumbers.clear(); //Vacía el HashSet
        System.out.println(setNumbers);

        System.out.println("-----------------------\n");

        //HashMap
        System.out.println("HashMap");

        //Creación de HashMap
        HashMap <String, Integer> contact = new HashMap<>();

        //Añadir elemento
        contact.put("Marta", 123456789);
        contact.put("Victor", 234567891);
        contact.put("Rodrigo", 987654321);
        contact.put("Carla", 987654321);
        contact.put("Carlos", 987654321);

        System.out.println(contact);

        //Ver tamaño del HashMap
        System.out.println(contact.size());

        //Acceder al elemento
        System.out.println(contact.get("Marta"));

        //Eliminar elemento
        contact.remove("Rodrigo"); //Elimina el elemento indicado por la clave
        System.out.println(contact);

        contact.clear(); //Vacía el HashMap
        System.out.println(contact);

        System.out.println("-----------------------\n");

        //EXTRA
        System.out.println("Extra");
        addressBook();
    }

    public static void addressBook() {
        System.out.println("Agenda de Contactos");

        HashMap<String, Integer> contacts = new HashMap<>();
        Scanner input = new Scanner(System.in);
        Scanner inputName = new Scanner(System.in);
        Scanner inputPhone = new Scanner(System.in);
        boolean open = true;
        String name;
        String phone;

        //Menú de opciones de la agenda de contactos
        while (open) {
            System.out.print("""
                    1 - Ver Contactos
                    2 - Búsqueda de Contactos
                    3 - Añadir Contactos
                    4 - Actualización de Contactos
                    5 - Eliminar Contactos
                    6 - Salir
                    Introduce el número de la acción a realizar:
                    """);

            int inputOption = input.nextInt();


            switch (inputOption) {
                case 1:
                    System.out.println("Contactos");
                    contacts.forEach((contactName, phoneNumber) ->
                            System.out.println(contactName + ": " + phoneNumber));
                    break;
                case 2:
                    System.out.println("Introduce el contacto a buscar:");
                    name = inputName.nextLine();

                    if (contacts.containsKey(name)) {
                        System.out.println(contacts.get(name));
                    }else {
                        System.out.println("Contacto no encontrado");
                    }

                    break;
                case 3:
                    System.out.println("Introduce el nombre del contacto:");
                    name = inputName.nextLine();

                    System.out.println("Introduce el número de teléfono:");
                    phone = inputPhone.nextLine();

                    if(phone.length() == 9) {
                        try {
                            int phoneNumber = Integer.parseInt(phone);
                            contacts.put(name, phoneNumber);
                            System.out.println("Contacto creado correctamente");
                        }catch (NumberFormatException e) {
                            System.out.println("Error, no has introducido un número.");
                        }
                    }else {
                        System.out.println("Error, el número de teléfono debe tener una longitud de 9 números.");
                    }

                    break;
                case 4:
                    System.out.println("Introduce el nombre del contacto:");
                    name = inputName.nextLine();

                    if(contacts.containsKey(name)) {
                        System.out.println("Introduce el número de teléfono a actualizar:");
                        phone = inputPhone.nextLine();

                        if(phone.length() == 9) {
                            try {
                                int phoneNumber = Integer.parseInt(phone);
                                contacts.replace(name, phoneNumber);
                                System.out.println("Contacto actualizado correctamente");
                            }catch (NumberFormatException e) {
                                System.out.println("Error,"+e.getMessage()+". Introduce el número de teléfono");
                            }
                        }else {
                            System.out.println("Error, el número de teléfono debe tener una longitud de 9 números.");
                        }

                    }
                    break;
                case 5:
                    System.out.println("Introduce el nombre del contacto a eliminar:");
                    name = inputName.nextLine();

                    if(contacts.containsKey(name)) {
                        contacts.remove(name);
                        System.out.println("Contacto eliminado correctamente");
                    }else{
                        System.out.println("Contacto no encontrado");
                    }
                    break;
                case 6:
                    open = false;
                    break;
                default:
                    System.out.println("Debes introducir una opción valida.\nMarcando números del 1 al 6");
            }
        }
    }
}
