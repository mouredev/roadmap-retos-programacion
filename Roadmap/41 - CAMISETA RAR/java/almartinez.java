import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

public class almartinez {
    public static void main(String[] args) {
        Path sourceFile = Paths.get("ruta/nombre_fichero_a_comprimir.txt");
        Path zipFileName = Paths.get("ruta/nombre_del_archivo_comprimido.zip");

        try {
            compressFile(sourceFile, zipFileName);
            System.out.println("Archivo comprimido creado: " + zipFileName);
        } catch (IOException ioe) {
            System.err.println("Error al comprimir el archivo: " + ioe.getMessage());
        }
    }

    private static void compressFile(Path sourceFile, Path zipFileName) throws IOException {
        try (ZipOutputStream zipOutputStream = new ZipOutputStream(Files.newOutputStream(zipFileName))) {
            
            ZipEntry zipEntry = new ZipEntry(sourceFile.getFileName().toString());
            zipOutputStream.putNextEntry(zipEntry);

            Files.copy(sourceFile, zipOutputStream);

        } catch (FileNotFoundException fnfe) {
            System.err.println("Archivo no encontrado: " + fnfe.getMessage());
            throw fnfe;
        } catch (IOException ioe) {
            System.err.println("Error de I/O: " + ioe.getMessage());
            throw ioe;
        }
        
    }

}
