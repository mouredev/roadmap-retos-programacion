import java.util.*;

public class Ldre3 {
    private static HashMap<String, Integer> agenda = new HashMap<>();

    public static void main(String[] args) {
        int [] array = new int[5];
        for(int i = 0; i < array.length; i++) {
          array[i] = i;
        }

        ArrayList<String> lista = new ArrayList<>();
        lista.add("Elemento 1");
        lista.add("Elemento 2");
        Collections.sort(lista);
        lista.remove(1);


        HashSet<Integer> set = new HashSet<>();
        set.add(1);
        set.add(2);
        set.add(3);
        set.removeIf(n -> n%2 == 0);

        HashMap<String, Integer> mapa = new HashMap<>();
        mapa.put("A",1);
        mapa.put("B",2);
        Integer clave = mapa.get("A");


        /*
         * DIFICULTAD EXTRA (opcional):
         * Crea una agenda de contactos por terminal.
         * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
         * - Cada contacto debe tener un nombre y un número de teléfono.
         * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
         *   los datos necesarios para llevarla a cabo.
         * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
         *   (o el número de dígitos que quieras)
         * - También se debe proponer una operación de finalización del programa.
         */
        boolean salir = false;
        int opcion;
        Scanner ent = new Scanner(System.in);
        while (!salir){
            System.out.println("Introduce una opcion 1. Busqueda 2. Insertar 3. Actualizacion 4. Eliminacion 5.Salir");
            opcion = ent.nextInt();
            ent.nextLine();
            switch (opcion){
                case 1 -> {
                    System.out.println("Introduce el nombre a buscar");
                    String busqueda = ent.nextLine();
                    Optional <Integer> telefono = busquedaContacto(busqueda);
                    String mostrar = telefono.map(integer -> "El numero de "+ busqueda+" es " + integer).orElse("No existe el contacto");
                    System.out.println(mostrar);
                }
                case 2 -> {
                    System.out.println("Introduce el nombre a introducir");
                    String nombre = ent.nextLine();
                    System.out.println("Introduce el telefono a introducir");
                    int telefono = ent.nextInt();
                    ent.nextLine();
                    if (insertarContacto(nombre, telefono)) System.out.println("Contacto insertado");
                    else System.out.println("El contacto ya existe");

                }
                case 3 -> {
                    System.out.println("Introduce el nombre a actualizar");
                    String nombre = ent.nextLine();
                    System.out.println("Introduce el telefono a actualizar");
                    int telefono = ent.nextInt();
                    ent.nextLine();
                    if (actualizar(nombre, telefono)) System.out.println("Contacto actualizado");
                    else System.out.println("El contacto no existe");
                }

                case 4 -> {
                    System.out.println("Introduce el nombre a eliminar");
                    String nombre = ent.nextLine();

                    if (eliminar(nombre)) System.out.println("Contacto eliminado");
                    else System.out.println("El contacto no existe");
                }

                case 5 -> {
                    salir=true;
                }
            }
        }

    }
    private static Optional<Integer> busquedaContacto(String nombre){
        return Optional.ofNullable(agenda.get(nombre));
    }

    private static boolean insertarContacto (String nombre, int telefono){
        if (String.valueOf(telefono).length()>9) throw new IllegalArgumentException("El numero no puede tener mas de 9 digitos");
        return agenda.putIfAbsent(nombre, telefono) == null;
    }

    private static boolean actualizar (String nombre, int telefono){
        if (String.valueOf(telefono).length()>9) throw new IllegalArgumentException("El numero no puede tener mas de 9 digitos");
        return agenda.replace(nombre, telefono) != null;
    }

    private static boolean eliminar (String nombre){
        return agenda.remove(nombre) != null;
    }
}