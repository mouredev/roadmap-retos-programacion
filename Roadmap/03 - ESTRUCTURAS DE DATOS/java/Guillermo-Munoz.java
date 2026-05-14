import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;
import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.ArrayDeque;

public class GuillermoMunoz {
    /*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
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


    public static void main(String[] args) {

        //========================================================================
        // *************** Array ****************
        // Un array es una estructura de datos que almacena elementos del mismo tipo en una posición contigua de memoria.
        //========================================================================

        System.out.println("------- ARRAY ------- \n");

        int[] numeros = {4, 5, 1, 2, 3};
        String[] colores = {"Rojo", "Verde", "Azul"};

        // No se pueden insertar o eliminar elementos en un array, pero si se pueden actualizar
        
        // Actualización de un elemento
        colores[1] = "Amarillo";
        System.out.println("Actualización de un elemento: " + colores[1]);

        // Ordenación de un array
        System.out.println("Ordenación de un array:" + " Antes: " + Arrays.toString(numeros));
        Arrays.sort(numeros);
        System.out.println("Ordenación de un array:" + " Después: " + Arrays.toString(numeros));

        //========================================================================
        // ************* ArrayList **************** 
        // ArrayList es una clase que implementa la interfaz List, y permite almacenar elementos de forma dinámica.
        //=========================================================================

        System.out.println("\n------- ARRAYLIST ------- \n");

        ArrayList<Integer> numerosList = new ArrayList<Integer>();

        // Inserción de elementos
        numerosList.add(10);
        numerosList.add(20);
        numerosList.add(30);
        numerosList.add(55);
        numerosList.add(88);

        // Borrado de un elemento
        numerosList.remove(3); // Elimina el elemento en la posición 3 (55)

        // Actualización de un elemento
        numerosList.set(2, 15);

        // Ordenación de un ArrayList
        System.out.println("Ordenación de un ArrayList:" + " Antes: " + numerosList);
        numerosList.sort(null); 
        System.out.println("Ordenación de un ArrayList:" + " Después: " + numerosList);

        //========================================================================
        // ************* Array Multidimensionales **************** 
        // Un array multidimensional es un array que contiene otros arrays como elementos, permitiendo almacenar datos en múltiples dimensiones.
        //=========================================================================


        System.out.println("\n------- ARRAY MULTIDIMENSIONAL ------- \n");

        int[][] matriz = {
            {1,2,3},
            {4,5,6},
            {7,8,9}
        };

        // Inserción de un elemento
        matriz[0][0] = 10; // Inserta el valor 10 en la posición (0,0)

        // Borrado de un elemento (no se puede eliminar un elemento de un array, pero se puede establecer a un valor específico)
        matriz[1][1] = 0; // Establece el valor en la posición (1,1) a 0

        // Actualización de un elemento
        matriz[2][2] = 20; // Actualiza el valor en la posición (2,2) a 20

        // Ordenación de un array multidimensional (no se puede ordenar directamente, pero se puede ordenar cada fila o columna por separado)
       for ( int i = 0; i < matriz.length; i++){
        System.out.println(Arrays.toString(matriz[i]));
       }

        for (int i = 0; i < matriz.length; i++) {
            Arrays.sort(matriz[i]);
        }{
            System.out.println("Ordenación de un array multidimensional:" + " Después: ");
            for (int i = 0; i < matriz.length; i++) {
                System.out.println(Arrays.toString(matriz[i]));
            }
        }

        //========================================================================
        // ************* HashSet **************** 
        // HashSet es una clase que implementa la interfaz Set, y permite almacenar elementos únicos de forma no ordenada.
        //=========================================================================

        System.out.println("\n------- HASHSET ------- \n");

        HashSet<String> coloresSet = new HashSet<String>();

        //Inserción de elementos
        coloresSet.add("rojo");
        coloresSet.add("verde");
        coloresSet.add("amarillo");
        coloresSet.add("negro");
        coloresSet.add("blanco");
        coloresSet.add("rojo"); // No se añadirá porque ya existe
        coloresSet.add("morado"); 

        //Borrado de un elemento
        coloresSet.remove("negro");

        //Actualización de un elemento (no se puede actualizar directamente, pero se puede eliminar el elemento antiguo y agregar el nuevo)
        
        // Ordenación de un HashSet (no se puede ordenar directamente, pero se puede convertir a un TreeSet y ordenar esa lista)

        Set<String> coloresOrdenados = new TreeSet<>(coloresSet);
        System.out.println("Ordenación de un HashSet:" + " Antes: " + coloresSet);
        System.out.println("Ordenación de un HashSet:" + " Después: " + coloresOrdenados);


        //========================================================================
        // ************* HashMap **************** 
        // HashMap es una clase que implementa la interfaz Map, y permite almacenar pares clave-valor.
        //=========================================================================

        System.out.println("\n------- HASHMAP ------- \n");

        HashMap<String, String> contactos = new HashMap<String, String>();

        //Inserción de elementos
        contactos.put("Juan", "123456789");
        contactos.put("María", "987654321");
        contactos.put("Pedro", "555555555");
        contactos.put("Ana", "111111111");

        //Borrado de un elemento
        contactos.remove("Pedro");

        //Actualización de un elemento
        contactos.put("Juan", "999999999");

        // Ordenación de un HashMap (no se puede ordenar directamente, pero se puede convertir a un TreeMap y ordenar esa lista)
        Map<String, String> contactosOrdenados = new TreeMap<>(contactos);
        System.out.println("Ordenación de un HashMap:" + " Antes: " + contactos);
        System.out.println("Ordenación de un HashMap:" + " Después: " + contactosOrdenados);

        //========================================================================
        // ************* PriorityQueue **************** 
        // PriorityQueue es una clase que implementa la interfaz Queue, y permite almacenar elementos de forma ordenada según su prioridad.
        //=========================================================================

        System.out.println("\n------- PRIORITYQUEUE ------- \n");

        PriorityQueue<Integer> colaPrioridad = new PriorityQueue<Integer>();

        //Inserción de elementos
        colaPrioridad.add(5);
        colaPrioridad.add(2);
        colaPrioridad.add(8);
        colaPrioridad.add(1);
        colaPrioridad.add(3) ;

        //Borrado de un elemento (elimina el elemento con mayor prioridad, que en este caso es el número más pequeño)  
        colaPrioridad.poll(); // Elimina el elemento con menor valor (prioridad más alta)
        System.out.println("Cola de prioridad: " + colaPrioridad);

        //Actualización de un elemento (no se puede actualizar directamente, pero se puede eliminar el elemento antiguo y agregar el nuevo)
        colaPrioridad.remove(3); // Elimina el elemento 3
        colaPrioridad.add(4); // Agrega el nuevo elemento 4
        System.out.println("Cola de prioridad después de la actualización: " + colaPrioridad);

        // Ordenación de una PriorityQueue (la cola de prioridad ya mantiene los elementos ordenados según su prioridad, por lo que no es necesario ordenarla manualmente)
        System.out.println("Cola de prioridad ordenada: " + colaPrioridad);

        //========================================================================
        // ************* ArrayDeque **************** 
        // ArrayDeque es una clase que implementa la interfaz Deque, y permite almacenar elementos de forma dinámica en ambos extremos de la cola.
        //=========================================================================

        System.out.println("\n------- ARRAYDEQUE ------- \n");

        ArrayDeque<Integer> colaArray = new ArrayDeque<Integer>();

        //Inserción de elementos
        colaArray.add(5);
        colaArray.add(2);
        colaArray.add(8);
        colaArray.add(1);
        colaArray.add(3) ;

        //Borrado de un elemento (elimina el primer elemento de la cola)
        colaArray.pollFirst(); // Elimina el primer elemento
        System.out.println("Cola ArrayDeque: " + colaArray);

        //Actualización de un elemento (no se puede actualizar directamente, pero se puede eliminar el elemento antiguo y agregar el nuevo)
        colaArray.remove(3); // Elimina el elemento 3
        colaArray.addLast(4); // Agrega el nuevo elemento 4 al final de la cola
        System.out.println("Cola ArrayDeque después de la actualización: " + colaArray);

    

         /*
 * EJERCICIO:
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
ejecutarAgenda();
             
}

 //========================================================================
        // ************* EJERCICIO **************** 
        // Crea una agenda de contactos por terminal.
        //=========================================================================
          // Constantes de color
        public static final String RESET = "\u001B[0m";
        public static final String VERDE = "\u001B[32m";
        public static final String VERDE_CLARO = "\u001B[92m";
        public static final String AMARILLO = "\u001B[33m";
        public static final String CYAN = "\u001B[36m";

        public static void ejecutarAgenda() {
            
                // Aquí iría la lógica para manejar las opciones del menú y realizar las operaciones correspondientes
                HashMap<String, String> agenda = new HashMap<String, String>(); // Esta estructura de datos se utilizaría para almacenar los contactos de la agenda
                int opcion = 0; // Esta variable se actualizaría con la opción seleccionada por el usuario
                // Ejemplo de manejo de opciones (esto es solo un esquema, no es funcional)
                Scanner scanner = new Scanner(System.in);
                do{ // Mientras la opción no sea la de salir
                     mostrarMenu();
                     opcion = scanner.nextInt(); // Leer la opción seleccionada por el usuario
                     scanner.nextLine(); // Limpiar el buffer después de leer un número
                switch (opcion) {
                 

                    case 1:
                        System.out.println(VERDE + "Inserta un nombre de contacto." + RESET);
                        String nombre = scanner.nextLine(); // Leer el nombre del contacto
                        System.out.println(VERDE + "Inserta un número de teléfono." + RESET);
                        String telefono = scanner.nextLine(); // Leer el número de teléfono del contacto
                        // Validar el número de teléfono (debe ser numérico y tener un máximo de 11 dígitos)
                        if(telefono.matches("\\d{1,11}")) {
                            // Lógica para insertar el contacto en la agenda
                            System.out.println(VERDE + "Contacto insertado: " + nombre + " - " + telefono + RESET);
                            agenda.put(nombre,  telefono); // Insertar el contacto en la agenda

                        } else {
                            System.out.println(AMARILLO + "Número de teléfono no válido. Debe ser numérico y tener un máximo de 11 dígitos." + RESET);
                        }
                        break;
                    case 2:
                        System.out.println(VERDE + "Inserta el nombre del contacto que deseas buscar." + RESET);
                        String nombreBusqueda = scanner.nextLine(); // Leer el nombre del contacto a buscar
                        // Lógica para buscar el contacto en la agenda
                        if(agenda.containsKey(nombreBusqueda)){
                            System.out.println(VERDE + "Contacto encontrado: " + nombreBusqueda + " - " + agenda.get(nombreBusqueda) + RESET);
                        } else {
                            System.out.println(AMARILLO + "Contacto no encontrado." + RESET);
                        }
                        break;
                    case 3:
                        System.out.println(VERDE + "Inserta el nombre del contacto que deseas actualizar." + RESET);
                        String nombreActualizacion = scanner.nextLine(); // Leer el nombre del contacto a actualizar
                        if(agenda.containsKey(nombreActualizacion)){
                            System.out.println(VERDE + "Inserta el nuevo número de teléfono." + RESET);
                            String nuevoTelefono = scanner.nextLine(); // Leer el nuevo número de teléfono
                            agenda.put(nombreActualizacion, nuevoTelefono); // Actualizar el contacto en la agenda
                            System.out.println(VERDE + "Contacto actualizado: " + nombreActualizacion + " - " + nuevoTelefono + RESET);
                        } else {
                            System.out.println(AMARILLO + "Contacto no encontrado." + RESET);
                        }
                        break;
                    case 4:
                        System.out.println(VERDE + "Inserta el nombre del contacto que deseas eliminar." + RESET);
                        String nombreEliminar = scanner.nextLine(); // Leer el nombre del contacto a eliminar
                        if(agenda.containsKey(nombreEliminar)){
                            agenda.remove(nombreEliminar); // Eliminar el contacto de la agenda
                            System.out.println(VERDE + "Contacto eliminado: " + nombreEliminar + RESET);   
                        } else {
                            System.out.println(AMARILLO + "Contacto no encontrado." + RESET);
                        }
                        break;
                    case 5:
                        System.out.println(VERDE + "Mostrando todos los contactos:" + RESET);
                        agenda.entrySet().stream()
                        .forEach(contacto -> System.out.println(">" + contacto.getKey() + ": "+
                            CYAN + contacto.getValue() + RESET
                        ));
                        break;
                    case 6:
                        // Lógica para salir del programa
                        System.out.println(VERDE + "¡Gracias por usar la agenda de contactos!" + RESET);
                        break;
                    default:
                        System.out.println(AMARILLO + "Opción no válida. Por favor, selecciona una opción del menú." + RESET);
                }

                //Cerrar el scanner al finalizar el programa
                
            }while(opcion != 6);
            scanner.close();
      
        
      
        }
          public static void mostrarMenu() {
            // Borde superior en verde claro
            System.out.println(VERDE_CLARO + "╔════════════════════════════╗" + RESET);
            
            // Título en amarillo
            System.out.println(AMARILLO + "║    AGENDA DE CONTACTOS     ║" + RESET);
            
            // Línea divisoria en verde claro
            System.out.println(VERDE_CLARO + "╠════════════════════════════╣" + RESET);
            
            // Opciones en verde normal
            System.out.println(VERDE + "║ 1. Insertar contacto       ║" + RESET);
            System.out.println(VERDE + "║ 2. Buscar contacto         ║" + RESET);
            System.out.println(VERDE + "║ 3. Actualizar contacto     ║" + RESET);
            System.out.println(VERDE + "║ 4. Eliminar contacto       ║" + RESET);
            System.out.println(VERDE + "║ 5. Mostrar todos           ║" + RESET);
            
            // Opción salir en color diferente
            System.out.println(CYAN + "║ 6. Salir                   ║" + RESET);
            
            // Borde inferior en verde claro
            System.out.println(VERDE_CLARO + "╚════════════════════════════╝" + RESET);
            
            // Prompt en verde
            System.out.print(VERDE + "Selecciona una opción: " + RESET);
        }
      

}

         
 

        

