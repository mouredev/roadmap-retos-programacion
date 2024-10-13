import java.util.*;

public class LucasAG01 {

    /*
    Estructuras de datos son elemntos fundamentales en la programacion que permiten organizar y almacenar datos de una forma eficiente.

    Actuan como cimiento para construir aplicaciones y algoritmos

    Hay que elegir la estructura adecuada de datos, ya que entran aquí puntos esenciales como La optimización del rendimeinto, La organización en si, La reutilización del código,
    y facilitar ka resolucion de problemas

     */

    public static void main(String[] args) {

    /*
    ARRAYS :
    Son colecciones de elemntos del mismo tipo, accesibles a traves de un inidice, Son estáticos, lo que significa que no podemos cambiar su tamaño después de crearlos
     */
        int[] arreglo = new int[5]; //creamos un array de 10 valores de tipo int
        int[][] arreglo2 = new int[5][5]; //bidimensional


        arreglo[0] = 1; //Selecciono la posicion, y lo que le añado
        arreglo[1] = 2;
        arreglo[2] = 3;
        arreglo[3] = 4;
        arreglo[4] = 5;

        //Otra forma tambín puede ser int[] arreglo = {1,2,3,4,5};
        //Recorramos el array para printarlo
        for (int num : arreglo) {
            System.out.println(num);
        }

    /*
    ARRAYLIST
        Esta coleccion es de tipo dinámica, es decir, despues de creada la podemos ir modificando en funcion de nuestras necesidades, aparte tienen metodos incorporados para
        modificarlas
     */

        ArrayList<String> nombres = new ArrayList<>();

        nombres.add("Lucas");
        nombres.add("Ana");
        nombres.add("Pedro");
        System.out.println(nombres); //se imprime la lista
        //para acceder a los metodos se pone nombre. y aparecera muchas cosas


    /*
    LINKEDLIST
        Es una lista enlazada que permite inserciones y eliminaciones efeicientes Ideal cuando se necesita acceder y manipular elementos en ambas direcciones
    */

        LinkedList<String> nombres2 = new LinkedList<>();
        nombres2.add("Ana");
        nombres2.add("Pedro");
        nombres2.add("Lucas");
        System.out.println(nombres2);

    /*
    HASHMAP
        Esta estructura, alamcena pares clave-valor
         veremos ejemplo complejos para lañdir mas cosas y los ordena por orden alfabetico en este caso
     */
        HashMap<String, Integer> edades = new HashMap<>();
        edades.put("Pedro", 23);
        edades.put("Ana", 33);
        edades.put("Lucas", 22);
        System.out.println(edades); //todo
        System.out.println(edades.get("Pedro")); //solo pedro
        for (String key : edades.keySet()) {
            System.out.println(key + " -> " + edades.get(key));
        }


    /*
    HASHSET
        Es una colección que almacena elemtos únicos sin mantener ningún order específico. Ideal para evitar duplicados
    */
        HashSet<String> nombresSet = new HashSet<>();
        nombresSet.add("Pedro");
        nombresSet.add("Ana");
        nombresSet.add("Lucas");
        nombresSet.add("Lucas");
        System.out.println(nombresSet); //Cuando lo imprima, solo habrá 1 Lucas, el IDE ya me avisa de ello

    /*
    TREESET
        Implementacion del Set que alamcena elementos de forma ordenada (por defecto en orden natural)
     */

        TreeSet<String> nombresTreeSet = new TreeSet<>(); //El parectesis que hay al lado del new, podemos poner el nombre de otra lista creada y así no escribir mas
        nombresTreeSet.add("Pedro");
        nombresTreeSet.add("Ana");
        nombresTreeSet.add("Lucas");
        System.out.println(nombresTreeSet); //[Ana, Lucas, Pedro]

    /*
    QUEUE (LinkedList)
         Queue es una estructura FIFO (First In, First Out). LinkedList se puede usar para implementar una cola.
     */
        Queue<String> cola = new LinkedList<>();
        cola.add("Lucas");
        cola.add("Pedro");
        cola.add("Ana");
        System.out.println(cola.poll());// Imprimimos y removemos el primer elemento en la cola, en este caso, saldrá por pantalla Lucas, pero al volver a ejecutar el cola.poll() , aparecera Pedro


    /*
    PRIORITYQUEUE
            Ordena los elementos de forma natural o por un comparador proporcionado
     */

        PriorityQueue<Integer> colaPrioridad = new PriorityQueue<>();

        colaPrioridad.add(23);
        colaPrioridad.add(33);
        colaPrioridad.add(22);
        System.out.println(colaPrioridad.poll()); //Imprimimos y removemos el elemento con la mayor prioridad Si son sumeros del pequeño al grande

    /*
    STACK
        Estructura LIFO (last in m First out)
     */
        Stack<String> pila = new Stack<>();

        pila.push("Lucas");
        pila.push("Pedro");
        pila.push("Ana");

        System.out.println(pila.pop()); //Imprimimos y removemos el último elemento agregado (LIFO)


    /*
    DEQUE (ArrayDeque)
        Cola de doble extremo que permite agregar y eliminar elemntos de ambos extremos
     */
        ArrayDeque<String> deque = new ArrayDeque<>();

        deque.addFirst("Pimero");
        deque.addLast("Ultimo");
        deque.push("Lucas"); //equivalente a addLast

        System.out.println(deque.pollFirst());
        System.out.println(deque.pollLast());
        System.out.println(deque);


    /*
     HASHTABLE
        Similar a HashMap, pero es sincronizado y no permite claves ni valores nulos
     */
        Hashtable<String, Integer> hash = new Hashtable<>();

        hash.put("Pedro", 23);
        hash.put("Ana", 33);
        hash.put("Lucas", 22);
        System.out.println(hash);


    /*
    LINKEDHASHMAP
        Mantiene el orden de insercion de elmentos no los ordena como el HashMap
     */
        LinkedHashMap<String, Integer> linkedHashMap = new LinkedHashMap<>();
        linkedHashMap.put("Pedro", 23);
        linkedHashMap.put("Ana", 33);
        linkedHashMap.put("Lucas", 22);
        System.out.println(linkedHashMap);


    /*
    TREEMAP
        Mapa ordenado que ordena las claves de forma natural o con comparador no claves nulas.
        En el HashMap, los elementos no están en ningún orden específico, mientras que en el TreeMap,
        los elementos están ordenados alfabéticamente por las claves.

    */
        TreeMap<String, Integer> mapaOrdenadoPorClave = new TreeMap<>(); // Creamos un TreeMap

        mapaOrdenadoPorClave.put("Pedro", 25);
        mapaOrdenadoPorClave.put("Ana", 30);
        mapaOrdenadoPorClave.put("Lucas", 22);
        System.out.println(mapaOrdenadoPorClave); // Imprimimos todo el TreeMap
        for (String key : mapaOrdenadoPorClave.keySet()) {
            System.out.println(key + " -> " + mapaOrdenadoPorClave.get(key));
        }




        //Agengfa del ejercicio

        HashMap<String,Integer> agenda = new HashMap<>();

        // Primero sacamos el scanner Peticion
        Scanner scanner = new Scanner(System.in);

        int opiconElexida=0;


        //Hay que hacer un bucle con los case y dentro de cada case la opcion

        while (opiconElexida!=6) {

            System.out.println("""
                     /*/*/*/*/ AGENDA TELEFÓNICA /*/*/*/
                     
                     1.Buscar contacto
                     2.Añadir contacto
                     3.Modificar contacto
                     4.Borrar contacto
                     5.Ver todos
                     6.Salir
                         
                    """);

            opiconElexida = scanner.nextInt();
            switch (opiconElexida) {
                case 1:
                    BuscarContaco(agenda);
                    break;
                case 2:
                    AgregarContacto(agenda,scanner);
                    break;
                case 3:
                    ModificarContacto(agenda,scanner);
                    break;
                case 4:
                    BorrarContacto(agenda,scanner);
                    break;
                case 5:
                    verContactos(agenda);
                    break;
                case 6:
                    System.out.println("No tengo ni puta idea de como voy a aprender esto xddd");
                    break;




            }


        }

    }

