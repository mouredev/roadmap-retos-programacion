
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 */
class Marianoemir {

    public static void main(String[] args) {

        //Array 
        //Creación
        int[] numeros = {9, 4, 2, 8, 10};

        //Actualización
        numeros[1] = 5;

        //Ordenación
        Arrays.sort(numeros);

        //Mostrar Array
        for (int num : numeros) {
            System.out.println(num);
        }

        //ArrayList
        //Creación
        ArrayList<String> lista = new ArrayList<>();

        //Inserciòn
        lista.add("Ford");
        lista.add("Toyota");
        lista.add("Fiat");
        lista.add("Alfa Romeo");

        //Borrado
        lista.remove("Fiat");

        //Actualización
        lista.set(0, "Ferrari");

        //Ordenación
        Collections.sort(lista);

        //Mostrar ArrayList
        for (String autos : lista) {
            System.out.println(autos);
        }

        //HashMap
        //Creación
        HashMap<Integer, String> mapa = new HashMap<>();

        //Inserciòn
        mapa.put(1, "Uno");
        mapa.put(2, "Dos");
        mapa.put(3, "Tres");

        //Borrado
        mapa.remove(2);

        //Actualización
        mapa.put(1, "Actualización de uno");

        //Mostrar HashMap
        for (Map.Entry<Integer, String> entry : mapa.entrySet()) {
            System.out.println("Clave: " + entry.getKey() + ", Valor: " + entry.getValue());
        }

        //HashSet
        //Creación
        HashSet<String> conjunto = new HashSet<>();

        //Inserción
        conjunto.add("A");
        conjunto.add("B");
        conjunto.add("C");

        //Borrado
        conjunto.remove("B");

        //Mostrar HashSet
        for (String elemento : conjunto) {
            System.out.println(elemento);
        }

        //LinkedList
        //Creación
        LinkedList<String> listaEnlazada = new LinkedList<>();

        //Inserción 
        listaEnlazada.add("Rojo");
        listaEnlazada.add("Azul");
        listaEnlazada.add("Verde");

        //Inserción en una posición especifica
        listaEnlazada.add(1, "Amarilla");

        //Borrado
        listaEnlazada.remove("Azul");

        //Actualizaciòn
        listaEnlazada.set(2, "Morado");

        //Ordenación
        Collections.sort(listaEnlazada);

        for (String color : listaEnlazada) {
            System.out.println(color);
        }

        /*
        * DIFICULTAD EXTRA (opcional):
        * Crea una agenda de contactos por terminal.
        * - Debes implementar funcionalidades de búsqueda, inserción, actualización
        *   y eliminación de contactos.
        * - Cada contacto debe tener un nombre y un número de teléfono.
        * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
        *   y a continuación los datos necesarios para llevarla a cabo.
        * - El programa no puede dejar introducir números de teléfono no númericos y con más
        *   de 11 dígitos (o el número de dígitos que quieras).
        * - También se debe proponer una operación de finalización del programa.
         */
        HashMap<String, String> agenda = new HashMap<>();
        ;

        Scanner sc = new Scanner(System.in);
        String entrada1, entrada2;
        int menu = 0;
        boolean condi = true;
        boolean telefonoValido = false;
        boolean condifinal = true;

        do {

            System.out.println("¿Qué operación desea realizar?");
            System.out.println("1. Agregar un número a la agenda");
            System.out.println("2. Actualizar un número de la agenda");
            System.out.println("3. Eliminar contactos de la agenda");
            System.out.println("4. Salir del Programa.");
            menu = sc.nextInt();
            sc.nextLine();

            switch (menu) {
                case 1:
                    do {
                        do {
                            System.out.println("Ingrese el Nombre:");
                            entrada1 = sc.nextLine();

                            System.out.println("Ingrese el Telefono:");
                            entrada2 = sc.nextLine();

                            if (entrada2.matches("\\d{11}")) {
                                telefonoValido = true;
                                agenda.put(entrada1, entrada2);
                            } else {
                                System.out.println("El teléfono debe contener exactamente 11 dígitos numéricos.");
                            }
                        } while (!telefonoValido); // Repite hasta que el teléfono sea válido

                        String respuesta;
                        boolean respuestaValida = false;

                        do {
                            System.out.println("¿Desea continuar ingresando números? S=Sí/N=No");
                            respuesta = sc.nextLine().trim().toUpperCase();

                            if (respuesta.equals("S")) {
                                condi = true;
                                respuestaValida = true;
                            } else if (respuesta.equals("N")) {
                                condi = false;
                                respuestaValida = true;
                            } else {
                                System.out.println("Por favor, ingrese solo 'S' o 'N'.");
                            }
                        } while (!respuestaValida);

                    } while (condi);
                    break;
                    
                case 2:
                    if (agenda.isEmpty()) {
                        System.out.println("La agenda está vacía.");
                    } else {
                        int contador = 1;  // Contador para numerar los contactos
                        HashMap<Integer, String> indiceAgenda = new HashMap<>();  // Para mapear el número a la clave

                        // Mostrar la agenda con un índice numérico
                        for (Map.Entry<String, String> entry : agenda.entrySet()) {
                            System.out.println(contador + ". Nombre: " + entry.getKey() + ", Número: " + entry.getValue());
                            indiceAgenda.put(contador, entry.getKey());  // Mapeo del índice al nombre
                            contador++;
                        }

                        // Pedir al usuario que seleccione un número
                        System.out.println("Ingrese el número del contacto que desea actualizar:");
                        int seleccion = sc.nextInt();
                        sc.nextLine();  // Consumir el salto de línea

                        // Validar que la selección sea válida
                        if (indiceAgenda.containsKey(seleccion)) {
                            String nombreSeleccionado = indiceAgenda.get(seleccion);
                            System.out.println("Ha seleccionado: " + nombreSeleccionado);

                            // Preguntar qué desea modificar
                            System.out.println("¿Qué desea modificar?");
                            System.out.println("1. Solo el número de teléfono");
                            System.out.println("2. Solo el nombre");
                            System.out.println("3. Ambos");

                            int opcion = sc.nextInt();
                            sc.nextLine();  // Consumir el salto de línea

                            switch (opcion) {
                                case 1:
                                    // Modificar solo el número de teléfono
                                    System.out.println("Ingrese el nuevo número de teléfono:");
                                    String nuevoNumero = sc.nextLine();
                                    if (nuevoNumero.matches("\\d{11}")) {
                                        agenda.put(nombreSeleccionado, nuevoNumero);
                                        System.out.println("Número actualizado correctamente.");
                                    } else {
                                        System.out.println("El teléfono debe contener exactamente 11 dígitos numéricos.");
                                    }
                                    break;

                                case 2:
                                    // Modificar solo el nombre
                                    System.out.println("Ingrese el nuevo nombre:");
                                    String nuevoNombre = sc.nextLine();
                                    if (!agenda.containsKey(nuevoNombre)) {
                                        String numeroExistente = agenda.remove(nombreSeleccionado);  // Remover el contacto con el nombre anterior
                                        agenda.put(nuevoNombre, numeroExistente);  // Añadir el contacto con el nuevo nombre y el mismo número
                                        System.out.println("Nombre actualizado correctamente.");
                                    } else {
                                        System.out.println("Ese nombre ya existe en la agenda.");
                                    }
                                    break;

                                case 3:
                                    // Modificar tanto el nombre como el número de teléfono
                                    System.out.println("Ingrese el nuevo nombre:");
                                    nuevoNombre = sc.nextLine();
                                    System.out.println("Ingrese el nuevo número de teléfono:");
                                    nuevoNumero = sc.nextLine();

                                    if (!agenda.containsKey(nuevoNombre) && nuevoNumero.matches("\\d{11}")) {
                                        agenda.remove(nombreSeleccionado);  // Eliminar el contacto con el nombre anterior
                                        agenda.put(nuevoNombre, nuevoNumero);  // Añadir el nuevo nombre y el nuevo número
                                        System.out.println("Nombre y número actualizados correctamente.");
                                    } else {
                                        System.out.println("El nuevo nombre ya existe o el número no es válido.");
                                    }
                                    break;

                                default:
                                    System.out.println("Opción no válida.");
                                    break;
                            }
                        } else {
                            System.out.println("Selección no válida.");
                        }
                    }
                    break;

                case 3:
                    if (agenda.isEmpty()) {
                        System.out.println("La agenda está vacía.");
                    } else {
                        int contador = 1;
                        HashMap<Integer, String> indiceAgenda = new HashMap<>();  // Mapeo del índice al nombre

                        // Mostrar la agenda con índices numéricos
                        for (Map.Entry<String, String> entry : agenda.entrySet()) {
                            System.out.println(contador + ". Nombre: " + entry.getKey() + ", Número: " + entry.getValue());
                            indiceAgenda.put(contador, entry.getKey());
                            contador++;
                        }

                        // Pedir al usuario que seleccione un número para eliminar
                        System.out.println("Ingrese el número del contacto que desea eliminar:");
                        int seleccion = sc.nextInt();
                        sc.nextLine();  // Consumir el salto de línea

                        // Validar la selección y eliminar el contacto
                        if (indiceAgenda.containsKey(seleccion)) {
                            String nombreSeleccionado = indiceAgenda.get(seleccion);
                            agenda.remove(nombreSeleccionado);
                            System.out.println("Contacto eliminado correctamente.");
                        } else {
                            System.out.println("Selección no válida.");
                        }
                    }
                    break;

                case 4:
                    condifinal = false;
                    System.out.println("Numeros cargados en la agenda (ordenados alfabéticamente): ");

                    // Convertir el HashMap a TreeMap para ordenar alfabéticamente
                    TreeMap<String, String> agendaOrdenada = new TreeMap<>(agenda);

                    for (Map.Entry<String, String> entry : agendaOrdenada.entrySet()) {
                        System.out.println("Nombre: " + entry.getKey() + ", Número: " + entry.getValue());
                    }
                    break;

                default:
                    System.out.println("Opción no válida.");
                    break;
            }

        } while (condifinal);

    }

}
