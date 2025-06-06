import java.io.*;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

public class MohamedElderkaoui {

    public static void main(String[] args) {
        String filePath = "archivo.txt";  // Cambia esta ruta por la del archivo a comprimir
        String zipFilePath = "archivo.zip";  // Ruta donde se guardará el archivo comprimido

        try {
            compressToZip(filePath, zipFilePath);
            System.out.println("Archivo comprimido correctamente en: " + zipFilePath);
        } catch (IOException e) {
            System.err.println("Error al comprimir el archivo: " + e.getMessage());
        }
    }

    // Método para comprimir un archivo en formato ZIP
    public static void compressToZip(String filePath, String zipFilePath) throws IOException {
        File fileToZip = new File(filePath);
        if (!fileToZip.exists()) {
            throw new FileNotFoundException("El archivo no existe: " + filePath);
        }

        // Crear flujo de salida para el archivo ZIP
        try (FileOutputStream fos = new FileOutputStream(zipFilePath);
             ZipOutputStream zipOut = new ZipOutputStream(fos);
             FileInputStream fis = new FileInputStream(fileToZip)) {

            // Crear una entrada de ZIP para el archivo
            ZipEntry zipEntry = new ZipEntry(fileToZip.getName());
            zipOut.putNextEntry(zipEntry);

            // Leer y escribir los datos del archivo en el archivo ZIP
            byte[] buffer = new byte[1024];
            int length;
            while ((length = fis.read(buffer)) >= 0) {
                zipOut.write(buffer, 0, length);
            }

            // Cerrar la entrada ZIP
            zipOut.closeEntry();
        }
    }
}