    //LA FORMA MAS SENCIALLA DE HACER EL MENU ES CREANO FUERA LOS MÉTODOS

    //En los métodos que te he mostrado, se usan agenda y scanner como parámetros porque estos son necesarios para que los métodos funcionen correctamente.
    //Scanner scanner sale del scanner del menu. sirve para utilizar ese scanner y que vaya mejor el programa.

    /*
    Cosas Importanmtes aprendidas:
    -En el sout, poniendo """ puedo hacer lo que quiera de forma más cómoda a la hora de crear menús.
    -Dependiendo de lo que pidan hay que revisar que tipo de estructura te viene mejor.
    - Es importante respetar el orden de KEY, VALUE
    -metodos de containskey, contains value
    -metodo de String.valueOf(telefonoContacto) sirve para converttir un int en un String
    -cuando una opcion requiere que le usuario ponga algo de nuevo si se equivoca, es importante hacer un while en vez de un IF
    -el bucle de imprimir maps for (Map.Entry<String, Integer> entry : agenda.entrySet())

    -Para crear una función, hay que ir desglosandolo poco a poco, un analisis de un problema, para tatra de encontrar la solución adecuada
    por ejemplo, tenemos qué queremos que sea le resultado basico ej: porner nombre y poner numero
    ahora podemos crear los criterios como por ejemplo si el numero es x digitois de largo, ahí sabemos que la forma mas facil de contar los caracteres es en un String y existe
    el método de convertir el int a String

    -Es importante saber que la reutilizacion es usando los pasos de atrás vamos hacia delante. PERO hay que crear una función apropiada para reutilizar, en el caso de la linea 336.
    -Se puede complicar de una manera LOCA





     */

