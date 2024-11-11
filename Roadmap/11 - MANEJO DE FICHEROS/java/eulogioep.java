import java.io.*;
import java.util.*;

public class eulogioep {
    // Constantes para el nombre del archivo y el archivo de ventas
    private static final String FILENAME = "eulogioep.txt";
    private static final String SALES_FILENAME = "ventas.txt";

    public static void main(String[] args) {
        // Parte 1: Creación y manipulación de archivos
        crearArchivoPersonal();
        
        // Parte 2: Gestión de ventas (DIFICULTAD EXTRA)
        gestionVentas();
    }

    // Método para crear y manipular el archivo personal
    private static void crearArchivoPersonal() {
        try {
            // Creación del archivo
            FileWriter fw = new FileWriter(FILENAME);
            BufferedWriter bw = new BufferedWriter(fw);

            // Escritura en el archivo
            bw.write("Nombre: Eulogio");
            bw.newLine();
            bw.write("Edad: 30");
            bw.newLine();
            bw.write("Lenguaje de programación favorito: Java");
            bw.close();

            System.out.println("Archivo creado y escrito con éxito.");

            // Lectura y impresión del contenido
            BufferedReader br = new BufferedReader(new FileReader(FILENAME));
            String linea;
            System.out.println("Contenido del archivo:");
            while ((linea = br.readLine()) != null) {
                System.out.println(linea);
            }
            br.close();

            // Borrado del archivo
            File file = new File(FILENAME);
            if (file.delete()) {
                System.out.println("Archivo borrado con éxito.");
            } else {
                System.out.println("No se pudo borrar el archivo.");
            }
        } catch (IOException e) {
            System.out.println("Error de E/S: " + e.getMessage());
        }
    }

    // Método para la gestión de ventas
    private static void gestionVentas() {
        Scanner scanner = new Scanner(System.in);
        boolean salir = false;

        while (!salir) {
            System.out.println("\n--- Gestión de Ventas ---");
            System.out.println("1. Añadir producto");
            System.out.println("2. Consultar productos");
            System.out.println("3. Actualizar producto");
            System.out.println("4. Eliminar producto");
            System.out.println("5. Calcular venta total");
            System.out.println("6. Calcular venta por producto");
            System.out.println("7. Salir");
            System.out.print("Seleccione una opción: ");

            int opcion = scanner.nextInt();
            scanner.nextLine(); // Consumir el salto de línea

            switch (opcion) {
                case 1:
                    anadirProducto(scanner);
                    break;
                case 2:
                    consultarProductos();
                    break;
                case 3:
                    actualizarProducto(scanner);
                    break;
                case 4:
                    eliminarProducto(scanner);
                    break;
                case 5:
                    calcularVentaTotal();
                    break;
                case 6:
                    calcularVentaPorProducto(scanner);
                    break;
                case 7:
                    salir = true;
                    borrarArchivoVentas();
                    break;
                default:
                    System.out.println("Opción no válida.");
            }
        }
        scanner.close();
    }

    // Método para añadir un producto al archivo de ventas
    private static void anadirProducto(Scanner scanner) {
        try {
            FileWriter fw = new FileWriter(SALES_FILENAME, true);
            BufferedWriter bw = new BufferedWriter(fw);

            System.out.print("Nombre del producto: ");
            String nombre = scanner.nextLine();
            System.out.print("Cantidad vendida: ");
            int cantidad = scanner.nextInt();
            System.out.print("Precio: ");
            double precio = scanner.nextDouble();

            bw.write(String.format("%s, %d, %.2f", nombre, cantidad, precio));
            bw.newLine();
            bw.close();

            System.out.println("Producto añadido con éxito.");
        } catch (IOException e) {
            System.out.println("Error al añadir producto: " + e.getMessage());
        }
    }

    // Método para consultar los productos en el archivo de ventas
    private static void consultarProductos() {
        try {
            BufferedReader br = new BufferedReader(new FileReader(SALES_FILENAME));
            String linea;
            System.out.println("\nProductos:");
            while ((linea = br.readLine()) != null) {
                System.out.println(linea);
            }
            br.close();
        } catch (IOException e) {
            System.out.println("Error al consultar productos: " + e.getMessage());
        }
    }

