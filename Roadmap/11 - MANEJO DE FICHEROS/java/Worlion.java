import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.Scanner;


public class Worlion {
    public static final String GREEN = "\u001B[32m";
    public static final String RED = "\u001B[31m";
    public static final String RED_BACKGROUND = "\u001B[41m";
    public static final String ANSI_RESET = "\u001B[0m";

    public static final String SHOP_ITEMS = "shop.txt";

    public static void clearScreen() {
        System.out.print("\033\143");
    }

    Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        Worlion w = new Worlion();

        w.filesBasics();
        w.extra();
    }

    public void filesBasics() {
        /**
         * EJERCICIO: Básico
         */

        String fileName = "Worlion.txt";

        StringBuffer fileContain = new StringBuffer();
        fileContain.append("Name: Worlion\n");
        fileContain.append("Age: 40\n");
        fileContain.append("Favourite language: Java\n");

        try {
            System.out.println("Writing file...");
            FileWriter fileWriter = new FileWriter(fileName);

            fileWriter.write(fileContain.toString());
            fileWriter.close();
            System.out.println("File writed.");

            System.out.println("Reading file...");
            Path path = Paths.get(fileName);
            List<String> lines = Files.readAllLines(path);
            for (String line : lines) {
                System.out.println("\t" + line);
            }
            System.out.println("File ended");

            System.out.println("Deleting file...");
            File myObj = new File(fileName);
            if (myObj.delete()) {
                System.out.println("Deleted the file: " + myObj.getName());
            } else {
                System.out.println("Failed to delete the file.");
            }
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    public void extra() {
        /**
         * DIFICULTAD EXTRA (opcional): Shop stock
         */
        clearScreen();
        System.out.println("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n");

        String option = "";
        while (!"0".equals(option)) {
            option = showMenu();
            processOption(option);
        }

    }

    private String showMenu() {

        System.out.println("\n¿Qué desea hacer?\n");
        System.out.println("\t1.- Añadir producto");
        System.out.println("\t2.- Consultar producto");
        System.out.println("\t3.- Actualizar producto");
        System.out.println("\t4.- Eliminar producto");
        System.out.println("\t5.- Consultar totales");

        System.out.println(RED + "\t0.- SALIR" + ANSI_RESET);

        return scanner.nextLine().trim();
    }

    private void processOption(String option) {
        System.out.println("Opción elegida: " + option);
        switch (option) {
            case "1": // Añadir producto
                System.out.println("Añadir producto: ");
                addProduct();
                break;
            case "2": // Consultar producto
                System.out.println("Consultar producto");
                findProduct();
                break;
            case "3": // Actualizar producto
                System.out.println("Actualizar producto");
                updateProduct();
                break;
            case "4": // Eliminar producto
                System.out.println("Eliminar producto");
                deleteProduct();
                break;
            case "5": // Consultar totales
                System.out.println("Consultar totales");
                printTotals();
                break;
            case "0":
                System.out.println("Hasta pronto...");
                System.out.println("Deleting file...");
                File myObj = new File(SHOP_ITEMS);
                if (myObj.delete()) {
                    System.out.println("Deleted the file: " + myObj.getName());
                } else {
                    System.out.println("Failed to delete the file.");
                }
                break;
            default:
                System.out.println(RED + "Opción no valida. Por favor vuelva a intentarlo." + ANSI_RESET);
                option = null;
                break;
        }
    }

    public void addProduct() {
        System.out.print("Escriba el nombre del producto: ");
        String name = scanner.nextLine();

        int quantity = 0;
        System.out.print("Cantidad: ");
        String quantityString = scanner.nextLine();
        try {
            quantity = Integer.parseInt(quantityString);
        } catch (NumberFormatException e) {
            System.err.println(RED + "Número no valido" + ANSI_RESET);
            return;
        }

        float price = 0.0f;
        System.out.print("Precio unitario del producto: ");
        String priceString = scanner.nextLine();
        try {
            price = Float.parseFloat(priceString);
        } catch (NumberFormatException e) {
            System.err.println(RED + "Número no valido" + ANSI_RESET);
            return;
        }

        Product product = new Product(name, quantity, price);
        try {
            FileWriter fileWriter = new FileWriter(SHOP_ITEMS, true);
            fileWriter.append(product.toString()+"\n");
            fileWriter.close();
        } catch (IOException e) {
            System.err.println(RED + "Excepción escribiendo el fichero: " + ANSI_RESET+ e);
        }
    }

    public void findProduct() {
        System.out.print("Escriba el nombre del producto a consultar: ");
        String name = scanner.nextLine();
        Product product = finProduct(name);
        if(product!=null) {
            System.out.print("Producto encontrado:");
            System.out.print(product.toString());
            System.out.print("Total: "+product.getTotal());
        }
    }

    private Product finProduct(String name) {
        try {
            Path path = Paths.get(SHOP_ITEMS);
            List<String> lines;
            lines = Files.readAllLines(path);
            Product p;
            for (String line : lines) {
                p = new Product(line);
                if(p.name.equals(name)){
                    System.out.print("Encontrado!");
                    return p;
                }
            }
            System.out.println("Producto no encontrado :(");
            return null;
        } catch (IOException e) {
            System.err.println(RED + "Excepción leyendo el fichero: " + ANSI_RESET+ e);
            return null;
        }
    }

    private void updateProduct() {
        System.out.print("Escriba el nombre del producto a modificar: ");
        String name = scanner.nextLine();
        Product product = finProduct(name);
        if(product!=null) {
            System.out.print("\nEstado actual: "+ product);
            
            System.out.print("\nEscriba nombre nuevo (o enter para dejarlo igual):");
            String newName = scanner.nextLine();
            if( newName==null || newName.isBlank() ){
                newName = product.name;
            }

            System.out.print("\nEscriba la nueva cantidad (o enter para dejarlo igual):");
            String q = scanner.nextLine();
            int newQuantity = product.quantity;
            if( q!=null && !q.isBlank() ){
                newQuantity = Integer.parseInt(q);
            }

            System.out.print("\nEscriba precio nuevo (o enter para dejarlo igual):");
            float newPrice = product.price;;
            String p = scanner.nextLine();
            if( p!=null && !p.isBlank() ){
                newPrice = Float.parseFloat(p);
            }

            Product newProduct = new Product(newName, newQuantity, newPrice);

            updateProduct(name, newProduct);

            System.out.print(product.toString());
            System.out.print("Total: "+product.getTotal());
        }
    }

    private void updateProduct(String oldName, Product value) {
        StringBuilder s = new StringBuilder();

        Path path = Paths.get(SHOP_ITEMS);
        List<String> lines;
        try {
            lines = Files.readAllLines(path);
            Product p;
            for (String line : lines) {
                p = new Product(line);
                if(p.name.equals(oldName)){
                    s.append(value+"\n");
                }
                else {
                    s.append(p+"\n");
                }
            }
        
            FileWriter fileWriter = new FileWriter(SHOP_ITEMS);
            fileWriter.write(s.toString());
            fileWriter.close();
        } catch (IOException e) {
            System.err.println(RED + "Excepción actualizando el fichero: " + ANSI_RESET+ e);
        }

    }

    private void deleteProduct() {
        System.out.print("Escriba el nombre del producto a "+RED_BACKGROUND+"eliminar: "+ANSI_RESET);
        String name = scanner.nextLine();
        Product product = finProduct(name);

        if(product!=null) {
            StringBuilder s = new StringBuilder();

            Path path = Paths.get(SHOP_ITEMS);
            List<String> lines;
            try {
                lines = Files.readAllLines(path);
                Product p;
                for (String line : lines) {
                    p = new Product(line);
                    if(!p.name.equals(product.name)){
                        s.append(line+"\n");
                    }
                }
            
                FileWriter fileWriter = new FileWriter(SHOP_ITEMS);
                fileWriter.write(s.toString());
                fileWriter.close();
            } catch (IOException e) {
                System.err.println(RED + "Excepción actualizando el fichero: " + ANSI_RESET+ e);
            }
        }
    
    }
    
    private void printTotals() {
        double total = 0;
        try {
            System.out.println("\tNombre\tCantidad\tPrecio\tTOTAL");
            Path path = Paths.get(SHOP_ITEMS);
            List<String> lines;
            lines = Files.readAllLines(path);
            Product p;
            int i = 0;
            for (String line : lines) {
                p = new Product(line);
                System.out.println("" + ++i + "\t"+ p.toString() + "\t" + p.getTotal());
                total += p.getTotal();
            }
            total = Math.round(total*100)/100.0f;
            System.out.println("\n\tTOTAL: " + total + " €");
        } catch (IOException e) {
            System.err.println(RED + "Excepción leyendo el fichero: " + ANSI_RESET+ e);
        }
    }
}
    class Product {
        String name;
        int quantity;
        float price;

        public Product(String name, int quantity, float price) {
            this.name = name;
            this.quantity = quantity;
            this.price = (Math.round(price*100)/100.0f);
        }

        public Product(String fullLine) {
            String[] values = fullLine.split(",\t");
            this.name = values[0];
            this.quantity = Integer.parseInt(values[1]);
            this.price = (Math.round(Float.parseFloat(values[2])*100)/100.0f);
        }

        public float getTotal() {
            float r = this.price*this.quantity;
            return Math.round(r*100)/100.0f;
        }

        public String toString() {
            return this.name + ",\t" + this.quantity + ",\t" + this.price;
        }
    }
