package MauroDevRetos;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class reto_10 {
    public static List<productos> listaproductos = new ArrayList<>();
    public static Scanner input = new Scanner(System.in);
    public static String fileName2 = "producto.txt";

    public static void main(String[] args) {

        String githubUsername = "julian98789";
        String fileName = githubUsername + ".txt";

        String name = "julian";
        int age = 19;
        String favoriteProgrammingLanguage = "Java";

        // Crear el archivo y escribir en él
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            writer.write("Nombre: " + name + "\n");
            writer.write("Edad: " + age + "\n");
            writer.write("Lenguaje de programación favorito: " + favoriteProgrammingLanguage + "\n");
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Leer e imprimir el contenido del archivo
        File file = new File(fileName);
        try (java.util.Scanner scanner = new java.util.Scanner(file)) {
            while (scanner.hasNextLine()) {
                System.out.println(scanner.nextLine());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Borrar el archivo
        if (file.delete()) {
            System.out.println("El archivo " + fileName + " ha sido borrado exitosamente.");
        } else {
            System.out.println("Error al borrar el archivo " + fileName);
        }

        boolean entrar = true;
        while (entrar) {
            System.out.println("\n ******* productos *******\n");
            System.out.println("1. agregar producto");
            System.out.println("2. consultar producto");
            System.out.println("3. actualizar producto");
            System.out.println("4. eliminar producto");
            System.out.println("5. calcular venta total ");
            System.out.println("6. salir \n");

            int opcion = input.nextInt();
            switch (opcion) {
                case 1:
                    agregarProducto();
                    break;
                case 2:
                    consultarProductos();
                    break;
                case 3:
                    actualizarProducto();

                    break;
                case 4:
                    eliminarProducto();

                    break;
                case 5:
                    calcularVentaTotal();

                    break;
                case 6:
                File file2 = new File(fileName2);
                if (file2.delete()) {
                    System.out.println("El archivo " + fileName2 + " ha sido borrado exitosamente.");
                } else {
                    System.out.println("Error al borrar el archivo " + fileName2);
                }
                entrar = false;
                    break;

                default:
                    break;
            }
        }

    }

   
  

    private static void agregarProducto() {

        System.out.println("Cantidad vendida: ");
        int cantidad = input.nextInt();
        input.nextLine();

        System.out.println("Nombre del producto: ");
        String name = input.nextLine();

        System.out.println("Precio: ");
        int precio = input.nextInt();
        input.nextLine();

        productos agrgarProductos = new productos(name, cantidad, precio);
        listaproductos.add(agrgarProductos);

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName2, true))) {
            writer.write("Nombre: " + name + "\n");
            writer.write("Cantidad vendida: " + cantidad + "\n");
            writer.write("Precio: " + precio + "\n");
            writer.write("-------------------------\n");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void consultarProductos() {
        File file = new File(fileName2);
        try (java.util.Scanner scanner = new java.util.Scanner(file)) {
            while (scanner.hasNextLine()) {
                System.out.println(scanner.nextLine());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void actualizarProducto() {
        System.out.println("Cantidad vendida: ");
        int cantidad = input.nextInt();
        input.nextLine();

        System.out.println("Nombre del producto: ");
        String name = input.nextLine();

        System.out.println("Precio: ");
        int precio = input.nextInt();
        input.nextLine();

        List<String> contenidoActual = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader("fileName"))) {
            String linea;
            while ((linea = reader.readLine()) != null) {
                contenidoActual.add(linea);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        contenidoActual.add("Nombre: " + name);
        contenidoActual.add("Cantidad vendida: " + cantidad);
        contenidoActual.add("Precio: " + precio);
        contenidoActual.add("-------------------------");

        // Escribir el contenido actualizado de nuevo en el archivo
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName2))) {
            for (String linea : contenidoActual) {
                writer.write(linea);
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private static void eliminarProducto() {
        input.nextLine();
        System.out.println("Nombre del producto a eliminar: ");
        String nombreAEliminar = input.nextLine();

        List<String> contenidoActual = new ArrayList<>();
        boolean encontrado = false;

        try (BufferedReader reader = new BufferedReader(new FileReader(fileName2))) {
            String linea;
            while ((linea = reader.readLine()) != null) {
                if (linea.startsWith("Nombre: " + nombreAEliminar)) {
                    encontrado = true;
                    reader.readLine();
                    reader.readLine();
                    reader.readLine();
                } else {
                    contenidoActual.add(linea);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        if (encontrado) {
            try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName2))) {
                for (String linea : contenidoActual) {
                    writer.write(linea);
                    writer.newLine();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
            System.out.println("El producto '" + nombreAEliminar + "' ha sido eliminado.");
        } else {
            System.out.println("El producto '" + nombreAEliminar + "' no fue encontrado.");
        }
    }
    private static void calcularVentaTotal() {
        int ventaTotal = 0;
        int vetaPorProducto = 0;

        try (BufferedReader reader = new BufferedReader(new FileReader(fileName2))) {
            String linea;
            while ((linea = reader.readLine()) != null) {
                if (linea.startsWith("Cantidad vendida: ")) {
                    int cantidad = Integer.parseInt(linea.split(": ")[1]);
                    linea = reader.readLine(); // Leer la línea del precio
                    int precio = Integer.parseInt(linea.split(": ")[1]);
                    ventaTotal += cantidad * precio;
                    vetaPorProducto = cantidad * precio;;
                    String name = (linea.split(": ")[1]);

                    System.out.println("veta total potr ptoducto: " + name +": " + vetaPorProducto);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("La venta total es: " + ventaTotal);
    }
 }


class productos {
    private String name;
    private int cantidad;
    private int precio;

    public productos(String name, int cantidad, int precio) {
        this.name = name;
        this.cantidad = cantidad;
        this.precio = precio;
    }
}
