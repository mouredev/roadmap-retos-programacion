import java.lang.reflect.Array;
import java.util.*;

public class simonguzman {
    public enum Dias{
        Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        //*********************Arrays*********************
        int [] numbers = {1,2,3,4,5}; 
        int newLength = 8;
        //update
        numbers[0] = 13;
        //sort
        Arrays.sort(numbers);
        //Insertion
        int [] newArray = new int[newLength];
        for (int i = 0; i < numbers.length; i++) {
            newArray[i] = numbers[i];
        }
        numbers = newArray;
        //Delete
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = 0;
        }
        //Show the array
        System.out.println(Arrays.toString(numbers));
        //Alternative to show the array
        for (int i = 0; i < numbers.length; i++){
            System.out.println(numbers[i]);
        }

        ////*********************Bidimensional Array****************
        int [][] numId = new int[2][2];

        //Insertion
        numId[0][0] = 0;
        numId[0][1] = 1;
        numId[1][0] = 2;
        numId[1][1] = 3;
        //update
        numId[0][1] = 4;
        //Delete
        numId[1][1] = 0;
        //Alternative delele
        for (int i = 0; i < numId.length; i++){
            for (int j = 0; j < numId[i].length; j++){
                numId[i][j] = 0;
            }
        }

        //Show the bidimensional array
        for (int i = 0; i < numId.length; i++){
            for (int j = 0; j < numId[i].length; j++){
                System.out.println(numId[i][j]);
            }
        }


        //*********************Lists*********************
        ArrayList<String> names = new ArrayList<>();
        //Insertion
        names.add("Simon");
        names.add("Julian");
        names.add("Camilo");
        names.add("Santiago");
        names.add("Carlos");
        //Delete    
        names.clear();
        //Update
        names.set(2, "Juliana");
        //Sort
        Collections.sort(names);
        //Show the list
        System.out.println(names);

        //LinkedList
        LinkedList<String> lista = new LinkedList<>();

        //Insertion
        lista.add("Primer elemento");
        lista.add("Segundo elemento");
        lista.add("Tercer elemento");
        lista.add("Cuarto elemento");
        lista.add("Ultimo elemento");
        //Update
        lista.set(4, "Nuevo elemento");
        //Delete
        lista.remove(3);
        lista.remove("Tercer elemento");
        //Alternative of delete
        //lista.removeFirst();
        //lista.removeLast();
        //lista.removeAll(lista);
        //Sort
        Collections.sort(lista);
        //Show linked list
        for(String item: lista){
            System.out.println(item);
        }

        //*********************Maps*********************
        HashMap<String, Integer> infoPersonal = new HashMap<>();
        //Insertion
        infoPersonal.put("Simon", 20);
        infoPersonal.put("Julian", 22);
        infoPersonal.put("Camilo", 24);
        infoPersonal.put("Santiago", 21);
        infoPersonal.put("Carlos", 28);
        //Uodate
        infoPersonal.put("Juliana", 22);
        //Delete
        infoPersonal.remove("Camilo");
        //Show the map
        System.out.println(infoPersonal.keySet() + " " + infoPersonal.values());
        //Alternative option
        for(Map.Entry<String, Integer> entry : infoPersonal.entrySet()){
            System.out.println(entry.getKey() + " " + entry.getValue());
        }

        //*********************Colections*********************
        ArrayList<Integer> edades = new ArrayList<>();
        //Insertion
        edades.add(22);
        edades.add(30);
        edades.add(21);
        edades.add(24);
        //update
        edades.set(1, 29);
        //Delete
        edades.remove(2);
        //Sort
        Collections.sort(edades);
        //Show the colections
        int age = edades.get(0);
        System.out.println(age);
        for (int i = 0; i < edades.size(); i++){
            System.out.println(edades.get(i));
        }

        //*********************TreeSet*********************
        TreeSet<Integer> set = new TreeSet<>();

        //Insertion
        set.add(10);
        set.add(11);
        set.add(12);
        set.add(13);
        set.add(14);
        set.add(15);
        //Delete
        set.remove(13);
        //Show the TreeSet
        for(Integer i: set){
            System.out.println(i);
        }

        //*********************HashSet*********************
        HashSet<String> namesPersonal = new HashSet<>();
        //Insertion
        namesPersonal.add("Juan");
        namesPersonal.add("Maria");
        namesPersonal.add("Adriano");
        //Update
        names.remove("Maria");
        //Show HashSet
        for(String name : names){
            System.out.println(name);
        }

        //*********************Enum*********************
        Dias dia = Dias.Lunes;

