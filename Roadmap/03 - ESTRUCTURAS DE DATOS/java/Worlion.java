import java.util.TreeMap;
import java.util.LinkedList;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Queue;
import java.util.Scanner;

public class Worlion {

            
    Scanner scanner = new Scanner(System.in);
    HashMap<String, String> agenda = new HashMap<>();

    public static void main(String[] args) {
        System.out.println("Estructuras de datos en Java");

        new Worlion().run();
    }

    public void run() {
        estructurasDeDatos();
        extra();
    }

    /*
    * EJERCICIO: Estructuras de datos en Java
    */

    private void estructurasDeDatos() {
        // Ejemplos de creación de estructuras de datos en Java
        // Arrays
        int [] numbers = new int[5];

        // ArrayList
        ArrayList<String> listaCadenas = new ArrayList<>();
        System.out.println("Lista: " +listaCadenas);

        //HashMap
        HashMap<Integer, String> mapaEnteroCadena = new HashMap<>();
        System.out.println("Mapa: " +mapaEnteroCadena);

        //HashSet 
        HashSet<String> conjuntoCadenas = new HashSet<>();
        System.out.println("Conjunto: " +conjuntoCadenas);

        // LinkedList
        LinkedList<Integer> listaEnteros = new LinkedList<>();
        System.out.println("Lista: " +listaEnteros);

        // TreeMap
        TreeMap<String, Integer> mapaCadenaEntero = new TreeMap<>();
        System.out.println("Mapa: " +mapaCadenaEntero);

        // Cola
        Queue<Integer> cola = new LinkedList<>();
        System.out.println("Cola: " +cola);

        // inserción 
        listaCadenas.add("Hola");
        listaCadenas.add("Mundo");
        listaCadenas.add("Java");
        listaCadenas.add("Estructuras de datos");

        System.out.println("Lista tras la inserción: " +listaCadenas);
        
        //borrado, 
        listaCadenas.remove("Java");
        System.out.println("Lista tras borrado: " +listaCadenas);
        
        //actualización 
        listaCadenas.set(2, "Java");
        System.out.println("Lista tras actualización: " +listaCadenas);
        
        //ordenación.
        listaCadenas.sort(null);
        System.out.println("Lista ordenada: " +listaCadenas);
    }


    private void extra() {

        /*
        * DIFICULTAD EXTRA (opcional): Agenda de contactos
        */

        

        System.out.println(" \n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n");

        var option = "";
        while(!option.equals("0")){

            option = showMenu();
            manageOption(option);
        }
    
    }

    private String showMenu() {
        
        System.out.println("\n AGENDA DE CONTACTOS\n");
        System.out.println("\t 1.- Búsqueda de un contacto");
        System.out.println("\t 2.- Añadir un contacto");
        System.out.println("\t 3.- Actualización de un contacto");
        System.out.println("\t 4.- Borrar un contacto");
        System.out.println("\t 5.- Mostrar agenda (extra)");
        System.out.println("\t 0.- Salir");
        System.out.println("\n Selecciona una opción:");
        return scanner.nextLine();
    }

    private void manageOption(String option) {
        switch (option) {
            case "1":
                System.out.println(findContact());
                break;
            case "2":
                addContact();
                break;
            case "3":
                updateContact();
                break;
            case "4":
                deleteContact();
                break;
            case "5":
                showDirectory();
                break;
            case "0":
                System.out.println("Saliendo...");
                break;
            default:
                System.out.println("WARNING: Opción no válida");
                break;
        }
    }

    private String findContact() {
        System.out.println("Introduce el nombre del contacto que quieres buscar:");
        var name = scanner.nextLine();
        var phone = agenda.get(name);

        if(phone != null){
            return phone;
        } else {
            return "No se ha encontrado el contacto";
        }
    }

    private void addContact() {
        System.out.println("Introduce el nombre del contacto que quieres añadir:");
        var name = scanner.nextLine();
        System.out.println("Introduce el teléfono del contacto que quieres añadir:");
        var phone = readValidPhone();
        if(phone != null){
            agenda.put(name, phone);
            System.out.println("Contacto añadido");
        } else {
            System.out.println("ERROR: No se ha podido añadir el contacto");
        }
    }

    private void updateContact(){
        System.out.println("Introduce el nombre del contacto que quieres actualizar:");
        var name = scanner.nextLine();
        var phone = readValidPhone();
        if(phone != null){
            agenda.put(name, phone);
            System.out.println("Contacto actualizado");
        } else {
            System.out.println("ERROR: No se ha podido actualizar el contacto");
        }
    }

    private void deleteContact(){
        System.out.println("Introduce el nombre del contacto que quieres eliminar:");
        var name = scanner.nextLine();
        var phone = agenda.get(name);
        if(phone != null){
            agenda.remove(name);
            System.out.println("Contacto eliminado");
        } else {
            System.out.println("ERROR: No se ha encontrado el contacto");
        }
    }

    private void showDirectory(){
        System.out.println("\nAgenda de contactos:");
        for (String name : agenda.keySet()) {
            System.out.println(" - Nombre: " + name + " - Teléfono: " + agenda.get(name));
        }
        System.out.println("\nTotal de contactos: " + agenda.size() + "\n");
    }

    private String readValidPhone() {
        System.out.println("Introduce el teléfono:");
        var phone = scanner.nextLine();
        while(!validPhone(phone)){
            System.out.println(" # Teléfono no valido # ¿Desea volver a intentarlo? (s/n): ");
            var retry = scanner.nextLine();
            if(retry.equals("n")){
                return null;
            }
            System.out.println("Introduce el teléfono:");
            phone = scanner.nextLine();
        }
        return phone;
    
    }

    private boolean validPhone(String phone) {
        return phone.matches("[0-9]+") && phone.length() <= 11;
    }



}
