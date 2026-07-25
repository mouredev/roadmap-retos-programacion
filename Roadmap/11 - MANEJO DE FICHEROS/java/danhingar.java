import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class danhingar {

    public static void main(String[] args) throws IOException {
        try {
            String content = """
                    Nombre:   Daniel
                    Edad:     27
                    Lenguaje: Java
                    """;

            Path path = Path.of("danhingar.txt");
            Files.writeString(path, content);

            Files.readAllLines(path).forEach(line -> System.out.println(line));

            Files.delete(path);
        } catch (Exception e) {
            System.out.println("Se ha producido un error");
        }

        salesManager();
    }

    List<Product> products = new ArrayList<>();

    // Extra
    private static void salesManager() throws IOException {
        Path path = Path.of("stockManager1.txt");
        Files.writeString(path, "");
        while (Boolean.TRUE) {
            Scanner sc = new Scanner(System.in);
            System.out.println("1. Añadir producto");
            System.out.println("2. Consultar producto");
            System.out.println("3. Actualizar producto");
            System.out.println("4. Eliminar producto");
            System.out.println("5. Mostrar productos");
            System.out.println("6. Calcular venta total");
            System.out.println("7. Calcular venta total por producto");
            System.out.println("8. Salir");
            System.out.print("Selecciona una opción: ");
            String option = sc.nextLine();
            switch (option) {
                case "1":
                    System.out.print("Nombre: ");
                    String name = sc.nextLine();
                    System.out.print("Cantidad: ");
                    String quantity = sc.nextLine();
                    System.out.print("Precio: ");
                    String price = sc.nextLine();
                    String product = String.format("%s, %s, %s \n", name, quantity, price);
                    Files.writeString(path, product, StandardOpenOption.APPEND);
                    break;
                case "2":
                    System.out.print("Buscar el producto: ");
                    String searchName = sc.nextLine();
                    String[] result = Files.readAllLines(path).stream().map(r -> r.trim().split(","))
                            .filter(array -> array[0].equalsIgnoreCase(searchName)).findFirst().orElse(null);
                    System.out.println(result != null ? String.format("%s,%s,%s", result[0], result[1], result[2])
                            : "No existe el producto " + searchName);
                    break;
                case "3":
                    System.out.print("Nombre: ");
                    String name1 = sc.nextLine();
                    System.out.print("Cantidad: ");
                    String quantity1 = sc.nextLine();
                    System.out.print("Precio: ");
                    String price1 = sc.nextLine();
                    String content = "";
                    for (String line : Files.readAllLines(path)) {
                        if (line.trim().split(",")[0].equalsIgnoreCase(name1)) {
                            content = content.concat(String.format("%s, %s, %s \n", name1, quantity1, price1));
                        } else {
                            content = content.concat(line + "\n");
                        }
                    }
                    Files.writeString(path, content);
                    break;
                case "4":
                    System.out.print("Eliminar el producto: ");
                    String deleteName = sc.nextLine();
                    String lines = Files.readAllLines(path).stream().map(r -> r.trim().split(","))
                            .filter(array -> !array[0].equalsIgnoreCase(deleteName))
                            .map(x -> String.format("%s, %s, %s \n", x[0], x[1], x[2])).reduce(String::concat)
                            .orElse("");
                    Files.writeString(path, lines);
                    break;
                case "5":
                    Files.readAllLines(path).forEach(line -> System.out.println(line));
                    break;
                case "6":
                    Double totalSales = Files.readAllLines(path).stream().map(l -> l.trim().split(","))
                            .map(h -> Double.parseDouble(h[1]) * Double.parseDouble(h[2]))
                            .mapToDouble(Double::doubleValue).sum();
                    System.out.println("Ventas totales: " + totalSales);
                    break;
                case "7":
                    System.out.print("Nombre el producto: ");
                    String nameProduct = sc.nextLine();
                    Files.readAllLines(path).stream().map(l -> l.trim().split(","))
                            .filter(array -> array[0].equalsIgnoreCase(nameProduct))
                            .forEach(element-> System.out.println("Ventas totales de " +nameProduct+" : " + Double.parseDouble(element[1]) * Double.parseDouble(element[2])));
                    break;
                case "8":
                    sc.close();
                    Files.delete(path);
                    System.exit(0);
                    break;

                default:
                    System.out.println("Opción no válida");
                    break;
            }
        }
    }
}
