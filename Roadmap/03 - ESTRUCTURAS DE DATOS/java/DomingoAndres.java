import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Scanner;

public class DomingoAndres {
    public static void main(String[]args){

        //EJERCICIO 03: ESTRUCTURAS DE DATOS

        //ARRAY
        String[] nombres = new String[3]; //Creamos el array
        
        //Le insertamos datos
        nombres[0] = "Pedro";
        nombres[1] = "Juan";
        nombres[2] = "Diego";

        //en los arrays no existe eliminacion directa
        //podriamos hacer un tipo de limpieza asignando un valor nulo
        //al indice que queremos "eliminar"
        nombres[1] = null;

        //actualizamos datos
        nombres[0] = "Domingo";
        nombres[2] = "Andres";
        nombres[1] = "Juanito";

        //Ordenamos el array por orden alfabetico
        Arrays.sort(nombres);


        //LIST
        List<Integer> calificaciones = new ArrayList<>(); //Creamos una lista de tipo ArrayList

        //Insertamos datos
        calificaciones.add(4);
        calificaciones.add(3);
        calificaciones.add(8);
        calificaciones.add(1);
        calificaciones.add(10);

        //Eliminamos datos
        calificaciones.remove(1); //aca estamos eliminando el elemento del indice 1 que seria el valor 3

        //Actualizamos datos
        calificaciones.set(0, 9); //aca actualizamos el valor del indice 0, paso de 4 a 9

        //Ordenamiento
        calificaciones.sort(null); //el null los ordena de menor a mayor


        //SETS
        Set<Integer> numeroTelefonico = new HashSet<>(); //creamos un set que alamacenara numeros telefonicos

        //Insertamos datos
        numeroTelefonico.add(12345678);
        numeroTelefonico.add(78945612);
        numeroTelefonico.add(65123488);


        //Eliminamos datos
        numeroTelefonico.remove(12345678);

        //Los datos de los sets no pueden ser actualizados directamente

        //Los sets no pueden ser ordenados directamente ya que esta estructura no prioriza el orden si no la unicidad.
        


        //MAPS
        Map <String, Integer> productos = new HashMap<>(); //Creamos un mapa de productos con sus respectivos precios

        //Insertamos datos
        productos.put("Hamburguesa", 5000);
        productos.put("Completo", 2500);
        productos.put("Bebida", 1500);

        //Eliminamos datos por su clave
        productos.remove("Completo");

        //actualizamos
        productos.replace("Hamburguesa", 5000, 4500);//aca actualizamos el precio de la hamburguesa, paasó de 5000 a 4500

        //Los maps no pueden ser ordenados directamente


        //----------------DIFICULTAD EXTRA--------------------------//

        Map <String, String> contactos = new HashMap<>();//creamos la agenda de contactos

        //Agregamos algunos contactos para que la agenda no este vacia
        contactos.put("Maria", "12345678916");
        contactos.put("Juan", "7894561234");
        contactos.put("Pedro", "4561237893");

        //Agregamos el scanner para las selecciones del usuario
        Scanner scanner = new Scanner(System.in);

        //agregamos un booleano para salir del bucle
        boolean salir = false;
        
        while (!salir) {

            System.out.println("|----------------------------------|");
            System.out.println("       AGENDA DE CONTACTOS");
            System.out.println("|----------------------------------|");
            System.out.println("\n¿Que accion desea realiar?");
            System.out.println("1. Buscar Contacto");
            System.out.println("2. Agregar Contacto");
            System.out.println("3. Actualizar Contacto");
            System.out.println("4. Eliminar Contacto");
            System.out.println("5. Salir");
            System.out.println("Ingrese su eleccion a continuacion:");
            

            if (scanner.hasNextInt()) {
                int opcion = scanner.nextInt();
                scanner.nextLine();

                switch (opcion) {
                case 1:
                    System.out.println("Ingrese el nombre del contacto que desea buscar:");
                    String nombreBuscar = scanner.nextLine();
                    
                    if(contactos.containsKey(nombreBuscar)){
                        System.out.println("el numero de contacto para " + nombreBuscar + " es: " + contactos.get(nombreBuscar));
                    }else{
                        System.out.println("El numero de contacto para " + nombreBuscar + " no existe.");
                    }
                    break;
                case 2:
                    System.out.println("Ingrese el nombre del nuevo contacto:");
                    String nombreNuevo = scanner.nextLine();
                    System.out.println("Ingrese el numero de nuevo contacto:");
                    String numeroNuevo = scanner.nextLine();
                    if(numeroNuevo.length() > 11){
                        System.out.println("Numero de contacto demasiado largo. No pude tener mas de 11 numeros.");
                    }else {
                        System.out.println("Nuevo contacto agregado exitosamente.");
                        contactos.put(nombreNuevo, numeroNuevo);
                    }
                    break;
                case 3:
                    System.out.println("Ingrese el nombre del contacto que desea actualiar:");
                    String nombreActualizar = scanner.nextLine();
                    
                    if(contactos.containsKey(nombreActualizar)){
                        System.out.println("Ingrese el nuevo nombre para ese contacto:");
                        String nuevoNombre = scanner.nextLine();
                        
                        System.out.println("Ingrese el nuevo numero para ese contacto:");
                        String nuevoNumero = scanner.nextLine();
                        
                        if(nuevoNumero.length() > 11){
                            System.out.println("Numero de contacto demasiado largo. No pude tener mas de 11 numeros.");
                        }else {
                            contactos.remove(nombreActualizar);

                            contactos.put(nuevoNombre, nuevoNumero);

                            System.out.println("Contacto actualizado correctamente.");
                        }
                    }else {
                        System.out.println("El numero de contacto para " + nombreActualizar + " no existe.");
                    }
                    break;
                case 4:
                    System.out.println("Ingrese el nombre del contacto que desea eliminar:");
                    String nombreEliminar = scanner.nextLine();
                    if (contactos.containsKey(nombreEliminar)) {
                        contactos.remove(nombreEliminar);
                        System.out.println("El contacto de " + nombreEliminar + " se ha eliminado exitosamente de la agenda.");
                    }else {
                        System.out.println("El contacto de " + nombreEliminar + " no existe.");
                    }
                    break;
                case 5:
                    System.out.println("Saliendo de la agenda...");
                    salir = true;
                    break;
            
                default:
                    System.out.println("Opcion incorrecta. Elija una opcion numerica del 1 al 5");
                }
            }else {
                System.out.println("Opcion incorrecta. Elija una opcion numerica del 1 al 5");
                scanner.nextLine();
            }
            
        }
        scanner.close();

    }

}
