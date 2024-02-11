package com.dm4.roadmap;

import java.util.*;

/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
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

public class Roadmap03_EstructuraDatos {

    public static Scanner teclado = new Scanner(System.in);
    public static ArrayList<Contacto> listAgenda;


    public static void main(String[] args) {

        System.out.println(" *** HashMap *** ");
        //Creamos un HashMap para almacebar notas
        Map<String, Double>notasAlumnos = new HashMap<>();
        //Agregamos datos al HashMap
        notasAlumnos.put("Daniela", 8.5);
        notasAlumnos.put("Diego", 8.0);
        notasAlumnos.put("Franchezca", 10.0);
        //Acceder a las notas
        double notaDaniela = notasAlumnos.get("Daniela");
        double notaDiego = notasAlumnos.get("Diego");
        double notaFranchezca = notasAlumnos.get("Franchezca");
        System.out.println("Nota de Daniela es: " + notaDaniela);
        System.out.println("Nota de Diego es: " + notaDiego);
        System.out.println("Nota de Franchezca es: " + notaFranchezca);
        //Modificar la nota de un alumno
        notasAlumnos.put("Daniela", 9.0);
        //Imprimir las notas de los alumnos
        System.out.println("Nota de los alumnos");
        for (Map.Entry<String,Double> entry: notasAlumnos.entrySet()) {
            String nombre = entry.getKey();
            double nota = entry.getValue();
            System.out.println(nombre + " : " + nota);
        }

        System.out.println(" *** Array *** ");
        //Creamos un arreglo inicial
        int [] arregloOriginal = {1,2,3,4,5};
        //Nuevo tamaño deseado para el arreglo
        int nuevoTamanio = 8;
        //Creamos un nuevo arreglo con el nuevo tamanio
        int [] nuevoArreglo = new int[nuevoTamanio];
        //Copiar los elementos de arreglo original al nuevo arreglo
        for (int i = 0; i < arregloOriginal.length; i++) {
            nuevoArreglo[i] = arregloOriginal[i];
        }
        //Tenemos un nuevo arreglo con un tamaño mayor
        arregloOriginal = nuevoArreglo;
        //Imprimimos el nuevo arreglo
        for (int elemento:arregloOriginal) {
            System.out.println(elemento + " ");
        }

        System.out.println();
        System.out.println(" *** ArrayList *** ");
        ArrayList<String> ciudades = new ArrayList<>();
        //Agregamos las ciudades
        ciudades.add("Cuenca");
        ciudades.add("Guayaquil");
        ciudades.add("Quito");
        //Recorrer un ArrayList
        for (int i = 0; i < ciudades.size(); i++) {
            System.out.println(i + " : "  + ciudades.get(i));
        }
        //Eliminar una ciudad
        ciudades.remove("Cuenca");


        /**
         * Dificultad Extra
         */

        listAgenda = new ArrayList<Contacto>();

        int opcion = 0;

        //Bucle para pedir las opciones hasta que elijamos salir
        while (opcion != 6) {
            System.out.println();
            System.out.println("------------------------");
            System.out.println(" **** AGENDA **** ");
            System.out.println("------------------------");
            System.out.println();

            //opciones
            System.out.println("1. Crear Contacto");
            System.out.println("2. Listar Contactos");
            System.out.println("3. Buscar Contacto");
            System.out.println("4. Actualizar Contacto");
            System.out.println("5. Borrar Contacto");
            System.out.println("6. Salir");

            try {
                System.out.println();
                System.out.print("Seleccione una opcion: ");
                opcion = teclado.nextInt();
                switch (opcion) {
                    case 1:
                        add();
                        break;
                    case 2:
                        getLista();
                        break;
                    case 3:
                        mostrar(search());
                        break;
                    case 4:
                        update();
                        break;
                    case 5:
                        delete();
                        break;
                    case 6:
                        System.out.println("Fin del programa");
                        teclado.close();
                        System.exit(0);
                        break;
                    default:
                        System.out.println("Las opciones son entre 1 y 6");
                }

                //controla la excepcionn en caso de que se introduzca un valor no correcto
            } catch (InputMismatchException e) {
                System.out.println("Debes escribir un numero");
                teclado.next();
            }
        }
    }


