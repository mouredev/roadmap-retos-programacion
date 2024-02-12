/**
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * @version v1
 * 
 * @since 27/01/2024
 * 
 * @author Blas Barragán
 * 
 */

 import java.util.ArrayList;
 import java.util.LinkedList;
 import java.util.Scanner;
 import java.util.HashMap;
 import java.util.HashSet;
 
 public class BlasBarragan {
 
 // VARIABLES GLOBALES PARA DIFICULTAD EXTRA
 static Scanner sc = new Scanner(System.in);
     // HashMap para almacenar contactos
 private static HashMap<String, Integer> AgendaContactos = new HashMap<String, Integer>();
 
 /**
  * Arrays (vectores).
  * Almacenan de manera estructurada un conjunto de valores del mismo tipo de dato (entero, caracter, objeto, etc..)
  */ 
 
     /**
      * Array estatico (tiene un tamaño fijo)
      * Lo declaramos de la siguiente forma:
      * tipoDeDato[] nombreArray = new tipoDeDato[tamañoArray];
      */ 
     public static void ArrayEstatico() {
         // Declaramos Array
         int[] notas = new int[4];
 
         // Inserción
             // Insertamos datos de la siguiente forma:
             // nombreArray[indiceDelDatoInsertado] = valorDato;
             // Los indices del array siempre empiezan en 0, por lo que seguiran el patron:
             // indice: 0 posicion:1, indice:1 posicion:2, indice:2 posicion:3, etc...
             // y asi como posiciones (tamaño total) tenga el array.
             notas[0] = 6;
             notas[1] = 3;
             notas[2] = 10;
             notas[3] = 8;
 
             // Si conocemos los datos del array con antelacion, tambien podriamos insertar diectamente esos datos en su declaracion.
             String[] alumnos = {"Blas", "Marcos"}; 
         
         // Actualización 
             // Para actualizar datos, simplemente llamaos al array con el indice deseado e igualamos al nuevo valor.
             System.out.println("Valor posición 1 del array: " + notas[0]);
             notas[0] = 5; 
             System.out.println("Valor posición 1 del array actualizada: " + notas[0]);
 
         // Borrado 
             // Como los arrays tienen un tamaño estatico, el borrado de datos no se puede realizar como tal.
             // Podriamos declarar el tamaño del array con una variable y con esto cambiar el tamaño del array pero no eliminar un dato en una posicion concreta.
             int tamanoArray = 5;
             int[] array = new int[tamanoArray];
             System.out.println("Tamaño array: " + array.length);
             tamanoArray = 10;
             System.out.println("Nuevo tamaño array: " + array.length);
 
         // Ordenación
             // La ordenacion de los Array viene dada por sus indices de 0 a N-1.
             // Siendo N el tamaño del array. 
         
         // ## Si importamos en nuestro programa la clase Array (import java.util.Arrays;) 
         // podremos utilizar diferentes metodos extra de manipulacion de arrays que nos ofrece dicha biblioteca. 
         // https://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html
     }
     
     /**
      * Array multidimensional (matrices/tablas)
      * Un array dentro de un array.
      * Nos permite almacenar y manejar elementos como si tuvieramos una tabla.
      * Lo declaramos de la siguiente forma:
      * tipoDeDato[][] nombreArray = new tipoDeDato[tamañoArray/filas][tamañoArray2/columnas];
      */
 
      public static void ArrayMultidimensional() {
         // Inserción
 
         int notasCurso[][] = new int [2][3];
         notasCurso[0][0] = 7;
         notasCurso[0][1] = 5;
         notasCurso[0][2] = 9;
         notasCurso[1][0] = 4;
         notasCurso[1][1] = 6;
         notasCurso[1][2] = 10;
 
         // Tambien podemos inicializarlo de la siguiente forma, añadiendo a su vez los datos.
         int[][] notasCurso2 = {
             {9,5,6},
             {8,8,10},
             {5,4,5},
             {3,4,2},
         };
 
         // Por lo demas, los arrays multidimensionales (matrices) se tratan igual que los array estaticos.
      }
 
 /**
  * ArrayList (Arrays con vitaminas).
  * import java.util.ArrayList;
  * Con esto, podremos crear y usar arrays con distintos metodos incluidos en Java que nos facilitaran trabajar con ellos.
  */ 
 
      public static void ArrayConVitaminas() {
         // Inicializacion
         ArrayList<String> coches = new ArrayList<String>();
 
         // Insercion
         coches.add("Hyundai");
         coches.add("Ford");
         coches.add("Fiat");
         System.out.println(coches);
 
         // Actualizacion
         coches.set(0, "Opel");
         coches.set(2, "Mazda");
         coches.set(1, "Audi");
 
         // Borrado
         coches.remove(2);
         coches.remove(1);
             // Para vaciar el array
         coches.clear();
      }
 
      // Existe una "Variante" de los ArrayList que se comporta igual pero trabaja en segundo plano de forma diferente.
      // Hablamos de las LinkedList que estan mas optimizadas para manipular datos al contrario que los Array que funcionan mejor para almacenarlos.
      // import java.util.LinkedList
      public static void ListaParaManipularDatos(){
         LinkedList<String> motos = new LinkedList<String>();
         motos.add("Honda");
         motos.add("Aprilia");
 
         // Tiene una serie de metodos utiles
         motos.addFirst("Kawasaki"); // Añade los datos en la primera posicion.
         motos.addLast("Triumph"); // Añade los datos en la ultima posicion.
         motos.removeFirst(); // Elimina el dato en primera posicion.
         motos.removeLast(); // Elimina el dato en ultima posicion.
         motos.getFirst(); // Devuelve el dato en primera posicion.
         motos.getLast(); // Devuelve el dato en ultima posicion.
      }
 
 /**
  * HashMap
  * import java.util.HashMap;
  * A difierencia de los arrays o las listas no se almacenan los datos ordenados. 
  * En su lugar, almacena parejas de datos en forma clave/valor para acceder a ellos.
  */
      public static void AlmacenClaveValor() {
         // Inicializacion
         // Podemos emparejar datos de distinto tipo
         HashMap<String, String> PueblosDeEspaña = new HashMap<String, String>();
 
         // Insercion
         // Para insertar datos lo haremos con nombreDelHashMap.put("clave",'valor');
         PueblosDeEspaña.put("Valencia","Alaquas");
         PueblosDeEspaña.put("Valencia", "L'eliana");
         PueblosDeEspaña.put("Alicante", "Elche");
         PueblosDeEspaña.put("Castellon", "Onda");
 
         // Borrado
         PueblosDeEspaña.remove("Valencia");
         PueblosDeEspaña.remove("Castellon");
             // Para vaciar 
         PueblosDeEspaña.clear();
      }
 
 /**
  * HashSet
  * import java.util.HashSet;
  * Coleccion de datos UNICOS. 
  */
      public static void DatosUnicos() {
         // Inicializacion
         HashSet<String> Marcas = new HashSet<String>();
 
         // Insercion
         Marcas.add("Logitech");
         Marcas.add("Asus");
         Marcas.add("Razer");
 
         // Borrado
         Marcas.remove("Asus");
             // Para vaciar 
         Marcas.clear();
      }
 
     public static void main(String[] args) {
         dificultadExtra();
     }
 
     /** DIFICULTAD EXTRA (opcional):
     * Crea una agenda de contactos por terminal.
     * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
     * - Cada contacto debe tener un nombre y un número de teléfono.
     * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
     *   los datos necesarios para llevarla a cabo.
     * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
     *   (o el número de dígitos que quieras)
     * - También se debe proponer una operación de finalización del programa.
     */
 
     public static void dificultadExtra() {
 
         int opcion = 0;
         do {
             System.out.println("##### Agenda #####");
             System.out.println("<---Menu agenda--->");
             System.out.println("1. Añadir contacto");
             System.out.println("2. Buscar contacto");
             System.out.println("3. Actualizar contacto");
             System.out.println("4. Eliminar contacto");
             System.out.println("5. Salir");
             System.out.println("Selecciona una opcion: ");
             opcion = sc.nextInt();
 
             switch (opcion) {
                 case 1:
                     // Añadir contacto
                     anadir();
                     break;
                 case 2:
                     // Buscar contacto
                     buscar();
                     break;
                 case 3:
                     // Actualizar contacto
                     actualizar();
                     break;
                 case 4:
                     // Eliminar contacto
                     eliminar();
                     break;
                 case 5:
                     // Salir
                     break;
                 default:
                     System.out.println("Opcion no valida");
             }
         } while (opcion !=5);
         System.out.println("< ==== Salir ==== >");
 
     }
 
     public static void anadir(){
         System.out.println("< ==== Añadir nuevo contacto ==== > \n");
         System.out.println("Nombre: ");
         String nuevoNombre = sc.next();
         System.out.println("Telefono: ");
         Integer nuevoTelefono = sc.nextInt();
         while (nuevoTelefono < 0 || nuevoTelefono > 999999999) {
             System.out.println("Error: El telefono debe ser numerico max. 9 digitos");
             System.out.println("\nTelefono: ");
             nuevoTelefono = sc.nextInt();
         }
         AgendaContactos.put(nuevoNombre,nuevoTelefono);
         System.out.println("Nuevo contacto añadido.");
     }
 
     public static void buscar(){
         System.out.println("< ==== Buscar contacto ==== > \n");
         System.out.println("Nombre: ");
         String nombre = sc.next();
         
         if (AgendaContactos.get(nombre) != null){
             System.out.println("Contacto: " + nombre);
             System.out.println("Telefono: " + AgendaContactos.get(nombre));
         } else {
             System.out.println("El contacto no existe");
         }
     }
 
     public static void actualizar(){
         System.out.println("< ==== Actualizar contacto ==== > \n");
         System.out.println("Nombre: ");
         String nombre = sc.next();
         
         if (AgendaContactos.get(nombre) != null){
             System.out.println("Nuevo numero de telefono: ");
             Integer actualizarTelefono = sc.nextInt();
         while (actualizarTelefono < 0 || actualizarTelefono > 999999999) {
             System.out.println("Error: El telefono debe ser numerico max. 9 digitos");
             System.out.println("\nNuevo numero de telefono:  ");
             actualizarTelefono = sc.nextInt();
         }
         AgendaContactos.put(nombre,actualizarTelefono);
         System.out.println("El contacto: " + nombre);
         System.out.println("Ha sido actualizado con el telefono: " + actualizarTelefono);
         } else {
             System.out.println("El contacto no existe");
         }
     }
     public static void eliminar(){
         System.out.println("< ==== Eliminar contacto ==== > \n");
         System.out.println("Nombre: ");
         String nombre = sc.next();
         
         if (AgendaContactos.get(nombre) != null){
             System.out.println("El contacto: " + nombre);
             System.out.println("Con telefono: " + AgendaContactos.get(nombre));
             AgendaContactos.remove(nombre);
             System.out.println("Ha sido eliminado");
             
         } else {
             System.out.println("El contacto no existe");
         }
     }
 
 }
 