    public static void BuscarContaco(Map<String, Integer> agenda) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Introduce el nombre del contacto: ");
        String nombre = scanner.nextLine();

        if (agenda.containsKey(nombre)) {
            System.out.println(nombre +":"+ agenda.get(nombre)+ "\n");
        }else {
            System.out.println("El contacto no existe"+ nombre +"\n");
        }

    }

    public static void AgregarContacto(Map<String, Integer> agenda, Scanner scanner) {
        System.out.println("Introduce el nombre del contacto: ");
        String nombreContacto = scanner.nextLine();

        System.out.println("Introduce el telefono RECUERDA QUER SON 9 CIFRAS");
        int telefonoContacto = scanner.nextInt();


        while (String.valueOf(telefonoContacto).length()==9 || agenda.containsValue(telefonoContacto)){

            if(String.valueOf(telefonoContacto).length()!=9){
                System.out.println("9 CIFRAS");
                telefonoContacto = scanner.nextInt();
            } else if (agenda.containsValue(telefonoContacto)) {
                System.out.println("Error el número"+telefonoContacto+" ya existe en la agenda");
                telefonoContacto= scanner.nextInt();
            }

            agenda.put (nombreContacto,telefonoContacto);

            System.out.println("El nombre "+nombreContacto+ " de numero "+telefonoContacto+ " se ha gregado.\n");


        }


    }

    public static void ModificarContacto (Map<String,Integer>agenda, Scanner scanner){
        System.out.println("Introduce el nombre del contacto a MODIFICAR");
        String nombreMod = scanner.nextLine();


        if(!agenda.containsKey(nombreMod)){
            System.out.println("Contacto no encontrado... dale otro try");
            ModificarContacto(agenda,scanner);

        }else {
            //No hay forma de usar el metodo replace.
            agenda.remove(nombreMod);

            //AgregarContacto(agenda,scanner); si reutilizase de buena manera el codigo si no lo modifico, haria esto y lo de abajo me lo ahorro.
            //copiamos EL bloque de añadir contacto.
            System.out.println("Introduce el nombre del contacto: ");
            String nombreContacto = scanner.nextLine();

            System.out.println("Introduce el telefono RECUERDA QUER SON 9 CIFRAS");
            int telefonoContacto = scanner.nextInt();


            while (String.valueOf(telefonoContacto).length()==9 || agenda.containsValue(telefonoContacto)){

                if(String.valueOf(telefonoContacto).length()!=9){
                    System.out.println("9 CIFRAS");
                    telefonoContacto = scanner.nextInt();
                } else if (agenda.containsValue(telefonoContacto)) {
                    System.out.println("Error el número"+telefonoContacto+" ya existe en la agenda");
                    telefonoContacto= scanner.nextInt();
                }

                agenda.put (nombreContacto,telefonoContacto);

                System.out.println("El nombre "+nombreContacto+ " de numero "+telefonoContacto+ " se ha MODIFICADO.\n");

            }
        }
    }

    public static void BorrarContacto (Map<String,Integer>agenda, Scanner scanner){
        System.out.println("Introduzca el numero del contacto a eliminar");
        String numeroContacto = scanner.nextLine();

        if (agenda.containsKey(numeroContacto)) {
        String nombre= null;

        for(Map.Entry<String ,Integer> entry : agenda.entrySet()){
            if(entry.getKey().equals(numeroContacto)){
                nombre= entry.getValue().toString();
            }
            break;
        }
        agenda.remove(numeroContacto);

            System.out.println("Contacto "+nombre+ " con número "+numeroContacto+ " se ha eliminado.\n");

        }else{
            System.out.println("Numenro ingresado no existe.\n ");
        }
    }

    public static void verContactos (Map<String,Integer>agenda){
        for (Map.Entry<String, Integer> entry : agenda.entrySet()) {
            System.out.println("Nombre: " + entry.getValue() + ", Número: " + entry.getKey());
        }

    }









































}
