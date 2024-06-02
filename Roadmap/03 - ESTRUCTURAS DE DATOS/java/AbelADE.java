/**
 * Solución al ejercicio #03 ESTRUCTURAS DE DATOS.
 * 
 * @author AbelADE
 */
public class AbelADE {
    
    /**
     * Estructuras de datos por defecto en Java:
     *      -- Arrays: son un conjunto de datos del mismo tipo
     *          almacenados en posiciones con consecutivas de memoria, 
     *          cuya extensión es inmutable.
     *      -- Listas: secuencia de datos del mismo tipo, donde cada
     *          elemento está enlazado al siguiente. La extensión es mutable.
     *      -- Pilas: Los elementos se apilan uno encima del otro, 
     *          y solo se puede acceder al último elemento agregado (LIFO).
     *      -- Colas: Los elementos se encolan uno detrás del otro, 
     *          y solo se puede acceder al primer elemento agregado (FIFO).
     *      -- Conjuntos: son colecciones de elementos únicos sin orden.
     *      -- Diccionarios: son colecciones guardadas en pares de clave-valor,
     *          donde cada clave se asocia con un valor. El concepto de clave
     *          es similar al de primary key en bases de datos.
     */
    
    /**
     * Arrays.
     */
    
    // Inicializar un array con datos.
    private int [] array = new int[]{0,1,2,3,4,5,6,7,8,9};

    // Inicializar un array con su longitud.
    private int [] array2 = new int[10];
    
    /**
     * Listas.
     */
    ArrayList<Integer> lista = new ArrayList<>();
    
    /**
     * Conjuntos.
     */
    HashSet<Integer> conjunto = new HashSet<>();
    
    /**
     * Diccionarios.
     */
    HashMap<Integer, Integer> diccionario = new HashMap<>();
    
    /**
     * Pilas
     */
    Stack<Integer> pila = new Stack<>();
    
    /**
     * Colas
     */
    Queue<Integer> cola = new LinkedList<>();
    
    //Métodos a usar en el Ejercicio extra
    
    public static String getName(){
        Scanner scan = new Scanner(System.in);
        System.out.print("Dame el nombre: ");
        return scan.nextLine();
    }
    
    public static Long getPhone(){
        Scanner scan;
        boolean validTel = false;          
        long tel = Long.MIN_VALUE;

        do {       
            scan = new Scanner(System.in);
            try {
                System.out.print("Dame el número de teléfono: ");

                String telText = scan.nextLine();

                tel = Long.parseLong(telText);

                if (telText.length() > 11) {
                   System.out.println("El teléfono debe tener menos de 11 dígitos");
                   System.out.println();
                }else{
                   validTel = true;
                }
            } catch (NumberFormatException e) {
                System.out.println("Número de teléfono no válido");
            }

        } while (!validTel);
        
        return tel;
    }
    
    public static void getResult(Long result, String success){
        if (result!= null) {
            System.out.println(success);
        }else{
            System.out.println("Operación fallida");
        }
    }
    

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        AbelADE estructuras = new AbelADE();
        
        //Operaciones con Arrays.
        
            //Inserción en Array
            estructuras.array2[0] = 5;
            estructuras.array2[1] = 15;
            estructuras.array2[2] = 25;

            //No se puede borrar en un Array, 
            //pero se podría realizar un borrado lógico,
            //en este caso un dato a cero sería equivalente a no tener dato
            estructuras.array2[1] = 0;

            //Actualización de un dato en un Array.
            estructuras.array2[2] = 20;

            //Ordenar un array
            Arrays.sort(estructuras.array2);
        
        //Operaciones con Listas.
            
            // Inserción
            estructuras.lista.add(20);
            estructuras.lista.add(10);
            estructuras.lista.add(30);

            // Borrar el primer elemento
            estructuras.lista.remove(0);

            // Actualizar el primer dato
            estructuras.lista.set(0, 15);

            // Ordenar
            Collections.sort(estructuras.lista);
            
        // Operaciones con Conjuntos.
        
            // Inserción
            estructuras.conjunto.add(20);
            estructuras.conjunto.add(10);
            estructuras.conjunto.add(30);
            
            //Borrar el dato que sea igual a 20
            estructuras.conjunto.remove(20);
        
            // No se puede Actualizar, pero podemos eliminar el elemento antigüo
            // y añadir un nuevo elemento
            estructuras.conjunto.remove(10);
            estructuras.conjunto.add(15);
            
            // No se puede Ordenar
            
        // Operaciones con Diccionarios.
        
            // Inserción
            estructuras.diccionario.put(0, 0);
            estructuras.diccionario.put(5, 5);
            estructuras.diccionario.put(10, 10);
            estructuras.diccionario.put(6, 6);
            
            //Borrar por clave
            estructuras.diccionario.remove(0);
            
            // Actualizar
            estructuras.diccionario.replace(10, 20);
            
            // Ordenar - No existe un método nativo
            
         // Operaciones con Pilas
            
            // Inserción
            estructuras.pila.add(50);
            estructuras.pila.add(10);
            estructuras.pila.add(90);
            
            //Borrar el primer elemento
            estructuras.pila.remove(0);
            
            // Actualizar 
            estructuras.pila.set(1, 9);
            
            // Ordenar 
            Collections.sort(estructuras.pila);
            
         // Operaciones con Colas
         
            // Inserción
            estructuras.cola.add(50);
            estructuras.cola.add(10);
            estructuras.cola.add(90);
            
            //Borrar
             estructuras.cola.remove(0);
             
            // No se puede Actualizar, pero podemos borrar
            // e insertar el nuevo valor.
            
            // No existe un método nativo para Ordenar     
            
            
            
         /**
          * DIFICULTAD EXTRA: Crea una agenda de contactos por terminal
          */   
         Scanner scan = new Scanner(System.in);
         boolean exit = false;
         HashMap<String,Long> contacts = new HashMap<>();
         
         do {           
             System.out.println("Bienvenido a la agenda de contactos");
             System.out.println("¿Qué deseas hacer?");
             System.out.println("1 - Crear un contacto");
             System.out.println("2 - Buscar un contacto");
             System.out.println("3 - Actualizar un contacto");
             System.out.println("4 - Eliminar un contacto");
             System.out.println("5 - Salir");
             System.out.println();
             
             System.out.print("Elige una opción: ");
             int option = scan.nextInt();
             scan.nextLine();
             
             String name = "";
             if (option != 5) {
                name = getName();
                 System.out.println();
             }
             
             switch (option) {
                 case 1:     
                     getResult(contacts.put(name, getPhone()), "Contacto añadido");
                     break;
                 case 2:
                     Long telUser = contacts.get(name);
           
                     getResult(telUser, "El teléfono de " + name + " es: " + telUser);                     
                     break;
                 case 3:
                     getResult(contacts.replace(name, getPhone()), "Contacto actualizado");
                     
                     System.out.println("El nuevo teléfono de " + name + " es: " + contacts.get(name));
                     break;
                 case 4:
                      getResult(contacts.remove(name), name + " se ha eliminado");
                     break;
                 case 5:
                     exit = true;
                     break;
                 default:
                     System.out.println("Opción no válida!");
             }
             
             System.out.println();
             
        } while (!exit);
            
    }
    
}
