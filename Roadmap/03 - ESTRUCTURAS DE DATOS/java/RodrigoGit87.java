import java.util.*;

public class RodrigoGit87 {
    //EXTRA
    // Objeto contacto
    public static class Contacto {
        private String nombre;
        private String telefono;
        public static int contador = 1; //contador estatico(afecta a todas las instancias) para usar en la variable id.
        private int id;

        //Constructor
        public Contacto(String nombre, String telefono) {
            this.nombre = nombre;
            setTelefono(telefono);
            this.id = contador++;
        }

        //getters
        public int getId() {
            return id;
        }

        public String getTelefono() {
            return telefono;
        }

        public String getNombre() {
            return nombre;
        }

        //setter para que telefono cumpla las condiciones de digitos y longitud máxima
        public void setTelefono(String telefono) {
            if (telefono.length() > 11) {
                throw new IllegalArgumentException("El telefono no debe tener más de 11 caracteres");
            }
            if (!telefono.matches("\\d+")) { //  \\d+ es una expresión q signifca q solo admite dígitos
                throw new IllegalArgumentException(" Solo se admite dígitos");
            }
            this.telefono = telefono;
        }
        //setter nombre
        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        @Override
        public String toString() {
            return "Contacto{" +
                    "nombre='" + nombre + '\'' +
                    ", telefono='" + telefono + '\'' +
                    ", id=" + id +
                    '}';
        }
    }


        // Objeto Agenda
        public static class Agenda {
            private HashMap<Integer, Contacto> contactos;

            //Constructor
            public Agenda() {
                this.contactos = new HashMap<>();
            }
                //metodo inserción
                public void añadirContacto (Contacto contacto){
                    this.contactos.put(contacto.getId(), contacto);
                }
                //metodo buscar
                public Contacto buscarId (int id){
                if(!contactos.containsKey(id)){
                    throw new IllegalArgumentException("No existe el contacto con el id: " + id);
                }
                return this.contactos.get(id);
                }
                //metodo eliminar
                public Contacto eliminarContacto (int id){
                    if(!contactos.containsKey(id)){
                        throw new IllegalArgumentException("No existe el contacto con el id: " + id);
                    }
                    return this.contactos.remove(id);
                }
                //metodo modificar
                public void modificarContacto (int id, String nuevoNombre, String nuevoTelefono){
                if(!contactos.containsKey(id)){
                    throw new IllegalArgumentException("No existe el contacto con el id: " + id);
                }
                Contacto c = contactos.get(id);
                if ( nuevoNombre != null && !nuevoNombre.isEmpty()) {
                    c.setNombre(nuevoNombre);
                }
                if ( nuevoTelefono != null && !nuevoTelefono.isEmpty()) {
                    c.setTelefono(nuevoTelefono);
                }
            }
        }


