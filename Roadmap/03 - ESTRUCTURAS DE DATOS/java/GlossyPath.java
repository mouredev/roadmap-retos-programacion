/**
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * @version v1.0
 * 
 * @since 20/06/2024
 * 
 * @author GlossyPath
 * 
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.InputMismatchException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;
 
public class GlossyPath {

    /*
     * Arrays (también conocidos como vectores).
     * Tenemos dos tipos de Arrays: los estáticos y los dinámicos.
     * Los estáticos son aquellos Arrays en los que en su definición se especifica el número de elementos máximo que podrá almacenar la estructura de datos.
     * A diferencia de los anteriores los dinámicos son aquellos Arrays en los que no se especifica un número máximo de elementos y es la máquina virtual de Java,
     * quien se encarga por nosotros de gestionar la memoria de forma transparente.
     * En ambos podemos utilizar tipos de datos primitivos como objetos.
     */

     /*
      * Descripción: método para implementar las diferentes operaciones con Arrays estáticos.
      */
     public static void vectorStatic(){

        char[] hola = {'h', 'o', 'l', 'a'}; //definimos los caracteres de los que esta compuesto el Array.
        String[] isbn = new String[5]; // definimos el tamaño del Array (mediante la instanciación se reserva la memoria para poder almacenar los elementos deseados).

        //Inserción
            //Para insertar datos se hace de la siguiente manera.
            //Los elementos en los Arrays tienen asociado un índice. Estos comienzan desde 0.
            //Por lo tanto para insertar un elemento solamente tendremos que indicar su indice y el valor a introducir.
            //Siempre se hace de la misma forma: nombreDelArray[indice] = valor;

        isbn[0] = "933-3-16-121410-0";
        isbn[1] = "238-8-16-248110-2";
        isbn[2] = "178-9-16-123410-0";
        isbn[3] = "978-3-16-148410-3";
        isbn[4] = "111-1-16-956789-0";

        //Actualización
            //Para actualizar los datos se hace de la siguiente manera.
            //De la misma manera que se hace con la inserción, debemos acceder al indice del elemento que queremos actualizar o modificar.
            //Siempre se hace de la misma forma: nombreDelArray[indice] = nuevoValor;

        System.out.println("Valor actual del Array con indice 0 es: " + isbn[0]);

        isbn[0] = "999-3-99-999999-0";
        
        System.out.println("Nuevo valor del Array con indice 0 es: " + isbn[0]);

        //Borrado
            //En los Arrays estáticos no podemos variar su tamaño como tal una vez ha sido creado.
            //Lo que si podemos hacer es reemplazar el valor del elemento con un valor predeterminado (como null para referencias de objetos, 0 para enteros, false para booleanos, etc.).
            //De esta manera eliminamos el valor original.

        hola[0] = '\u0000'; //En los tipo char, de esta manera, el valor del elemento se establece en el carácter nulo.

        //Ordenación.
            //Para odenar los Arrays podemos utilizar la clase "Arrays" y uno de sus metodos, en concreto el método sort().
            //Devemos importar la clase Arrays (import java.util.Arrays;).
        
        System.out.println("Array isbn sin ordenar sería como sigue:");

        for(int i= 0; i<isbn.length; i++){
            System.out.println(isbn[i]);
        }
        System.out.println();

        System.out.println("Ahora el Array isbn ordenado:");

        Arrays.sort(isbn); //Ordenamos el Array con el método sort

        for(int i= 0; i<isbn.length; i++){
            System.out.println(isbn[i]);
        }
     }



     /*
      * En JAVA como en otros lenguajes de programación también tenemos los Arrays multidimensionales (tablas o matrices), que son
      * estructuras de datos que permiten almacenar elementos en un formato de filas y columnas, similar a una tabla. 
      * Cada elemento en un array multidimensional se accede usando dos índices: el índice de la fila y el índice de la columna.
      * Su declaración sería como sigue: tipoDeDato[][] nombreDelArray = new tipoDeDato[tamañoArray/filas][tamañoArray/columnas];
      */

     /*
      * Descripcion: método para implementar las diferentes operaciones con Arrays multidimensionales.
      */
      public static void arrayMultidimensional(){

        //A la hora de declarar el Array se hace de la misma manera que con los estáticos.
        int[][] matriz = {
            {4, 2, 93},
            {41, 25, 6},
            {72, 8, 19}
        };

        char[][] sopaLetras = new char[5][5];

        //Inserción, actualizacíon, borrado.
            //Sigue la misma pauta que los Arrays estáticos, lo único que tenemos que tener en cuenta es la posición del segundo índice.


        //Ordenación
            //El método sort() de la clase Arrays no tiene soporte para los multidimensionales.
            //En el caso de que sepamos como queremos ordenar cada filo o columna si que podriamos ordenarlas individualemnte.

        System.out.println("\nMostramos la matriz actual:");

        for(int i=0; i<matriz.length; i++){
            for(int j=0; j<matriz[i].length; j++){
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println("\nAhora la matriz ordenada:");

        for(int i=0; i<matriz.length; i++){
            Arrays.sort(matriz[i]); //en este caso ordenamos solo las filas.
        }

        for(int i=0; i<matriz.length; i++){
            for(int j=0; j<matriz[i].length; j++){
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
      }


      /*
       * Ahora pasemos a los Arrays dinámicos.
       * Su principal ventaja es que se basan en memoria dinámica, podemos almacenar tantos elementos como queramos de los mismos.
       * Los arrays dinámicos se implementan principalmente mediante la interfaz List y sus diversas implementaciones.
       * Podemos almacenar cualquier tipo de Objeto pero es importante destacar que no se pueden almacenar tipos de datos primitivos.
       */
     

     /*
      * Descripción: método para implementar las diferentes operaciones con ArrayList.
      */
     public static void arrayList(){

        //Los ArrayList tienen la siguiente estructura: ArrayList<String> miArrayList = new ArrayList<String>();

        ArrayList <String> nombres = new ArrayList<>();

        //Inserción
            //Para insertar elementos utilizamos el método 'add'.
        
        nombres.add("Juan");
        nombres.add("Laura");

        //Borrado
            //Para eliminar objetos del ArrayList tenemos que escribir la posición del elemento que queremos borrar.
            //Utilizaremos el método 'remove'.
        
        nombres.remove(0);

        nombres.clear();//vaciamos el ArrayList
        
        //Actualización
            //Para actualizar objetos, insertaremos dos argumentos al metodo 'set' que serán el indice y el nuevo valor.

        nombres.add("Juan");
        nombres.set(0, "Pedro");

        //Ordenación
            //Para ordenar objetos podriamos implementar la interfaz Comparable<T> en la clase que queramos comparar y en la misma implementar el método
            //compareTo y ya en el main realizar la comparación con la clase Collections y su método sort().
     }

     /*
      * Descripción: método para implemetar las diferentes operaciones con la clase Stack (pila).
      */
     public static void listaStack(){

        //La clase Stact (conocido como pila) tiene la siguiente estructura: Stack(TipoDato) miStack = new Stack<tipoDato>();
        //El comportamiento de la pila se conoce como LIFO (Last In, First Out), es decir, 
        //el último elemento que se añade será el primero en eliminarse/consultarse. 

        Stack <String> nombres = new Stack<String>();

        //Inserción
            //Para insertar elementos utilizamos el método 'push()'.

        nombres.push("Paco"); 
        nombres.push("Alexia"); //vamos apilando uno encima de otro

        //Borrado
            //Para eliminar objetos utilizamos el método pop(), el cual elimina el elemento que esta en la cima de la pila
        
        nombres.pop(); // Alexia sería eliminado.

        //Actualización
            //En la clase Stack no disponemos de ningún método para actulizar un objeto mediante su indice.
        
     }

     /*
      * Descripción: método para implementar las diferentes operaciones con la interfaz Queue y la clase LinkdList.
      */
      public static void listaQueue(){

        //La clase LinkedList la utilzamos en conjunto con la interfaz Queue para implementar las colas.
        //Su estructura es la siguiente: Queue<tipoDato> miQueue = new LinkedList<tipoDato>();
        //El comportamiento de la cola se conoce como FIFO (First in, First Out), es decir, 
        //el primer elemento que se añade será el primero en eliminarse/consultarse. 

        Queue<String> personas = new LinkedList<String>();

        //Inserción
            //Para insertar elementos utilizamos el método 'add'.

        personas.add("Clara");
        personas.add("Lucas");
        personas.add("Jose");


        //Borrado
            //Para eliminar objetos utilizamos el método remove(), el cual elimina el primer elemento que llegó a la cola.

        personas.remove();

        System.out.println();

        while(!personas.isEmpty()){
            System.out.println("Nombre: " + personas.poll()); //también podemos utilizar el método poll() para eliminar la cabeza de la cola.
        }

        //Actualización
            //En las colas en concreto con la interfaz Queue no disponemos de ningún método para actulizar un objeto mediante su indice.
      }

      /*
       * En JAVA también disponemos de los conjuntos. Matemáticamente un conjunto es una colección no ordenada de elementos no repetidos. 
       * Por una parte, es no ordenada porque no podemos acceder a los elementos a través de un índice. 
       * Y por otra, no repetidos porque cada elemento del conjunto es único.
       */

       /*
        * Descripción: método para implementar las diferentes operaciones con la clase HashSet.
        */
        public static void conjuntoHashSet(){

            //La clase HashSet la utilzamos para implementar los conjuntos.
            //Su estructura es la siguiente: HashSet<tipoDato> miHashSet = new HashSet<tipoDato>();

            HashSet<String> direcciones = new HashSet<String>();

            //Inserción
                //Para insertar elementos utilizamos el método 'add'.

                direcciones.add("calle macarron");
                direcciones.add("calle santón");
            
            //Borrado
                //Para eliminar objetos utilizamos el método remove(), el cual elimina el objeto que le digamos (si existe).
            
            direcciones.remove("calle macarron");
            direcciones.clear();//elimina todos los elementos del conjunto.

        }

/*
 * DIFICULTAD EXTRA (opcional):
 * - Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
*/

/* 
 * Para la dificultad extra vamos a utilizar los diccionarios.
 * Los Diccionarios, al igual que las listas, los datos están indexados. 
 * Sin embargo, sus índices (claves) pueden ser cualquier tipo de valor. 
 * Por tanto, a los Diccionarios se les conoce como dato dinámico de tipo CLAVE-VALOR.
 */


 /*
  * Descripción: enum para escoger opción del menu de selección.
  */
    public enum AccionesMenu{

        B("Buscar contacto"),
        I("Insertar contacto"),
        A("Actualizar contacto"),
        E("Elimina contacto"),
        L("Listar contactos"),
        C("Contar"),
        S("Salir del menú");

        private final String valor;

        private AccionesMenu(String valor){

            this.valor = valor;
        }

        public String getValor(){

            return this.valor;
        }
    }

    /*
     * Descripción: método para imprimir el menu
     */
    private static void imprimirMenu(){

        Arrays.stream(AccionesMenu.values()).forEach(item ->System.out.println(String.format("(%s)%s", item.name(), item.getValor().substring(1))));
        System.out.print("Seleccione la inicial de la operación que quieres realizar: ");
    }

    /*
     * Descripción: metodo para insertar contactos
     */
    public static void insertarContacto(HashMap<String, Integer> contactos){

        Scanner sc = new Scanner(System.in);

        String nombre;
        boolean nombreNulo;
        
        Integer numTelefono = 0;

        try{

        do{

            System.out.println("\nIntroduce en nombre del contacto que quieres añadir: ");
            nombre = sc.nextLine().toUpperCase();
            nombreNulo = (nombre.isEmpty() || nombre.isBlank());
            
        } while(nombreNulo);
        

        do{

            try{

                System.out.println("\nIntroduce el telefono del conctato que quieres añadir (tiene que tener 9 dígitos): ");
                numTelefono = Integer.parseInt(sc.nextLine());

            } catch(NumberFormatException e){
                System.out.println("Error: Ingresa solo números para el teléfono y asegúrate de que tenga 9 dígitos.");
            }
    
        } while(numTelefono.toString().length() != 9);
        

        contactos.put(nombre, numTelefono); // utilizamos el método put() para añadir los elementos.
        System.out.println("Contacto añadido correctamente.");

        } catch (InputMismatchException e){
            System.out.println("Datos introducidos incorrectos");
            e.printStackTrace();
        } 
    }

    /*
     * Descripción: método para buscar contactos.
     */
    public static void buscarContacto(HashMap<String, Integer> contactos){

        Scanner sc = new Scanner(System.in);

        String nombre;

        if(contactos != null && !(contactos.isEmpty())){

            System.out.println("\nIntroduce el nombre del contacto que quieres buscar");
            nombre = sc.nextLine();

            for(String s: contactos.keySet()){ // devuelve la clave de nuestro HashMap.
                Integer telefono = contactos.get(s); // devuelve el valor de nuestro HashMap.
                if(s.equals(nombre.toUpperCase())){
                    System.out.println("Nombre: " + s + " " + "Telefono: " + telefono);
                } else {
                    System.out.println("El contacto no esta en la lista");
                }
            }

        } else {
            System.out.println("Lista no existe o esta vacia");
        } 

    }
    /*
     * Descripciópn: método para actulizar contactos.
     */
    public static void actualizarContacto(HashMap<String, Integer> contactos){

        Scanner sc = new Scanner(System.in);

        String nombre;

        Integer nuevoTelefono;

        if(contactos != null && !(contactos.isEmpty())){

            System.out.println("\nIntroduce el nombre del contacto que quieres actualizar: ");
            nombre = sc.nextLine().toUpperCase();

            if(contactos.containsKey(nombre)){

                Integer telefono = contactos.get(nombre);
                System.out.println("Nombre: " + nombre + " Teléfono: " + telefono);
                System.out.println("\nIntroduce el nuevo teléfono:");

                try {
                    nuevoTelefono = Integer.parseInt(sc.nextLine());

                    if (nuevoTelefono.toString().length() != 9) {
                        System.out.println("El número de teléfono debe tener 9 dígitos.");
                    } else {
                        contactos.put(nombre, nuevoTelefono);
                        System.out.println("El contacto ha sido actualizado.");
                    }
                    
                } catch (NumberFormatException e) {
                    System.out.println("Entrada no válida. Por favor, introduce un número de teléfono válido.");
                }

            } else {
                System.out.println("El contacto no está en la lista.");
            }

        } else {
            System.out.println("La lista no existe o está vacía.");
        }
    }
    
    /*
     * Descripción: método para eliminar un contacto
     */
    public static void eliminarContacto(HashMap<String, Integer> contactos){

        Scanner sc = new Scanner(System.in);

        String nombre;

        if(!contactos.isEmpty()){

            try{

                System.out.println("\nIntroduce el nombre del contacto que quieres eliminar: ");
                nombre = sc.nextLine().toUpperCase();

                if(contactos.containsKey(nombre)) {
                    contactos.remove(nombre);
                    System.out.println("Contacto eliminado.");

                } else {
                    System.out.println("El contacto no está en la lista.");
                }

            } catch(InputMismatchException e){
                System.out.println("Datos introducidos incorrectos, debes introducir un nombre valido.");
            }
            

        } else {
            System.out.println("La lista no existe o está vacía.");
        }
    }

    /*
     * Descripción: método para mostrar todos los contactos por terminal
     */
    public static void listarContactos(HashMap<String, Integer> contactos){

        if(!contactos.isEmpty()){
            for(String s: contactos.keySet()){
                Integer numTelefono = contactos.get(s);
                System.out.println("\nNOMBRE: " + s + " TELÉFONO: " + numTelefono);
            }
        } else {
            System.out.println("La lista no existe o está vacía.");
        }
    }

    public static void contarContactos(HashMap<String, Integer> contactos){

        int cantidadContactos = 0;

        cantidadContactos = contactos.size();

        System.out.println("La agenda tiene " + cantidadContactos + " contactos.");
    }
    /*
     * Descripción: meétodo main
     */
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        HashMap<String, Integer> contactos = new HashMap<>();
        AccionesMenu accionesMenu = null;
        String opcion;

        do{
            System.out.println("\n---------MENU--------");
            imprimirMenu();
            opcion = sc.nextLine(); //capturamos la entrada del usuario y lo guardamos en una variable.

            try{

                accionesMenu = AccionesMenu.valueOf(opcion.toUpperCase());

                switch(accionesMenu){

                    case B:
                        buscarContacto(contactos);
                        break;

                    case I:
                        insertarContacto(contactos);
                        break;
                    
                    case A:
                        actualizarContacto(contactos);
                        break;
                    
                    case E:
                        eliminarContacto(contactos);
                        break;
                    
                    case L:
                        listarContactos(contactos);
                        break;
                
                    case C:
                        contarContactos(contactos);
                        break;
                    
                    case S:
                        System.out.println("Salir del menú");
                        break;
                }
            } catch (IllegalArgumentException e){
                System.out.println("Error al introducir la inicial de la operación a realizar"); //aseguramos que el argumento pasado sea alguna constante del Enum.
                e.printStackTrace();
            }

        }
        while(accionesMenu != null && accionesMenu != AccionesMenu.S);

        sc.close();

     }
}
 