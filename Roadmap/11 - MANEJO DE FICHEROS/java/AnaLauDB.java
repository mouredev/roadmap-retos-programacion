import java.io.*;
import java.util.*;

public class AnaLauDB {
    private static final String ARCHIVO_USUARIO = "AnaLauDB.txt";
    private static final String ARCHIVO_VENTAS = "ventas.txt";

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\n=== MENÚ PRINCIPAL ===");
            System.out.println("1. Versión básica (archivo con datos personales)");
            System.out.println("2. Versión extra (gestor de ventas)");
            System.out.println("3. Salir");
            System.out.print("Elige una opción: ");
            opcion = sc.nextInt();
            sc.nextLine(); // limpiar buffer

            switch (opcion) {
                case 1 -> versionBasica();
                case 2 -> gestorVentas(sc);
                case 3 -> System.out.println("Adiós");
                default -> System.out.println("Opción no válida.");
            }
        } while (opcion != 3);

        sc.close();
    }

    // -------------------- VERSIÓN BÁSICA --------------------
    private static void versionBasica() {
        try {
            File file = new File(ARCHIVO_USUARIO);

            // 1. Crear archivo
            if (file.createNewFile()) {
                System.out.println("Archivo creado: " + file.getName());
            } else {
                System.out.println("El archivo ya existía, será sobrescrito.");
            }

            // 2. Escribir datos
            FileWriter writer = new FileWriter(file);
            writer.write("Nombre: Laura Ana\n");
            writer.write("Edad: 25\n");
            writer.write("Lenguaje favorito: Java\n");
            writer.close();

            // 3. Leer contenido
            System.out.println("\nContenido del archivo:");
            BufferedReader reader = new BufferedReader(new FileReader(file));
            String linea;
            while ((linea = reader.readLine()) != null) {
                System.out.println(linea);
            }
            reader.close();

            // 4. Borrar archivo
            if (file.delete()) {
                System.out.println("\nArchivo borrado: " + file.getName());
            } else {
                System.out.println("No se pudo borrar el archivo.");
            }

        } catch (IOException e) {
            System.out.println("Ocurrió un error: " + e.getMessage());
        }
    }

    // -------------------- VERSIÓN EXTRA: GESTOR DE VENTAS --------------------
    private static void gestorVentas(Scanner sc) {
        int opcion;
        do {
            System.out.println("\n=== GESTOR DE VENTAS ===");
            System.out.println("1. Añadir producto");
            System.out.println("2. Consultar productos");
            System.out.println("3. Actualizar producto");
            System.out.println("4. Eliminar producto");
            System.out.println("5. Calcular venta total");
            System.out.println("6. Calcular venta por producto");
            System.out.println("7. Salir del gestor (borra archivo)");
            System.out.print("Elige una opción: ");
            opcion = sc.nextInt();
            sc.nextLine(); // limpiar buffer

            switch (opcion) {
                case 1 -> anadirProducto(sc);
                case 2 -> consultarProductos();
                case 3 -> actualizarProducto(sc);
                case 4 -> eliminarProducto(sc);
                case 5 -> calcularVentaTotal();
                case 6 -> calcularVentaPorProducto(sc);
                case 7 -> salirGestor();
                default -> System.out.println("Opción no válida.");
            }
        } while (opcion != 7);
    }

    // ---------------- Métodos del gestor ----------------
    private static void anadirProducto(Scanner sc) {
        try (FileWriter fw = new FileWriter(ARCHIVO_VENTAS, true)) {
            System.out.print("Nombre producto: ");
            String nombre = sc.nextLine();
            System.out.print("Cantidad vendida: ");
            int cantidad = sc.nextInt();
            System.out.print("Precio unitario: ");
            double precio = sc.nextDouble();
            sc.nextLine();

            fw.write(nombre + ", " + cantidad + ", " + precio + "\n");
            System.out.println("✅ Producto añadido.");
        } catch (IOException e) {
            System.out.println(" Error al escribir en archivo: " + e.getMessage());
        }
    }

    private static void consultarProductos() {
        try (BufferedReader br = new BufferedReader(new FileReader(ARCHIVO_VENTAS))) {
            System.out.println("\n--- Productos ---");
            String linea;
            while ((linea = br.readLine()) != null) {
                System.out.println(linea);
            }
        } catch (IOException e) {
            System.out.println(" No hay productos o error leyendo archivo.");
        }
    }

    private static void actualizarProducto(Scanner sc) {
        System.out.print("Nombre del producto a actualizar: ");
        String nombre = sc.nextLine();
        List<String> lineas = new ArrayList<>();
        boolean encontrado = false;

        try (BufferedReader br = new BufferedReader(new FileReader(ARCHIVO_VENTAS))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                if (linea.startsWith(nombre + ",")) {
                    encontrado = true;
                    System.out.print("Nueva cantidad: ");
                    int cantidad = sc.nextInt();
                    System.out.print("Nuevo precio: ");
                    double precio = sc.nextDouble();
                    sc.nextLine();
                    lineas.add(nombre + ", " + cantidad + ", " + precio);
                } else {
                    lineas.add(linea);
                }
            }
        } catch (IOException e) {
            System.out.println(" Error: " + e.getMessage());
            return;
        }

        if (!encontrado) {
            System.out.println(" Producto no encontrado.");
            return;
        }

        try (FileWriter fw = new FileWriter(ARCHIVO_VENTAS)) {
            for (String l : lineas) {
                fw.write(l + "\n");
            }
            System.out.println("✅ Producto actualizado.");
        } catch (IOException e) {
            System.out.println(" Error escribiendo archivo: " + e.getMessage());
        }
    }

    private static void eliminarProducto(Scanner sc) {
        System.out.print("Nombre del producto a eliminar: ");
        String nombre = sc.nextLine();
        List<String> lineas = new ArrayList<>();
        boolean eliminado = false;

        try (BufferedReader br = new BufferedReader(new FileReader(ARCHIVO_VENTAS))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                if (linea.startsWith(nombre + ",")) {
                    eliminado = true;
                } else {
                    lineas.add(linea);
                }
            }
        } catch (IOException e) {
            System.out.println(" Error: " + e.getMessage());
            return;
        }

        if (!eliminado) {
            System.out.println(" Producto no encontrado.");
            return;
        }

        try (FileWriter fw = new FileWriter(ARCHIVO_VENTAS)) {
            for (String l : lineas) {
                fw.write(l + "\n");
            }
            System.out.println("✅ Producto eliminado.");
        } catch (IOException e) {
            System.out.println(" Error escribiendo archivo: " + e.getMessage());
        }
    }

    private static void calcularVentaTotal() {
        double total = 0;
        try (BufferedReader br = new BufferedReader(new FileReader(ARCHIVO_VENTAS))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                String[] partes = linea.split(", ");
                int cantidad = Integer.parseInt(partes[1]);
                double precio = Double.parseDouble(partes[2]);
                total += cantidad * precio;
            }
            System.out.println("💰 Venta total: " + total);
        } catch (IOException e) {
            System.out.println(" Error: " + e.getMessage());
        }
    }

    private static void calcularVentaPorProducto(Scanner sc) {
        System.out.print("Nombre del producto: ");
        String nombre = sc.nextLine();
        double total = 0;
        try (BufferedReader br = new BufferedReader(new FileReader(ARCHIVO_VENTAS))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                String[] partes = linea.split(", ");
                if (partes[0].equals(nombre)) {
                    int cantidad = Integer.parseInt(partes[1]);
                    double precio = Double.parseDouble(partes[2]);
                    total += cantidad * precio;
                }
            }
            System.out.println("💰 Venta total de " + nombre + ": " + total);
        } catch (IOException e) {
            System.out.println(" Error: " + e.getMessage());
        }
    }

    private static void salirGestor() {
        File file = new File(ARCHIVO_VENTAS);
        if (file.exists() && file.delete()) {
            System.out.println(" Archivo de ventas borrado. ¡Hasta pronto!");
        } else {
            System.out.println("No había archivo que borrar.");
        }
    }
}
