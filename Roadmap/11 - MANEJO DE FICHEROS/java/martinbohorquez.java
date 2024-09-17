/**
 * #11 MANEJO DE FICHEROS
 *
 * @author martinbohorquez
 */

import java.io.*;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class martinbohorquez {
    protected static FileOperation operation = new FileOperation();
    private static String process;
    private static Scanner scanner = new Scanner(System.in);
    private static File venta;

    public static void main(String[] args) {
        String stringFile = "src/data.txt";
        String string = """
                Nombre: Martin
                Edad: 29
                Lenguaje de programación: Java
                """;
        testFile(stringFile, string);

        /*
         * DIFICULTAD EXTRA
         */
        String fileString = "src/venta.txt";
        salesManager(fileString);
    }

    private static void testFile(String stringFile, String string) {
        File file = operation.create(stringFile);
        operation.write(file, string);
        operation.read(file);
        operation.delete(file);
    }

    private static void salesManager(String fileString) {
        outterlooper:
        while (true) {
            System.out.print("""
                    =========================================
                    ***** PROGRAMA DE GESTIÓN DE VENTAS *****
                    1. Añadir producto
                    2. Mostar productos
                    3. Consultar producto
                    4. Actualizar producto
                    5. Borrar producto
                    6. Calcular venta total
                    7. Calcular venta por producto
                    8. Salir
                    """);
            System.out.print("Selecciona la opción (1, 2, 3, 4, 5, 6, 7, 8): ");
            String option = scanner.next();
            Product product = new Product();
            switch (option) {
                case "1" -> {
                    product.add(fileString);
                }
                case "2" -> product.read(venta);
                case "3" -> product.consultar(venta);
                case "4" -> product.actualizar(venta);
                case "5" -> product.delete(venta);
                case "6" -> product.calcularVentaTotal(venta);
                case "7" -> product.calcularVenta(venta);
                case "8" -> {
                    product.deleteAll(venta);
                    System.out.println("Saliendo del programa de gestión de ventas!");
                    break outterlooper;
                }
                default -> System.out.println("Debe seleccionar un número de opción válido!");
            }
        }
    }

    protected static class FileOperation {

        private File create(String string) {
            File file = new File(string);
            if (file.getParentFile() != null) file.getParentFile().mkdirs();// Crear la carpeta si no existe
            return file;
        }

        private void write(File file, String string) {
            process = "escribir";
            try (FileWriter writer = new FileWriter(file, true); Scanner reader = new Scanner(file)) {
                writer.append(string).append(System.lineSeparator());
                if (!reader.hasNext()) System.out.printf("Archivo '%s' creado!%n", file.toString());
                else System.out.printf("Archivo '%s' modificado!%n", file.toString());
            } catch (IOException e) {
                printfException(e);
            }
        }

        private void read(File file) {
            process = "leer";
            if (file != null) {
                try (Scanner reader = new Scanner(file)) {
                    System.out.println("Contenido del archivo: ");
                    while (reader.hasNext()) System.out.println(reader.nextLine());
                } catch (FileNotFoundException e) {
                    printfException(e);
                }
            } else System.out.println("El archivo se encuentra vacío, no tiene registros!");
        }

        private void delete(File file) {
            process = "eliminar";
            if (file != null && file.delete()) {
                if (file.getParentFile() != null && file.getParentFile().delete())
                    System.out.printf("Folder '\\%s' eliminado correctamente!%n", file.getParentFile().toString());
                System.out.printf("Archivo '%s' eliminado correctamente!%n", file.toString());
            }
        }

        private void printfException(IOException e) {
            System.out.printf("Error al '%s' en el archivo: '%s'%n", process, e.getMessage());
        }
    }

    private static class Product {
        private String name;
        private Integer quantity;
        private Float price;

        public Product() {
        }

        public Float getPrice() {
            return price;
        }

        public void setPrice(Float price) {
            this.price = price;
        }

        public Integer getQuantity() {
            return quantity;
        }

        public void setQuantity(Integer quantity) {
            this.quantity = quantity;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        @Override
        public String toString() {
            return getName() + ", " + getQuantity() + ", " + getPrice();
        }

        public void add(String fileString) {
            System.out.print("Ingresar el nombre de producto: ");
            setName(scanner.next());
            add(fileString, getName());
        }

        public void add(String fileString, String name) {
            if (!contains(venta, name)) {
                if (venta == null) venta = operation.create(fileString);
                setName(name);
                System.out.print("Ingresar la cantidad vendida(unidades): ");
                setQuantity(scanner.nextInt());
                System.out.print("Ingresar el precio unitario de producto($): ");
                setPrice(scanner.nextFloat());
                operation.write(venta, toString());
            } else System.out.printf("El producto %s ya está registrado, usar la opción de actualizar!%n", name);
        }

        private boolean contains(File venta, String productName) {
            process = "contains";
            if (venta == null) return false;
            try (Scanner reader = new Scanner(venta)) {
                while (reader.hasNext()) {
                    String productF = reader.nextLine();
                    String productNameF = productF.substring(0, productF.indexOf(","));
                    if (productNameF.equals(productName)) return true;
                }
            } catch (FileNotFoundException e) {
                operation.printfException(e);
            }
            return false;
        }

        private void read(File venta) {
            operation.read(venta);
        }

        private void consultar(File venta) {
            process = "consultar";
            outterlooper:
            if (venta != null) {
                try (Scanner reader = new Scanner(venta)) {
                    System.out.print("Introduce el nombre de producto que desea consultar: ");
                    String productName = scanner.next();
                    while (reader.hasNext()) {
                        String productF = reader.nextLine();
                        String productNameF = productF.substring(0, productF.indexOf(","));
                        if (productNameF.equals(productName)) {
                            System.out.println(productF);
                            break outterlooper;
                        }
                    }
                    System.out.printf("El producto '%s' no se encuentra en el registro de ventas!%n", productName);
                } catch (FileNotFoundException e) {
                    operation.printfException(e);
                }
            } else System.out.println("El archivo se encuentra vacío, no tiene registros!");
        }

        private void actualizar(File venta) {
            process = "actualizar";
            outterlooper:
            if (venta != null) {
                List<String> fileContent = new LinkedList<>();
                System.out.print("Introduce el nombre de producto que desea actualizar: ");
                setName(scanner.next());
                if (contains(venta, getName())) {
                    try (BufferedReader reader = new BufferedReader(new FileReader(venta))) {
                        String line;
                        System.out.print("Ingresar la cantidad vendida(unidades): ");
                        setQuantity(scanner.nextInt());
                        System.out.print("Ingresar el precio unitario de producto($): ");
                        setPrice(scanner.nextFloat());

                        while ((line = reader.readLine()) != null) {
                            if (line.contains(getName())) line = toString();
                            fileContent.add(line); // Añadimos la línea (modificada o no) a la lista
                        }
                    } catch (IOException e) {
                        operation.printfException(e);
                    }
                    // Reescribimos el archivo con el contenido actualizado
                    try (BufferedWriter writer = new BufferedWriter(new FileWriter(venta))) {
                        for (String fila : fileContent) writer.append(fila).append(System.lineSeparator());
                        System.out.printf("El producto '%s' se ha actualizado correctamente!%n", getName());
                    } catch (IOException e) {
                        operation.printfException(e);
                    }
                } else {
                    System.out.printf("El producto '%s' no se encuentra en el registro de ventas!%n", getName());
                }
            } else System.out.println("El archivo se encuentra vacío, no tiene registros!");
        }

        public void delete(File venta) {
            process = "eliminar producto";
            outterlooper:
            if (venta != null) {
                List<String> fileContent = new LinkedList<>();
                System.out.print("Introduce el nombre de producto que desea eliminar: ");
                setName(scanner.next());
                if (contains(venta, getName())) {
                    try (BufferedReader reader = new BufferedReader(new FileReader(venta))) {
                        String line;
                        while ((line = reader.readLine()) != null) {
                            if (line.contains(getName())) line = null;
                            fileContent.add(line); // Añadimos la línea (modificada o no) a la lista
                        }
                    } catch (IOException e) {
                        operation.printfException(e);
                    }
                    // Reescribimos el archivo con el contenido actualizado
                    try (BufferedWriter writer = new BufferedWriter(new FileWriter(venta))) {
                        for (String fila : fileContent) {
                            if (fila != null) writer.append(fila).append(System.lineSeparator());
                        }
                        System.out.printf("El producto '%s' se ha eliminado correctamente!%n", getName());
                    } catch (IOException e) {
                        operation.printfException(e);
                    }
                } else {
                    System.out.printf("El producto '%s' no se encuentra en el registro de ventas!%n", getName());
                }
            } else System.out.println("El archivo se encuentra vacío, no tiene registros!");
        }

        public void calcularVentaTotal(File venta) {
            process = "calcularVentaTotal";
            Double calcularTotal = 0.0;
            if (venta != null) {
                try (Scanner reader = new Scanner(venta)) {
                    while (reader.hasNext()) {
                        String productF = reader.nextLine();
                        Double productQuantityF = Double.parseDouble(productF.substring(productF.indexOf(",") + 2,
                                productF.lastIndexOf(",")));
                        Double productPriceF = Double.parseDouble(productF.
                                substring(productF.lastIndexOf(",") + 2));
                        calcularTotal += productQuantityF * productPriceF;
                    }
                    System.out.printf("La venta total: %.2f%n", calcularTotal);
                } catch (FileNotFoundException e) {
                    operation.printfException(e);
                }
            } else System.out.println("El archivo se encuentra vacío, no tiene registros!");
        }

        public void calcularVenta(File venta) {
            process = "calcularVenta";
            Double calcular = 0.0;
            if (venta != null) {
                try (Scanner reader = new Scanner(venta)) {
                    System.out.print("Introduce el nombre de producto que desea consultar: ");
                    String productName = scanner.next();
                    while (reader.hasNext()) {
                        String productF = reader.nextLine();
                        String productNameF = productF.substring(0, productF.indexOf(","));
                        if (productNameF.equals(productName)) {
                            Double productQuantityF = Double.parseDouble(productF.substring(productF.indexOf(",") + 2,
                                    productF.lastIndexOf(",")));
                            Double productPriceF = Double.parseDouble(productF.
                                    substring(productF.lastIndexOf(",") + 2));
                            calcular = productQuantityF * productPriceF;
                        }
                    }
                    System.out.printf("La venta total del producto '%s': %.2f%n", productName, calcular);
                } catch (FileNotFoundException e) {
                    operation.printfException(e);
                }
            } else System.out.println("El archivo se encuentra vacío, no tiene registros!");
        }

        private void deleteAll(File venta) {
            operation.delete(venta);
        }
    }
}