        switch (dia) {
            case Lunes:
                System.out.println("Es el dia lunes");
                break;
            case Martes:
                System.out.println("Es el dia martes");
                break;
            case Miercoles:
                System.out.println("Es el dia miercoles");
                break;
            case Jueves:
                System.out.println("Es el dia jueves");
                break;
            case Viernes:
                System.out.println("Es el dia viernes");
                break;
            case Sabado:
                System.out.println("Es el dia sabado");
                break;
            case Domingo:
                System.out.println("Es el dia domingo");
                break;
            default:
                System.out.println("El dia no existe");
                break;
        }
        //*Ejecucion del ejercicio adicional */
        agendaContactos();
    }
    //******************************Ejercicio adicional******************************/
    public static void agendaContactos(){
        HashMap<String, Long> contactos = new HashMap();
        Scanner scanner = new Scanner(System.in);
        int opcion;
        do{
            menuPresentacion();
            opcion = scanner.nextInt();
            opcionMenu(opcion, contactos, scanner);
        }while( opcion !=5 );
        scanner.close();
    }

    public static void presentacion(){
        System.out.println("*******************************");
        System.out.println("Bienvenido al sistema");
        System.out.println("*******************************");
    }

    public static void menuPresentacion(){
        presentacion();
        System.out.println("1. Busqueda");
        System.out.println("2. Insercion");
        System.out.println("3. Actualizacion");
        System.out.println("4. Eliminar");
        System.out.println("5. Salir");
        System.out.println("Ingrese una opcion: ");
    }

    public static void opcionMenu(int opcion, HashMap<String,Long> contactos ,Scanner scanner){
        switch (opcion) {
            case 1:
                    buscarContacto(contactos, scanner);
                break;
            case 2:
                    insertarContacto(contactos, scanner);
                break;
            case 3:
                    actualizarContacto(contactos, scanner);
                break;
            case 4:
                    eliminarContacto(contactos, scanner);
                break;
            case 5:
                    System.out.println("Saliendo del programa....");
                break;
        
            default:
                System.out.println("ERROR: Ingrese una opcion validad");
                break;
        }
    }

    public static void insertarContacto(HashMap<String, Long> contactos ,Scanner scanner){
        System.out.println("Ingrese el nombre del contacto: ");
        String name = scanner.next();
        Long numPhone = validInput(scanner, "Ingrese el numero de telefono:");
        if(validacionCompleta(numPhone)){
            contactos.put(name, numPhone);
            System.out.println("Contacto ingresado con exito");
        }else{
            System.out.println("ERROR: El número de teléfono debe ser numérico y tener un máximo de 11 dígitos.");
        }
    }

    public static void buscarContacto(HashMap<String, Long> contactos, Scanner scanner){
        if(validarVacios(contactos)){
            System.out.println("Ingrese el nombre del contacto: ");
            String nombre = scanner.next();
            Long telefono = contactos.get(nombre);
            if(telefono != null){
                System.out.println("Nombre del contacto: "+ nombre + " Telefono : "+ telefono); 
            }else{
                System.out.println("El contacto no existe");
            }
        }
    }

    public static void actualizarContacto(HashMap<String,Long> contactos, Scanner scanner){
        if(validarVacios(contactos)){
            System.out.println("Ingrese el nombre del contacto: ");
            String nombre = scanner.next();
            if(contactos.containsKey(nombre)){
                Long telefono = validInput(scanner, "Ingrese el numero de telefono nuevo: ");
                if(validacionCompleta(telefono)){
                    contactos.put(nombre, telefono);
                    System.out.println("Contacto actualizado con exito");
                }else{
                    System.out.println("ERROR: El número de teléfono debe ser numérico y tener un máximo de 11 dígitos.");
                }
            }else{
                System.out.println("El contacto no fue encontrado o no existe");
            }
        }
    }

    public static void eliminarContacto(HashMap<String,Long> contactos, Scanner scanner){
        if(validarVacios(contactos)){
            System.out.println("Ingrese el nombre del contacto: ");
            String nombre = scanner.next();
            if(contactos.remove(nombre)!=null) {
                System.out.println("Contacto eliminado con exito");
            }else{
                System.out.println("El contacto no ha sido encontrado");
            }
        }
    }

    public static boolean validarTelefono(Long numPhone){
        String numPhoneString = String.valueOf(numPhone);
        if(numPhoneString.length() > 11){
            return false;
        }
        return true;
    }


    public static boolean validarNoNumericos(Long numPhone){
        String numPhoneString = String.valueOf(numPhone);
        for (int i = 0; i < numPhoneString.length(); i++){
            char c = numPhoneString.charAt(i);
            if(!Character.isDigit(c)){
                return false;
            }
        }
        return true;        
    }

    public static boolean validacionCompleta(Long numPhone){
        boolean valPhone = validarTelefono(numPhone);
        boolean valNotNumeric = validarNoNumericos(numPhone);

        return valPhone && valNotNumeric;
    }

    public static boolean validarVacios(HashMap<String, Long> contactos){
        if(contactos.isEmpty()){
            System.out.println("No hay contactos");
            return false;
        }else{
            return true;
        }
    }


    public static Long validInput(Scanner scanner, String input){
        boolean isValidInput = false;
        Long inputNumber = null;
        while (!isValidInput) {
            try {
                System.out.println(input);
                inputNumber = scanner.nextLong();
                isValidInput = true;
            } catch (InputMismatchException e) {
                System.out.println("Error: el numero de telefono solo puede tener digitos");
                scanner.next();
            }
        }
        return inputNumber;
    }
}
