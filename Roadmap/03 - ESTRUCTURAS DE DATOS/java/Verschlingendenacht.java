package source;

import java.util.*;

public class Verschlingendenacht {
    
    public static void main(String[] args){
        //arreglos();
        //arreglosBidimensionales();
        //arrayLists();
        //stacks();
        //queues();
        //linkedLists();
        //sets();
        //maps();
        extra();
    }

    public static void arreglos(){
        String[] colors = new String[5];

        colors[0] = "Green";
        colors[1] = "Yellow";
        colors[2] = "Purple";
        colors[3] = "Red";
        colors[4] = "Blue";

        System.out.println(Arrays.toString(colors));

        int[] numbers = {100, 200, 300};

        for(int i = 0; i < numbers.length; i++){
            System.out.println(numbers[i]);
        }

        for(int i = numbers.length-1; i >= 0; i--){
            System.out.println(numbers[i]);
        }

        for(int number : numbers){
            System.out.println(number);
        }

        Arrays.stream(numbers).forEach(System.out::println);
        //el doble :: nos permite referenciar una funcion o metodo sin llamarla dentro de otra funcion como foreach

        //La clase arrays contiene muchos metodos para lidiar con arreglos
        //Pero debemos recordar que los arreglos en Java no pueden cambiar su tamaño, por tanto no podemos realizar operaciones como eliminar realmente
        //Si queremos actualizar algun elemento de nuestro arreglo basta con usar el operador de asignacion a modo de actualizacion:
        colors[0] = "Pink";
        System.out.println(colors[0]);

        //Mientras que, si queremos eliminar un elemento, lo mejor sera asignarle un valor null

    }