    /**
     * Clase Contacto
     */
    public static class Contacto {

        public String nombre;
        public String correo;
        public Long telefono;

        public Contacto(String nombre, String correo, Long telefono) {
            this.nombre = nombre;
            this.correo = correo;
            this.telefono = telefono;
        }

        public Contacto() {
        }

        public String getNombre() {
            return nombre;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public String getCorreo() {
            return correo;
        }

        public void setCorreo(String correo) {
            this.correo = correo;
        }

        public Long getTelefono() {
            return telefono;
        }

        public void setTelefono(Long telefono) {
            this.telefono = telefono;
        }

    }

    /**
     * Metodo para agregar un contacto
     */
    private static boolean add() {
        try {
            teclado = new Scanner(System.in);
            System.out.println("-----------------------------------");
            System.out.println("---Crear Contacto---");
            System.out.println("Ingrese los datos");
            System.out.println();
            System.out.println("* Ingrese el Nombre:");
            String nombre = teclado.nextLine();
            System.out.println("* Ingrese el correo: ");
            String correo = teclado.nextLine();
            int size = 0;
            long telefono = 0;
            do {
                teclado = new Scanner(System.in);
                System.out.println("* Ingrese el telefono (11 digitos)):");
                try {
                    telefono = teclado.nextLong();
                } catch (Exception e) {
                    System.out.println("# telefono invalido");
                }
                size = String.valueOf(telefono).length();
            } while (size != 11);
            listAgenda.add(new Contacto(nombre, correo, telefono));
            System.out.println();
            System.out.println("*** Datos ingresados correctamente ***");
            System.out.println();
            System.out.println("-----------------------------------");
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    /**
     * Metodo para listar los contactos existentes
     *
     * @return
     */
    public static boolean getLista() {
        System.out.println("-----------------------------------");
        System.out.println("--- Lista de Contactos ---");
        System.out.println();
        for (int i = 0; i < listAgenda.size(); i++) {
            System.out.println(i + " Nombre: " + listAgenda.get(i).getNombre() + "| Correo: " + listAgenda.get(i).getCorreo() + "| Telefono: " + listAgenda.get(i).getTelefono());
        }
        return true;
    }

    /**
     * Metodo para buscar un contacto por el nombre
     *
     * @return
     */
    public static Contacto search() {
        System.out.println("-----------------------------------");
        System.out.println("--- Buscar Contacto ---");
        System.out.println("* Ingrese el nombre: ");
        teclado = new Scanner(System.in);
        String nombre = teclado.nextLine();
        for (Contacto c : listAgenda) {
            if (c.getNombre().equals(nombre)) {
                return c;
            }
        }
        return null;
    }

    /**
     * Metodo para mostrar el contacto por el nombre
     *
     * @param search
     */
    public static void mostrar(Contacto search) {
        //System.out.println("-----------------------------------");
        //System.out.println("Buscar Contacto");
        //System.out.println("Ingrese el nombre: ");
        if (search != null) {
            System.out.println();
            System.out.println(" --- Contacto encontrado --- ");
            System.out.println();
            System.out.println("Nombre: " + search.getNombre() + "| Correo: " + search.getCorreo() + "| Telefono: " + search.getTelefono());
        } else {
            System.out.println("--- El contacto no existe ---");
        }
    }

    /**
     * Metodo para actualizar un contacto
     */
    public static void update() {
        System.out.println("-----------------------------------");
        System.out.println("--- Actualizar Contacto ---");
        Contacto ca = search();
        if (ca != null) {
            if (add()) {
                listAgenda.remove(ca);
                System.out.println("--- Contacto actualizado ---");
                System.out.println("Liste los contactos para ver los cambios");
            }
        } else {
            System.out.println(" --- No existe el contacto --- ");
        }
    }

    /**
     * Metodo para borrar un contacto buscado por el nombre
     */
    public static void delete() {
        Contacto borrar = search();
        if (borrar != null) {
            listAgenda.remove(borrar);
            System.out.println("--- Contacto eliminado ---");
        } else {
            System.out.println("--- El contacto no existe ---");
        }
    }
}


