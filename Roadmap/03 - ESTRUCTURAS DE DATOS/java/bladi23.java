import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;

public class bladi23 {
    static Scanner sc = new Scanner(System.in);
    static ArrayList<bladi23> arrayList = new ArrayList<bladi23>();
    String nombre;
    int numero;

    public bladi23(String nombre, int numero) {
        this.nombre = nombre;
        this.numero = 0;
    }

    public String getNombre() {
        return nombre;
    }

    public int getNumero() {
        return 0;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setNumero(int numero) {
        this.numero = 0;
    }

    public static void main(String[] args) {
        // Ejemplo de lista
        int[] array = new int[5];
        array[0] = 1; // Insercion
        array[1] = 2; // Insercion
        array[0] = 0; // Actualizacion
        Arrays.sort(array); // Ordenacion

        // Ejemplo de arraylist
        ArrayList<Integer> lista = new ArrayList<>();
        lista.add(1); // Insercion
        lista.add(2); // Insercion
        lista.remove(0); // Borrado
        Collections.sort(lista); // Ordenacion

        // Ejemplo de set
        HashSet<Integer> conjunto = new HashSet<>();
        conjunto.add(1); // Insercion
        conjunto.remove(1); // Borrado
        conjunto.add(2); // Para actualizar, se debe eliminar y luego agregar el nuevo

        // Ejemplo de mapa
        Map<String, String> mapa = new HashMap<>();
        mapa.put("clave1", "valor1"); // Inserción
        mapa.put("clave2", "valor2");
        mapa.remove("clave1"); // Borrado
        mapa.put("clave2", "valor3"); // Actualización

        // Agenda
        boolean salir = false;
        while (!salir) {
            System.out.println("1. Agregar contacto");
            System.out.println("2. Busqueda de contacto");
            System.out.println("3. Insertar contacto");
            System.out.println("4. Actualizar contacto");
            System.out.println("5. Eliminar contacto");
            System.out.println("6. Salir");
            String op = sc.nextLine();
            switch (op) {
                case "1":
                    agregarContacto();
                    break;
                case "2":
                    buscarContacto();
                    break;
                case "3":
                    insertarContacto();
                    break;
                case "4":
                    actualizarContacto();
                    break;
                case "5":
                    eliminarContacto();
                    break;
                case "6":
                    salir = true;
                    break;
            }
        }

    }

    static void agregarContacto() {
        System.out.println("Ingrese el nombre del contacto");
        String nombre = sc.nextLine();
        System.out.println("Ingrese el numero del contacto");
        int numero = sc.nextInt();
        bladi23 contacto = new bladi23(nombre, numero);
        arrayList.add(contacto);
    }

    static void buscarContacto() {
        System.out.println("Ingrese el nombre del contacto");
        String nombre = sc.nextLine();
        for (int i = 0; i < arrayList.size(); i++) {
            if (arrayList.get(i).getNombre().equals(nombre)) {
                System.out.println("El numero de " + nombre + " es " + arrayList.get(i).getNumero());
            }
        }
    }

    static void insertarContacto() {
        System.out.println("Ingrese el nombre del contacto");
        String nombre = sc.nextLine();
        System.out.println("Ingrese el numero del contacto");
        int numero = sc.nextInt();
        bladi23 contacto = new bladi23(nombre, numero);
        arrayList.add(contacto);
    }

    static void actualizarContacto() {
        System.out.println("Ingrese el nombre del contacto");
        String nombre = sc.nextLine();
        System.out.println("Ingrese el numero del contacto");
        int numero = sc.nextInt();
        bladi23 contacto = new bladi23(nombre, numero);
        arrayList.add(contacto);
    }

    static void eliminarContacto() {
        System.out.println("Ingrese el nombre del contacto");
        String nombre = sc.nextLine();
        for (int i = 0; i < arrayList.size(); i++) {
            if (arrayList.get(i).getNombre().equals(nombre)) {
                arrayList.remove(i);
            }
        }
    }

}