    public static void arreglosBidimensionales(){

        char[][] board = new char[3][3];

        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                board[i][j] = '-';
            }
        }

        System.out.println(Arrays.deepToString(board)); //usamos deepToString ya que es un arreglo bidimensional

        char[][] board2 = {
                new char[] {'-','-','-'},
                new char[] {'-','-','-'},
                new char[] {'-','-','-'}
        };

        System.out.println(Arrays.deepToString(board2));

    }

    public static void arrayLists(){
        /*
        las listas son implentaciones de las colecciones (las listas son interfaces que al mismo tiempo implementan a las colecciones)
        la diferencia entre una coleccion y una lista es que la lista contiene mas informacion y metodos
         */

        //A pesar de que podemos hacer algo como esto como hariamos en Python:
        List colors = new ArrayList();
        colors.add("Blue");
        colors.add("Purple");
        colors.add(1);
        colors.add(true);
        colors.add(new Object());

        //O esto:

        ArrayList names = new ArrayList();
        names.add("Alejandro");
        names.add("Carlos");
        names.add("Oscar");

        //Debemos tomar preferencia por determinar el tipo a almacenar usando <> (formalizacion) y usar el contrato en la declaracion de la lista
        //NOTA: El operador <> no admite tipos primitivos
        List<String> colors2 = new ArrayList<>();
        colors2.add("Red");
        colors2.add("Yellow");
        //colors2.add(1); Esta linea resulta en un error de restriccion

        //ELIMINAR
        names.remove("Alejandro");
        names.remove(1);

        //ACTUALIZAR
        colors2.set(0, "Blue");

        //Al usar List en la declaracion no nos preocupamos por la implementacion que usemos en la asignacion, en la asignacion solo referenciaremos el constructor de alguna implementacion de List como ArrayList

        System.out.println(colors2); //Imprime los contenidos de la lista por defecto
        System.out.println(colors2.contains("Yellow")); //Imprime la existencia o no del elemento especificado

        //Tambien podemos iterar listas de la forma clasica
        for(String color : colors2){
            System.out.println(color);
        }

        colors2.forEach(System.out::println);

        //List tambien nos permite simular tuplas por medio del metodo of el cual retorna una lista inmutable
        List<String> colorsUnmodifiable = List.of("blue","red","black");
        //colorsUnmodifiable.add("white"); Esta linea resulta en un error de modificacion

        System.out.println(colorsUnmodifiable);

    }

    public static void stacks(){
        /*
        Podemos pensar en un stack como una lata de pringles.
        Esto quiere decir que la primera papa en entrar es la ultima en salir
         */

        //Se declaran de la misma forma que declarariamos una lista
        //Al igual que con las listas, el parametro de tipo para un stack no puede ser primitivo
        //Por ello usamos clases envolventes o wrapper classes en su lugar
        Stack<Integer> numbers = new Stack<>();

        //push() añade items al stack en orden desde el indice 0
        numbers.push(1);
        numbers.push(20);
        numbers.push(43);

        System.out.println(numbers.peek()); //con peek() podemos ver el item almacenado en el ultimo indice (o en este caso, encima del stack)
        System.out.println(numbers.size()); //retorna el tamaño del stack
        System.out.println(numbers.pop()); //elimina el elemento en el ultimo indice y lo retorna
        System.out.println(numbers.size());
        System.out.println(numbers.empty()); //Retorna si el stack se encuentra vacio o no
        System.out.println(numbers.search(20)); //Retorna el indice del objeto a buscar
        numbers.set(0, 10); //Actualiza el indice 0

        /*
        Stack hereda de Vector y Vector es una implementacion de List, por lo tanto, Stack es una implementacion de List.
        La diferencia entre un Stack y una lista es que los stack son sincronos,
        mientras que las listas se emplean en entornos multithreading, por ello se debe
        saber cuando emplear un stack dado que puede ralentizar algunas operaciones
         */

        //Entonces, esto nos permite tener objetos como este
        List<Integer> numbers2 = new Stack<>();
        numbers2.add(2); //Ahora podemos usar metodos de List mientras conserva algo del comportamiento de un Stack

        //Por ejemplo, ya que Stack no sobreescribe add() podemos emplearlo como si fuese push()
        //En resumen, podremos usar metodos de List mientras no esten sobreescritos por Stack para este caso
        //Aun asi, lo recomendable es declarar la variable como Stack

    }

    public static void queues(){

        /*
        Podemos pensar en las queues como "primero que llega primero que sale"
        de la misma forma que se haria en una fila, por definicion, una queue se refiere a
        una coleccion diseñada para almacenar elementos antes de procesarlos
         */

        //Ya que Queue es una interface, declaremos la siguiente queue usando una de sus implementaciones
        Queue<Persona> filaMercado = new LinkedList<>();

        //AÑADIR
        filaMercado.add(new Persona("Alejandro", 22));
        filaMercado.add(new Persona("Maria",31));
        filaMercado.add(new Persona("Carlos", 18));


        System.out.println(filaMercado.peek());
        //Podemos ver entonces que, a diferencia de un stack, en una queue, quien va primero o encima es quien primero ingresa

        System.out.println(filaMercado.size());
        System.out.println(filaMercado.poll()); //Equivalente a pop() en stacks, poll elimina el objeto a la cabeza
        System.out.println(filaMercado.size());
        System.out.println(filaMercado.peek()); //Podemos ver que ahora la cabeza de la queue se ha movido al siguiente objeto

        //Tambien contamos con otros metodos adicionales:
        System.out.println(filaMercado.remove()); //Misma utilidad que poll, difiere en que arroja una excepcion si la queue se encuentra vacia
        System.out.println(filaMercado.offer(new Persona("Oscar", 25))); //Misma utilidad que add, difiere en que no arroja una excepcion en caso de restricciones de tamaño como si lo haria add(), simplemente arroja un booleano confirmando el resultado de la operacion
        System.out.println(filaMercado.isEmpty()); //Retorna si la queue se encuentre vacia o no
    }

    public static void linkedLists(){
        /*
        Como sabemos, linkedList es una implementacion de Queues
        Conceptualmente, las linkedLists son cadenas de nodos (siendo los nodos de los extremos cabeza y cola respectivamente), donde cada nodo contiene 2 cosas:
        1- Un valor u objeto almacenado
        2- Una o dos referencias

        La referencia representara ya sea el nodo anterior o posterior
        Aqui es donde tenemos dos casos, si una linkedList contiene dos referencias se considera una linkedList bidireccional donde cada referencia apunta al nodo anterior y posterior
        De lo contrario, la referencia de cada nodo apuntara unicamente a uno de los nodos en una direccion determinada

        Cabe entender que: si queremos añadir un nodo a nuestra linkedList, debemos crear este nodo antes de insertarlo teniendo en cuenta las dos caracteristicas mencionadas anteriormente
        esto quiere decir que, para cada agregado debemos actualizar las referencias
         */

        LinkedList<Persona> linkedList = new LinkedList<>();

        //AÑADIR
        linkedList.add(new Persona("Roberto", 43));
        linkedList.add(new Persona("Alex", 18));
        linkedList.addFirst(new Persona("Elizabeth", 25));
        linkedList.addLast(new Persona("Julian", 39));
        linkedList.add(2, new Persona("Carolle", 30));

        //ELIMINAR
        linkedList.remove(2);
        linkedList.remove(new Persona("Alex", 18));

        //ACTUALIZAR
        linkedList.set(0, new Persona("Arthur", 27));

        //Podemos iterar esta linkedList por medio de listIterator()
        ListIterator<Persona> personaListIterator = linkedList.listIterator(); //listIterator() nos permite acceder a metodos que nos permiten tener visualizacion de los nodos en una linkedList

        //listIterator cuenta con un cursor o un marcador de posicion entre los nodos, este nodo se inicializa antes del primer elemento
        while(personaListIterator.hasNext()){ //Solo itera mientras haya un nodo a la derecha del cursor
            System.out.println(personaListIterator.next()); //En caso de haber un nodo a la derecha del cursor, imprime este mismo y el cursor es ubicado antes del nuevo nodo
        }

        //para poder usar previous debemos haber movido el cursor al final de la linkedList
        while(personaListIterator.hasPrevious()){
            System.out.println(personaListIterator.previous()); //de esta forma se imprime el anterior y el cursor es movido a la derecha del nuevo nodo
        }

        //Aun asi, podemos seguir empleando las mismas visualizaciones a cuando se emplean listas:
        System.out.println(linkedList);

        for(Persona persona : linkedList){
            System.out.println(persona);
        }

        for (int i = 0; i < linkedList.size(); i++){
            System.out.println(linkedList.get(i));
        }

    }

    public static void sets(){
        /*
        Podemos pensar en los sets como colecciones desordenadas donde ningun elemento se repite
        por ello podemos imaginar a los sets como bolsas
         */

        //Los sets son interfaces con varias implementaciones
        Set<Pelota> pelotas = new HashSet<>();
        pelotas.add(new Pelota("Blue"));
        pelotas.add(new Pelota("Yellow"));
        pelotas.add(new Pelota("Red"));

        pelotas.forEach(System.out::println);

        //Si llegas a añadir un duplicado al set este sera ignorado y no habran cambios
        //El set define un duplicado como objetos de igual constructor, campos, metodos, etc
        //Podriamos tener una clase dedicada a pelotas al mismo tiempo que el record, esto permitira duplicados (mientras no se sobreescriba equals, hashcode y toString)

        //Cabe tambien mencionar que una de las implementaciones de set son los TreeSet los cuales otorgan un orden natural a sus elementos (alfabetico o numerico)

        //ELIMINAR
        //Ya que los hashset no cuentan con indices, solo podemos eliminar referenciando el objeto como tal a eliminar
        pelotas.remove(new Pelota("Yellow"));

    }

    public static void maps(){
        /*
        Podemos pensar en los maps como colecciones de clave valor
        Para el caso de la clase Map, esta se refiere a una interfaz con multiples implementaciones como:

        -> HashTable = no permite valores null, sincronizado (si trabajas con multithreading, esta opcion puede ser mas lenta)
        -> HashMap = permite valores null
            -> LinkedHashMap = permite valores null, implementacion basada en linkedList, lento
       -> SortedMap
       -> NavigableMap
       -> TreeMap = Ordenado, no permite valores null
         */

        Map<Integer, Persona> map = new HashMap<>();

        //AÑADIR
        map.put(1, new Persona("Alexander", 24));
        map.put(2, new Persona("Carolina", 23));
        map.put(3, new Persona("Martin", 26));

        //ACTUALIZAR
        //Podemos actualizar un item reasignando por medio del mismo indice
        map.put(3, new Persona("Garcia", 31));
        System.out.println(map);

        //ELIMINAR
        map.remove(2);
        System.out.println(map);

        //Otros metodos:
        System.out.println(map.size()); //retorna el tamaño
        System.out.println(map.get(1)); //retorna el item por medio de su llave
        System.out.println(map.containsKey(4)); //retorna si existe la llave o no
        System.out.println(map.keySet()); //retorna un set con las llaves del hashmap
        System.out.println(map.values()); //Retorna un set con los valores del hashmap
        System.out.println(map.entrySet()); //retorna un set con los items del hashmap
        System.out.println(map.getOrDefault(2, new Persona("Gomez", 34))); //Retora el elemento que tiene como llave el primer parametro, de lo contrario, usa esta llave y asigna el segundo parametro como su nuevo valor

        //Tambien podemos usar getKey y getValue en los elementos de un map
        map.entrySet().forEach(persona -> System.out.println(persona.getKey() + " " + persona.getValue()));
        map.forEach((llave, persona) -> System.out.println(llave + " " + persona));

        ////////////////////////////////////////////////
        //funciones Hash y HashCode
        /*
        Cuando ejecutamos por ejemplo map.put(1, "Hello"), map ingresa la llave a una funcion hash la cual retornada un hashcode el cual sera usado para referenciar la llave internamente
        en el caso de numeros enteros, el hashcode resultante termina siendo el mismo numero.
        Pero hay casos en donde puede que tengamos algo como:

        map.put(new Person("Camila"), new Diamante());

        Aqui estamos usando un objeto como llave, entonces, lo que resulta de la funcion hash al pasar esto como parametro sera un hashcode que sera un numero entero dificil de leer como -2083476985, a diferencia de con un entero, este sera generado por un algoritmo especifco.
        numero que map usara para referenciar a la llave de este elemento del map, cabe recalcar que no importa cuantas veces ingresemos esta llave, siempre se retornara la misma llave.

        Esto no es eficiente y es por ello recomendable que sobreescribamos los metodos equals y hashcode en nuestras clases
         */

        Map<Persona, Auto> map2 = new HashMap<>();

        map2.put(new Persona("Isabela", 29), new Auto("Mercedes"));

        System.out.println(map2.get(new Persona("Isabela", 29))); //si no hemos sobreescrito la clase de la llave, esto retornara null, la busqueda se hace comparando los hashcodes de ambas partes, nunca entre los objetos por si mismos
    }

    public static void extra(){

        int opcion;
        Scanner scanner = new Scanner(System.in);
        boolean ejecutar = true;
        String menu = "-AGENDA DE CONTACTOS- \n\n"+"1-Buscar Contactos\n"+"2-Insertar Contactos\n"+"3-Actualizar Contactos\n"+"4-Eliminar Contactos\n"+"5-Finalizar Programa\n";

        String restriccionNumero = "^\\d{10}$";

        List<List<Object>> contactos = new ArrayList<>();

        while(ejecutar){
            System.out.println();
            System.out.println(menu);
            System.out.println();
            System.out.print("Ingresa una opcion: ");
            try{
                opcion = Integer.parseInt(scanner.nextLine());
                if(opcion < 1 || opcion > 5){
                    throw new Exception();
                }
            }catch(Exception e){
                System.out.println("ERROR: Ingresa un numero u opcion valida");
                continue;
            }

            switch(opcion){
                case 5:
                    System.out.println("Fin del Programa");
                    ejecutar = false;
                    break;
                case 1:

                    int opcionMenuBuscar;

                    while(true){
                        try{
                            System.out.println("1- Mostrar todos los contactos");
                            System.out.println("2- Buscar contacto en especifico");
                            opcionMenuBuscar = Integer.parseInt(scanner.nextLine());
                            if(opcionMenuBuscar < 1 || opcionMenuBuscar > 2){
                                throw new Exception();
                            }
                            break;
                        }catch (Exception e){
                            System.out.println("Ingresa una opcion valida");
                        }
                    }

                    if(opcionMenuBuscar == 1){
                        for(List<Object> c : contactos){
                            System.out.println(c);
                        }
                    }else{
                        System.out.println("Ingresa el Nombre o Numero del contacto a buscar");
                        String busqueda = scanner.nextLine();
                        String resultado = "";
                        for(List<Object> contacto : contactos){
                            if(contacto.get(0).toString().equalsIgnoreCase(busqueda) || contacto.get(1).toString().equals(busqueda)){
                                resultado = contacto.toString();
                            }
                        }

                        if(resultado.isEmpty()){
                            System.out.println("No se encontro algun contacto relacionado");
                        }else{
                            System.out.println(resultado);
                        }
                    }

                    break;
                case 2:

                    String nombreIngresar;
                    String numeroIngresar;

                    while(true){
                        try{
                            System.out.print("Nombre: ");
                            nombreIngresar = scanner.nextLine();
                            if(nombreIngresar.isBlank() || nombreIngresar.length() > 25){
                                throw new Exception();
                            }
                            break;
                        }catch(Exception e){
                            System.out.println("ERROR: Ingresa un nombre valido");
                        }
                    }

                    while(true){
                        try{
                            System.out.print("Numero: ");
                            numeroIngresar = scanner.nextLine();
                            if(numeroIngresar.isBlank() || !numeroIngresar.matches(restriccionNumero)){
                                throw new Exception();
                            }
                            break;
                        }catch(Exception e){
                            System.out.println("ERROR: Ingresa un numero valido");
                        }
                    }

                    contactos.add(Arrays.asList(nombreIngresar, numeroIngresar));
                    break;

                case 3:
                    int opcionContacto = -1;
                    int opcionMenuActualizar;
                    for(int i = 0; i < contactos.size(); i++){
                        System.out.println((i+1)+"-"+contactos.get(i));
                    }
                    while(true){
                        if(contactos.isEmpty()){
                            break;
                        }
                        try{
                            System.out.print("Escribe el identificador del contacto a actualizar: ");
                            opcionContacto = Integer.parseInt(scanner.nextLine());
                            if(opcionContacto < 1 || opcionContacto > contactos.size()){
                                throw new Exception();
                            }
                            break;
                        }catch (Exception e){
                            System.out.println("Ingresa un identificador valido");
                        }
                    }

                    while(true){
                        try{
                            System.out.println("¿Que deseas actualizar?");
                            System.out.println("1- Nombre");
                            System.out.println("2- Numero");
                            opcionMenuActualizar = Integer.parseInt(scanner.nextLine());
                            if(opcionMenuActualizar < 1 || opcionMenuActualizar > 2){
                                throw new Exception();
                            }
                            break;
                        }catch (Exception e){
                            System.out.println("Ingresa una opcion valida");
                        }
                    }

                    if(opcionMenuActualizar == 1){
                        String nombreNuevo;
                        while(true){
                            try{
                                System.out.print("Nombre: ");
                                nombreNuevo = scanner.nextLine();
                                if(nombreNuevo.isBlank() || nombreNuevo.length() > 25){
                                    throw new Exception();
                                }
                                break;
                            }catch(Exception e){
                                System.out.println("ERROR: Ingresa un nombre valido");
                            }
                        }
                        contactos.get(opcionContacto-1).set(0, nombreNuevo);

                    }else{
                        String numeroNuevo;
                        while(true){
                            try{
                                System.out.print("Numero: ");
                                numeroNuevo = scanner.nextLine();
                                if(numeroNuevo.isBlank() || !numeroNuevo.matches(restriccionNumero)){
                                    throw new Exception();
                                }
                                break;
                            }catch(Exception e){
                                System.out.println("ERROR: Ingresa un numero valido");
                            }
                        }
                        contactos.get(opcionContacto-1).set(1, numeroNuevo);
                    }

                    break;

                case 4:
                    int opcionEliminar = -1;
                    for(int i = 0; i < contactos.size(); i++){
                        System.out.println((i+1)+"-"+contactos.get(i));
                    }

                    while(true){
                        if(contactos.isEmpty()){
                            break;
                        }
                        try{
                            System.out.print("Escribe el identificador del contacto a eliminar: ");
                            opcionEliminar = Integer.parseInt(scanner.nextLine());
                            if(opcionEliminar < 1 || opcionEliminar > contactos.size()){
                                throw new Exception();
                            }
                            break;
                        }catch (Exception e){
                            System.out.println("Ingresa un identificador valido");
                        }
                    }

                    contactos.remove(contactos.get(opcionEliminar-1));
                    break;

            }
        }
    }

    //DTOS para ejemplos [queues, sets]
    static class Persona{

        String nombre;
        int edad;

        public Persona(String nombre, int edad) {
            this.nombre = nombre;
            this.edad = edad;
        }

        @Override
        public String toString() {
            return "Persona{" +
                    "nombre='" + nombre + '\'' +
                    ", edad=" + edad +
                    '}';
        }

        @Override //sobreescribir equals es necesario para la comparacion al momento de buscar un elemento
        public boolean equals(Object o) {
            if (o == null || getClass() != o.getClass()) return false;
            Persona persona = (Persona) o;
            return edad == persona.edad && Objects.equals(nombre, persona.nombre);
        }

        @Override //Esta es la funcion hash, sin esta sobreescritura, no se puede encontrar elementos en un map donde su llave sea un objeto, hace que objetos identicos retornen exactamente el mismo hashcode
        public int hashCode() {
            return Objects.hash(nombre, edad); //retorna un hashcode
        }
    }
    //record Persona(String nombre, int edad){}
    record Pelota(String color){}
    record Auto(String marca){}

}