    // Método para actualizar un producto en el archivo de ventas
    private static void actualizarProducto(Scanner scanner) {
        try {
            List<String> lineas = new ArrayList<>();
            BufferedReader br = new BufferedReader(new FileReader(SALES_FILENAME));
            String linea;
            while ((linea = br.readLine()) != null) {
                lineas.add(linea);
            }
            br.close();

            System.out.print("Nombre del producto a actualizar: ");
            String nombreActualizar = scanner.nextLine();

            boolean encontrado = false;
            for (int i = 0; i < lineas.size(); i++) {
                String[] partes = lineas.get(i).split(", ");
                if (partes[0].equals(nombreActualizar)) {
                    System.out.print("Nueva cantidad vendida: ");
                    int nuevaCantidad = scanner.nextInt();
                    System.out.print("Nuevo precio: ");
                    double nuevoPrecio = scanner.nextDouble();
                    lineas.set(i, String.format("%s, %d, %.2f", nombreActualizar, nuevaCantidad, nuevoPrecio));
                    encontrado = true;
                    break;
                }
            }

            if (encontrado) {
                FileWriter fw = new FileWriter(SALES_FILENAME);
                BufferedWriter bw = new BufferedWriter(fw);
                for (String l : lineas) {
                    bw.write(l);
                    bw.newLine();
                }
                bw.close();
                System.out.println("Producto actualizado con éxito.");
            } else {
                System.out.println("Producto no encontrado.");
            }
        } catch (IOException e) {
            System.out.println("Error al actualizar producto: " + e.getMessage());
        }
    }

    // Método para eliminar un producto del archivo de ventas
    private static void eliminarProducto(Scanner scanner) {
        try {
            List<String> lineas = new ArrayList<>();
            BufferedReader br = new BufferedReader(new FileReader(SALES_FILENAME));
            String linea;
            while ((linea = br.readLine()) != null) {
                lineas.add(linea);
            }
            br.close();

            System.out.print("Nombre del producto a eliminar: ");
            String nombreEliminar = scanner.nextLine();

            boolean encontrado = false;
            for (int i = 0; i < lineas.size(); i++) {
                String[] partes = lineas.get(i).split(", ");
                if (partes[0].equals(nombreEliminar)) {
                    lineas.remove(i);
                    encontrado = true;
                    break;
                }
            }

            if (encontrado) {
                FileWriter fw = new FileWriter(SALES_FILENAME);
                BufferedWriter bw = new BufferedWriter(fw);
                for (String l : lineas) {
                    bw.write(l);
                    bw.newLine();
                }
                bw.close();
                System.out.println("Producto eliminado con éxito.");
            } else {
                System.out.println("Producto no encontrado.");
            }
        } catch (IOException e) {
            System.out.println("Error al eliminar producto: " + e.getMessage());
        }
    }

    // Método para calcular la venta total
    private static void calcularVentaTotal() {
        try {
            BufferedReader br = new BufferedReader(new FileReader(SALES_FILENAME));
            String linea;
            double ventaTotal = 0;
            while ((linea = br.readLine()) != null) {
                String[] partes = linea.split(", ");
                int cantidad = Integer.parseInt(partes[1]);
                double precio = Double.parseDouble(partes[2]);
                ventaTotal += cantidad * precio;
            }
            br.close();
            System.out.printf("Venta total: %.2f\n", ventaTotal);
        } catch (IOException e) {
            System.out.println("Error al calcular venta total: " + e.getMessage());
        }
    }

    // Método para calcular la venta por producto
    private static void calcularVentaPorProducto(Scanner scanner) {
        try {
            System.out.print("Nombre del producto: ");
            String nombreProducto = scanner.nextLine();

            BufferedReader br = new BufferedReader(new FileReader(SALES_FILENAME));
            String linea;
            boolean encontrado = false;
            while ((linea = br.readLine()) != null) {
                String[] partes = linea.split(", ");
                if (partes[0].equals(nombreProducto)) {
                    int cantidad = Integer.parseInt(partes[1]);
                    double precio = Double.parseDouble(partes[2]);
                    double ventaProducto = cantidad * precio;
                    System.out.printf("Venta de %s: %.2f\n", nombreProducto, ventaProducto);
                    encontrado = true;
                    break;
                }
            }
            br.close();

            if (!encontrado) {
                System.out.println("Producto no encontrado.");
            }
        } catch (IOException e) {
            System.out.println("Error al calcular venta por producto: " + e.getMessage());
        }
    }

    // Método para borrar el archivo de ventas al salir
    private static void borrarArchivoVentas() {
        File file = new File(SALES_FILENAME);
        if (file.delete()) {
            System.out.println("Archivo de ventas borrado con éxito.");
        } else {
            System.out.println("No se pudo borrar el archivo de ventas.");
        }
    }
}