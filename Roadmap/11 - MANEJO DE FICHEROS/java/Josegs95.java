import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.StandardOpenOption;
import java.util.List;
import java.util.Scanner;

public class Josegs95 {
    public static void main(String[] args) {
        //Ficheros
        File file = new File("Josegs95.txt");
        try(FileWriter out = new FileWriter(file); Scanner in = new Scanner(file)){
            //FileWriter crea ya un archivo al crearse el objeto
            if (file.createNewFile())
                System.out.println("Archivo creado: " + file.getName());
            else
                System.out.println("No se ha creado el archivo " + file.getName() + " porque ya existía");


            out.write("Nombre: Josegs95" + System.lineSeparator());
            out.write("Edad: 29" + System.lineSeparator());
            out.write("Lenguaje: Java" + System.lineSeparator());
            out.flush();

            while (in.hasNext()){
                System.out.println(in.nextLine());
            }

        } catch (IOException e) {
            throw new RuntimeException(e);
        } finally {
            if (file.delete())
                System.out.println("Se ha borrado el archivo: " + file.getName());
            else
                System.out.println("No se ha podido borrar el archivo: " + file.getName());
        }

        //Reto
        System.out.println("\n");
        retoFinal();
    }

    static File file;
    public static void retoFinal(){
        file = new File("Ventas.txt");
        try(Scanner sc = new Scanner(System.in);
            FileWriter out = new FileWriter(file, true)){

            loop: while(true){
                showMenu();
                System.out.print("Seleccione una opción: ");
                String option = sc.nextLine();
                switch (option){
                    case "1": //Añadir
                        addProduct(out, askProductDetails(sc));
                        break;
                    case "2": //Consultar
                        showProduct(sc);
                        break;
                    case "3": //Actualizar
                        updateProduct(askProductDetails(sc));
                        break;
                    case "4": //Eliminar
                        deleteProduct(sc);
                        break;
                    case "5": //Calculo venta producto
                        calculateProductSales(sc);
                        break;
                    case "6": //Calculo venta total
                        calculateTotalSales();
                        break;
                    case "7": //Salir
                        break loop;
                    default:
                        System.out.println("Error. Debe elegir una opción válida (0-7).");
                        break;
                }
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        } finally {
            deleteFile();
        }

    }

    private static void showMenu(){
        System.out.println("------------------");
        System.out.println("1- Añadir producto");
        System.out.println("2- Consultar producto");
        System.out.println("3- Actualizar producto");
        System.out.println("4- Eliminar producto");
        System.out.println("5- Calcular venta producto");
        System.out.println("6- Calcular venta total");
        System.out.println("7- Salir");
        System.out.println("------------------");
    }

    private static String[] askProductDetails(Scanner userInput){
        System.out.print("Introduzca el nombre del producto: ");
        String product = userInput.nextLine().toLowerCase();
        System.out.print("Introduzca la cantidad del producto: ");
        String quantity = userInput.nextLine().toLowerCase(); //Habría que controlar que es un número
        System.out.print("Introduzca el precio del producto: ");
        String price = userInput.nextLine().toLowerCase(); //Habría que controlar que es un número

        return new String[]{product, quantity, price};
    }

    private static void addProduct(FileWriter outFile, String[] product) throws IOException {
        //Habría que controlar que el producto no existiera ya en el archivo
        String productLine = product[0] + ", " + product[1] + ", " + product[2] + System.lineSeparator();

        outFile.write(productLine);
        outFile.flush();
    }

    private static void showProduct(Scanner userInput) throws IOException {
        System.out.print("Introduzca el nombre del producto: ");
        String product = userInput.nextLine().toLowerCase();

        String[] productDetails;

        List<String> lines = Files.readAllLines(file.toPath());
        for (String line : lines){
            productDetails = line.split(", ");
            if (productDetails[0].equals(product)){
                System.out.println("Producto: " + productDetails[0] + ", Cantidad: " + productDetails[1] + ", Precio: " + productDetails[2]);
                return;
            }
        }

        System.out.println("No está registrado el producto: " + product);
    }

    private static void updateProduct(String[] product) throws IOException {
        String productLine = product[0] + ", " + product[1] + ", " + product[2];

        List<String> lines = Files.readAllLines(file.toPath());
        String[] productDetails;
        boolean isUpdated = false;
        for (int i = 0; i < lines.size(); i++){
            productDetails = lines.get(i).split(", ");
            if (productDetails[0].equals(product[0])){
                lines.set(i, productLine);
                isUpdated = true;
                break;
            }
        }

        if (isUpdated)
            System.out.println("Se ha actualizado el producto: " + product[0]);
        else
            System.out.println("El producto '" + product[0] + "' no está registrado.");

        Files.write(file.toPath(), lines, StandardCharsets.UTF_8);
    }

    private static void deleteProduct(Scanner userInput) throws IOException {
        System.out.print("Introduzca el nombre del producto: ");
        String product = userInput.nextLine().toLowerCase();

        String[] productDetails;
        boolean isRemoved = false;

        List<String> lines = Files.readAllLines(file.toPath());
        for (int i = 0; i < lines.size(); i++){
            productDetails = lines.get(i).split(", ");
            if (productDetails[0].equals(product)){
                lines.remove(i);
                isRemoved = true;
                break;
            }
        }

        if (isRemoved)
            System.out.println("Se ha borrado el producto: " + product);
        else
            System.out.println("El producto " + product + " no está registrado.");

        Files.write(file.toPath(), lines, StandardCharsets.UTF_8);
    }

    private static void calculateProductSales(Scanner userInput) throws IOException{
        System.out.print("Introduzca el nombre del producto: ");
        String product = userInput.nextLine().toLowerCase();

        List<String> lines = Files.readAllLines(file.toPath());
        String[] productDetails;
        Double total = 0.0;
        for (String line : lines){
            productDetails = line.split(", ");
            if (productDetails[0].equals(product)){
                Integer quantity = Integer.parseInt(productDetails[1]);
                Double price = Double.parseDouble(productDetails[2]);
                total = quantity * price;
                break;
            }
        }

        if (total != 0)
            System.out.printf("Venta del producto %s de %.2f€.%n", product, total);
        else
            System.out.println("El producto " + product + " no está registrado.");
    }

    private static void calculateTotalSales() throws IOException {
        List<String> lines = Files.readAllLines(file.toPath());
        String[] productDetails;
        Double total = 0.0;
        for (String line : lines){
            productDetails = line.split(", ");
            Integer quantity = Integer.parseInt(productDetails[1]);
            Double price = Double.parseDouble(productDetails[2]);
            total += quantity * price;
        }

        System.out.printf("Venta total de %.2f€.%n", total);
    }

    private static void deleteFile(){
        if (file.delete())
            System.out.println("Se ha borrado el archivo: " + file.getName());
        else
            System.out.println("No se ha podido borrar el archivo: " + file.getName());
    }
}
