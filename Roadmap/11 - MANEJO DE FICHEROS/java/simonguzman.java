import java.io.FileWriter;
import java.io.FileReader;
import java.io.IOException;
import java.io.BufferedReader;

public class simonguzman {
    
    public static void main(String[] args) {
        testFile();
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