    public static void main (String[] args){
     //EXTRA
    Scanner sc = new Scanner(System.in);
    var agenda = new Agenda();
    boolean finalizar = false;
    int opcion;


    do{
        System.out.println("Introduce la opcion a realizar ");
        System.out.println("1.Añadir contacto \n2. Buscar contacto \n3. Modificar contacto \n4. Eliminar contacto \n5 Finalizar");
        try{
            opcion = sc.nextInt();
        } catch (Exception e) {
            opcion = 0;
            sc.nextLine();
        }
        sc.nextLine();
        switch (opcion){
            case 1: // insertar
                try {
                    System.out.println("Introduce el nombre del contacto : ");
                    String nombre = sc.nextLine().trim().toUpperCase();
                    System.out.println("Introduce la telefono del contacto : ");
                    String tfn = sc.nextLine().trim();

                    Contacto nuevo = new Contacto (nombre, tfn);
                    agenda.añadirContacto(nuevo);
                    System.out.println( " Nuevo contacto creado con id: " + nuevo.getId());
                } catch (IllegalArgumentException e){
                    System.err.println(e.getMessage());
                }
                break;
            case 2: //buscar
                System.out.println(" Introduce la ID del contacto a buscar: ");
                int idScanner = sc.nextInt();
                sc.nextLine();
                try{
                   Contacto encontrado = agenda.buscarId(idScanner);
                    System.out.println("Encontrado: " + encontrado.toString());
                } catch (IllegalArgumentException e){
                    System.err.println(e.getMessage());
                }
                break;
            case 3: // modificar
                System.out.println(" Introduce la ID del contacto a modificar: ");
                int idMod = sc.nextInt();
                sc.nextLine();

                try {
                    Contacto actual = agenda.buscarId(idMod); // Solo para mostrar el nombre actual
                    System.out.println("Editando a: " + actual.getNombre());

                    System.out.print("Nuevo nombre (pulsa ENTER para mantener el actual): ");
                    String nuevoNombre = sc.nextLine();

                    System.out.print("Nuevo teléfono (pulsa ENTER para mantener el actual): ");
                    String nuevoTlf = sc.nextLine();

                    agenda.modificarContacto(idMod, nuevoNombre, nuevoTlf);
                    System.out.println(">> ¡Contacto actualizado!");

                } catch (IllegalArgumentException e) {
                    System.out.println("ERROR: " + e.getMessage());
                }
                break;
            case 4: // Eliminar
                System.out.print("ID a eliminar: ");
                int idBorrar = sc.nextInt();
                sc.nextLine();

                try {
                    Contacto eliminado = agenda.eliminarContacto(idBorrar);
                    System.out.println(">> Se ha eliminado a: " + eliminado.getNombre());
                } catch (IllegalArgumentException e) {
                    System.out.println("ERROR: " + e.getMessage());
                }
                break;
            case 5:
                finalizar = true;
                System.out.println("¡Hasta la vista, baby !");
                break;
            default:
                System.out.println(" opcion incorrecta ");
        }
    } while (!finalizar);
    sc.close();


/* -------- Ejercicios Principales ----------*/
        System.out.println(" -------------- \n");
    //ARRAYS
        //declarar
    int[] arrayDeNumeros = new int[10]; /* se indica q hay 10 posiciones en índice, se cuentan del 0 al 9, en este caso
    las posiciones están vacías. Para rellenarlas, se puede manualmente indice a indice o con un ciclo for.*/

        //declarar array y asignar a la vez
        String[] frutas =  {"piña","manzana","kiwi","melon","fruta del dragón","coco","pepinaco"};
        System.out.println(" ");
        //Acceso al array -> con metodo .toString
        System.out.println("Frutas: " + Arrays.toString(frutas));
            // o, con un for-each
        for(String itemFruta: frutas){
            System.out.println("Fruta: " + itemFruta);
        }

    // asignar valor a un indice del array
    arrayDeNumeros [0]= 69;

    //asignar mediante ciclo for
        for (int i= 0; i < arrayDeNumeros.length; i++){
            arrayDeNumeros[i] = (i + 1) * 5 ; //Esto hace q la primera posicion del array, [0], empieze valiendo 1, luego multiplica por
            //5 y tenemos 5 como valor guardado en [0]. Siguiente iteracion, y ahora tenemos q en [1] = 5x5 = 10, [1] guarda el valor 10 y así...
        }
    //recorrer el array - con un for each
        for (int numero: arrayDeNumeros ){
            System.out.println(" ");
            System.out.println(numero);
        } // tenemos una maravillosa tabla del 5 guardada como un Array

   // LIST
        //declarar
    ArrayList<Integer> listaDeNumeros = new ArrayList<>();
    ArrayList<String> listaDeAlumnos = new ArrayList<>();
        //asignar
        listaDeAlumnos.add("RodrigoGit87");
        listaDeAlumnos.add("AbelADE");
        listaDeAlumnos.add("BlasBarragan");
        listaDeAlumnos.add("Cesar-ch");
        listaDeAlumnos.add("danhingar");
        IO.print("- listaDeAlumnos -");
        IO.println("\n"+ listaDeAlumnos + "\nTotal de alumnos: " + listaDeAlumnos.size());

        //Acceder a elementos
        //listaDeAlumnos.get(posicion));
        IO.println("---");
        IO.println(".get(1) = " + listaDeAlumnos.get(1));
        // otras formas -> .getFirst(); y .getLast();
        IO.println(".getFirst() = " + listaDeAlumnos.getFirst() + "\n");
        IO.println(".getLast() = " + listaDeAlumnos.getLast() + "\n");

        //modificar elementos
        listaDeAlumnos.set(3, "AnaLauDB");
        //ahora  la posicion 3 es AnaLauDB, antes era cesar-ch, lo comprobamos:
        IO.println(".get(3), despues de haber 'setteado' = " + listaDeAlumnos.get(3) + "\n");

    //HashSet,HashMap -> Aqui no existen indices, el valor se guarda en hashes, y de forma aleatoria, sin orden
    //HASHSET
        System.out.println("-- HashSet ---");
        //Declaracion y creacion
        HashSet<String> names = new HashSet<>();//una manera
        var id = new HashSet<String>();//otra manera

        // añadir
        names.add("Doom The Slayer");
        names.add("Rosa Melano");
        names.add("Gandalf el coder gris");
        names.add("Elver");

        // quitar
        names.remove("Elver");
        System.out.println(" hashSet: " + names.size());

        //acceso; no se puede, no hay indices como en array o arraylist
        //Se puede 'buscar' con .contains()
        IO.println("names.contains('Gandalf') " + names.contains("Gandalf")); //<- false, tiene q estar escrito exactamente igual
        IO.println("names.contains('Gandalf el coder gris') " + names.contains("Gandalf el coder gris")); // <- true

        System.out.println(" ");
        //conjuntos (añadir un hashset a otro, tienen q ser del mismo tipo)
        id.add("001");
        id.add("002");
        id.add("003");
        id.add("004");
        names.addAll(id);// ahora names contiene los elementos de id
        IO.println(names);
        names.removeAll(id);//ahora no
        IO.println(names);

    //HASHMAP Funciona con pares 'clave:valor' (Una Clave = Un Valor, no se puede asignar a la misma clave más de un valor )
        System.out.println(" ---- Hashmap ---");
        var mapa1 = new HashMap<String, String>(); // Indicar el tipo para <clave, valor>

        //.put para añadir
        mapa1.put("Humano","Aragorn");
        mapa1.put("Elfo","Legolas");
        mapa1.put("Mago","Gandalf");
        IO.println(mapa1.size());
        IO.println(mapa1);

        //.get para acceder (sabiendo la key y tipeando exactamente igual)
        IO.println(mapa1.get("Humano")); // <- Aragorn

        // comprobamos el principio de 1 key = 1 value
        mapa1.put("Humano", "Frodo"); //<- Ahora el valor del key "humano" es Frodo. Técnicamente: el puntero 'Humano' apunta a un hash, y ese hash solo
        //guarda un valor, el último asignado (al igual q una variable primitiva normal)
        IO.println(mapa1.get("Humano"));

        //.containsValue() o .containsKey(); para verificar (true o false).
        // De paso comprobamos q Aragorn ya no existe al usar la misma clave "Humano" para Frodo
        IO.println(mapa1.containsValue("Aragorn")); // <- false, osea, mapa1 no contiene/no existe el valor "Aragorn".
    }
}
