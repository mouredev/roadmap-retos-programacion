import java.io.*;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;
import java.util.zip.ZipOutputStream;

public class martinbohorquez {
    public static void main(String[] args) throws FileNotFoundException {
        File sourceFile = new File("AZ900-2024.pdf");
        File zipFile = zipFile(sourceFile);
        System.out.printf("El archivo '%s' ha sido comprimido: %s%n", sourceFile, zipFile);
        File unzipFile = unzipFile(zipFile);
        System.out.printf("El archivo '%s' ha sido descomprimido: %s%n", zipFile, unzipFile);
    }

    private static File zipFile(File sourceFile) throws FileNotFoundException {
        if (!sourceFile.exists()) throw new FileNotFoundException("El archivo no existe: " + sourceFile);

        String fileName = sourceFile.toString()
                .substring(0, sourceFile.toString().lastIndexOf("."));
        File targetFile = new File(fileName.concat(".zip"));

        try (FileOutputStream fos = new FileOutputStream(targetFile);
             ZipOutputStream zipOut = new ZipOutputStream(fos);
             FileInputStream fis = new FileInputStream(sourceFile)) {

            ZipEntry zipEntry = new ZipEntry(sourceFile.getName());
            zipOut.putNextEntry(zipEntry);

            byte[] buffer = new byte[1024];
            int length;
            while ((length = fis.read(buffer)) >= 0) zipOut.write(buffer, 0, length);

            zipOut.closeEntry();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return targetFile;
    }

    private static File unzipFile(File sourceFile) throws FileNotFoundException {
        if (!sourceFile.exists()) throw new FileNotFoundException("El archivo no existe: " + sourceFile);
        File targetFile = null;
        try (FileInputStream fis = new FileInputStream(sourceFile);
             ZipInputStream zipOut = new ZipInputStream(fis)) {

            ZipEntry zipEntry;

            if ((zipEntry = zipOut.getNextEntry()) != null) {
                targetFile = new File("unzip-" + zipEntry.getName());
                try (FileOutputStream fos = new FileOutputStream(targetFile)) {
                    byte[] buffer = new byte[1024];
                    int length;
                    while ((length = zipOut.read(buffer)) >= 0) fos.write(buffer, 0, length);
                }

                zipOut.closeEntry();
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return targetFile;
    }
}
