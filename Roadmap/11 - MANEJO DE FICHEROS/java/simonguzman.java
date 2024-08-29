import java.io.FileWriter;
import java.io.FileReader;
import java.io.IOException;
import java.io.BufferedReader;
import java.util.Scanner;

public class simonguzman {
    
    public static void main(String[] args) {
        testFile();
    }


    static void salesManager(){
        Scanner sc = new Scanner(System.in);
        int opcion;
        do{
            menu();
            System.out.println("Ingrese una opcion:");
            opcion = sc.nextInt();
            opcionsMenu(opcion);
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

    static void opcionsMenu(int opcion){
        switch (opcion) {
            case 1:
                addProducts();
                break;
            case 2:
                consultProducts();
                break;
            case 3:
                updateProducts();
                break;
            case 4:
                deleteProducts();
                break;
            case 5:
                exit();
                break;
            default:
            System.out.println("ERROR: Opcion no valida...");
                break;
        }
    }

    static void addProducts(){

    }

    static void consultProducts(){

    }

    static void updateProducts(){

    }

    static void deleteProducts(){

    }

    static void exit(){
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
