import java.io.FileWriter;
import java.io.FileReader;
import java.io.File;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class simonguzman {
    
    public static void main(String[] args) {
        testFile();
        salesManager();
    }


    static void salesManager(){
        Scanner sc = new Scanner(System.in);
        int opcion;
        do{
            menu();
            System.out.println("Ingrese una opcion:");
            opcion = sc.nextInt();
            sc.nextLine();
            opcionsMenu(opcion, sc);
        }while(opcion != 5);
    }

    static void menu(){
        System.out.println("**************** GESTION DE VENTAS ****************");
        System.out.println("1. Añadir productos");
        System.out.println("2. Consultar productos");
        System.out.println("3. Actualizar productos");
        System.out.println("4. Eliminar productos");
        System.out.println("5. Salir");
    }

    static void opcionsMenu(int opcion, Scanner sc){
        switch (opcion) {
            case 1:
                addProducts(sc);
                break;
            case 2:
                consultProducts();
                break;
            case 3:
                updateProducts(sc);
                break;
            case 4:
                deleteProducts(sc);
                break;
            case 5:
                exit();
                break;
            default:
            System.out.println("ERROR: Opcion no valida...");
                break;
        }
    }

    static void addProducts(Scanner sc){
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("ventas.txt", true))){
                System.out.println("Ingrese el nombre del producto: ");
                String nameProduct = sc.next();
                System.out.println("Ingrese la cantidad vendida: ");
                int cantProduct = sc.nextInt();
                System.out.println("Ingrese el precio del producto: ");
                double priceProduct = sc.nextDouble();
                sc.nextLine();
                writer.write(nameProduct + " , "+cantProduct+" , "+priceProduct);
                writer.newLine();
                System.out.println("Producto añadido correctamente");
        } catch (IOException e) {
            System.out.println("ERROR: No se ha podido añadir el producto"+e.getMessage());
        }
    }

    static void consultProducts(){
        try (BufferedReader reader = new BufferedReader(new FileReader("ventas.txt"))){
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("ERROR: No se pudo consultar los productos..."+e.getMessage());
        }
    }   

    static void updateProducts(Scanner sc){
        List<String> products = new ArrayList<>();
        String line;
        boolean productFound = false;
        
        try (BufferedReader reader = new BufferedReader(new FileReader("ventas.txt"))){
            while((line = reader.readLine()) != null){
                products.add(line.trim());
            }
        } catch (IOException e) {
            System.out.println("ERROR: No se pudo leer el archivo..."+e.getMessage());
            return;
        }

        System.out.println("Ingrese el producto a actualizar: ");
        String productName = sc.next().trim();

        for(int i = 0; i < products.size(); i++){
            String[] details = products.get(i).split(", ");
            if(details[0].trim().equalsIgnoreCase(productName)){
                System.out.println("Ingrese la nueva cantidad vendida; ");
                int productCant = sc.nextInt();
                System.out.println("Ingrese el nuevo precio del producto: ");
                double productPrice = sc.nextDouble();
                sc.nextLine();

                products.set(i, productName + " , "+productCant+" , "+productPrice);
                productFound = true;
                break;
            } 
        }

        if(productFound){
            try (BufferedWriter writer = new BufferedWriter(new FileWriter("ventas.txt"))){
                for(String product : products){
                    writer.write(product);
                    writer.newLine();
                }
                System.out.println("Producto actualizado correctamente...");
            } catch (IOException e) {
                System.out.println("ERROR: No se pudo actualizar el producto..."+e.getMessage());
            }
        }else{
            System.out.println("Producto no encontrado.");
        }
    }

    static void deleteProducts(Scanner sc){
        List<String> products = new ArrayList<>();
        String line;
        boolean productFound = false;

        try (BufferedReader reader = new BufferedReader(new FileReader("ventas.txt"))){
            while ((line = reader.readLine()) != null) {
                products.add(line.trim());   
            }
        } catch (Exception e) {
            System.out.println("ERROR: No se pudo leer el archivo..."+e.getMessage());
            return;
        }

        System.out.println("Ingrese el producto a eliminar: ");
        String productName = sc.next().trim();

        for (int i = 0; i < products.size(); i++){
            String[] details = products.get(i).split(", ");
            if(details[0].trim().equalsIgnoreCase(productName)){
                products.remove(i);
                productFound = true;
                break;
            }
        }

        if (productFound){
            try (BufferedWriter writer = new BufferedWriter(new FileWriter("ventas.txt"))){
                for(String product : products){
                    writer.write(product);
                    writer.newLine();
                }
                System.out.println("Producto eliminado correctamente.");
            } catch (IOException e) {
                System.out.println("ERROR: El producto no pudo ser eliminado..."+e.getMessage());
            }
        }else{
            System.out.println("No se encontro el producto");
        }
    }

    static void exit(){
        File file = new File("ventas.txt");
        if(file.delete()){
            System.out.println("Fichero eliminado.");
        }else{
            System.out.println("ERROR: No se pudo eliminar el archivo.");
        }
        System.out.println("Saliendo del programa...");
    }

    static void testFile(){
        createAndWriteFile();
        readFile();
        deleteFile();
    }

    //Crear y escribrir el fichero
    static void createAndWriteFile(){
        try (FileWriter writer = new FileWriter("simonguzman.txt")){
            writer.write("Nombre: Simon\n");
            writer.write("Edad: 22\n");
            writer.write("Lenguaje de programacion favorito: Java\n");
        } catch (IOException e) {
            System.out.println("ERROR: No se puede crear o escribir el archivo...."+e.getMessage());
        }
    }

    //Leer el fichero
    static void readFile(){
        try (BufferedReader reader = new BufferedReader(new FileReader("simonguzman.txt"))){
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("ERROR: No se pudo leer el archivo..."+e.getMessage());
        }
    }

    static void deleteFile(){
        java.io.File file = new java.io.File("simonguzman.txt");
        if(file.delete()){
            System.out.println("Archivo eliminado correctamente");
        }else{
            System.out.println("ERROR: No se puede eliminar el archivo...");
        }
    }
}
