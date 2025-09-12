import java.io.*;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

import static java.lang.Double.parseDouble;

/**
 * #11 MANEJO DE FICHEROS
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    private static final FileOperation operation = new FileOperation();
    private static final Scanner scanner = new Scanner(System.in);
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
        boolean flag = true;
        while (flag) {
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
                case "1" -> product.add(fileString);
                case "2" -> product.read(venta);
                case "3" -> product.consultar(venta);
                case "4" -> product.update(venta);
                case "5" -> product.delete(venta);
                case "6" -> product.calcularVentaTotal(venta);
                case "7" -> product.calcularVenta(venta);
                case "8" -> {
                    product.deleteAll(venta);
                    System.out.println("Saliendo del programa de gestión de ventas!");
                    flag = false;
                }
                default -> System.out.println("Debe seleccionar un número de opción válido!");
            }
        }
    }

    private static void printFileEmpty() {
        System.out.println("El archivo se encuentra vacío, no tiene registros!");
    }

    private static void printfException(IOException e, String process) {
        System.out.printf("Error al '%s' en el archivo: '%s'%n", process, e.getMessage());
    }

    protected static class FileOperation {

        private File create(String string) {
            File file = new File(string);
            if (file.getParentFile() != null) file.getParentFile().mkdirs();// Crear la carpeta si no existe
            return file;
        }

        private void write(File file, String string) {
            try (FileWriter writer = new FileWriter(file, true); Scanner reader = new Scanner(file)) {
                writer.append(string).append(System.lineSeparator());
                if (!reader.hasNext()) System.out.printf("Archivo '%s' creado!%n", file);
                else System.out.printf("Archivo '%s' modificado!%n", file);
            } catch (IOException e) {
                printfException(e, "escribir");
            }
        }

        private void read(File file) {
            if (file == null || file.length() == 0) printFileEmpty();
            else {
                try (Scanner reader = new Scanner(file)) {
                    System.out.println("Contenido del archivo: ");
                    while (reader.hasNext()) System.out.println(reader.nextLine());
                } catch (FileNotFoundException e) {
                    printfException(e, "leer");
                }
            }
        }

        private void delete(File file) {
            if (file != null && file.delete()) {
                if (file.getParentFile() != null && file.getParentFile().delete())
                    System.out.printf("Folder '\\%s' eliminado correctamente!%n", file.getParentFile().toString());
                System.out.printf("Archivo '%s' eliminado correctamente!%n", file);
            }
        }
    }

    private static class Product {
        private String name;
        private Integer quantity;
        private Float price;

        private static void printProductNotFind(String name) {
            System.out.printf("El producto '%s' no se encuentra en el registro de ventas!%n", name);
        }

        private static void printWrongOperation(String name) {
            System.out.printf("La operación '%s' no es válida en este método!%n", name);
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
            setNameScanner("registrar");
            add(fileString, getName());
        }

        public void add(String fileString, String name) {
            if (!contains(venta, name)) {
                if (venta == null) venta = operation.create(fileString);
                setName(name);
                setQuantityAndPriceScan();
                operation.write(venta, toString());
            } else System.out.printf("El producto %s ya está registrado, usar la opción de actualizar!%n", name);
        }

        private void read(File venta) {
            if (venta == null || venta.length() == 0) printFileEmpty();
            else operation.read(venta);
        }

        private void consultar(File venta) {
            if (venta == null || venta.length() == 0) printFileEmpty();
            else {
                try (Scanner reader = new Scanner(venta)) {
                    boolean flag = true;
                    setNameScanner("consultar");
                    while (flag && reader.hasNext()) {
                        String productF = reader.nextLine();
                        String productNameF = productF.split(", ")[0];
                        if (productNameF.equals(getName())) {
                            System.out.println(productF);
                            flag = false;
                        }
                    }
                    if (flag) printProductNotFind(getName());
                } catch (FileNotFoundException e) {
                    printfException(e, "consultar");
                }
            }
        }

        private void update(File venta) {
            updateOrDelete(venta, "actualizar");
        }

        public void delete(File venta) {
            updateOrDelete(venta, "eliminar");
        }

        public void calcularVentaTotal(File venta) {
            if (venta == null || venta.length() == 0) printFileEmpty();
            else {
                try (Scanner reader = new Scanner(venta)) {
                    double calcularTotal = 0.0;
                    while (reader.hasNext()) {
                        String[] components = reader.nextLine().split(", ");
                        calcularTotal += parseDouble(components[1]) * parseDouble(components[2]);
                    }
                    System.out.printf("La venta total: %.2f%n", calcularTotal);
                } catch (FileNotFoundException e) {
                    printfException(e, "calcularVentaTotal");
                }
            }
        }

        public void calcularVenta(File venta) {
            if (venta == null || venta.length() == 0) printFileEmpty();
            else {
                try (Scanner reader = new Scanner(venta)) {
                    setNameScanner("consultar");
                    double calcular = 0.0;
                    while (reader.hasNext()) {
                        String[] components = reader.nextLine().split(", ");
                        if (components[0].equals(getName()))
                            calcular = parseDouble(components[1]) * parseDouble(components[2]);
                    }
                    System.out.printf("La venta total del producto '%s': %.2f%n", getName(), calcular);
                } catch (FileNotFoundException e) {
                    printfException(e, "calcularVenta");
                }
            }
        }

        private void deleteAll(File venta) {
            operation.delete(venta);
        }

        private void updateOrDelete(File venta, String operation) {
            boolean operationFlag = operation.matches("actualizar|eliminar");
            if (!operationFlag) printWrongOperation(operation);
            if (venta == null || venta.length() == 0) printFileEmpty();
            if (venta != null && operationFlag) {
                boolean flag = false;
                boolean flagUpdate = operation.equals("actualizar");
                List<String> fileContent = new LinkedList<>();
                setNameScanner(operation);
                try (BufferedReader reader = new BufferedReader(new FileReader(venta))) {
                    String line;
                    if (flagUpdate) setQuantityAndPriceScan();
                    while ((line = reader.readLine()) != null) {
                        String productNameF = line.split(", ")[0];
                        if (productNameF.equals(getName())) {
                            line = flagUpdate ? toString() : null;
                            flag = true;
                        }
                        fileContent.add(line); // Actualizamos la linea de la lista
                    }
                } catch (IOException e) {
                    printfException(e, operation);
                }
                if (flag) {
                    // Reescribimos el archivo con el contenido actualizado
                    try (BufferedWriter writer = new BufferedWriter(new FileWriter(venta))) {
                        for (String line : fileContent) {
                            if (line != null) writer.append(line).append(System.lineSeparator());
                        }
                        System.out.printf("El producto '%s' se ha '%so' correctamente!%n",
                                getName(), operation.substring(0, operation.length() - 2));
                    } catch (IOException e) {
                        printfException(e, operation);
                    }
                } else printProductNotFind(getName());
            }
        }

        private void setNameScanner(String operation) {
            System.out.printf("Introduce el nombre de producto que desea %s: ", operation);
            setName(scanner.next());
        }

        private void setQuantityAndPriceScan() {
            System.out.print("Ingresar la cantidad vendida(unidades): ");
            setQuantity(scanner.nextInt());
            System.out.print("Ingresar el precio unitario de producto($): ");
            setPrice(scanner.nextFloat());
        }

        private boolean contains(File venta, String productName) {
            if (venta == null || venta.length() == 0) return false;
            try (Scanner reader = new Scanner(venta)) {
                while (reader.hasNext()) {
                    String productNameF = reader.nextLine().split(", ")[0];
                    if (productNameF.equals(productName)) return true;
                }
            } catch (FileNotFoundException e) {
                printfException(e, "contains");
            }
            return false;
        }
    }
}