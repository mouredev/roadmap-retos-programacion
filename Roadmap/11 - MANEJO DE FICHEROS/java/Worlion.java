import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class Worlion {
    /**
     * EJERCICIO: Básico
     */
    public static void main(String[] args) {

        Worlion w = new Worlion();

        w.filesBasics();
    }

    public void filesBasics() {

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
            for( String line: lines) {
                System.out.println("\t"+line);
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
}
