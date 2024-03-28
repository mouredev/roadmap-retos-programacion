import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;

public class achreal {

    public static void main(String[] args) {
        try{
            File file = new File("AchRealG.txt");
            if (file.createNewFile()) {
            System.out.println("Fichero creado: " + file.getName());
            } else {
            System.out.println("El fichero ya existe");
            }
            }catch (IOException e) {
            System.out.println("Error: No puedo crear el fichero");
         }

         try (PrintWriter pw = new PrintWriter("AchRealG.txt")) {
            pw.println("Mi nombre es Axel");
            pw.println("Mi edad es 20");
            pw.println("Mi lenguaje de programacion favorito es Java");
         } catch (Exception e) {
            
         }

         try {
            File file = new File("AchRealG.txt");
            BufferedReader br = new BufferedReader(new FileReader(file));
            String linea = br.readLine(); //fr.read(), para un caracter
            System.out.println();
            while(linea != null) {
                System.out.println(linea);
                linea = br.readLine();
            }
            br.close();
            file.delete();
            } catch(IOException e) {
            e.printStackTrace();
            }


            
    }
}