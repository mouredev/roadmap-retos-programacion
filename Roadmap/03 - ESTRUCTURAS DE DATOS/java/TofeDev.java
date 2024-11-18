import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;
import java.util.TreeSet;

public class TofeDev {
    public static void main(String[] args) {

        //ARRAY------

        //Array declaración manual
        int numeros [] = new int [8]; //(con Strings se haría igual, pero en vez de int, String)
        numeros[0] = 10;
        numeros[1] = 51;
        numeros[2] = 98;
        numeros[3] = 41;
        numeros[4] = 50;
        numeros[5] = 39;
        numeros[6] = 87;
        numeros[7] = 17;
        for (int i = 0; i<8;i++) {
            System.out.println("Índice: " + i + " Valor: " + numeros[i]);
        }

        //Otra forma de incersión:
        int [] listaNum = {2, 5, 7, 10};

        for (int i = 0; i<listaNum.length;i++) {
            System.out.println("Índice: " + i + " Valor: " + listaNum[i]);
        }

        //Array bidimencional
        int cajas [][] = new int[3][4]; 
        cajas[0][0] = 10;
        cajas[0][1] = 50;
        cajas[0][2] = 75;
        cajas[0][3] = 15;
        cajas[1][0] = 64;
        cajas[1][1] = 93;
        cajas[1][2] = 34;
        cajas[1][3] = 37;
        cajas[2][0] = 41;
        cajas[2][1] = 19;
        cajas[2][2] = 24;
        cajas[2][3] = 87;
        for (int i = 0; i < cajas.length; i++) {
            for (int j = 0; j < cajas[i].length; j++) {
                System.out.print("Fila: " + i + " Columna: " + j + " Valor: " + cajas[i][j] + " ");
            }
            System.out.println();
        }

        //LISTAS------

        //ArrayList, integer, declaración manual
        ArrayList<Integer> listaNumeros = new ArrayList<>();
        listaNumeros.add(5);
        listaNumeros.add(7);
        listaNumeros.add(3);
        for (Integer num : listaNumeros) {
            System.out.println(num);
        }

        //Ordenacion
        listaNumeros.sort((a, b) -> a - b);
        for (Integer num : listaNumeros) {
            System.out.println(num);
        }

        //ArrayList, Strings, declaraciones con una array
        String [] nombres = {"Marco","Maria","Roberto"};
        List<String> listaNombres = Arrays.asList(nombres);
        for (String nombre : listaNombres) {
            System.out.println(nombre);
        }

        //LinkedList, Strings, datos relacionados del siguiente y el anterior
        LinkedList<String> listaStrings = new LinkedList<>();
        listaStrings.add("Hoy");
        listaStrings.add("hace");
        listaStrings.add("frio.");
        for (String palabras : listaStrings) {
            System.out.println(palabras);
        }

        //Conjuntos-------

        //Hashset, cada dato tiene que ser único, no asegura que los datos estén ordenados
        HashSet<String> idiomas = new HashSet<String>();
        idiomas.add("Español");
        idiomas.add("Inglés");
        idiomas.add("Portugués");
        idiomas.add("Francés");
        for (String idioma : idiomas) {
            System.out.println(idioma);
        }

        //Borrado de datos
        idiomas.remove("Francés");
        for (String idioma : idiomas) {
            System.out.println(idioma);
        }

        /*TreeSet, los datos si están ordenados
        (si es String se ordena en orden alfabético)*/
        TreeSet<Integer> numOrdenados = new TreeSet<Integer>();
        numOrdenados.add(1);
        numOrdenados.add(100);
        numOrdenados.add(20);
        numOrdenados.add(50);
        for (Integer ordenados : numOrdenados) {
            System.out.println(ordenados);
        }

        //LinkedHashSet, mantiene el orden de incersión
        LinkedHashSet<String> notasMusicales = new LinkedHashSet<String>();
        notasMusicales.add("Do");
        notasMusicales.add("Re");
        notasMusicales.add("Mi");
        for (String notas : notasMusicales) {
            System.out.println(notas);
        }

        //Mapas---------

        //HashMap, un mapa con una key y un valor relacionado, no asegura que los datos estén ordenados
        HashMap<String, Integer> mapaInventario = new HashMap<>();
        mapaInventario.put("Cubo", 2);
        mapaInventario.put("Hacha", 1);
        mapaInventario.put("Carbón", 50);
        mapaInventario.put("Pan", 20);
        for (String key : mapaInventario.keySet()) {
            System.out.println(key + " - " + mapaInventario.get(key));
        }

        //Actualización
        mapaInventario.put("Pan", 15);
        for (String key : mapaInventario.keySet()) {
            System.out.println(key + " - " + mapaInventario.get(key));
        }

        //TreeMap, los datos están ordenados según la key
        TreeMap<Integer, String> mapaRanking = new TreeMap<>();
        mapaRanking.put(1, "Python");
        mapaRanking.put(3, "Java");
        mapaRanking.put(2, "JavaScript");
        for (Integer key : mapaRanking.keySet()) {
            System.out.println(key + " - " + mapaRanking.get(key));
        }

        //LinkedTreeMap, mantiene el orden de incersión
        LinkedHashMap<String, Integer> mapaRandom = new LinkedHashMap<>();
        mapaRandom.put("cinco", 5);
        mapaRandom.put("uno", 1);
        mapaRandom.put("siete", 7);
        for (String key : mapaRandom.keySet()) {
            System.out.println(key + " - " + mapaRandom.get(key));
        }

        /* DIFICULTAD EXTRA (opcional):
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

        System.out.println("---------AGENDA---------");
        Scanner name = new Scanner(System.in);
        Scanner number = new Scanner(System.in);
        Scanner eleccion = new Scanner(System.in);
        Scanner buscar = new Scanner(System.in);
        Scanner actualizar = new Scanner(System.in);
        Scanner actualizarNum = new Scanner(System.in);

        Map<String, Long> agenda = new HashMap<>();

        System.out.println("""
                    Seleccione una opción:
                    1. Agregar contacto
                    2. Buscar contacto
                    3. Actualizar contacto
                    4. Borrar contacto
                    5. Salir """);

        int opcion = eleccion.nextInt();

        while (opcion != 5) {
            // Agregar contacto
            if (opcion == 1) {
                System.out.print("Ingrese el nombre del contacto: ");
                String nombre = name.nextLine();
                System.out.print("Ingrese el número del contacto: ");
                Long numero = number.nextLong();
                agenda.put(nombre, numero);
            } else if (opcion == 2) {
            // Buscar contacto
                System.out.print("Ingrese el nombre del contacto a buscar: ");
                String buscarNombre = buscar.nextLine();
                Long numberFind = agenda.get(buscarNombre);
                if (numberFind != null) {
                    System.out.println("Resultado de la búsqueda: ");
                    System.out.println("Nombre: " + buscarNombre + " Número: " + numberFind);
                } else {
                    System.out.println("Resultado de la búsqueda: ");
                    System.out.println("El nombre ingresado no está en la agenda de contactos.");
                }
                System.out.println();
            } else if (opcion == 3) {
            // Actualizar número de contacto
                System.out.print("Ingrese el nombre del contacto a actualizar: ");
                String actualizarContacto = actualizar.nextLine();
                System.out.print("Ingrese el nuevo núnero: ");
                Long nuevoNumero = actualizarNum.nextLong();
                agenda.put(actualizarContacto, nuevoNumero);
                System.out.println("Contacto actualizado." + actualizarContacto);
            } else if (opcion == 4) {
            // Eliminar contacto
                System.out.print("Ingrese el nombre del contacto a eliminar: ");
                String eliminarContaco = actualizar.nextLine();
                agenda.remove(eliminarContaco);
                System.out.println("Contacto eliminado: " + eliminarContaco);
            } else if (opcion > 5 || opcion == 0) {
                System.out.println("Opción no valida. Intente de nuevo");
            }
            System.out.println("Agenda" + agenda);
            System.out.println("""
                    Seleccione una opción:
                    1. Agregar contacto
                    2. Buscar contacto
                    3. Actualizar contacto
                    4. Borrar contacto
                    5. Salir """);
            opcion = eleccion.nextInt();
        }
        name.close();
        number.close();
        buscar.close();
        actualizar.close();
        actualizarNum.close();
        eleccion.close();
    }

}