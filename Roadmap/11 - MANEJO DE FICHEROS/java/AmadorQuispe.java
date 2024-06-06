import java.io.IOException;
import java.math.BigDecimal;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.text.DecimalFormat;
import java.util.List;
import java.util.Scanner;

public class ManagerFile {
    public static void main(String[] args) {
        try {
            basic();
            extra();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    /*
     * EJERCICIO:
     * Desarrolla un programa capaz de crear un archivo que se llame como
     * tu usuario de GitHub y tenga la extensión .txt.
     * Añade varias líneas en ese fichero:
     * - Tu nombre.
     * - Edad.
     * - Lenguaje de programación favorito.
     * Imprime el contenido.
     * Borra el fichero.
     * 
     */
    private static void basic() throws IOException {
        Path path = Path.of("AmadorQuispe.txt");
        if (!Files.exists(path)) {
            Files.createFile(path);
        }
        String content = """
                Nombre                             : Amador Quispe
                Edad                               : 31 Años
                Lenguaje de Programación Favorito  : Java
                """;
        Files.writeString(path, content);
        List<String> data = Files.readAllLines(path);
        data.forEach(System.out::println);
        Files.delete(path);
    }

    /*
     * DIFICULTAD EXTRA (opcional):
     * Desarrolla un programa de gestión de ventas que almacena sus datos en un
     * archivo .txt.
     * - Cada producto se guarda en una línea del archivo de la siguiente manera:
     * [nombre_producto], [cantidad_vendida], [precio].
     * - Siguiendo ese formato, y mediante terminal, debe permitir añadir,
     * consultar,
     * actualizar, eliminar productos y salir.
     * - También debe poseer opciones para calcular la venta total y por producto.
     * - La opción salir borra el .txt.
     */
    private static void extra() throws IOException {
        Path path = Path.of("sales.txt");
        if (!Files.exists(path)) {
            path = Files.createFile(path);
        }

        SalesManager salesManager = new SalesManager(path);
        salesManager.init();
    }

}

/**
 * SalesManager
 */
class SalesManager {
    private Path path;
    private Scanner scanner;
    private String regex;

    public SalesManager(Path path) {
        this.path = path;
        this.scanner = new Scanner(System.in);
        this.regex = "^(\\w+)\\|(\\d+(\\.\\d+)?)\\|(\\d+(\\.\\d+)?)$";
    }

    public void init() {
        boolean exit = false;
        int opt = 0;
        while (!exit) {
            System.out.println("--------------------------------");
            System.out.println("-------------OPCIONES------------");
            System.out.println("--------------------------------");
            System.out.println("1 - Mostrar todos los productos");
            System.out.println("2 - Añadir producto");
            System.out.println("3 - Consultar producto");
            System.out.println("4 - Actualizar producto");
            System.out.println("5 - Eliminar producto");
            System.out.println("6 - Calcular venta total");
            System.out.println("7 - Calcular venta total por producto");
            System.out.println("8 - Salir");
            System.out.print("\nElija la operación a realizar: ");

            if (scanner.hasNextInt()) {
                opt = scanner.nextInt();
            }

            switch (opt) {
                case 1:
                    try (Scanner sc = new Scanner(path)) {
                        while (sc.hasNext()) {
                            System.out.println(sc.next());
                        }
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                    break;
                case 2:
                    StringBuffer line = new StringBuffer();
                    System.out.print("Ingrese el nombre del producto: ");
                    line.append(scanner.next()).append("|");
                    System.out.print("Ingrese la cantidad vendida: ");
                    line.append(scanner.next()).append("|");
                    System.out.print("Ingrese el precio: ");
                    line.append(scanner.next());
                    addProduct(line.toString());
                    break;
                case 3:
                    System.out.print("Ingrese el nombre del producto a buscar: ");
                    String search = scanner.next();
                    searchProduct(search);
                    break;
                case 4:
                    // TODO : En caso no exista
                    StringBuffer lineUpdate = new StringBuffer();
                    System.out.print("Ingrese el nombre del producto a modificar: ");
                    String nameProductUpdate = scanner.next();
                    System.out.print("Ingrese el nuevo nombre del producto: ");
                    lineUpdate.append(scanner.next()).append("|");
                    System.out.print("Ingrese la nueva cantidad vendida: ");
                    lineUpdate.append(scanner.next()).append("|");
                    System.out.print("Ingrese el nuevo precio: ");
                    lineUpdate.append(scanner.next());
                    updateProduct(nameProductUpdate, lineUpdate.toString());
                    break;
                case 5:
                    System.out.print("Ingrese el nombre del producto a eliminar: ");
                    String nameProductDelete = scanner.next();
                    deleteProduct(nameProductDelete);
                    break;
                case 6:
                    totalSales();
                    break;
                case 7:
                    salesPerProduct();
                    break;
                case 8:
                    exit = true;
                    destroy();
                    break;
                default:
                    System.out.println("\nNo se reconoce el comando, inténtelo de nuevo");
                    init();
                    break;
            }
        }
    }

    private void addProduct(String line) {
        try {
            if (!line.matches(regex)) {
                System.out.println("El formato no es correcto");
                return;
            }
            Files.writeString(path, line + "\n", StandardOpenOption.APPEND);

        } catch (IOException e) {
            System.out.println("Error al insertar el producto ");
        }
    }

    private void searchProduct(String productName) {
        try (Scanner read = new Scanner(path)) {
            read.useDelimiter("\n");
            while (read.hasNext()) {
                String next = read.next();
                String[] parts = next.split("\\|");
                if (parts[0].equalsIgnoreCase(productName)) {
                    System.out.println("\nProductos encontrados: " + productName);
                    System.out.println("Nombre producto | Cant. Vendida | Precio");
                    System.out.println("-> " + next);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void updateProduct(String productName, String updateLine) {
        StringBuilder content = new StringBuilder();
        try (Scanner read = new Scanner(path)) {
            read.useDelimiter("\n");
            while (read.hasNext()) {
                String next = read.next();
                String[] parts = next.split("\\|");
                if (parts[0].equals(productName)) {
                    content.append(updateLine).append("\n");
                } else {
                    content.append(next).append("\n");
                }
            }
            Files.writeString(path, content.toString());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void deleteProduct(String productName) {
        StringBuilder content = new StringBuilder();
        try (Scanner read = new Scanner(path)) {
            read.useDelimiter("\n");
            while (read.hasNext()) {
                String next = read.next();
                String[] parts = next.split("\\|");
                if (!parts[0].equals(productName)) {
                    content.append(next).append("\n");
                }
            }
            Files.writeString(path, content.toString());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void totalSales() {
        BigDecimal total = new BigDecimal(0);
        try (Scanner read = new Scanner(path)) {
            read.useDelimiter("\n");
            while (read.hasNext()) {
                String next = read.next();
                String[] parts = next.split("\\|");
                double price = Double.parseDouble(parts[2]);
                int quantity = Integer.parseInt(parts[1]);
                total = total.add(BigDecimal.valueOf(price * quantity));
            }
            System.out.println("TOTAL VENTAS :" + total.doubleValue());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void salesPerProduct() {
        try (Scanner read = new Scanner(path)) {
            read.useDelimiter("\n");
            System.out.println("--RESUMEN POR PRODUCTO--");
            System.out.println("Producto | Cant. Vendida | Total $");
            while (read.hasNext()) {
                String next = read.next();
                String[] parts = next.split("\\|");
                double price = Double.parseDouble(parts[2]);
                int quantity = Integer.parseInt(parts[1]);
                DecimalFormat f = new DecimalFormat("##.00");
                Double total = price * quantity;
                System.out.println(String.format("%s | %s | %s", parts[0], quantity, f.format(total)));
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void destroy() {
        scanner.close();
        try {
            Files.delete(path);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
