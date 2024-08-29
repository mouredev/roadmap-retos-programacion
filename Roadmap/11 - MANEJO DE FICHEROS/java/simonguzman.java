import java.io.FileWriter;
import java.io.IOException;

public class simonguzman {
    
    public static void main(String[] args) {
        createAndWriteFile();
    }

    static void createAndWriteFile(){
        try (FileWriter writer = new FileWriter("simonguzman.txt")){
            writer.write("Nombre: Simon\n");
            writer.write("Edad: 22\n");
            writer.write("Lenguaje de programacion favorito: Java\n");
        } catch (IOException e) {
            System.out.println("ERROR: No se puede crear o escribir el archivo...."+e.getMessage());
        }
    }
}
